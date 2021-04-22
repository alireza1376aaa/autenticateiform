from django.db import models

# Create your models here.
class register(models.Model):

    firstname=models.CharField(verbose_name='نام',max_length=40)
    lastname=models.CharField(verbose_name='نام خانوادگی',max_length=40)
    username=models.CharField(verbose_name='نام کاربری',max_length=30)
    email=models.EmailField(verbose_name="ایمیل ")
    datebirth=models.DateField(verbose_name="تاریخ تولد")
    city=models.CharField(verbose_name="شهر",max_length=20)
    idcard=models.BigIntegerField(verbose_name='کد ملی')
    fathername=models.CharField(verbose_name='نام پدر',max_length=40)
    gender= models.CharField(max_length=10, verbose_name="جنسیت")
    address=models.TextField(verbose_name='آدرس')
    postcode=models.CharField(verbose_name='کد پستی',null=True,blank=True,max_length=12)
    phone_mobile=models.CharField(verbose_name='شماره مبایل ',max_length=40)
    phone_home=models.CharField(verbose_name='شماره منزل',max_length=40)
    religen=models.CharField(verbose_name="دین",null=True,blank=True,max_length=40)
    maritalstatus=models.BooleanField(default=False,verbose_name="وضعیت تاهل")
    job=models.CharField(verbose_name='شغل',max_length=40,null=True,blank=True)
    education=models.CharField(verbose_name='تحصیلات',max_length=40)
    Universitydegree=models.CharField(verbose_name='مدرک دانشگاهی',max_length=40,null=True,blank=True)
    university=models.CharField(verbose_name='دانشگاه',max_length=40,null=True,blank=True)
    password=models.TextField(verbose_name="پسورد")

    def __str__(self):
        return self.username

    class Meta():
        verbose_name='اهراز هویت کاربر'
        verbose_name_plural='اهراز هویت کاربران'