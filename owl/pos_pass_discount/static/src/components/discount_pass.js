odoo.define("pos_pass_discount.discount",function (require) {
    "use strict";

    const Registries = require('point_of_sale.Registries');
    const DiscountButton = require('pos_discount.DiscountButton');
    const NumberBuffer = require('point_of_sale.NumberBuffer');


    const PosDiscountPass =( DiscountButton )=> class extends DiscountButton {
        async onClick() {
            console.log("hello from inside js file")
            var self = this;
            const { confirmed, payload } = await this.showPopup('NumberPopup',{
                isPassword: true,
                title: this.env._t('Discount Password'),
            });

            if ( payload ==this.env.pos.config.discount_passcode){
                NumberBuffer.reset()
                const { confirmed, payload } = await this.showPopup('NumberPopup',{
                    title: this.env._t('Discount Percentage'),
                    startingValue: this.env.pos.config.discount_pc,
                    isInputSelected: true
                });
                if (confirmed) {
                    const val = Math.max(0,Math.min(100,parseFloat(payload)));
                    await self.apply_discount(val);
                }
                NumberBuffer.reset()
            }else {
                NumberBuffer.reset()
                await this.showPopup('ErrorPopup', { title: 'Error Password is invalid', body: 'Please write another Password valid' });
            }

        }

    };


    Registries.Component.extend(DiscountButton, PosDiscountPass);

    return PosDiscountPass;


});