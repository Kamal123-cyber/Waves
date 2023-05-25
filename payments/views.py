from django.shortcuts import render, redirect
from . models import Donations
import razorpay

def Pay(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        amount = int(request.POST.get('amount')) * 100
        print(name)
        print(amount)
        client = razorpay.Client(auth =('rzp_test_5XKZFFelqusIpq', 'QFvS3DgUGUvPf1ocR73AQFcC'))
        payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture':'1'})
        print(payment)
        donation = Donations(name= name, amount= amount, payment_id= payment['id'])
        print(donation)
        return render(request, 'payments/pay.html',{'payment':payment})

    return render(request, 'payments/pay.html')
def success(request):
    if request.method == 'POST':
        a = request.POST
        print(a)
    return render(request, 'payments/success.html')