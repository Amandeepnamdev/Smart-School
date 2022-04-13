from django.contrib import admin,messages
from .models import Teacher,Student,Subscribe,NewStudent,BookInstance,Schools,YoutubeVideo,Notification,Homework,Onlineclass,Subject,Notes,Enroll,AboutUsSchool,Facilities,Achievements,SchoolReviews,Product
from django.utils.translation import ngettext

# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    
    fieldsets = (
        (None , {
            'fields':('teacher','teacher_id2',),
        }),
        ('School Details',{
            'fields':(('teacher_school','teacher_school_id'),'school'),
        }),
        ('Teacher Details',{
            'classes':('wide','extrapretty',),
                'fields' : (('teacher_name','teacher_dept'),('teacher_sub','teacher_class'),('teacher_number','teacher_aadhar_number'),
    ('teacher_joining_date','teacher_leaving_date'),('teacher_salary','remaining_salary'),'teacher_gender','teacher_photo'),
        }),
            ('Address Details',{
            'classes':('wide','extrapretty',),
            'fields':(('teacher_address','teacher_address2'),('teacher_city','teacher_state'),'teacher_zip')
        }),
    )
    # fields=[('teacher_name','teacher_dept'),('teacher_sub','teacher_class'),('teacher_number','teacher_aadhar_number'),
    # ('teacher_joining_date','teacher_leaving_date'),('teacher_salary','remaining_salary')]
    list_display = ('teacher_id2','teacher_name','teacher_sub','teacher_school','teacher_school_id')
    list_filter=['teacher_sub']
    search_fields = ['teacher_name','teacher_id2']
    list_display_links = ['teacher_name','teacher_id2']
class TeacherInline(admin.TabularInline):
    model = Teacher
    extra = 0
    
admin.site.register(Teacher,TeacherAdmin)



class StudentAdmin(admin.ModelAdmin):
    
    fieldsets = (
        ('User',{
            'fields':('student_user','student_school')
        }),
        ('Fees Details',{
            'fields':(('fee_status','stu_fee'),('stu_fee_submitted','remaining_fee')),

        }),
        ('Personal Details',{
            'classes':('wide','extrapretty',),
            'fields':('stu_photo',('stu_roll_no','stu_class'),('stu_name','stu_number'),('stu_father_name','stu_father_occupation'),('stu_mother_name','stu_mother_occupation'),'stu_gender',('stu_brother','stu_sisters'),('stu_mob_number','stu_pho_number'),'stu_date',('stu_caste','stu_caste_certificate_number'),'stu_samagra_id',('stu_bank_account_no','stu_bank_name'),('stu_ifsc','stu_annual_income'),('stu_aadhar_number','stu_ration_card'))
        }),
        ('Academic details',{
            'classes':('wide','extrapretty',),
            'fields':(('stu_8_school','stu_medium'),('stu_8_per','stu_9_per'),('stu_11_per','stu_10_per'))
        }),
        ('Address Details',{
            'classes':('wide','extrapretty',),
            'fields':(('stu_address','stu_address2'),('stu_city','stu_state'),'stu_zip')
        }),
        # ('Documents',{
        #     'classes':('wide','extrapretty',),
        #     'fields':('stu_doc1','stu_doc2','stu_doc3')
        # }),
    )
    
    # fields=['stu_roll_no','stu_class','stu_name','stu_number','stu_father_name','stu_mother_name','stu_gender','stu_father_occupation','stu_mother_occupation','stu_brother','stu_sisters','stu_mob_number','stu_pho_number','stu_date','stu_caste','stu_caste_certificate_number','stu_samagra_id','stu_bank_account_no','stu_ifsc','stu_bank_name','stu_annual_income','stu_aadhar_number','stu_ration_card','stu_8_school','stu_medium','stu_8_per','stu_9_per',
    # 'stu_11_per','stu_10_per','stu_address','stu_address2','stu_city','stu_state','stu_zip']
    list_display = ('stu_roll_no','full_name','stu_class','stu_father_name','fee_status','remaining_fees','student_school')
    list_filter = ['stu_class']
    list_display_links = ['stu_roll_no','full_name',]
    search_fields=['stu_name']
    actions = ['fee_submitted']
    def fee_submitted(self,request,queryset):
        updated = queryset.update(fee_status = 'OK')
        self.message_user(request,ngettext(
            '%d fee submitted.',
            '%d fee not submitted.',
            updated,
        )% updated,messages.SUCCESS)
    
    fee_submitted.short_description = "Mark students who submitted fee"
admin.site.register(Student,StudentAdmin)

class SubscribeAdmin(admin.ModelAdmin):

    fields = ['subs_name','subs_email']
    list_display = ('subs_name','subs_email')

admin.site.register(Subscribe,SubscribeAdmin)

class AboutUsSchoolAdmin(admin.ModelAdmin):
    fields = ['heading','description','school']
    list_display = ('heading','school')
admin.site.register(AboutUsSchool,AboutUsSchoolAdmin)

class FacilitiesAdmin(admin.ModelAdmin):
    fields = ['heading','description','school']
    list_display = ('heading','school')
admin.site.register(Facilities,FacilitiesAdmin)

class AchievementsAdmin(admin.ModelAdmin):
    fields = ['heading','description','school']
    list_display = ('heading','school')
admin.site.register(Achievements,AchievementsAdmin)

class SchoolReviewsAdmin(admin.ModelAdmin):
    fields = ['name','review','school','rating']
    list_display = ('name','school','rating')
admin.site.register(SchoolReviews,SchoolReviewsAdmin)

class NewStudentAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Personal details',{
            'classes':('wide','extrapretty','collapse'),
            'fields':('std_photo',('std_fname','std_lname'),'std_class',('std_father_name','std_father_occupation'),('std_mother_name','std_mother_occupation'),'std_gender',('std_brother','std_sisters'),('std_mob_number','std_pho_number'),'std_date',('std_caste','std_caste_certificate_number'),'std_samagra_id',('std_bank_account_no','std_ifsc','std_bank_name'),('std_annual_income','std_aadhar_number'),'std_ration_card')
        }),
        ('Academic details',{
            'classes':('wide','extrapretty','collapse'),
            'fields':(('std_8_school','std_medium'),('std_8_per','std_9_per'),('std_11_per','std_10_per'))
        }),
        ('Address Details',{
            'classes':('wide','extrapretty','collapse'),
            'fields':('std_address','std_address2',('std_city','std_state'),'std_zip')
        }),

        
    )
    # fields = [
    #     # 'std_fname','std_lname','std_class','std_father_name','std_mother_name','std_gender','std_father_occupation','std_mother_occupation','std_brother','std_sisters','std_mob_number','std_pho_number','std_date','std_caste','std_caste_certificate_number','std_samagra_id','std_bank_account_no','std_ifsc','std_bank_name','std_annual_income','std_aadhar_number','std_ration_card','std_8_school','std_medium','std_8_per','std_9_per',
    # 'std_11_per','std_10_per','std_address','std_address2','std_city','std_state','std_zip']
    list_display=('full_name','std_class','std_father_name','std_aadhar_number')
    list_filter = ['std_class']
    # list_editable = ('std_class',)
    list_display_links = ('full_name','std_class')
    empty_value_display = '-empty-'
    # radio_fields = {"std_fname":admin.VERTICAL}
    # autocomplete_fields []
    
    # list_select_related = ('full_name','std_father_name')
    search_fields = ['std_fname','std_lname','std_class','std_father_name','std_mother_name','std_gender','std_father_occupation','std_mother_occupation','std_brother','std_sisters','std_mob_number','std_pho_number','std_date','std_caste','std_caste_certificate_number','std_samagra_id','std_bank_account_no','std_ifsc','std_bank_name','std_annual_income','std_aadhar_number','std_ration_card']
    # autocomplete_fields = ['std_ifsc']
    # view_on_site = False
admin.site.register(NewStudent,NewStudentAdmin)


class BookInstanceAdmin(admin.ModelAdmin):
    fieldsets = (
        (None,{
            'fields':('borrower',)
        }),
    )
admin.site.register(BookInstance,BookInstanceAdmin)
class YoutubeVideoAdmin(admin.ModelAdmin):
    fieldsets = (
        (None,{
            'fields':('video_id','video_embed_link','video_class','video_subject','video_topic','video_school')
        }),
    )
    list_display = ('video_id','video_class','video_subject','video_topic','video_school')
    list_filter= ['video_school','video_class']
    list_display_links = ('video_id','video_class','video_subject','video_topic','video_school')
    search_fields = ['video_id','video_subject','video_topic']
   
class YoutubeVideoInline(admin.TabularInline):
    model = YoutubeVideo
    extra = 0
admin.site.register(YoutubeVideo,YoutubeVideoAdmin)

class SchoolsAdmin(admin.ModelAdmin):
    inlines = [
        

        TeacherInline,
        YoutubeVideoInline,
        ]
    fieldsets = (
        (None, {
            'fields':('school_id2','school_name','school_img','school_image_link','school_vision',
            )
        }),
        ('Contact', {
            'fields' : (('school_mobile_no','school_email_id'),'school_city',('school_address1','school_address2'),)
        }),
    )
    # fields = ['school_id2','school_name','school_img']
admin.site.register(Schools,SchoolsAdmin)

class NotificationAdmin(admin.ModelAdmin):
    fieldsets = (
        ('School',{
            'fields':('school',)
        }),
        ('Notification',{
            'fields':('notification','notification_link',)
        }),

    )
admin.site.register(Notification,NotificationAdmin)

class HomeworkAdmin(admin.ModelAdmin):
    fieldsets = (
        (None,{
            'fields':('teacher','homework_topic','homework_detail','homework_class','homework_school')
        }),
    )
    list_display = ('teacher','homework_class','homework_topic','homework_school')
    list_filter = ('homework_school','homework_class')
admin.site.register(Homework,HomeworkAdmin)

class SubjectAdmin(admin.ModelAdmin):
    fieldsets = (
        (None,{
            'fields':('subject',),
        }),
    )
admin.site.register(Subject,SubjectAdmin)

class NotesAdmin(admin.ModelAdmin):
    fields = ['notes_link','notes_teacher','notes_subject','notes_topic']
    
    list_display = ['notes_teacher','notes_subject','notes_topic']
    
    list_filter = ['notes_teacher']
admin.site.register(Notes,NotesAdmin)


class OnlineclassAdmin(admin.ModelAdmin):
    fieldsets = (
        (None,{
            'fields':('teacher','class_topic','class_app','class_id','class_password','class_details')
        }),
    )
    list_display = ('teacher',)
    search_fields = ('teacher',)
admin.site.register(Onlineclass,OnlineclassAdmin)

class EnrollAdmin(admin.ModelAdmin):
    fieldsets = (
        (None,{
            'fields': ('teacher','enroll_form_link','enroll_school_name','enroll_form_subject')
        }),
    )
    list_display = ('teacher','enroll_school_name',)
admin.site.register(Enroll,EnrollAdmin)

class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        (None,{
            'fields': ('product_img_link','product_img_a_src','product_img_src','product_link','product_name','product_detail',)
        }),
    )
    list_display = ('product_name',)
admin.site.register(Product,ProductAdmin)
