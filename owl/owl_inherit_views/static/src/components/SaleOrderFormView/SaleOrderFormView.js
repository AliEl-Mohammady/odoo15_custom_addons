/** @odoo-module */
    const { Component } = owl;
    const { useState } = owl.hooks;
    const FormRenderer = require('web.FormRenderer');
    import { ComponentWrapper } from 'web.OwlCompatibility';

    class PartnerSaleOrder extends Component{
        partner=useState({});
        constructor(self,partner){
            super();
            this.partner=partner;
        }
    }

    PartnerSaleOrder.template="owl_inherit_views.PartnerOrderSummery";
//    Object.assign(PartnerSaleOrder, {
//        template:"owl_inherit_views.PartnerOrderSummery"
//    });
    FormRenderer.include({
        async _renderView(){
            var self = this;
            await this._super(...arguments);
            console.log("Hello ali El-Mohammady")
            if(this.state.data.partner_id){
                for(const element of this.el.querySelectorAll(".js_sale_order_view")){
                    await this._rpc({
                        model: 'res.partner',
                        method: 'read',
                        args: [[this.state.data.partner_id.res_id]],
                    }).then(data => {
                        (new ComponentWrapper(this, PartnerSaleOrder, useState(data[0]))).mount(element);
                    });
                }
            }
//            for(const element of this.el.querySelectorAll(".js_sale_order_view")){
//                    (new ComponentWrapper(this, PartnerSaleOrder)).mount(element);
//            }
        }
    });