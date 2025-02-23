import json
import logging
import functools
from odoo import http
from odoo.addons.project_api.models.common import invalid_response, valid_response
from odoo.http import request

_logger = logging.getLogger(__name__)


def validate_token(func):
    @functools.wraps(func)
    def wrap(self, *args, **kwargs):
        access_token = request.httprequest.headers.get("access_token")
        if not access_token:
            return invalid_response("access_token_not_found", "missing access token in request header", 401)
        access_token_data = request.env["api.access_token"].sudo().search([("token", "=", access_token)],order="id DESC", limit=1)

        if access_token_data.find_or_create_token(user_id=access_token_data.user_id.id) != access_token:
            return invalid_response("access_token", "token seems to have expired or invalid", 401)

        request.session.uid = access_token_data.user_id.id
        request.uid = access_token_data.user_id.id
        return func(self, *args, **kwargs)
    return wrap



class DeleteTemplate(http.Controller):
    @validate_token
    @http.route(["/api/unlink/project"], methods=["DELETE"], type="http", auth="none", csrf=False)
    def unlink_project(self, **post):
        user_id = request.uid
        user_obj = request.env['res.users'].browse(user_id)
        payload = request.httprequest.data.decode()
        payload = json.loads(payload)
        print(payload)
        proj_id = payload.get("project_id")
        proj_obj = request.env['project.project']
        read_projects = proj_obj.with_user(user_obj).search([('id', '=', int(proj_id))])
        if read_projects:
            read_projects.unlink()
            return valid_response(
                [{"message": "Project Id %s successfully deleted" % (proj_id,), "delete": True}])



