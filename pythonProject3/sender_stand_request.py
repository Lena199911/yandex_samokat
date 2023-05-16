import configuration
import requests
import data


# def post_products_kits(products_ids):
#     return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, json=products_ids,
#                          headers=data.headers)
#
#
# response = post_products_kits(data.product_ids);
# print(response.status_code)
# print(response.json())

def post_zakaz(new_zakaz):
    return requests.post(configuration.URL_SERVICE + configuration.ORDERS, json=new_zakaz,
                         headers=data.headers)


def post_zakaz_track(track):
    return requests.post(configuration.URL_SERVICE + configuration.ORDERS_NUMBER + track, json=track,
                         headers=data.headers)



