import json
import logging
import functools
from odoo import http
from odoo.addons.project_api.models.common import invalid_response, valid_response
from odoo.http import request
from odoo.exceptions import AccessDenied, AccessError

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



class ReadTemplate(http.Controller):
    @validate_token
    @http.route("/api/all_stages/read", methods=["POST"], type="http", auth="none", csrf=False)
    def all_project_stages(self, **post):
        user_id = request.uid
        user_obj = request.env['res.users'].browse(user_id)

        stages_obj = request.env['project.task.type']
        read_stages = stages_obj.with_user(user_obj).search([])
        stages_list = []
        for crm in read_stages:
            value_dict = {}
            for f in crm._fields:
                try:
                    value_dict[f] = str(getattr(crm, f))
                except AccessError as aee:
                    print(aee)
            stages_list.append(value_dict)
        return valid_response(stages_list, status=200)


    @validate_token
    @http.route("/api/stage/read", methods=["POST"], type="http", auth="none", csrf=False)
    def read_crm(self, **post):
        user_id = request.uid
        user_obj = request.env['res.users'].browse(user_id)
        payload = request.httprequest.data.decode()
        payload = json.loads(payload)
        project_id = payload.get("project_id")
        stages_obj = request.env['project.task.type']
        # read_stages = stages_obj.with_user(user_obj).filtered(lambda e: int(project_id) in e.project_ids.ids)
        read_stages = stages_obj.with_user(user_obj).search([('project_ids', 'in', [int(project_id)])])
        if read_stages:
            status = 200
            stages_list = []
            for crm in read_stages:
                value_dict = {}
                for f in crm._fields:
                    try:
                        value_dict[f] = str(getattr(crm, f))
                    except AccessError as aee:
                        print(aee)
                stages_list.append(value_dict)
        else:
            stages_list = []
            status = 204
            value_dict = {
                "message": "no data found"
            }
            stages_list.append(value_dict)
        return valid_response(stages_list, status=status)

# Response from postman : {
#     "count": 11,
#     "data": [
#         {
#             "active": "True",
#             "name": "New",
#             "description": "False",
#             "sequence": "1",
#             "project_ids": "project.project(1, 3, 2)",
#             "legend_blocked": "Blocked",
#             "legend_done": "Ready",
#             "legend_normal": "In Progress",
#             "mail_template_id": "mail.template(7,)",
#             "fold": "False",
#             "rating_template_id": "mail.template()",
#             "auto_validation_kanban_state": "False",
#             "is_closed": "False",
#             "disabled_rating_warning": "- Office Design\n- Renovations\n- Research & Development",
#             "user_id": "res.users()",
#             "id": "1",
#             "__last_update": "2025-01-19 21:29:01.904064",
#             "display_name": "New",
#             "create_uid": "res.users(1,)",
#             "create_date": "2025-01-19 21:29:01.904064",
#             "write_uid": "res.users(1,)",
#             "write_date": "2025-01-19 21:29:01.904064"
#         },