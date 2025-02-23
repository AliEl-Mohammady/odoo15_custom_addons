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



class CreateTemplate(http.Controller):
    @validate_token
    @http.route("/api/create", methods=["POST"], type="http", auth="none", csrf=False)
    def create_project(self, **post):
        user_id = request.uid ##Important for valid token
        user_obj = request.env['res.users'].browse(user_id)
        payload = request.httprequest.data.decode()  #Get data from body of request
        payload = json.loads(payload)                #Change data from json to object
        proj_name = payload.get("proj_name")
        proj_desc = payload.get("proj_desc")
        proj_obj = request.env['project.project']
        new_proj = proj_obj.with_user(user_obj).create({
            'name': proj_name,
            'description': proj_desc,
        })
        if new_proj:
            return valid_response([{"project_id": new_proj.id, "message": "Project created successfully"}], status=201)
