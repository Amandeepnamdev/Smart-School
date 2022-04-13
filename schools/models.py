from django.db import models
from django.forms import ModelForm
from django.utils import timezone,dates
from django.utils.html import format_html
from django.contrib.auth.models import User


class Schools(models.Model):
    school_id = models.AutoField
    school_id2 = models.IntegerField(default=0)
    school_name = models.CharField(max_length=100)
    school_img = models.ImageField(upload_to='schools/images/',default="")
    school_image_link = models.URLField(max_length=200,default='')
    # Contact
    school_mobile_no = models.IntegerField(default=0)
    school_email_id = models.EmailField(max_length=200)
    school_address1 = models.CharField(max_length=250)
    school_address2 = models.CharField(max_length=250)
    school_city = models.CharField(max_length=100)
    # vision and mission
    school_vision = models.CharField(max_length=300,default="")

    class Meta:
        ordering = ['school_name']
    def __str__(self):
        return self.school_name

# Create your models here.
class Teacher(models.Model):

    teacher_id=models.AutoField
    
    teacher_name = models.CharField(max_length=50)
    teacher_id2 = models.IntegerField(default=0)
    teacher_sub = models.CharField(max_length=50)
    teacher_class= models.CharField(max_length=50)
    teacher_number= models.IntegerField()
    teacher_dept = models.CharField(max_length=50)
    teacher_joining_date = models.DateField(default=timezone.now)
    teacher_leaving_date = models.DateField(default=timezone.now)
    teacher_salary = models.IntegerField(default=0)
    remaining_salary = models.IntegerField(default=0)
    teacher_aadhar_number = models.IntegerField(default=0)
    teacher_photo = models.ImageField(upload_to="schools/images/",default="")
    teacher_gender = models.CharField(max_length=50,default='')
        # Address
    teacher_address = models.CharField(max_length=200,default='')
    teacher_address2 = models.CharField(max_length=200,default='')
    teacher_city = models.CharField(max_length=200,default='')
    teacher_state = models.CharField(max_length=50,default='')
    teacher_zip = models.CharField(max_length=50,default='')
    # school
    teacher_school = models.CharField(max_length=250,default='')
    teacher_school_id = models.IntegerField(default=0)
    school = models.ForeignKey(Schools,on_delete=models.CASCADE)
    # Teacher User
    teacher =  models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    # teacher_user


    class  Meta:
        ordering = ['teacher_school_id']
    def __str__(self):
        return self.teacher_name
# Youtube Video
class YoutubeVideo(models.Model):
    video_id = models.IntegerField(default=0)
    video_embed_link = models.CharField(max_length=50,default="")
    video_class = models.IntegerField(default=0)
    video_subject = models.CharField(max_length=100,default=0)
    video_topic = models.CharField(max_length=150,default="")
    video_school = models.ForeignKey(Schools,default = 1,on_delete = models.CASCADE)
    class  Meta:
        ordering = ['video_class']


    def __str__(self):
        return self.video_topic

class YoutubeVideoForm(ModelForm):
    class Meta:
        model = YoutubeVideo
        fields = ['video_id','video_embed_link','video_class','video_subject','video_topic']

class Subject(models.Model):
    subject = models.CharField(max_length=50,default="")
    
    def __str__(self):
        return self.subject

class Notes(models.Model):
    notes_link = models.CharField(max_length=150,default="")
    notes_topic = models.CharField(max_length=80,default="")
    notes_subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    notes_teacher = models.ForeignKey(Teacher,default = 1, on_delete= models.CASCADE)

    
    class Meta:
        ordering = ['notes_teacher']
class NotesForm(ModelForm):
    class Meta:
        model = Notes
        fields = ['notes_link','notes_subject','notes_teacher','notes_topic']

class Notification(models.Model):
    # school
    school = models.ForeignKey(Schools,default = 1,on_delete=models.CASCADE)
    # Notifications
    notification = models.CharField(max_length=500,default='')
    notification_link = models.CharField(max_length=100,default='')
    

# Teacher class Notification form
class NotificationForm(ModelForm):
    class Meta:
        model = Notification
        fields = ['notification','notification_link']
class Homework(models.Model):
    # teacher
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    homework_topic = models.CharField(max_length=100,default='')
    homework_detail = models.CharField(max_length=500,default='')
    homework_class = models.IntegerField(default=0)
    homework_school = models.CharField(max_length=100,default='')

    def __str__(self):
        return self.teacher.teacher_name + self.teacher.teacher_class

class HomeworkForm(ModelForm):
    class Meta:
        model = Homework
        fields = ['teacher','homework_topic','homework_detail','homework_class','homework_school']

class Onlineclass(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    class_topic = models.CharField(max_length=100,default='')
    class_app = models.CharField(max_length=20,default='')
    class_id = models.CharField(max_length=100,default='')
    class_password = models.CharField(max_length=30,default='')
    class_details = models.CharField(max_length=400,default='')

class OnlineclassForm(ModelForm):
    class Meta:
        model = Onlineclass
        fields = ['teacher','class_topic','class_app','class_id','class_password','class_details']

# class Admit(models.Model):
#     teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
#     admit_form_link = models.CharField(max_length=100,default='')
#     admit_school_name = models.CharField(max_length=100,default='')
    
#     def __str__(self):
#         return self.teacher.teacher_school

# class AdmitForm(ModelForm):
#     class Meta:
#         model = Admit
#         fields = ['teacher','admit_form_link','admit_school_name']

class Enroll(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    enroll_form_link = models.CharField(max_length=300,default='')
    enroll_form_subject = models.CharField(max_length=50,default='')
    enroll_school_name = models.ForeignKey(Schools,on_delete=models.CASCADE)

    def __str__(self):
        return self.enroll_school_name.school_name
    
class EnrollForm(ModelForm):
    class Meta:
        model = Enroll
        fields = ['teacher','enroll_form_link','enroll_school_name','enroll_form_subject']

class Subscribe(models.Model):
    subs_id = models.AutoField
    subs_name = models.CharField(max_length=100)
    subs_email = models.EmailField()
    def __str__(self):
        return self.subs_name

class SubscribeForm(ModelForm):
    class Meta:
        model = Subscribe
        fields = ['subs_name','subs_email']

FEE_STATUS_CHOICES = [
    ('OK','Submitted'),
    ('NO','Not_submitted'),
]

class Student(models.Model):
    # teacher1=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    stu_id=models.AutoField
    stu_roll_no= models.IntegerField()
    stu_name = models.CharField(max_length=50)
    stu_class = models.CharField(max_length=50)
    stu_number = models.IntegerField(default=0)

    stu_father_name = models.CharField(max_length=100,default='')
    stu_mother_name = models.CharField(max_length=100,default='')
    stu_gender = models.CharField(max_length=100, default='')
    stu_father_occupation = models.CharField(max_length=100, default='')
    stu_mother_occupation = models.CharField(max_length=100,default='')
    stu_brother = models.IntegerField(default=0)
    stu_sisters = models.IntegerField(default=0)
    stu_mob_number = models.IntegerField(default=0)
    stu_pho_number = models.IntegerField(default=0)
    stu_date = models.DateField(default=timezone.now)
    stu_caste = models.CharField(max_length=100,default='')
    stu_caste_certificate_number = models.CharField(max_length=100,default='')
    stu_samagra_id =models.IntegerField(default=0)
    stu_bank_account_no = models.IntegerField(default=0)
    stu_ifsc = models.CharField(max_length=100,default='')
    stu_bank_name = models.CharField(max_length=100,default='')
    stu_annual_income = models.IntegerField(default=0)
    stu_aadhar_number = models.IntegerField(default=0)
    stu_ration_card = models.CharField(max_length=100,default='')
    # Academic details
    stu_8_school = models.CharField(max_length=100,default='')
    stu_medium = models.CharField(max_length=50,default='')
    stu_8_per = models.CharField(max_length=10,default='')
    stu_9_per = models.CharField(max_length=10,default='')
    stu_10_per = models.CharField(max_length=10,default='')
    stu_11_per = models.CharField(max_length=10,default='')
    # Address
    stu_address = models.CharField(max_length=200,default='')
    stu_address2 = models.CharField(max_length=200,default='')
    stu_city = models.CharField(max_length=200,default='')
    stu_state = models.CharField(max_length=50,default='')
    stu_zip = models.CharField(max_length=50,default='')

    # fee
    stu_fee = models.IntegerField(default=0)
    stu_fee_submitted = models.IntegerField(default=0)
    remaining_fee = models.IntegerField(default=0)
    fee_status = models.CharField(max_length=20,choices=FEE_STATUS_CHOICES,default='')
    # photo
    stu_photo = models.ImageField(upload_to="schools/images/",default="")
    # document
    # stu_doc1 = models.ImageField(upload_to="schools/images/",default="")
    # stu_doc2 = models.ImageField(upload_to="schools/images/",default="")
    # stu_doc3 = models.ImageField(upload_to="schools/images/",default="")
    #Student User
    student_user  =  models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    # Student School
    student_school = models.ForeignKey(Schools,on_delete=models.CASCADE,null=True,blank=True)

    def my_property1(self):
       return self.stu_fee - self.stu_fee_submitted
    my_property1.short_description = 'Remaining fees'
    remaining_fees = property(my_property1)
            
    def full_name(self):
        return format_html(
            '<span style="color:blue;">{}</span>',
            self.stu_name,
        )
    full_name.admin_order_field = '-stu_name'
    def __str__(self):
        return self.stu_name

class NewStudent(models.Model):
    std_id = models.AutoField
    std_fname = models.CharField(max_length=50)
    std_lname = models.CharField(max_length=50)
    std_class = models.IntegerField(default=0)
    std_father_name = models.CharField(max_length=100,default='')
    std_mother_name = models.CharField(max_length=100,default='')
    std_gender = models.CharField(max_length=100, default='')
    std_father_occupation = models.CharField(max_length=100, default='')
    std_mother_occupation = models.CharField(max_length=100,default='')
    std_brother = models.IntegerField(default=0)
    std_sisters = models.IntegerField(default=0)
    std_mob_number = models.IntegerField(default=0)
    std_pho_number = models.IntegerField(default=0)
    std_date = models.DateField(default=timezone.now)
    std_caste = models.CharField(max_length=100,default='')
    std_caste_certificate_number = models.CharField(max_length=100,default='')
    std_samagra_id =models.IntegerField(default=0)
    std_bank_account_no = models.IntegerField(default=0)
    std_ifsc = models.CharField(max_length=100,default='')
    std_bank_name = models.CharField(max_length=100,default='')
    std_annual_income = models.IntegerField(default=0)
    std_aadhar_number = models.IntegerField(default=0)
    std_ration_card = models.CharField(max_length=100,default='')
    # Academic details
    std_8_school = models.CharField(max_length=100,default='')
    std_medium = models.CharField(max_length=50,default='')
    std_8_per = models.CharField(max_length=10,default='')
    std_9_per = models.CharField(max_length=10,default='')
    std_10_per = models.CharField(max_length=10,default='')
    std_11_per = models.CharField(max_length=10,default='')
    # Address
    std_address = models.CharField(max_length=200,default='')
    std_address2 = models.CharField(max_length=200,default='')
    std_city = models.CharField(max_length=200,default='')
    std_state = models.CharField(max_length=50,default='')
    std_zip = models.CharField(max_length=50,default='')
    # photo
    std_photo = models.ImageField(upload_to='schools/images/',default="")
    
    def my_property(self):
        return self.std_fname + ' ' + self.std_lname
    my_property.short_description = "Full name of student"
    
    full_name = property(my_property)
    def __str__(self):
        return self.std_fname
    

class AboutUsSchool(models.Model):
    heading = models.CharField(max_length=100,default='')
    description = models.CharField(max_length=500,default='')
    # school
    school = models.ForeignKey(Schools,default = 1,on_delete=models.CASCADE)

class AboutUsSchoolForm(ModelForm):
    class Meta:
        model = AboutUsSchool
        fields = ['heading','description']

class Facilities(models.Model):
    heading = models.CharField(max_length=100,default='')
    description = models.CharField(max_length=500,default='')
    # school
    school = models.ForeignKey(Schools,default = 1,on_delete=models.CASCADE)

class FacilitiesForm(ModelForm):
    class Meta:
        model = Facilities
        fields = ['heading','description']

class Achievements(models.Model):
    heading = models.CharField(max_length=100,default='')
    description = models.CharField(max_length=500,default='')
    # school
    school = models.ForeignKey(Schools,default = 1,on_delete=models.CASCADE)

class AchievementsForm(ModelForm):
    class Meta:
        model = Achievements
        fields = ['heading','description']

class SchoolReviews(models.Model):
    name = models.CharField(max_length=100,default='')
    review = models.CharField(max_length=500,default='')
    rating = models.CharField(max_length=2,default='')
    # school
    school = models.ForeignKey(Schools,default = 1,on_delete=models.CASCADE)    

class NewStudentForm(ModelForm):
    class Meta:
        model = NewStudent
        fields = ['std_fname','std_lname'
        ,'std_class','std_father_name','std_mother_name',
           'std_gender','std_father_occupation','std_mother_occupation','std_brother','std_sisters','std_mob_number',
           'std_pho_number','std_date','std_caste','std_caste_certificate_number',
           'std_samagra_id','std_bank_account_no','std_ifsc','std_bank_name','std_annual_income','std_aadhar_number','std_ration_card',
           'std_8_school','std_medium','std_8_per','std_9_per','std_10_per','std_11_per','std_address','std_address2','std_city','std_state','std_zip',
           'std_photo',
        ]


class BookInstance(models.Model):
    borrower = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)

class Product(models.Model):
    product_img_link = models.URLField(max_length=1000,default='')
    product_img_a_src = models.URLField(max_length=1000,default='')
    product_img_src = models.URLField(max_length=1000,default='')
    product_link = models.URLField(max_length=300)
    product_name = models.CharField(max_length=100,default='')
    product_detail = models.CharField(max_length=300,default='')