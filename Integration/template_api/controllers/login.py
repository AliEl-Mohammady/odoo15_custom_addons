import json
import logging
import werkzeug.wrappers

from odoo import http
from odoo.addons.template_api.controllers.response import invalid_response, valid_response
from odoo.exceptions import AccessDenied, AccessError
from odoo.http import request

_logger = logging.getLogger(__name__)



class LoginTemplate(http.Controller):
    @http.route("/login", methods=["GET"], type="http", auth="none", csrf=False)
    def api_login(self, **post):
        """The token URL to be used for getting the access_token:
        Args:
            **post must contain login and password.
        Returns:
            returns https response code 404 if failed error message in the body in json format
            and status code 202 if successful with the access_token.
        Example:
           import requests
           headers = {'content-type': 'text/plain', 'charset':'utf-8'}
           data = {
               'login': 'admin',
               'password': 'admin',
               'db': 'galago.ng'
            }
           base_url = 'http://odoo.ng'
           eq = requests.post('{}/api/auth/token'.format(base_url), data=data, headers=headers)
           content = json.loads(req.content.decode('utf-8'))
           headers.update(access-token=content.get('access_token'))

        If you would like to use body to send the data you can do the following:
            payload = request.httprequest.data.decode()
            payload = json.loads(payload)
            db, username, password = (
                payload.get("db"),
                payload.get("login"),
                payload.get("password"),
            )
        """
        print(">>>>>>>>>>>>>>>>",post)
        params = ["db", "login", "password"]
        params = {key: post.get(key) for key in params if post.get(key)}
        db, username, password = (
            params.get("db"),
            post.get("login"),
            post.get("password"),
        )
        _credentials_includes_in_params = all([db, username, password])
        if not _credentials_includes_in_params:
            # The request post body is empty the credetials maybe passed via the headers.
            headers = request.httprequest.headers
            db = headers.get("db")
            username = headers.get("login")
            password = headers.get("password")
            _credentials_includes_in_headers = all([db, username, password])
            if not _credentials_includes_in_headers:
                # Empty 'db' or 'username' or 'password:
                return invalid_response(
                    "missing error", "either of the following are missing [db, username,password]", 403,
                )
        # Login in odoo database:
        try:
            request.session.authenticate(db, username, password)
        except AccessError as aee:
            return invalid_response("Access error", "Error: %s" % aee.name)
        except AccessDenied as ade:
            return invalid_response("Access denied", "Login, password or db invalid")
        except Exception as e:
            # Invalid database:
            info = "The database name is not valid {}".format((e))
            error = "invalid_database"
            _logger.error(info)
            return invalid_response("wrong database name", error, 403)

        uid = request.session.uid
        if not uid:
            info = "authentication failed"
            error = "authentication failed"
            _logger.error(info)
            return invalid_response("Not uid", error, info)

        # Generate tokens
        access_token = request.env["api.access_token"].find_or_create_token(user_id=uid, create=True)
        # Successful response:
        return werkzeug.wrappers.Response(
            status=200,
            content_type="application/json; charset=utf-8",
            headers=[("Cache-Control", "no-store"), ("Pragma", "no-cache")],
            response=json.dumps(
                {
                    "uid": uid,
                    "user_context": request.session.get_context() if uid else {},
                    "company_id": request.env.user.company_id.id if uid else None,
                    "company_ids": request.env.user.company_ids.ids if uid else None,
                    "partner_id": request.env.user.partner_id.id,
                    "access_token": access_token,
                    "company_name": request.env.user.company_name,
                    "country": request.env.user.country_id.name,
                    "contact_address": request.env.user.contact_address,
                }
            ),
        )

    #login using api key
    @http.route("/login/token_api_key", methods=["GET"], type="http", auth="none", csrf=False)
    def api_login_api_key(self, **post):
        params = ["db", "login", "password","api_key"]
        params = {key: post.get(key) for key in params if post.get(key)}
        db, username, password,api_key = (
            params.get("db"),
            post.get("login"),
            post.get("password"),
            post.get("api_key"),
        )
        _credentials_includes_in_params = all([db, username, password,api_key])
        if not _credentials_includes_in_params:
            # The request post params is empty the credentials maybe passed via the headers.
            headers = request.httprequest.headers
            db = headers.get("db")
            username = headers.get("login")
            password = headers.get("password")
            api_key = headers.get("api_key")
            _credentials_includes_in_headers = all([db, username, password,api_key])
            if not _credentials_includes_in_headers:
                # Empty 'db' or 'username' or 'password:
                return invalid_response(
                    "missing error", "either of the following are missing [db, username,password,api_key]", 403,
                )
        # Login in odoo database:
        user_id = request.env["res.users.apikeys"]._check_credentials(scope="rpc", key=api_key)
        # request.session.authenticate(db, username, api_key)
        if not user_id:
            info = "authentication failed"
            error = "authentication failed"
            _logger.error(info)
            return invalid_response(401, error, info)

        uid = user_id
        user_obj = request.env['res.users'].sudo().browse(int(uid))

        # Generate tokens
        # access_token = request.env["api.access_token"].find_or_create_token(user_id=uid, create=True)
        # Successful response:
        return werkzeug.wrappers.Response(
            status=200,
            content_type="application/json; charset=utf-8",
            headers=[("Cache-Control", "no-store"), ("Pragma", "no-cache")],
            response=json.dumps(
                {
                    "uid": uid,
                    # "user_context": request.session.get_context() if uid else {},
                    "company_id": user_obj.company_id.id if uid else None,
                    "company_ids": user_obj.company_ids.ids if uid else None,
                    "partner_id": user_obj.partner_id.id,
                    "access_token": api_key,
                    "company_name": user_obj.company_name,
                    "country": user_obj.country_id.name,
                    "contact_address": user_obj.contact_address,
                }
            ),
        )





##Respone returns from postman : {
#     "uid": 2,
#     "user_context": {
#         "lang": "en_US",
#         "tz": "Africa/Cairo",
#         "uid": 2
#     },
#     "company_id": 1,
#     "company_ids": [
#         1
#     ],
#     "partner_id": 3,
#     "access_token": "access_token_b40808fd47d26df4e25785777c3cca57ab764504",
#     "company_name": "YourCompany",
#     "country": "United States",
#     "contact_address": "YourCompany\n215 Vine St\n\nScranton PA 18503\nUnited States"
# }
