from django.conf import settings
from django.shortcuts import render
from autentication.forms import creatform
from autentication.models import register
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail

# Create your views here.

def register_page(request):

    register_form=creatform(request.POST or None)
    if register_form.is_valid():
        Firstname=register_form.cleaned_data.get('firstname')
        Lastname=register_form.cleaned_data.get('lastname')
        Datebirth=register_form.cleaned_data.get('datebirth')
        City=register_form.cleaned_data.get('city')
        Fathername=register_form.cleaned_data.get('fathername')
        Gender=register_form.cleaned_data.get('gender')
        Address=register_form.cleaned_data.get('address')
        Phone_home=register_form.cleaned_data.get('phone_home')
        Religen=register_form.cleaned_data.get('religen')
        Maritalstatus=register_form.cleaned_data.get('maritalstatus')
        Job=register_form.cleaned_data.get('job')
        Education=register_form.cleaned_data.get('education')
        Universitydegree=register_form.cleaned_data.get('Universitydegree')
        University=register_form.cleaned_data.get('university')
        Password=register_form.cleaned_data.get('password')
        Username=register_form.cleaned_data.get('username')
        Email=register_form.cleaned_data.get('email')
        Idcard=register_form.cleaned_data.get('idcard')
        Postcode=register_form.cleaned_data.get('postcode')
        Phone_mobile=register_form.cleaned_data.get('phone_mobile')
        password_hash = make_password(Password)

        register.objects.create(firstname=Firstname, lastname=Lastname, datebirth=Datebirth, city=City, gender=Gender,
                                address=Address, phone_home=Phone_home, religen=Religen, maritalstatus=Maritalstatus,
                                job=Job, education=Education, Universitydegree=Universitydegree, university=University,
                                username=Username, email=Email, idcard=Idcard, postcode=Postcode, phone_mobile=Phone_mobile,
                                password=password_hash,fathername=Fathername)

    subject = 'ثبت نام با موفقیت انجام پذیرفت'
    message = f'سلام {register.firstname}, جان مرسی که در سایت ما ثبت نام کردی.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [register.email, ]
    send_mail(subject, message, email_from, recipient_list)

    contex={'register_form':register_form}

    return render(request,'register/register13.html',contex)