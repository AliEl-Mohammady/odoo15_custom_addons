odoo.define('owl_server_action_controller.ArchiveAction', function (require) {
"use strict";

    const session = require('web.session');
    const BasicView = require('web.BasicView');



    BasicView.include({
        init: function (viewInfo, params) {
            this._super.apply(this, arguments);
            console.log(">>>>>>>>>>>>>>>>>>>>>>>>>>",params)
            console.log(">>>>>>>>>>>>>>>>>>>>>>>>>>",session)
            console.log(">>>>>>>>>>>>>>>>>>>>>>>>>>",this.controllerParams)
//            const currentModel=this.controllerParams.modelName
            const currentModel=params.modelName
            const restrictModel=['product.template']

            if (restrictModel.includes(currentModel) && session.uid !=2){
                console.log("Component working well")
                this.controllerParams.archiveEnabled = 'False' in this.fields;
                this.controllerParams.activeActions.duplicate =false ;
            }
        }
    })
})