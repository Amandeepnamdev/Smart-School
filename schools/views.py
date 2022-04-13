from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest,Http404
from .forms import NameForm,ContactForm
from .models import SubscribeForm,Subscribe,NewStudent,NewStudentForm,Student,Teacher,Schools,YoutubeVideo,YoutubeVideoForm,Notification,NotificationForm,Homework,HomeworkForm,Onlineclass,OnlineclassForm,Notes,NotesForm,Subject,Enroll,EnrollForm,AboutUsSchool,AboutUsSchoolForm, Facilities,FacilitiesForm,Achievements,AchievementsForm,SchoolReviews,Product
from django.core.mail import send_mail
# for login requirements
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def index(request):
    
    return render(request,'schools/index.html')
@staff_member_required
def students(request):
    
    allStudents = []
    class_wise_students = Student.objects.values('stu_class','stu_roll_no','stu_name')
    classes = {item['stu_class'] for item in class_wise_students}
    for clas in classes:
        student = Student.objects.filter(  stu_class = clas)
        allStudents.append(student)
    params = {'allStudents':allStudents}
    return render(request,'schools/students.html',params)

def teachers(request):
    allTeachers = []
    class_wise_teachers = Teacher.objects.values('teacher_class','teacher_name')
    classes = {item['teacher_class'] for item in class_wise_teachers}
    for clas in classes:
        teacher = Teacher.objects.filter(teacher_class =clas)
        allTeachers.append(teacher)
    params = {'allTeachers':allTeachers}
    return render(request,'schools/teachers.html',params)

@staff_member_required
def subscribe(request):
    form1= SubscribeForm(request.POST)
    if(form1.is_valid()):
        subs_name = form1.cleaned_data['subs_name']
        subs_email = form1.cleaned_data['subs_email']
    return render(request,'schools/subs.html',{'form1':form1})




@staff_member_required
def profile(request,roll):
    student = Student.objects.filter(stu_roll_no=roll)
    return render(request,'schools/profile.html',{'student':student[0]})
def profileteacher(request,number):
    teacher = Teacher.objects.filter(teacher_number = number)
    return render(request,'schools/profileteacher.html',{'teacher':teacher[0]})

    
def contact(request):
    
    
    form = ContactForm(request.POST)
    if(form.is_valid()):
        
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        sender = form.cleaned_data['sender']
        cc_myself = form.cleaned_data['cc_myself']

        recipents=['amandeep.namdev456@gmail.com']
        if cc_myself:
            recipents.append(sender)
        
        send_mail(subject,message,sender,recipents)
        return HttpResponseRedirect('/thanks/')
    return render(request,'schools/contact.html',{'form':form})

def aboutus(request):
    return render(request,'schools/aboutus.html')

@staff_member_required
def submit(request):
    
    sub = SubscribeForm(request.POST)

    name = request.POST.get('name1','')
    email = request.POST.get('email1','')
    p=Subscribe(subs_name=name,subs_email=email)
    p.save()
 
    return render(request,'schools/subs.html')

@staff_member_required
def register(request):
    if request.method == 'POST':
        print('hi')
    
        newForm = NewStudentForm(request.POST)
        
        std_fname = request.POST.get('std_fname','')
        std_lname = request.POST.get('std_lname','')
        std_class = request.POST.get('std_class',0)
        std_father_name = request.POST.get('std_father_name','')
        std_mother_name = request.POST.get('std_mother_name','')
        std_gender = request.POST.get('std_gender','')
        std_father_occupation = request.POST.get('std_father_occupation','')
        std_mother_occupation = request.POST.get('std_mother_occupation','')
        std_brother = request.POST.get('std_brother',0)
        std_sisters = request.POST.get('std_sisters',0)
        std_mob_number = request.POST.get('std_mob_number',0)
        std_pho_number = request.POST.get('std_pho_number',0)
        std_date = request.POST.get('std_date','2000-05-12')
        std_caste = request.POST.get('std_caste','')
        std_caste_certificate_number = request.POST.get('std_caste_certificate_number','')
        std_samagra_id = request.POST.get('std_samagra_id',0)
        std_bank_account_no = request.POST.get('std_bank_account_no',0)
        std_ifsc = request.POST.get('std_ifsc','')
        std_bank_name = request.POST.get('std_bank_name','')
        std_annual_income = request.POST.get('std_annual_income',0)
        std_aadhar_number = request.POST.get('std_aadhar_number',0)
        std_ration_card = request.POST.get('std_ration_card','')
        # Academic details
        std_8_school = request.POST.get('std_8_school','')
        std_medium  = request.POST.get('std_medium','')
        std_8_per  = request.POST.get('std_8_per','')
        std_9_per  = request.POST.get('std_9_per','')
        std_10_per  = request.POST.get('std_10_per','')
        std_11_per  = request.POST.get('std_11_per','')
        #Address details
        std_address  = request.POST.get('std_address','')
        std_address2 = request.POST.get('std_address2','')
        std_city  = request.POST.get('std_city','')
        std_state  = request.POST.get('std_state','')
        std_zip  = request.POST.get('std_zip','')
        
        # Photo
        std_photo = request.POST.get('std_photo','')

        new = NewStudent(std_fname=std_fname,std_lname=std_lname,
        std_class=std_class,std_father_name=std_father_name,
        std_mother_name=std_mother_name,std_gender=std_gender,std_father_occupation=std_father_occupation,std_mother_occupation=std_mother_occupation,
        std_brother=std_brother,std_sisters=std_sisters,std_mob_number=std_mob_number,std_pho_number=std_pho_number,std_date=std_date,
        std_caste=std_caste,std_caste_certificate_number=std_caste_certificate_number,std_samagra_id=std_samagra_id,std_bank_account_no=std_bank_account_no,
        std_ifsc=std_ifsc,std_bank_name=std_bank_name,std_annual_income=std_annual_income,std_ration_card=std_ration_card,
        std_aadhar_number=std_aadhar_number,std_8_per=std_8_per,std_9_per=std_9_per,std_10_per=std_10_per,std_11_per=std_11_per,

        std_8_school=std_8_school,std_medium=std_medium,
        std_address=std_address,std_address2=std_address2,std_city=std_city,std_state=std_state,std_zip=std_zip,std_photo = std_photo)
        new.save()
        return HttpResponse('Your form has been submitted successfully')

    else:
        HttpResponse('You are about to Hack')
    return render(request,'schools/register.html')




def fee(request):
    return render(request,'schools/fee.html')

from django.contrib.auth.mixins import LoginRequiredMixin
class StudentsGet(LoginRequiredMixin):

    model = Student,Teacher
    template_name = 'schools/students_get.html'
    paginated_by = 10
    def get_queryset(self):
        return Student.objects.filter(teacher1=self.request.user)

def school_home(request,school_name):
    this_school = Schools.objects.get(school_name=school_name)
    class_of_videos = set()
    videos = []
    all_videos = YoutubeVideo.objects.all()
    no_of_videos = YoutubeVideo.objects.count()
    for video in range(no_of_videos):
        if all_videos[video].video_school.school_name == school_name:
            videos.append(all_videos[video])
            class_of_videos.add(all_videos[video].video_class)
    
    class_of_videos = list(class_of_videos)
    # notifications
    notifications = Notification.objects.filter(school = this_school) 
    # About School--------------->
    aboutus = AboutUsSchool.objects.filter(school = this_school)
    # Facilities
    facilities = Facilities.objects.filter(school = this_school)
    # Achievements -------------->
    achievements = Achievements.objects.filter(school = this_school)
    # Admission---------->
    reviews = SchoolReviews.objects.filter(school = this_school)

    admission_links = Enroll.objects.filter(enroll_school_name = this_school)
    print(admission_links)
    print(notifications)
    params = {'this_school':this_school,'videos':videos,'class_of_videos':class_of_videos,'no_of_videos':no_of_videos,'notifications':notifications,'admission_links':admission_links,'aboutus':aboutus,'facilities':facilities,'achievements':achievements,'reviews':reviews}
    return render(request,'schools/school_home.html',params)


def schools_list(request):
    schools = Schools.objects.all()
    params = {'schools':schools}
    return render(request,'schools/schools_list.html',params)




def teacher_home(request,teacher_id1):
    teacher=Teacher.objects.get(teacher_id2=teacher_id1)
    teacher_classes = teacher.teacher_class.split(',')
    
    params = {'teacher':teacher,'teacher_classes':teacher_classes}
    return render(request,'schools/teacher_home.html',params)

@login_required
@permission_required('schools.view_teacher')
def teacher_class(request,teacher_id1,class1):
    if request.user.is_authenticated:
        subjects = Subject.objects.all()
        
        teacher=Teacher.objects.get(teacher_id2=teacher_id1)

        teacher_classes = teacher.teacher_class.split(',')
        teacher_school = teacher.school
        students = []
        school_students = Student.objects.filter(student_school = teacher.school)
        no_of_students1 = len(school_students)
        class12=str(class1)
        if str(class1) not in teacher_classes or teacher.teacher != request.user:            
            raise Http404
        for stu in range(no_of_students1):
            if school_students[stu].stu_class == class12:
                students.append(school_students[stu])


        no_of_students = students
        
   
        if request.method == 'POST' and 'YoutubeVideos' in request.POST:    # YoutubeVideos is name of button
            
            newvideoform = YoutubeVideoForm(request.POST)
            video_school = teacher_school
            no_of_videos= YoutubeVideo.objects.count()
            
            video_embed_link = request.POST.get('videoembedlink','')
            video_subject = request.POST.get('videosubject','')
            video_topic = request.POST.get('videotopic','')
            video_class = class1
            video_id = no_of_videos + 1
                
            # video_school = 4
            newvideo = YoutubeVideo(video_id = video_id,video_embed_link=video_embed_link,video_subject=video_subject,video_topic=video_topic,video_class=video_class,video_school=video_school)
            newvideo.save()
        if request.method == 'POST' and 'Notifications' in request.POST:
            
            notificationform = NotificationForm(request.POST)
            notification = request.POST.get('Notification','')
            notification_link = request.POST.get('Notificationlink','')
            school = teacher_school
            newnotification = Notification(notification = notification,notification_link = notification_link,school = school)
            newnotification.save()
        
        if request.method == 'POST' and 'Homework' in request.POST:
            
            homeworkform = HomeworkForm(request.POST)
            # teacher = request.POST.get('teacher')
            print('123')
            if homeworkform.is_valid():
                print('uor')
            homework_topic = request.POST.get('Homeworktopic','a')
    
            homework_detail = request.POST.get('Homeworkdetail','')
            homework_class = request.POST.get('Homeworkclass',0)
            homework_school = teacher_school
            homework = Homework(teacher=teacher,homework_topic=homework_topic,homework_detail=homework_detail,homework_class=homework_class,homework_school=homework_school)
            homework.save()
        
        if request.method == 'POST' and 'Onlineclass' in request.POST:
            
            Onlineclassform = OnlineclassForm(request.POST)
            class_topic = request.POST.get('Onlineclasstopic','')
            class_app = request.POST.get('Onlineclassapp','')
            class_id = request.POST.get('Onlineclassid','')
            class_password = request.POST.get('Onlineclasspassword','')
            class_details= request.POST.get('Onlineclassdetail','')
            teacher = teacher
            onlineclass = Onlineclass(class_topic = class_topic,class_app= class_app,class_id=class_id,class_password=class_password,class_details=class_details,teacher=teacher)
            onlineclass.save()
        if request.method == 'POST' and 'Notes' in request.POST:
            
            Notesform = NotesForm(request.POST)
            notes_link = request.POST.get('Noteslink')
            notes_subject1 = request.POST.get('Notessubject')
            notes_topic = request.POST.get('Notestopic')
            notes_teacher = teacher
            notes_subject = Subject.objects.get(subject = notes_subject1)
            print(type(notes_subject))

            notes = Notes(notes_link = notes_link,notes_teacher = notes_teacher , notes_subject = notes_subject , notes_topic = notes_topic)
            notes.save()
        
        if request.method == 'POST' and 'Admission' in request.POST:
            
            Enrollform = EnrollForm(request.POST)
            
            teacher = teacher
            enroll_form_link = request.POST.get('Admissionlink')
            enroll_school_name = teacher_school
            enroll_form_subject = request.POST.get('Admissionsubject')
            enroll = Enroll(teacher = teacher, enroll_form_link = enroll_form_link,enroll_school_name = enroll_school_name,enroll_form_subject = enroll_form_subject)
            enroll.save()
        
        if request.method == 'POST' and 'Aboutus' in request.POST:
             
            AboutusForm = AboutUsSchoolForm(request.POST)
            heading = request.POST.get('heading')
            description =  request.POST.get('description')
            school = teacher_school

            Aboutus = AboutUsSchool(heading = heading , description = description, school = school)
            Aboutus.save()
        
        if request.method == 'POST' and 'Facilities' in request.POST:

            Facilitiesform = FacilitiesForm(request.POST)
            heading = request.POST.get('heading')
            description = request.POST.get('description')
            school = teacher_school
            
            facilities = Facilities(heading = heading,description=description,school=school)
            facilities.save()

        if request.method == 'POST' and 'Achievements' in request.POST:

            Achievementsform = AchievementsForm(request.POST)
            heading = request.POST.get('heading')
            description = request.POST.get('description')
            school = teacher_school

            achievements = Achievements(heading=heading,description=description,school=school)
            achievements.save()


    school_name = teacher.school.school_name
    print(school_name)
    params = {'class1':class1,'school_name':school_name,'no_of_students':no_of_students,'students':students,'subjects':subjects}
        
    return render(request,'schools/teacher_class.html',params)


# Student Home page View
@login_required
@permission_required('schools.view_student')
def student_home(request,stu_roll_no):
    if request.user.is_authenticated:

        student = Student.objects.get(stu_roll_no = stu_roll_no)
        if student.student_user != request.user:            
            raise Http404
        school = Schools.objects.get(school_id2 =student.student_school.school_id2 )

        teachers = Teacher.objects.filter(school = school) 


        # Student related Teachers------>
        student_related_teachers = []
        for teacher in teachers:
            teacher_classes = teacher.teacher_class.split(',')
            if student.stu_class in teacher_classes:
                student_related_teachers.append(teacher)

        # Online Classes Schedule ---------->
        onlineclasses = []
        for teacher1 in student_related_teachers:
            onlineclass = Onlineclass.objects.filter(teacher = teacher1)
            if onlineclass != None:
                onlineclasses.append(onlineclass)

        # Homework ----->
        homeworks = []
        for teacher1 in student_related_teachers:
            homework = Homework.objects.filter(teacher = teacher1)
            homeworks.append(homework)

        
        # Notes ------------->
        notes = []
        subject_of_notes = set()
        for teacher1 in student_related_teachers:
            note = Notes.objects.filter(notes_teacher = teacher1)
            notes.append(note)
            for i in note:
                subject_of_notes.add(i.notes_subject)
        
        params = {'onlineclasses':onlineclasses,'homeworks':homeworks,'student':student,'notes':notes,'subject_of_notes': subject_of_notes}
        print(school)
        print(onlineclasses)
        # Onlineclasses = Onlineclass.objects.get('')
    return render(request,'schools/student_home.html',params)

def buy(request):
    products = Product.objects.all()
    params={'products':products}
    return render(request,'schools/buy.html',params)

            
        
     




























