from django import forms
from user.models import Paymentinfo

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Paymentinfo
        fields = ['fake_card_number', 'fake_sort_code', 'fake_name_on_card',
                  ]

class SecurityCodeForm(forms.Form):
    Fake_security_code=forms.IntegerField(min_value=100, max_value=999, help_text="Do NOT put your real card details any of in these boxes, just random numbers please.") #its max value for integer field apperently
    

        

   

