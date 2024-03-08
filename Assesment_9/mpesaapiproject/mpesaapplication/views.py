from django.shortcuts import render
from django_daraja.mpesa.core import MpesaClient
from django.http import HttpResponse


# Create your views here.
def index(request):
    cl = MpesaClient()
    phone_number = '0722000000'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = 'https://darajambili.herokuapp.com/express_payment'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)


def stk_push_callback(request):
    data = request.body
    return HttpResponse('Stk push in Django')


