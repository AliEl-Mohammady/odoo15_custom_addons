odoo.define('owl_form_controller_buttons.ButtonsController', function (require) {
"use strict";

    const session = require('web.session');
    var FormController = require('web.FormController');


    FormController.include({
        getSelectedIds: function () {
            var env = this.model.get(this.handle);
            console.log("Component is working Well");
            console.log(">>>>>>>>>>>>>>>>>>>>>>>>>>>>",session);
            console.log(">>>>>>>>>>>>>>>>>>>>>>>>>>>>env",env);
            if (this.modelName=="stock.picking"){
                var currentRecordDate=env.data;
                if (currentRecordDate.state == 'done'){
//                    this.$buttons.find(".o_form_button_edit").hide();
                    this.$buttons.find(".o_form_button_create").hide();
                }
            }

            return this._super.apply(this, arguments);
        },

    })
})