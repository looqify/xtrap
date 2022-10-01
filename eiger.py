from ast import Try
from time import time
import requests
import random
import json


def getCoupon():
    xx = 'QWERTYUIOPASDFGHJKLZXcVBNM1234567890'
    pre = 'EGXTR100'
    for a in range(0, 5):
        pre += xx[random.randint(0, len(xx)-1)]
    return pre


def checkCoupon(cp):
    url = 'https://eigeradventure.com/graphql'
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "sec-ch-ua": "\"Google Chrome\";v=\"105\", \"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"105\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "store": "eiger_indonesia",
        "cookie": "_gcl_au=1.1.482698404.1660229824; _ga=GA1.2.1233656308.1660229824; _tt_enable_cookie=1; _ttp=8a425dc1-8dbb-4863-85d6-57396251b858; _gid=GA1.2.1888779418.1664591325; _cc_id=22ac0354cf247b4b3df7d68ff25e2e17; panoramaId_expiry=1665196130415; panoramaId=77995ae986eecf2036c904b26d8c16d5393859970808237e226019a820accba2; spwa={}; next-i18next=en; __storeConfig_0={%22secure_base_media_url%22:%22https://magento.eigeradventure.com/media/%22%2C%22secure_base_static_url%22:%22https://magento.eigeradventure.com/static/version1664357201/%22%2C%22customer_password_minimum_password_length%22:8%2C%22customer_password_required_character_classes_number%22:3%2C%22base_media_url%22:%22http://magento.eigeradventure.com/media/%22%2C%22base_static_url%22:%22http://magento.eigeradventure.com/static/version1664357201/%22%2C%22base_url%22:%22http://magento.eigeradventure.com/%22%2C%22base_currency_code%22:%22IDR%22%2C%22code%22:%22eiger_indonesia%22%2C%22catalog_search_engine%22:%22elasticsuite%22%2C%22copyright%22:%22Copyright%20%C2%A9%202022%20Eigerindo%20Multi%20Produk%20Industri%2C%20Inc.%20All%20rights%20reserved.%22%2C%22catalog_default_sort_by%22:%22new_arrivals%22%2C%22category_url_suffix%22:%22.html%22%2C%22default_title%22:%22Eiger%20Adventure%20Official%22%2C%22default_keywords%22:null%2C%22default_description%22:null%2C%22default_display_currency_code%22:%22IDR%22%2C%22header_logo_src%22:%22stores/3/Mask_Group_60_2x.png%22%2C%22head_shortcut_icon%22:%22websites/2/eigericon_1_.png%22%2C%22icube_pinlocation_gmap_key%22:%22AIzaSyCmrJLYWS7iEqR96JWN-MUlu2iSTKTljj; __storeConfig_1000=c%22%2C%22logo_alt%22:%22Eiger%20adventure%20logo%22%2C%22logo_width%22:null%2C%22logo_height%22:null%2C%22store_name%22:%22IND%22%2C%22welcome%22:%22EIGER%20ADVENTURE%22%2C%22timezone%22:%22Asia/Bangkok%22%2C%22title_prefix%22:null%2C%22title_suffix%22:null%2C%22title_separator%22:%22-%22%2C%22website_id%22:2%2C%22weight_unit%22:%22kgs%22%2C%22oauth_access_token_lifetime_customer%22:%221%22%2C%22payments_configuration%22:%22{%5C%22pg-banktransfer%5C%22:%5C%22snap_mandiri_bill_payment%2Csnap_banktransfer%2Csnap_banktransfer_bca%2Csnap_banktransfer_bni%2Csnap_banktransfer_bri%2Csnap_banktransfer_permata%2Csnap_cimbclicks%5C%22%2C%5C%22pg-installment%5C%22:%5C%22indodana%2Csnap_akulaku%2Csnap_mandiri_installment%2Csnap_bca_installment%2Csnap_bni_installment%2Csnap_mandiri_installment_3%2Csnap_mandiri_installment_6%2Csnap_mandiri_installment_12%2Csnap_bca_installment%2Csnap_maybank_installment%2Csnap_bni_installment_3%2Csnap_bni_installment_6%2Csnap_bni_installment_12%2C%5C%22%2C%5C%22pg-creditcard%5C%22:%5C%22snap_creditcardbin%2Csnap%2Csnap_creditcard%5C%22%2C%5C%22pg-internetpayment%5C%22:%5C%22snap_bcaklikpay%2Csnap_klikbca%2Csnap_klikbca%2Csnap_gopay%2Csnap_bcaklikpay%2Csnap_shopeepay%5C%22%2C%5C%22pg-others%5C%22:%5C%22checkmo%2Cca; __storeConfig_2000=shondelivery%2Csnap_alfamart%2Csnap_indomaret%5C%22}%22%2C%22shipments_configuration%22:%22{%5C%22sg-freeshipping%5C%22:%5C%22freeshipping_freeshipping%2Cfreeshipping_null%2Cpickup_pickup%5C%22%2C%5C%22sg-express%5C%22:%5C%22gosend_instant%2Cgosend_sameday%2Cgrabexpress_instant%2Cgrabexpress_same_day%2Cgrabexpress_null%2Cgosend_null%5C%22%2C%5C%22Regular%20shipment%5C%22:%5C%22advancerate_null%2Cadvancerate_advancedmatrix0%2Cadvancerate_advancedmatrix1%2Ccodrate%5C%22%2C%5C%22sg-reguler%5C%22:%5C%22flatrate_flatrate%2Ctablerate_bestway%5C%22}%22%2C%22snap_client_key%22:%22VT-client-0A8N0CmDkEDdrfzm%22%2C%22allow_guest_checkout%22:true%2C%22snap_is_production%22:%221%22%2C%22aw_blog_general_enabled%22:%221%22%2C%22pickup_store%22:true%2C%22cookie_restriction%22:false%2C%22global_promo%22:{%22enable%22:false%2C%22text_color%22:%22#b05d5d%22%2C%22background_color%22:%22#ffe8e8%22}%2C%22cms_page%22:null}; __storeConfig_subKeys=%220%2C1000%2C2000%22; cto_bundle=WcR92V9xZXFyQnlaNkJwTjdac09ndW8zb2FoUFFJMndPMFlUMkRoUkNvUjJMcEoyYTdNaVM5UlZLTEN1ZHhxV216NHhCM01LRzdidmp5Nkp2TUpCOTFoSjNCQzJuUCUyQkZxN25keCUyQmIzbHF5T0ZHSnQlMkZYRllHcjR0U2xvTmhQcVJabFFUN3JNbXlndFJuRDBGNlVCbzN3QUtobFBFdFVJVE9PTTdDMDhtdlpLTE04ZmYlMkJDTlFhUE9jV1E3R2l6ZkpRVXBGU3NwQlk2Y1B1S2pNTERleFBRd0YzcWclM0QlM0Q; nci=pWBobZEq0eUjD0aYWBmQUig6lCIa62KF",
        "Referer": "https://eigeradventure.com/checkout",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }

    body = {
        "variables": {
            "cartId": "pWBobZEq0eUjD0aYWBmQUig6lCIa62KF",
            "coupon": cp
        },
        "query": "mutation ($cartId: String!, $coupon: String!) {\n  applyCouponToCart(input: {cart_id: $cartId, coupon_code: $coupon}) {\n    cart {\n      id\n      applied_coupons {\n        code\n        __typename\n      }\n      id\n      email\n      applied_cashback {\n        data {\n          amount\n          promo_name\n          __typename\n        }\n        is_cashback\n        total_cashback\n        __typename\n      }\n      applied_reward_points {\n        is_use_reward_points\n        reward_points_amount\n        __typename\n      }\n      applied_coupons {\n        code\n        __typename\n      }\n      applied_extra_fee {\n        extrafee_value {\n          currency\n          value\n          __typename\n        }\n        select_options {\n          default\n          label\n          option_id\n          price\n          __typename\n        }\n        show_on_cart\n        title\n        __typename\n      }\n      addtional_fees {\n        data {\n          enabled\n          fee_name\n          frontend_type\n          id_fee\n          options {\n            default\n            label\n            option_id\n            price\n            __typename\n          }\n          __typename\n        }\n        show_on_cart\n        __typename\n      }\n      applied_store_credit {\n        store_credit_amount\n        is_use_store_credit\n        __typename\n      }\n      prices {\n        discounts {\n          amount {\n            currency\n            value\n            __typename\n          }\n          label\n          __typename\n        }\n        subtotal_excluding_tax {\n          currency\n          value\n          __typename\n        }\n        subtotal_including_tax {\n          currency\n          value\n          __typename\n        }\n        applied_taxes {\n          amount {\n            value\n            currency\n            __typename\n          }\n          __typename\n        }\n        grand_total {\n          currency\n          value\n          __typename\n        }\n        __typename\n      }\n      available_free_items {\n        sku\n        quantity\n        promo_item_data {\n          ruleId\n          minimalPrice\n          discountItem\n          isDeleted\n          qtyToProcess\n          isAuto\n          __typename\n        }\n        __typename\n      }\n      promoBanner {\n        cms_block_id\n        name\n        cms_block_identifier\n        rule_id\n        __typename\n      }\n      shipping_addresses {\n        is_valid_city\n        firstname\n        lastname\n        street\n        city\n        postcode\n        telephone\n        region {\n          code\n          label\n          __typename\n        }\n        company\n        country {\n          code\n          label\n          __typename\n        }\n        selected_shipping_method {\n          method_code\n          carrier_code\n          amount {\n            value\n            currency\n            __typename\n          }\n          __typename\n        }\n        available_shipping_methods {\n          available\n          method_code\n          carrier_code\n          method_title\n          carrier_title\n          amount {\n            value\n            currency\n            __typename\n          }\n          shipping_promo_name\n          error_message\n          price_incl_tax {\n            value\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      available_payment_methods {\n        code\n        title\n        __typename\n      }\n      items {\n        id\n        quantity\n        ... on ConfigurableCartItem {\n          configurable_options {\n            option_label\n            value_label\n            __typename\n          }\n          __typename\n        }\n        pickup_item_store_info {\n          is_pickup\n          loc_code\n          __typename\n        }\n        prices {\n          row_total {\n            currency\n            value\n            __typename\n          }\n          row_total_including_tax {\n            currency\n            value\n            __typename\n          }\n          discounts {\n            amount {\n              currency\n              value\n              __typename\n            }\n            label\n            __typename\n          }\n          price {\n            value\n            currency\n            __typename\n          }\n          price_including_tax {\n            value\n            currency\n            __typename\n          }\n          __typename\n        }\n        product {\n          id\n          name\n          categories {\n            name\n            __typename\n          }\n          url_key\n          sku\n          stock_status\n          small_image {\n            url\n            label\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
    }
    res = requests.post(url=url, headers=headers, json=body)
    if (res.status_code == 200):
        result = json.loads(res.text)
    else:
        result = {'errors': [{'message': res.status_code}]}
    return result


for a in range(1, 1000):
    cp = getCoupon()
    res = checkCoupon(cp)
    # print(res)
    if "errors" in res:
        status = res['errors'][0]['message']
    else:
        status = res

    print(f'[{a}] Coupon : {cp}\nStatus: {status}')

# cp = getCoupon()
# res = checkCoupon(cp)
# print(f'[] Coupom : {cp}\nStatus: {res}')
