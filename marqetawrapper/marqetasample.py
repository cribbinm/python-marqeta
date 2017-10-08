"""
Python wrapper for marqeta API. Documentation at https://www.marqeta.com/api/guides
"""

import json
import requests

username=''
password=''
head={'Content-Type': 'application/json'}
api= 'https://shared-sandbox-api.marqeta.com/v3/'

def cardProduct(start_date, name, ecommerce,activate_upon_issue):
    encoded_body = json.dumps({
      "start_date": start_date 
      "name": name
      "config": {
        "fulfillment": {
          "payment_instrument": payment_instrument
         },
        "poi": {
          "ecommerce": ecommerce
        },
        "card_life_cycle": {
          "activate_upon_issue": activate_upon_issue
        }
      }
    })
    r=requests.post(api + 'cardproducts', data=encoded_body, auth=(username, password),headers=head)
    return r 

def funding(name):
    encoded_body = json.dumps({
    "name": name 
    })
    r=requests.post(api + 'fundingsources/program', data=encoded_body, auth=(username, password),headers=head)
    return r

def users(name):
    encoded_body = json.dumps({})
    r=requests.post(api + 'users', data=encoded_body, auth=(username, password),headers=head)
    return r

def card(user_token,card_product_token,show_pan,show_cvv_number):
    #show_pan and show_cvv should be strings, 'true' or 'false'
    encoded_body = json.dumps({
     "user_token": user_token,
     "card_product_token": card_product_token
    })
    r=requests.post(api + 'cards?show_cvv_number=' + show_cvv_number + '&show_pan=' + show_pan, data=encoded_body, auth=(username, password),headers=head)
    return r

def gpaorders(user_token,amount,currency_code,funding_source_token):
    encoded_body = json.dumps({
    "user_token": user_token,
    "amount": amount,
    "currency_code": currency_code,
    "funding_source_token": funding_source_token
    })
    r=requests.post(api + 'gpaorders', data=encoded_body, auth=(username, password),headers=head)
    return r

def transact(amount,mid,card_token,endpoint,end_username,end_password):
    encoded_body = json.dumps({{
    "amount": amount,
    "mid": mid,
    "card_token": card_token,
    "webhook": {
    "endpoint": endpoint,
    "username": end_username,
    "password": end_password, 
    }
    })
    r=requests.post(api + 'simulate/authorization', data=encoded_body, auth=(username, password),headers=head)
    return r

