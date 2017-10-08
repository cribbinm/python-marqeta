from . import session

class API(object):

    def __init__(self, id):
        self.id = id
        self.head{'Content-Type': 'application/json'}

    def user_info(self):
        path = 'https://shared-sandbox-api.marqeta.com/v3/users'.format(self.token)
        response = session.get(path)
        return response.json()

    @staticmethod
    def accepted_countries():
        path = 'https://shared-sandbox-api.marqeta.com/v3/acceptedcountries'
        response = session.get(path)
        return response.json()

    def cardProduct(self):
    encoded_body = json.dumps({
      "start_date": self.start_date 
      "name": self.name
      "config": {
        "fulfillment": {
          "payment_instrument": self.payment_instrument
         },
        "poi": {
          "ecommerce": self.ecommerce
        },
        "card_life_cycle": {
          "activate_upon_issue": self.activate_upon_issue
        }
      }
    })
    r=requests.post(self.api + 'cardproducts', data=encoded_body,headers=self.head)
    return r 

    def funding(self):
        encoded_body = json.dumps({
        "name": self.name 
        })
        r=requests.post(self.api + 'fundingsources/program', data=encoded_body,headers=self.head)
        return r


    def card(self):
        #show_pan and show_cvv should be strings, 'true' or 'false'
        encoded_body = json.dumps({
         "user_token": self.user_token,
         "card_product_token": self.card_product_token
        })
        r=requests.post(self.api + 'cards?show_cvv_number=' + self.show_cvv_number + '&show_pan=' + self.show_pan, data=encoded_body,headers=self.head)
        return r

    def gpaorders(self):
        encoded_body = json.dumps({
        "user_token": self.user_token,
        "amount": self.amount,
        "currency_code": self.currency_code,
        "funding_source_token": self.funding_source_token
        })
        r=requests.post(self.api + 'gpaorders', data=encoded_body,headers=self.head)
        return r