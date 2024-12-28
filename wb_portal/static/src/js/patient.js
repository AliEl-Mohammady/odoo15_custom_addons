odoo.define('wb_portal.NewPatientForm', function (require) {
"use strict";

var PublicWidget = require('web.public.widget');

PublicWidget.registry.NewPatientForm = PublicWidget.Widget.extend({
    selector:"#patient_create_from",
    events: {
        'submit': '_onSubmitClicked',
    },

    _onSubmitClicked: function (evt) {

        var patient_name = this.$("input[name='name']").val();
        var patient_phone = this.$('input[name="phone"]').val();
        var age = this.$('input[name="age"]').val();
        var tag_ids= this.$('select[name="tag_id"]').val();

        if (!patient_name) {
            $("#myAlert_to_side_client").html("Please Enter Patient_ Name");
            $("#myAlert_to_side_client").show();
            evt.preventDefault();
        }
        else if (!patient_phone) {
            $("#myAlert_to_side_client").html("Please Enter Phone Number");
            $("#myAlert_to_side_client").show();
            evt.preventDefault();
        }
        else if (!tag_ids.match(/^[0-9]+$/)) {
            $("#myAlert_to_side_client").html("Please Enter Valid Tag Id");
            $("#myAlert_to_side_client").show();
            evt.preventDefault();
        }
        else
        {
            console.log("THERE IS NAME",patient_name,patient_phone,age,tag_ids);
            alert("Created successfully");
        }
    }
})


});
