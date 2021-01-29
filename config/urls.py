"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from pprint import pprint
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect

from sslcommerz_lib import SSLCOMMERZ
ssl_settings = {
    'store_id': 'yourstoreid',
    'store_pass': 'yourstorepassword',
    'issandbox': True
}


def pay_wit_ssl_commerz(request):
    sslcommerz = SSLCOMMERZ(ssl_settings)

    post_body = {}
    post_body['total_amount'] = 100.26
    post_body['currency'] = "BDT"
    post_body['tran_id'] = "12345"
    post_body['success_url'] = "https://tareqmonwer.com"
    post_body['fail_url'] = "www.erpbud.com/blog/"
    post_body['cancel_url'] = "www.erpbud.com"
    post_body['emi_option'] = 0
    post_body['cus_name'] = "test"
    post_body['cus_email'] = "test@test.com"
    post_body['cus_phone'] = "01700000000"
    post_body['cus_add1'] = "customer address"
    post_body['cus_city'] = "Dhaka"
    post_body['cus_country'] = "Bangladesh"
    post_body['shipping_method'] = "NO"
    post_body['num_of_item'] = 1
    post_body['product_name'] = "Test"
    post_body['product_category'] = "Test Category"
    post_body['product_profile'] = "general"

    response = sslcommerz.createSession(post_body)
    pprint(response)

    if response['status'] == 'SUCCESS':
        return HttpResponseRedirect(response['GatewayPageURL'])
    return HttpResponse(response)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pay', pay_wit_ssl_commerz, name='payment'),
]
