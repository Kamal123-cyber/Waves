import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import StripePayment

stripe.api_key = settings.STRIPE_SECRET_KEY


def payment_view(request):
    if request.method == 'POST':
        amount = float(request.POST['amount'])
        name = request.POST['name']
        email = request.POST['email']
        billing_address = request.POST['billing_address']

        # Create a Price object
        price = stripe.Price.create(
            unit_amount=int(amount * 100),  # amount in cents
            currency='usd',
            product_data={
                'name': 'Waves Corps',
            },
        )

        # Create a Checkout Session with the Price object
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': price.id,
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('payment_success')) + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=request.build_absolute_uri(reverse('payment_cancel')),
        )

        # Save the payment data to the database
        payment = StripePayment.objects.create(
            name=name,
            email=email,
            billing_address=billing_address,
            amount=amount,
            stripe_session_id=session.id,
        )

        # Redirect the user to the Checkout Session
        return redirect(session.url)
    else:
        return render(request, 'stripe_payment/payment_form.html')
    
@csrf_exempt
def payment_success_view(request):
    session_id = request.GET.get('session_id')
    payment = StripePayment.objects.get(stripe_session_id=session_id)
    payment.status = 'PAID'
    payment.save()
    return render(request, 'stripe_payment/payment_success.html')

def payment_cancel_view(request):
    return render(request, 'stripe_payment/payment_cancel.html')
