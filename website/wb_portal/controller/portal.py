from crypt import methods

from odoo.addons.portal.controllers.portal import CustomerPortal,pager
from odoo.http import request
from odoo import http


class HospitalPortal(CustomerPortal):
    def _prepare_portal_layout_values(self):
        res = super(HospitalPortal, self)._prepare_portal_layout_values()
        res['patients_count'] = request.env["hospital.patient"].sudo().search_count([])
        return res


    @http.route(['/my/hospitals','/my/hospitals/page/<int:page>'],auth="public",type='http', website=True)
    def om_hospital_portal(self,page=1,sortby='id',search="",search_in="All", **kw):
        sorted_list = {"id":{"label":"Id","order":"id asc"},
                       "name":{"label":"Name","order":"name asc"},
                       "age":{"label":"Age","order":"age asc"}}

        search_list = {"All":{"label":"All","input":"All","domain":[]},
                       "Name":{"label":"Name","input":"Name","domain":[("name","ilike",search)]},
                       "Age":{"label":"Age","input":"Age","domain":[("age","=",search)]}}

        search_domain=search_list[search_in]["domain"]

        default_order_by=sorted_list[sortby]["order"]
        patient_obj=request.env["hospital.patient"]
        print(search_domain)
        total_patients=patient_obj.sudo().search_count(search_domain)
        page_detail = pager(url="/my/hospitals",
                            total=total_patients,
                            page=page,
                            url_args={"sortby": sortby, "search": search, "search_in": search_in},
                            step=2)
        patients=patient_obj.sudo().search(search_domain,limit=2,order=default_order_by,offset=page_detail["offset"])
        vals={'patients':patients,
              "page_name":"patient_list",
              "pager":page_detail,
              "sortby":sortby,
              "searchbar_sortings":sorted_list,
              "searchbar_inputs":search_list,
              "search_in":search_in,
              "search":search,}

        return request.render("wb_portal.portal_om_hospital_list",vals)

    @http.route(['/my/hospitals/<model("hospital.patient"):patient_id>'],auth="public",  type='http', website=True)
    def om_hospital_patient_detail(self,patient_id, **kw):
        vals={"patient":patient_id,"page_name":"patient_detail_form"}
        patients_records=request.env["hospital.patient"].search([])
        patient_ids=patients_records.ids
        patient_index=patient_ids.index(patient_id.id)

        if patient_index==0:
            vals["prev_record"]=f"/my/hospital/{patient_ids[-1]}"
        else:
            vals["prev_record"]=f"/my/hospital/{patient_ids[patient_index-1]}"
        if patient_index==len(patient_ids)-1:
            vals["next_record"]=f"/my/hospital/{patient_ids[0]}"
        else:
            vals["next_record"]=f"/my/hospital/{patient_ids[patient_index+1]}"

        return request.render("wb_portal.portal_om_hospital_detail_form",vals)

    @http.route(['/my/registerPatient'], auth="user", type='http',methods=['GET', 'POST'], website=True)
    def register_patient(self, **kw):
        tags=request.env["patient.tag"].search([])
        error_list=[]
        success_msg = ""
        error_msg = ""
        if request.httprequest.method == 'POST':
            if not kw.get("name"):
                error_list.append("Name")
            if not kw.get("age"):
                error_list.append("Age")
            if not kw.get("marital_state"):
                error_list.append("Marital State")

            if error_list:
                error_msg = "Please fill the following fields: " + ", ".join(error_list)
            else:
                patient_id=request.env["hospital.patient"].sudo().create({"phone":kw["phone"],"name":kw["name"],"age":kw["age"],"tag_ids":[int(kw.get("tag_id"))],"marital_state":kw["marital_state"]})
                success_msg = f"Patient  {kw['name']}  added successfully"

            # return request.render("wb_portal.portal_om_hospital_detail_form",{"patient":patient_id,"page_name":"patient_detail_form"})
        else:
            print("method not in ['POST', 'GET']")
        vals={"tags":tags,"page_name":"patient_register_form","success_msg":success_msg,"error_msg":error_msg}
        return request.render("wb_portal.portal_om_hospital_register_form",vals)
