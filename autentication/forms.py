from django import forms
from django.forms import ModelForm
from autentication.models import register

class creatform(ModelForm):

   class Meta:
      model=register
      chosemarital = [('True', 'بله'), ('False', 'خیر')]
      type_choices = [('men', 'مرد'), ('women', 'زن'), ('other', 'دیگر')]

      fields=['firstname','lastname','datebirth','city''fathername','gender','address','phone_home',
              'religen','maritalstatus','job','education','Universitydegree','university','password']

      widgets={

     'firstname': forms.TextInput(attrs={'placeholder': 'نام  خود را وارد کنید'}),
     'lastname': forms.TextInput(attrs={'placeholder': 'نام خانوادگی خود را وارد کنید'}),
     'datebirth' : forms.DateInput(attrs={'placeholder': 'تاریخ تولد خود را وارد کنید'}),
     'city' : forms.TextInput(attrs={'placeholder': 'شهر خود را وارد کنید'}),
     'fathername' : forms.TextInput(attrs={'placeholder': 'نام پدر خود را وارد کنید'}),
      'gender':  forms.CheckboxSelectMultiple(attrs={'placeholder': 'جنسیت خود را مشخص کنید'},choices=type_choices),
      'address' : forms.TextInput(attrs={'placeholder': 'آدرس خود را وارد کنید'}),
      'phone_home'  : forms.TextInput(attrs={'placeholder': 'شماره منزل خود را وارد کنید'}),
      'religen': forms.TextInput(attrs={'placeholder': 'دین خود را مشخص کنید'}),
      'maritalstatus' : forms.RadioSelect(attrs={'placeholder': 'وضعیت تاهل خود را مشخص کنید'},choices=chosemarital),
      'job' : forms.TextInput(attrs={'placeholder': 'شغل خود را وارد کنید'}),
      'education' : forms.TextInput(attrs={'placeholder': 'تحصیلات خود را وارد کنید'}),
      'Universitydegree'  : forms.TextInput(attrs={'placeholder': 'مدرک دانشگاهی خود را وارد کنید'}),
      'university'  : forms.TextInput(attrs={'placeholder': 'دانشگاه خود را وارد کنید'}),
      'password' : forms.PasswordInput(attrs={'placeholder': 'پسورد خود را وارد کنید'}),

      }
      labels = {
          "firstname": ("نام"),
          "lastname": ("نام خانوادگی"),
          "datebirth": ("تاریخ تولد"),
          "city": ("شهر"),
          "fathername": ("نام پدر"),
          "gender": ("جنسیت"),
          "address": ("آدرس"),
          "phone_home": ("شماره منزل"),
          "religen": ("دین"),
          "maritalstatus": ("وضعیت تاهل"),
          "job": ("شغل"),
          "education": ("تحصیلات"),
          "Universitydegree": ("مدرک دانشگاهی"),
          "university": ("دانشگاه"),
          "password": ("پسورد"),
      }
      required = (
        "firstname"
        "lastname"
        "datebirth"
        "city"
        "fathername"
        "gender"
        "address"
        "phone_home"
        "maritalstatus"
        "education"
        "password"
      )

   username = forms.CharField(
       widget=forms.TextInput(attrs={ "placeholder": "نام کاربری خود را وارد کنید"}),
       label="نام کاربری")

   email = forms.EmailField(
       widget=forms.EmailInput(attrs={ "placeholder": "ایمیل خود را وارد کنید"}),
       label="ایمیل")

   password_again = forms.CharField(
       widget=forms.PasswordInput(attrs={ "placeholder": "رمز عبور خود را وارد کنید"}),
       label="تکرار رمز عبور")

   idcard = forms.IntegerField(
       widget=forms.NumberInput(attrs={"placeholder": "کد ملی خود را وارد کنید"}),
       label="نام کاربری")

   postcode = forms.CharField(
       widget=forms.TextInput(attrs={"placeholder": "کد پستی خود را وارد کنید"}),
       label="نام کاربری",
       required=False
   )


   phone_mobile = forms.CharField(
       widget=forms.TextInput(attrs={"placeholder": "شماره مبایل خود را وارد کنید"}),
       label="نام کاربری")

   def clean_username(self):

       UserNmae = self.cleaned_data.get('username')

       qu = register.objects.filter(username=UserNmae)

       if qu.exists():
           raise forms.ValidationError("کاربری با همچین مشخصه ای موجود است")
       return UserNmae

   def clean_password_again(self):
       pass1 = self.cleaned_data.get('password')
       pass2 = self.cleaned_data.get('password_again')

       if pass1 != pass2:
           raise forms.ValidationError("پسورد با هم تطابق ندارد")

   def clean_email(self):

       Email = self.cleaned_data.get('email')

       qu = register.objects.filter(email=Email)

       if qu.exists():
           raise forms.ValidationError("ایمیلی با همچین مشخصه ای موجود است")
       return Email

   def clean_idcard(self):

       Idcard = self.cleaned_data.get('idcard')

       qu = register.objects.filter(idcard=Idcard)

       if qu.exists():
           raise forms.ValidationError("کد ملی  با همچین مشخصه ای موجود است")
       return Idcard

   def clean_postcode(self):

       Postcode = self.cleaned_data.get('postcode')

       qu = register.objects.filter(postcode=Postcode)

       if qu.exists():
           raise forms.ValidationError("کد پستی با همچین مشخصه ای موجود است")
       return Postcode

   def clean_phone_mobile(self):

       Phone_mobile = self.cleaned_data.get('email')

       qu = register.objects.filter(phone_mobile=Phone_mobile)

       if qu.exists():
           raise forms.ValidationError("شماره مبایل با همچین مشخصه ای موجود است")
       return Phone_mobile

