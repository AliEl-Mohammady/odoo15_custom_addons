odoo.define('pos_auth_discount.discount', function(require) {
    'use strict';
const DiscountButton=require(pos_discount.DiscountButton)
const Registries=require(pos_discount.Registries)
const NumberBuffer=require(pos_discount.NumberBuffer)

const POSDiscountButton=(DiscountButton)=>{
    class extends  DiscountButton {
        async onClick(){
            NumberBuffer.reset();
            var self=this;
            var userInput=await this.showPopup('NumberPopup',{
                isPassword:true,
                'title':this.env._t("Enter Password")
            });

            if(userInput('payload')==this.env.pos.config.discount_passcode){
                NumberBuffer.reset();
                var {confirmed,payload}=await this.showPopup('NumberPopup',{
                    "title": this.env._t("Discount Percentage")
                });

                if (confirmed){
                    self.apply_discount(payload);
                };

            }
            else{
                await this.showPopup('ErrorPopup',{
                    "title": this.env._t("Error"),
                    "body": this.env._t("Password Incorrect"),
                });
            }
        }

    }
    }
    Registries.Component.extend(DiscountButton,POSDiscountButton);
return POSDiscountButton;
});


