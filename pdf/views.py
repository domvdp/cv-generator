from django.shortcuts import render
from .models import Profile
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
import pdfkit
import os, sys, subprocess, platform
from django.views.decorators.clickjacking import xframe_options_exempt

# Create your views here.
def about(request):
    return render(request, 'about.html', {'title': 'About'})

def privacy_policy(request):
    return render(request, 'privacy_policy.html', {'title': 'Privacy Policy'})

def cookies_policy(request):
    return render(request, 'cookies_policy.html', {'title': 'Cookies Policy'})

def customer_service_form(request):
    if request.method == "POST":
        sum_1 = request.POST.get("sum_1", "")
        sum_2 = request.POST.get("sum_2", "")
        sum_3 = request.POST.get("sum_3", "")

        company_1 = request.POST.get("company_1", "")
        job_1 = request.POST.get("job_1", "")
        work_start_1 = request.POST.get("work_start_1", "")
        work_end_1 = request.POST.get("work_end_1", "")
        work_1a = request.POST.get("work_1a", "")
        work_1c = request.POST.get("work_1c", "")
        work_1e = request.POST.get("work_1e", "")

        company_2 = request.POST.get("company_2", "")
        job_2 = request.POST.get("job_2", "")
        work_start_2 = request.POST.get("work_start_2", "")
        work_end_2 = request.POST.get("work_end_2", "")
        work_2a = request.POST.get("work_2a", "")
        work_2c = request.POST.get("work_2c", "")
        work_2e = request.POST.get("work_2e", "")

        company_3 = request.POST.get("company_3", "")
        job_3 = request.POST.get("job_3", "")
        work_start_3 = request.POST.get("work_start_3", "")
        work_end_3 = request.POST.get("work_end_3", "")
        work_3a = request.POST.get("work_3a", "")
        work_3c = request.POST.get("work_3c", "")
        work_3e = request.POST.get("work_3e", "")

        company_4 = request.POST.get("company_4", "")
        job_4 = request.POST.get("job_4", "")
        work_start_4 = request.POST.get("work_start_4", "")
        work_end_4 = request.POST.get("work_end_4", "")
        work_4a = request.POST.get("work_4a", "")
        work_4c = request.POST.get("work_4c", "")
        work_4e = request.POST.get("work_4e", "")

        college_name = request.POST.get("college_name", "")
        college_course_type = request.POST.get("college_course_type", "")
        college_course_name = request.POST.get("college_course_name", "")
        college_grade = request.POST.get("college_grade", "")
        college_start = request.POST.get("college_start", "")
        college_end = request.POST.get("college_end", "")
        college_modules = request.POST.get("college_modules", "")
        college_notable = request.POST.get("college_notable", "")
        college_societies = request.POST.get("college_societies", "")

        upper_school_name = request.POST.get("upper_school_name", "")
        upper_school_start = request.POST.get("upper_school_start", "")
        upper_school_end = request.POST.get("upper_school_end", "")

        upper_school_subject_type_1 = request.POST.get("upper_school_subject_type_1", "")
        upper_school_subject_name_1 = request.POST.get("upper_school_subject_name_1", "")
        upper_school_subject_grade_1 = request.POST.get("upper_school_subject_grade_1", "")

        upper_school_subject_type_2 = request.POST.get("upper_school_subject_type_2", "")
        upper_school_subject_name_2 = request.POST.get("upper_school_subject_name_2", "")
        upper_school_subject_grade_2 = request.POST.get("upper_school_subject_grade_2", "")

        upper_school_subject_type_3 = request.POST.get("upper_school_subject_type_3", "")
        upper_school_subject_name_3 = request.POST.get("upper_school_subject_name_3", "")
        upper_school_subject_grade_3 = request.POST.get("upper_school_subject_grade_3", "")

        upper_school_subject_type_4 = request.POST.get("upper_school_subject_type_4", "")
        upper_school_subject_name_4 = request.POST.get("upper_school_subject_name_4", "")
        upper_school_subject_grade_4 = request.POST.get("upper_school_subject_grade_4", "")

        upper_school_subject_type_5 = request.POST.get("upper_school_subject_type_5", "")
        upper_school_subject_name_5 = request.POST.get("upper_school_subject_name_5", "")
        upper_school_subject_grade_5 = request.POST.get("upper_school_subject_grade_5", "")

        upper_school_clubs = request.POST.get("upper_school_clubs", "")

        lower_school_name = request.POST.get("lower_school_name", "")

        lower_school_start = request.POST.get("lower_school_start", "")
        lower_school_end = request.POST.get("lower_school_end", "")

        lower_school_subject_type_1 = request.POST.get("lower_school_subject_type_1", "")
        lower_school_subject_name_1 = request.POST.get("lower_school_subject_name_1", "")
        lower_school_subject_grade_1 = request.POST.get("lower_school_subject_grade_1", "")

        lower_school_subject_type_2 = request.POST.get("lower_school_subject_type_2", "")
        lower_school_subject_name_2 = request.POST.get("lower_school_subject_name_2", "")
        lower_school_subject_grade_2 = request.POST.get("lower_school_subject_grade_2", "")

        lower_school_subject_type_3 = request.POST.get("lower_school_subject_type_3", "")
        lower_school_subject_name_3 = request.POST.get("lower_school_subject_name_3", "")
        lower_school_subject_grade_3 = request.POST.get("lower_school_subject_grade_3", "")

        lower_school_subject_type_4 = request.POST.get("lower_school_subject_type_4", "")
        lower_school_subject_name_4 = request.POST.get("lower_school_subject_name_4", "")
        lower_school_subject_grade_4 = request.POST.get("lower_school_subject_grade_4", "")

        lower_school_subject_type_5 = request.POST.get("lower_school_subject_type_5", "")
        lower_school_subject_name_5 = request.POST.get("lower_school_subject_name_5", "")
        lower_school_subject_grade_5 = request.POST.get("lower_school_subject_grade_5", "")

        lower_school_subject_type_6 = request.POST.get("lower_school_subject_type_6", "")
        lower_school_subject_name_6 = request.POST.get("lower_school_subject_name_6", "")
        lower_school_subject_grade_6 = request.POST.get("lower_school_subject_grade_6", "")

        lower_school_subject_type_7 = request.POST.get("lower_school_subject_type_7", "")
        lower_school_subject_name_7 = request.POST.get("lower_school_subject_name_7", "")
        lower_school_subject_grade_7 = request.POST.get("lower_school_subject_grade_7", "")

        lower_school_subject_type_8 = request.POST.get("lower_school_subject_type_8", "")
        lower_school_subject_name_8 = request.POST.get("lower_school_subject_name_8", "")
        lower_school_subject_grade_8 = request.POST.get("lower_school_subject_grade_8", "")

        lower_school_subject_type_9 = request.POST.get("lower_school_subject_type_9", "")
        lower_school_subject_name_9 = request.POST.get("lower_school_subject_name_9", "")
        lower_school_subject_grade_9 = request.POST.get("lower_school_subject_grade_9", "")

        lower_school_subject_type_10 = request.POST.get("lower_school_subject_type_10", "")
        lower_school_subject_name_10 = request.POST.get("lower_school_subject_name_10", "")
        lower_school_subject_grade_10 = request.POST.get("lower_school_subject_grade_10", "")

        lower_school_subject_type_11 = request.POST.get("lower_school_subject_type_11", "")
        lower_school_subject_name_11 = request.POST.get("lower_school_subject_name_11", "")
        lower_school_subject_grade_11 = request.POST.get("lower_school_subject_grade_11", "")

        lower_school_clubs = request.POST.get("lower_school_clubs", "")

        cert_1 = request.POST.get("cert_1", "")
        cert_date_1 = request.POST.get("cert_date_1", "")
        cert_2 = request.POST.get("cert_2", "")
        cert_date_2 = request.POST.get("cert_date_2", "")
        cert_3 = request.POST.get("cert_3", "")
        cert_date_3 = request.POST.get("cert_date_3", "")

        activity_1 = request.POST.get("activity_1", "")

        tech_skills = request.POST.get("tech_skills", "")

        language_1 = request.POST.get("language_1", "")
        fluency_1 = request.POST.get("fluency_1", "")
        language_2 = request.POST.get("language_2", "")
        fluency_2 = request.POST.get("fluency_2", "")
        language_3 = request.POST.get("language_3", "")
        fluency_3 = request.POST.get("fluency_3", "")
        language_4 = request.POST.get("language_4", "")
        fluency_4 = request.POST.get("fluency_4", "")

        profile = Profile(
            sum_1=sum_1, sum_2=sum_2, sum_3=sum_3,

            company_1=company_1, job_1=job_1, work_start_1=work_start_1, work_end_1=work_end_1, work_1a=work_1a, work_1c=work_1c, work_1e=work_1e,

            company_2=company_2, job_2=job_2, work_start_2=work_start_2, work_end_2=work_end_2, work_2a=work_2a, work_2c=work_2c, work_2e=work_2e,

            company_3=company_3, job_3=job_3, work_start_3=work_start_3, work_end_3=work_end_3, work_3a=work_3a, work_3c=work_3c, work_3e=work_3e,

            company_4=company_4, job_4=job_4, work_start_4=work_start_4, work_end_4=work_end_4, work_4a=work_4a, work_4c=work_4c, work_4e=work_4e,

            college_name=college_name, college_course_type=college_course_type, college_course_name=college_course_name, college_start=college_start, college_grade=college_grade, college_end=college_end, college_modules=college_modules, college_notable=college_notable, college_societies=college_societies,

            upper_school_name=upper_school_name,

            upper_school_start=upper_school_start, upper_school_end=upper_school_end,

            upper_school_subject_type_1=upper_school_subject_type_1, upper_school_subject_name_1=upper_school_subject_name_1, upper_school_subject_grade_1=upper_school_subject_grade_1,

            upper_school_subject_type_2=upper_school_subject_type_2, upper_school_subject_name_2=upper_school_subject_name_2, upper_school_subject_grade_2=upper_school_subject_grade_2,

            upper_school_subject_type_3=upper_school_subject_type_3, upper_school_subject_name_3=upper_school_subject_name_3, upper_school_subject_grade_3=upper_school_subject_grade_3,

            upper_school_subject_type_4=upper_school_subject_type_4, upper_school_subject_name_4=upper_school_subject_name_4, upper_school_subject_grade_4=upper_school_subject_grade_4,

            upper_school_subject_type_5=upper_school_subject_type_5, upper_school_subject_name_5=upper_school_subject_name_5, upper_school_subject_grade_5=upper_school_subject_grade_5,

            upper_school_clubs=upper_school_clubs,

            lower_school_name=lower_school_name,

            lower_school_start=lower_school_start, lower_school_end=lower_school_end,

            lower_school_subject_type_1=lower_school_subject_type_1, lower_school_subject_name_1=lower_school_subject_name_1, lower_school_subject_grade_1=lower_school_subject_grade_1,

            lower_school_subject_type_2=lower_school_subject_type_2, lower_school_subject_name_2=lower_school_subject_name_2, lower_school_subject_grade_2=lower_school_subject_grade_2,

            lower_school_subject_type_3=lower_school_subject_type_3, lower_school_subject_name_3=lower_school_subject_name_3, lower_school_subject_grade_3=lower_school_subject_grade_3,

            lower_school_subject_type_4=lower_school_subject_type_4, lower_school_subject_name_4=lower_school_subject_name_4, lower_school_subject_grade_4=lower_school_subject_grade_4,

            lower_school_subject_type_5=lower_school_subject_type_5, lower_school_subject_name_5=lower_school_subject_name_5, lower_school_subject_grade_5=lower_school_subject_grade_5,

            lower_school_subject_type_6=lower_school_subject_type_6, lower_school_subject_name_6=lower_school_subject_name_6, lower_school_subject_grade_6=lower_school_subject_grade_6,

            lower_school_subject_type_7=lower_school_subject_type_7, lower_school_subject_name_7=lower_school_subject_name_7, lower_school_subject_grade_7=lower_school_subject_grade_7,

            lower_school_subject_type_8=lower_school_subject_type_8, lower_school_subject_name_8=lower_school_subject_name_8, lower_school_subject_grade_8=lower_school_subject_grade_8,

            lower_school_subject_type_9=lower_school_subject_type_9, lower_school_subject_name_9=lower_school_subject_name_9, lower_school_subject_grade_9=lower_school_subject_grade_9,

            lower_school_subject_type_10=lower_school_subject_type_10, lower_school_subject_name_10=lower_school_subject_name_10, lower_school_subject_grade_10=lower_school_subject_grade_10,

            lower_school_subject_type_11=lower_school_subject_type_11, lower_school_subject_name_11=lower_school_subject_name_11, lower_school_subject_grade_11=lower_school_subject_grade_11,

            lower_school_clubs=lower_school_clubs,

            cert_1=cert_1, cert_date_1=cert_date_1, cert_2=cert_2, cert_date_2=cert_date_2, cert_3=cert_3, cert_date_3=cert_date_3,

            activity_1=activity_1,

            tech_skills=tech_skills,

            language_1=language_1, fluency_1=fluency_1, language_2=language_2, fluency_2=fluency_2, language_3=language_3, fluency_3=fluency_3, language_4=language_4, fluency_4=fluency_4,
        )

        profile.save()

        return HttpResponseRedirect('../customer_service_resume')
    return render(request, 'customer_service_form.html', {'title': 'Customer Service CV'})


def construction_form(request):
    if request.method == "POST":
        sum_1 = request.POST.get("sum_1", "")

        construction_sum_1 = request.POST.get("construction_sum_1", "")
        construction_sum_2 = request.POST.get("construction_sum_2", "")
        construction_sum_3 = request.POST.get("construction_sum_3", "")
        construction_sum_4 = request.POST.get("construction_sum_4", "")
        construction_sum_5 = request.POST.get("construction_sum_5", "")

        company_1 = request.POST.get("company_1", "")
        job_1 = request.POST.get("job_1", "")
        work_start_1 = request.POST.get("work_start_1", "")
        work_end_1 = request.POST.get("work_end_1", "")
        work_1a = request.POST.get("work_1a", "")
        work_1c = request.POST.get("work_1c", "")
        work_1e = request.POST.get("work_1e", "")

        company_2 = request.POST.get("company_2", "")
        job_2 = request.POST.get("job_2", "")
        work_start_2 = request.POST.get("work_start_2", "")
        work_end_2 = request.POST.get("work_end_2", "")
        work_2a = request.POST.get("work_2a", "")
        work_2c = request.POST.get("work_2c", "")
        work_2e = request.POST.get("work_2e", "")

        company_3 = request.POST.get("company_3", "")
        job_3 = request.POST.get("job_3", "")
        work_start_3 = request.POST.get("work_start_3", "")
        work_end_3 = request.POST.get("work_end_3", "")
        work_3a = request.POST.get("work_3a", "")
        work_3c = request.POST.get("work_3c", "")
        work_3e = request.POST.get("work_3e", "")

        company_4 = request.POST.get("company_4", "")
        job_4 = request.POST.get("job_4", "")
        work_start_4 = request.POST.get("work_start_4", "")
        work_end_4 = request.POST.get("work_end_4", "")
        work_4a = request.POST.get("work_4a", "")
        work_4c = request.POST.get("work_4c", "")
        work_4e = request.POST.get("work_4e", "")

        college_name = request.POST.get("college_name", "")
        college_course_type = request.POST.get("college_course_type", "")
        college_course_name = request.POST.get("college_course_name", "")
        college_grade = request.POST.get("college_grade", "")
        college_start = request.POST.get("college_start", "")
        college_end = request.POST.get("college_end", "")
        college_modules = request.POST.get("college_modules", "")
        college_notable = request.POST.get("college_notable", "")
        college_societies = request.POST.get("college_societies", "")

        upper_school_name = request.POST.get("upper_school_name", "")
        upper_school_start = request.POST.get("upper_school_start", "")
        upper_school_end = request.POST.get("upper_school_end", "")

        upper_school_subject_type_1 = request.POST.get("upper_school_subject_type_1", "")
        upper_school_subject_name_1 = request.POST.get("upper_school_subject_name_1", "")
        upper_school_subject_grade_1 = request.POST.get("upper_school_subject_grade_1", "")

        upper_school_subject_type_2 = request.POST.get("upper_school_subject_type_2", "")
        upper_school_subject_name_2 = request.POST.get("upper_school_subject_name_2", "")
        upper_school_subject_grade_2 = request.POST.get("upper_school_subject_grade_2", "")

        upper_school_subject_type_3 = request.POST.get("upper_school_subject_type_3", "")
        upper_school_subject_name_3 = request.POST.get("upper_school_subject_name_3", "")
        upper_school_subject_grade_3 = request.POST.get("upper_school_subject_grade_3", "")

        upper_school_subject_type_4 = request.POST.get("upper_school_subject_type_4", "")
        upper_school_subject_name_4 = request.POST.get("upper_school_subject_name_4", "")
        upper_school_subject_grade_4 = request.POST.get("upper_school_subject_grade_4", "")

        upper_school_subject_type_5 = request.POST.get("upper_school_subject_type_5", "")
        upper_school_subject_name_5 = request.POST.get("upper_school_subject_name_5", "")
        upper_school_subject_grade_5 = request.POST.get("upper_school_subject_grade_5", "")

        upper_school_clubs = request.POST.get("upper_school_clubs", "")

        lower_school_name = request.POST.get("lower_school_name", "")

        lower_school_start = request.POST.get("lower_school_start", "")
        lower_school_end = request.POST.get("lower_school_end", "")

        lower_school_subject_type_1 = request.POST.get("lower_school_subject_type_1", "")
        lower_school_subject_name_1 = request.POST.get("lower_school_subject_name_1", "")
        lower_school_subject_grade_1 = request.POST.get("lower_school_subject_grade_1", "")

        lower_school_subject_type_2 = request.POST.get("lower_school_subject_type_2", "")
        lower_school_subject_name_2 = request.POST.get("lower_school_subject_name_2", "")
        lower_school_subject_grade_2 = request.POST.get("lower_school_subject_grade_2", "")

        lower_school_subject_type_3 = request.POST.get("lower_school_subject_type_3", "")
        lower_school_subject_name_3 = request.POST.get("lower_school_subject_name_3", "")
        lower_school_subject_grade_3 = request.POST.get("lower_school_subject_grade_3", "")

        lower_school_subject_type_4 = request.POST.get("lower_school_subject_type_4", "")
        lower_school_subject_name_4 = request.POST.get("lower_school_subject_name_4", "")
        lower_school_subject_grade_4 = request.POST.get("lower_school_subject_grade_4", "")

        lower_school_subject_type_5 = request.POST.get("lower_school_subject_type_5", "")
        lower_school_subject_name_5 = request.POST.get("lower_school_subject_name_5", "")
        lower_school_subject_grade_5 = request.POST.get("lower_school_subject_grade_5", "")

        lower_school_subject_type_6 = request.POST.get("lower_school_subject_type_6", "")
        lower_school_subject_name_6 = request.POST.get("lower_school_subject_name_6", "")
        lower_school_subject_grade_6 = request.POST.get("lower_school_subject_grade_6", "")

        lower_school_subject_type_7 = request.POST.get("lower_school_subject_type_7", "")
        lower_school_subject_name_7 = request.POST.get("lower_school_subject_name_7", "")
        lower_school_subject_grade_7 = request.POST.get("lower_school_subject_grade_7", "")

        lower_school_subject_type_8 = request.POST.get("lower_school_subject_type_8", "")
        lower_school_subject_name_8 = request.POST.get("lower_school_subject_name_8", "")
        lower_school_subject_grade_8 = request.POST.get("lower_school_subject_grade_8", "")

        lower_school_subject_type_9 = request.POST.get("lower_school_subject_type_9", "")
        lower_school_subject_name_9 = request.POST.get("lower_school_subject_name_9", "")
        lower_school_subject_grade_9 = request.POST.get("lower_school_subject_grade_9", "")

        lower_school_subject_type_10 = request.POST.get("lower_school_subject_type_10", "")
        lower_school_subject_name_10 = request.POST.get("lower_school_subject_name_10", "")
        lower_school_subject_grade_10 = request.POST.get("lower_school_subject_grade_10", "")

        lower_school_subject_type_11 = request.POST.get("lower_school_subject_type_11", "")
        lower_school_subject_name_11 = request.POST.get("lower_school_subject_name_11", "")
        lower_school_subject_grade_11 = request.POST.get("lower_school_subject_grade_11", "")

        lower_school_clubs = request.POST.get("lower_school_clubs", "")

        cert_1 = request.POST.get("cert_1", "")
        cert_date_1 = request.POST.get("cert_date_1", "")
        cert_2 = request.POST.get("cert_2", "")
        cert_date_2 = request.POST.get("cert_date_2", "")
        cert_3 = request.POST.get("cert_3", "")
        cert_date_3 = request.POST.get("cert_date_3", "")

        activity_1 = request.POST.get("activity_1", "")

        tech_skills = request.POST.get("tech_skills", "")

        language_1 = request.POST.get("language_1", "")
        fluency_1 = request.POST.get("fluency_1", "")
        language_2 = request.POST.get("language_2", "")
        fluency_2 = request.POST.get("fluency_2", "")
        language_3 = request.POST.get("language_3", "")
        fluency_3 = request.POST.get("fluency_3", "")
        language_4 = request.POST.get("language_4", "")
        fluency_4 = request.POST.get("fluency_4", "")

        profile = Profile(
            sum_1=sum_1,

            construction_sum_1=construction_sum_1, construction_sum_2=construction_sum_2, construction_sum_3=construction_sum_3, construction_sum_4=construction_sum_4, construction_sum_5=construction_sum_5,

            company_1=company_1, job_1=job_1, work_start_1=work_start_1, work_end_1=work_end_1, work_1a=work_1a, work_1c=work_1c, work_1e=work_1e,

            company_2=company_2, job_2=job_2, work_start_2=work_start_2, work_end_2=work_end_2, work_2a=work_2a, work_2c=work_2c, work_2e=work_2e,

            company_3=company_3, job_3=job_3, work_start_3=work_start_3, work_end_3=work_end_3, work_3a=work_3a, work_3c=work_3c, work_3e=work_3e,

            company_4=company_4, job_4=job_4, work_start_4=work_start_4, work_end_4=work_end_4, work_4a=work_4a, work_4c=work_4c, work_4e=work_4e,

            college_name=college_name, college_course_type=college_course_type, college_course_name=college_course_name, college_start=college_start, college_grade=college_grade, college_end=college_end, college_modules=college_modules, college_notable=college_notable, college_societies=college_societies,

            upper_school_name=upper_school_name,

            upper_school_start=upper_school_start, upper_school_end=upper_school_end,

            upper_school_subject_type_1=upper_school_subject_type_1, upper_school_subject_name_1=upper_school_subject_name_1, upper_school_subject_grade_1=upper_school_subject_grade_1,

            upper_school_subject_type_2=upper_school_subject_type_2, upper_school_subject_name_2=upper_school_subject_name_2, upper_school_subject_grade_2=upper_school_subject_grade_2,

            upper_school_subject_type_3=upper_school_subject_type_3, upper_school_subject_name_3=upper_school_subject_name_3, upper_school_subject_grade_3=upper_school_subject_grade_3,

            upper_school_subject_type_4=upper_school_subject_type_4, upper_school_subject_name_4=upper_school_subject_name_4, upper_school_subject_grade_4=upper_school_subject_grade_4,

            upper_school_subject_type_5=upper_school_subject_type_5, upper_school_subject_name_5=upper_school_subject_name_5, upper_school_subject_grade_5=upper_school_subject_grade_5,

            upper_school_clubs=upper_school_clubs,

            lower_school_name=lower_school_name,

            lower_school_start=lower_school_start, lower_school_end=lower_school_end,

            lower_school_subject_type_1=lower_school_subject_type_1, lower_school_subject_name_1=lower_school_subject_name_1, lower_school_subject_grade_1=lower_school_subject_grade_1,

            lower_school_subject_type_2=lower_school_subject_type_2, lower_school_subject_name_2=lower_school_subject_name_2, lower_school_subject_grade_2=lower_school_subject_grade_2,

            lower_school_subject_type_3=lower_school_subject_type_3, lower_school_subject_name_3=lower_school_subject_name_3, lower_school_subject_grade_3=lower_school_subject_grade_3,

            lower_school_subject_type_4=lower_school_subject_type_4, lower_school_subject_name_4=lower_school_subject_name_4, lower_school_subject_grade_4=lower_school_subject_grade_4,

            lower_school_subject_type_5=lower_school_subject_type_5, lower_school_subject_name_5=lower_school_subject_name_5, lower_school_subject_grade_5=lower_school_subject_grade_5,

            lower_school_subject_type_6=lower_school_subject_type_6, lower_school_subject_name_6=lower_school_subject_name_6, lower_school_subject_grade_6=lower_school_subject_grade_6,

            lower_school_subject_type_7=lower_school_subject_type_7, lower_school_subject_name_7=lower_school_subject_name_7, lower_school_subject_grade_7=lower_school_subject_grade_7,

            lower_school_subject_type_8=lower_school_subject_type_8, lower_school_subject_name_8=lower_school_subject_name_8, lower_school_subject_grade_8=lower_school_subject_grade_8,

            lower_school_subject_type_9=lower_school_subject_type_9, lower_school_subject_name_9=lower_school_subject_name_9, lower_school_subject_grade_9=lower_school_subject_grade_9,

            lower_school_subject_type_10=lower_school_subject_type_10, lower_school_subject_name_10=lower_school_subject_name_10, lower_school_subject_grade_10=lower_school_subject_grade_10,

            lower_school_subject_type_11=lower_school_subject_type_11, lower_school_subject_name_11=lower_school_subject_name_11, lower_school_subject_grade_11=lower_school_subject_grade_11,

            lower_school_clubs=lower_school_clubs,

            cert_1=cert_1, cert_date_1=cert_date_1, cert_2=cert_2, cert_date_2=cert_date_2, cert_3=cert_3, cert_date_3=cert_date_3,

            activity_1=activity_1,

            tech_skills=tech_skills,

            language_1=language_1, fluency_1=fluency_1, language_2=language_2, fluency_2=fluency_2, language_3=language_3, fluency_3=fluency_3, language_4=language_4, fluency_4=fluency_4,
        )

        profile.save()

        return HttpResponseRedirect('../construction_resume')
    return render(request, 'construction_form.html', {'title': 'Construction CV'})


def security_form(request):
    if request.method == "POST":
        sum_1 = request.POST.get("sum_1", "")
        sum_2 = request.POST.get("sum_2", "")

        security_sum_1 = request.POST.get("security_sum_1", "")

        company_1 = request.POST.get("company_1", "")
        job_1 = request.POST.get("job_1", "")
        work_start_1 = request.POST.get("work_start_1", "")
        work_end_1 = request.POST.get("work_end_1", "")
        work_1a = request.POST.get("work_1a", "")
        work_1c = request.POST.get("work_1c", "")
        work_1e = request.POST.get("work_1e", "")

        company_2 = request.POST.get("company_2", "")
        job_2 = request.POST.get("job_2", "")
        work_start_2 = request.POST.get("work_start_2", "")
        work_end_2 = request.POST.get("work_end_2", "")
        work_2a = request.POST.get("work_2a", "")
        work_2c = request.POST.get("work_2c", "")
        work_2e = request.POST.get("work_2e", "")

        company_3 = request.POST.get("company_3", "")
        job_3 = request.POST.get("job_3", "")
        work_start_3 = request.POST.get("work_start_3", "")
        work_end_3 = request.POST.get("work_end_3", "")
        work_3a = request.POST.get("work_3a", "")
        work_3c = request.POST.get("work_3c", "")
        work_3e = request.POST.get("work_3e", "")

        company_4 = request.POST.get("company_4", "")
        job_4 = request.POST.get("job_4", "")
        work_start_4 = request.POST.get("work_start_4", "")
        work_end_4 = request.POST.get("work_end_4", "")
        work_4a = request.POST.get("work_4a", "")
        work_4c = request.POST.get("work_4c", "")
        work_4e = request.POST.get("work_4e", "")

        college_name = request.POST.get("college_name", "")
        college_course_type = request.POST.get("college_course_type", "")
        college_course_name = request.POST.get("college_course_name", "")
        college_grade = request.POST.get("college_grade", "")
        college_start = request.POST.get("college_start", "")
        college_end = request.POST.get("college_end", "")
        college_modules = request.POST.get("college_modules", "")
        college_notable = request.POST.get("college_notable", "")
        college_societies = request.POST.get("college_societies", "")

        upper_school_name = request.POST.get("upper_school_name", "")
        upper_school_start = request.POST.get("upper_school_start", "")
        upper_school_end = request.POST.get("upper_school_end", "")

        upper_school_subject_type_1 = request.POST.get("upper_school_subject_type_1", "")
        upper_school_subject_name_1 = request.POST.get("upper_school_subject_name_1", "")
        upper_school_subject_grade_1 = request.POST.get("upper_school_subject_grade_1", "")

        upper_school_subject_type_2 = request.POST.get("upper_school_subject_type_2", "")
        upper_school_subject_name_2 = request.POST.get("upper_school_subject_name_2", "")
        upper_school_subject_grade_2 = request.POST.get("upper_school_subject_grade_2", "")

        upper_school_subject_type_3 = request.POST.get("upper_school_subject_type_3", "")
        upper_school_subject_name_3 = request.POST.get("upper_school_subject_name_3", "")
        upper_school_subject_grade_3 = request.POST.get("upper_school_subject_grade_3", "")

        upper_school_subject_type_4 = request.POST.get("upper_school_subject_type_4", "")
        upper_school_subject_name_4 = request.POST.get("upper_school_subject_name_4", "")
        upper_school_subject_grade_4 = request.POST.get("upper_school_subject_grade_4", "")

        upper_school_subject_type_5 = request.POST.get("upper_school_subject_type_5", "")
        upper_school_subject_name_5 = request.POST.get("upper_school_subject_name_5", "")
        upper_school_subject_grade_5 = request.POST.get("upper_school_subject_grade_5", "")

        upper_school_clubs = request.POST.get("upper_school_clubs", "")

        lower_school_name = request.POST.get("lower_school_name", "")

        lower_school_start = request.POST.get("lower_school_start", "")
        lower_school_end = request.POST.get("lower_school_end", "")

        lower_school_subject_type_1 = request.POST.get("lower_school_subject_type_1", "")
        lower_school_subject_name_1 = request.POST.get("lower_school_subject_name_1", "")
        lower_school_subject_grade_1 = request.POST.get("lower_school_subject_grade_1", "")

        lower_school_subject_type_2 = request.POST.get("lower_school_subject_type_2", "")
        lower_school_subject_name_2 = request.POST.get("lower_school_subject_name_2", "")
        lower_school_subject_grade_2 = request.POST.get("lower_school_subject_grade_2", "")

        lower_school_subject_type_3 = request.POST.get("lower_school_subject_type_3", "")
        lower_school_subject_name_3 = request.POST.get("lower_school_subject_name_3", "")
        lower_school_subject_grade_3 = request.POST.get("lower_school_subject_grade_3", "")

        lower_school_subject_type_4 = request.POST.get("lower_school_subject_type_4", "")
        lower_school_subject_name_4 = request.POST.get("lower_school_subject_name_4", "")
        lower_school_subject_grade_4 = request.POST.get("lower_school_subject_grade_4", "")

        lower_school_subject_type_5 = request.POST.get("lower_school_subject_type_5", "")
        lower_school_subject_name_5 = request.POST.get("lower_school_subject_name_5", "")
        lower_school_subject_grade_5 = request.POST.get("lower_school_subject_grade_5", "")

        lower_school_subject_type_6 = request.POST.get("lower_school_subject_type_6", "")
        lower_school_subject_name_6 = request.POST.get("lower_school_subject_name_6", "")
        lower_school_subject_grade_6 = request.POST.get("lower_school_subject_grade_6", "")

        lower_school_subject_type_7 = request.POST.get("lower_school_subject_type_7", "")
        lower_school_subject_name_7 = request.POST.get("lower_school_subject_name_7", "")
        lower_school_subject_grade_7 = request.POST.get("lower_school_subject_grade_7", "")

        lower_school_subject_type_8 = request.POST.get("lower_school_subject_type_8", "")
        lower_school_subject_name_8 = request.POST.get("lower_school_subject_name_8", "")
        lower_school_subject_grade_8 = request.POST.get("lower_school_subject_grade_8", "")

        lower_school_subject_type_9 = request.POST.get("lower_school_subject_type_9", "")
        lower_school_subject_name_9 = request.POST.get("lower_school_subject_name_9", "")
        lower_school_subject_grade_9 = request.POST.get("lower_school_subject_grade_9", "")

        lower_school_subject_type_10 = request.POST.get("lower_school_subject_type_10", "")
        lower_school_subject_name_10 = request.POST.get("lower_school_subject_name_10", "")
        lower_school_subject_grade_10 = request.POST.get("lower_school_subject_grade_10", "")

        lower_school_subject_type_11 = request.POST.get("lower_school_subject_type_11", "")
        lower_school_subject_name_11 = request.POST.get("lower_school_subject_name_11", "")
        lower_school_subject_grade_11 = request.POST.get("lower_school_subject_grade_11", "")

        lower_school_clubs = request.POST.get("lower_school_clubs", "")

        cert_1 = request.POST.get("cert_1", "")
        cert_date_1 = request.POST.get("cert_date_1", "")
        cert_2 = request.POST.get("cert_2", "")
        cert_date_2 = request.POST.get("cert_date_2", "")
        cert_3 = request.POST.get("cert_3", "")
        cert_date_3 = request.POST.get("cert_date_3", "")

        activity_1 = request.POST.get("activity_1", "")

        tech_skills = request.POST.get("tech_skills", "")

        language_1 = request.POST.get("language_1", "")
        fluency_1 = request.POST.get("fluency_1", "")
        language_2 = request.POST.get("language_2", "")
        fluency_2 = request.POST.get("fluency_2", "")
        language_3 = request.POST.get("language_3", "")
        fluency_3 = request.POST.get("fluency_3", "")
        language_4 = request.POST.get("language_4", "")
        fluency_4 = request.POST.get("fluency_4", "")

        profile = Profile(
            sum_1=sum_1, sum_2=sum_2,

            security_sum_1=security_sum_1,

            company_1=company_1, job_1=job_1, work_start_1=work_start_1, work_end_1=work_end_1, work_1a=work_1a, work_1c=work_1c, work_1e=work_1e,

            company_2=company_2, job_2=job_2, work_start_2=work_start_2, work_end_2=work_end_2, work_2a=work_2a, work_2c=work_2c, work_2e=work_2e,

            company_3=company_3, job_3=job_3, work_start_3=work_start_3, work_end_3=work_end_3, work_3a=work_3a, work_3c=work_3c, work_3e=work_3e,

            company_4=company_4, job_4=job_4, work_start_4=work_start_4, work_end_4=work_end_4, work_4a=work_4a, work_4c=work_4c, work_4e=work_4e,

            college_name=college_name, college_course_type=college_course_type, college_course_name=college_course_name, college_start=college_start, college_grade=college_grade, college_end=college_end, college_modules=college_modules, college_notable=college_notable, college_societies=college_societies,

            upper_school_name=upper_school_name,

            upper_school_start=upper_school_start, upper_school_end=upper_school_end,

            upper_school_subject_type_1=upper_school_subject_type_1, upper_school_subject_name_1=upper_school_subject_name_1, upper_school_subject_grade_1=upper_school_subject_grade_1,

            upper_school_subject_type_2=upper_school_subject_type_2, upper_school_subject_name_2=upper_school_subject_name_2, upper_school_subject_grade_2=upper_school_subject_grade_2,

            upper_school_subject_type_3=upper_school_subject_type_3, upper_school_subject_name_3=upper_school_subject_name_3, upper_school_subject_grade_3=upper_school_subject_grade_3,

            upper_school_subject_type_4=upper_school_subject_type_4, upper_school_subject_name_4=upper_school_subject_name_4, upper_school_subject_grade_4=upper_school_subject_grade_4,

            upper_school_subject_type_5=upper_school_subject_type_5, upper_school_subject_name_5=upper_school_subject_name_5, upper_school_subject_grade_5=upper_school_subject_grade_5,

            upper_school_clubs=upper_school_clubs,

            lower_school_name=lower_school_name,

            lower_school_start=lower_school_start, lower_school_end=lower_school_end,

            lower_school_subject_type_1=lower_school_subject_type_1, lower_school_subject_name_1=lower_school_subject_name_1, lower_school_subject_grade_1=lower_school_subject_grade_1,

            lower_school_subject_type_2=lower_school_subject_type_2, lower_school_subject_name_2=lower_school_subject_name_2, lower_school_subject_grade_2=lower_school_subject_grade_2,

            lower_school_subject_type_3=lower_school_subject_type_3, lower_school_subject_name_3=lower_school_subject_name_3, lower_school_subject_grade_3=lower_school_subject_grade_3,

            lower_school_subject_type_4=lower_school_subject_type_4, lower_school_subject_name_4=lower_school_subject_name_4, lower_school_subject_grade_4=lower_school_subject_grade_4,

            lower_school_subject_type_5=lower_school_subject_type_5, lower_school_subject_name_5=lower_school_subject_name_5, lower_school_subject_grade_5=lower_school_subject_grade_5,

            lower_school_subject_type_6=lower_school_subject_type_6, lower_school_subject_name_6=lower_school_subject_name_6, lower_school_subject_grade_6=lower_school_subject_grade_6,

            lower_school_subject_type_7=lower_school_subject_type_7, lower_school_subject_name_7=lower_school_subject_name_7, lower_school_subject_grade_7=lower_school_subject_grade_7,

            lower_school_subject_type_8=lower_school_subject_type_8, lower_school_subject_name_8=lower_school_subject_name_8, lower_school_subject_grade_8=lower_school_subject_grade_8,

            lower_school_subject_type_9=lower_school_subject_type_9, lower_school_subject_name_9=lower_school_subject_name_9, lower_school_subject_grade_9=lower_school_subject_grade_9,

            lower_school_subject_type_10=lower_school_subject_type_10, lower_school_subject_name_10=lower_school_subject_name_10, lower_school_subject_grade_10=lower_school_subject_grade_10,

            lower_school_subject_type_11=lower_school_subject_type_11, lower_school_subject_name_11=lower_school_subject_name_11, lower_school_subject_grade_11=lower_school_subject_grade_11,

            lower_school_clubs=lower_school_clubs,

            cert_1=cert_1, cert_date_1=cert_date_1, cert_2=cert_2, cert_date_2=cert_date_2, cert_3=cert_3, cert_date_3=cert_date_3,

            activity_1=activity_1,

            tech_skills=tech_skills,

            language_1=language_1, fluency_1=fluency_1, language_2=language_2, fluency_2=fluency_2, language_3=language_3, fluency_3=fluency_3, language_4=language_4, fluency_4=fluency_4,
        )

        profile.save()

        return HttpResponseRedirect('../security_resume')
    return render(request, 'security_form.html', {'title': 'Security CV'})


def customer_service_resume(request):
    # wkhtmltopdf lives and functions differently depending on Windows or Linux.
    # We need to support both since we develop on windows but deploy on Heroku,
    # which uses Linux.
    if platform.system() == "Windows":
        config = pdfkit.configuration(wkhtmltopdf=os.environ.get('WKHTMLTOPDF_BINARY', 'wkhtmltopdf\\bin\\wkhtmltopdf.exe'))
    else:
        os.environ['PATH'] += os.pathsep + os.path.dirname(sys.executable)

        WKHTMLTOPDF_CMD = subprocess.Popen(['which', os.environ.get('WKHTMLTOPDF_BINARY', 'wkhtmltopdf-pack')], stdout=subprocess.PIPE).communicate()[0].strip()

        config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_CMD)

    #config = pdfkit.configuration(wkhtmltopdf="..\\myapp\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")

    template = get_template('customer_service_template.html')
    profile = Profile.objects.all()

    for profile in profile:
        context = {
            'sum_1': profile.sum_1,
            'sum_2': profile.sum_2,
            'sum_3': profile.sum_3,

            'company_1': profile.company_1,
            'job_1': profile.job_1,
            'work_start_1': profile.work_start_1,
            'work_end_1': profile.work_end_1,
            'work_1a': profile.work_1a,
            'work_1c': profile.work_1c,
            'work_1e': profile.work_1e,

            'company_2': profile.company_2,
            'job_2': profile.job_2,
            'work_start_2': profile.work_start_2,
            'work_end_2': profile.work_end_2,
            'work_2a': profile.work_2a,
            'work_2c': profile.work_2c,
            'work_2e': profile.work_2e,

            'company_3': profile.company_3,
            'job_3': profile.job_3,
            'work_start_3': profile.work_start_3,
            'work_end_3': profile.work_end_3,
            'work_3a': profile.work_3a,
            'work_3c': profile.work_3c,
            'work_3e': profile.work_3e,

            'company_4': profile.company_4,
            'job_4': profile.job_4,
            'work_start_4': profile.work_start_4,
            'work_end_4': profile.work_end_4,
            'work_4a': profile.work_4a,
            'work_4c': profile.work_4c,
            'work_4e': profile.work_4e,

            'college_name': profile.college_name,
            'college_course_type': profile.college_course_type,
            'college_course_name': profile.college_course_name,
            'college_start': profile.college_start,
            'college_grade': profile.college_grade,
            'college_end': profile.college_end,
            'college_modules': profile.college_modules,
            'college_notable': profile.college_notable,
            'college_societies': profile.college_societies,

            'upper_school_name': profile.upper_school_name,

            'upper_school_start': profile.upper_school_start,
            'upper_school_end': profile.upper_school_end,

            'upper_school_subject_type_1': profile.upper_school_subject_type_1,
            'upper_school_subject_name_1': profile.upper_school_subject_name_1,
            'upper_school_subject_grade_1': profile.upper_school_subject_grade_1,

            'upper_school_subject_type_2': profile.upper_school_subject_type_2,
            'upper_school_subject_name_2': profile.upper_school_subject_name_2,
            'upper_school_subject_grade_2': profile.upper_school_subject_grade_2,

            'upper_school_subject_type_3': profile.upper_school_subject_type_3,
            'upper_school_subject_name_3': profile.upper_school_subject_name_3,
            'upper_school_subject_grade_3': profile.upper_school_subject_grade_3,

            'upper_school_subject_type_4': profile.upper_school_subject_type_4,
            'upper_school_subject_name_4': profile.upper_school_subject_name_4,
            'upper_school_subject_grade_4': profile.upper_school_subject_grade_4,

            'upper_school_subject_type_5': profile.upper_school_subject_type_5,
            'upper_school_subject_name_5': profile.upper_school_subject_name_5,
            'upper_school_subject_grade_5': profile.upper_school_subject_grade_5,

            'upper_school_clubs': profile.upper_school_clubs,

            'lower_school_name': profile.lower_school_name,

            'lower_school_start': profile.lower_school_start,
            'lower_school_end': profile.lower_school_end,

            'lower_school_subject_type_1': profile.lower_school_subject_type_1,
            'lower_school_subject_name_1': profile.lower_school_subject_name_1,
            'lower_school_subject_grade_1': profile.lower_school_subject_grade_1,

            'lower_school_subject_type_2': profile.lower_school_subject_type_2,
            'lower_school_subject_name_2': profile.lower_school_subject_name_2,
            'lower_school_subject_grade_2': profile.lower_school_subject_grade_2,

            'lower_school_subject_type_3': profile.lower_school_subject_type_3,
            'lower_school_subject_name_3': profile.lower_school_subject_name_3,
            'lower_school_subject_grade_3': profile.lower_school_subject_grade_3,

            'lower_school_subject_type_4': profile.lower_school_subject_type_4,
            'lower_school_subject_name_4': profile.lower_school_subject_name_4,
            'lower_school_subject_grade_4': profile.lower_school_subject_grade_4,

            'lower_school_subject_type_5': profile.lower_school_subject_type_5,
            'lower_school_subject_name_5': profile.lower_school_subject_name_5,
            'lower_school_subject_grade_5': profile.lower_school_subject_grade_5,

            'lower_school_subject_type_6': profile.lower_school_subject_type_6,
            'lower_school_subject_name_6': profile.lower_school_subject_name_6,
            'lower_school_subject_grade_6': profile.lower_school_subject_grade_6,

            'lower_school_subject_type_7': profile.lower_school_subject_type_7,
            'lower_school_subject_name_7': profile.lower_school_subject_name_7,
            'lower_school_subject_grade_7': profile.lower_school_subject_grade_7,

            'lower_school_subject_type_8': profile.lower_school_subject_type_8,
            'lower_school_subject_name_8': profile.lower_school_subject_name_8,
            'lower_school_subject_grade_8': profile.lower_school_subject_grade_8,

            'lower_school_subject_type_9': profile.lower_school_subject_type_9,
            'lower_school_subject_name_9': profile.lower_school_subject_name_9,
            'lower_school_subject_grade_9': profile.lower_school_subject_grade_9,

            'lower_school_subject_type_10': profile.lower_school_subject_type_10,
            'lower_school_subject_name_10': profile.lower_school_subject_name_10,
            'lower_school_subject_grade_10': profile.lower_school_subject_grade_10,

            'lower_school_subject_type_11': profile.lower_school_subject_type_11,
            'lower_school_subject_name_11': profile.lower_school_subject_name_11,
            'lower_school_subject_grade_11': profile.lower_school_subject_grade_11,

            'lower_school_clubs': profile.lower_school_clubs,

            'cert_1': profile.cert_1,
            'cert_date_1': profile.cert_date_1,
            'cert_2': profile.cert_2,
            'cert_date_2': profile.cert_date_2,
            'cert_3': profile.cert_3,
            'cert_date_3': profile.cert_date_3,

            'activity_1': profile.activity_1,

            'tech_skills': profile.tech_skills,

            'language_1': profile.language_1,
            'fluency_1': profile.fluency_1,
            'language_2': profile.language_2,
            'fluency_2': profile.fluency_2,
            'language_3': profile.language_3,
            'fluency_3': profile.fluency_3,
            'language_4': profile.language_4,
            'fluency_4': profile.fluency_4,

            'work_1_list': [profile.work_1a, profile.work_1c, profile.work_1e],
            'work_2_list': [profile.work_2a, profile.work_2c, profile.work_2e],
            'work_3_list': [profile.work_3a, profile.work_3c, profile.work_3e],
            'work_4_list': [profile.work_4a, profile.work_4c, profile.work_4e],

            'work_skill_interpersonal_skills': "Displayed excellent interpersonal skills when dealing with customers to provide the best possible service.",
            'work_skill_verbal_and_written_communication': "Demonstrated effective levels of verbal and written communication in all levels of engagement.",
            'work_skill_persuasive': "Used persuasive skills effectively to drive sales whilst retaining a focus on excellent customer treatment.",
            'work_skill_customer_service': "Communicated with customers regularly to ensure the delivery of excellent service and quality of treatment.",
            'work_skill_deal_with_difficult_customers': "Dealt with difficult customer complaints in a patient and friendly manner whilst working to ensure an appropriate and timely resolution.",
            'work_skill_non_judgemental': "Dealt with customers from a variety of backgrounds and worked to ensure equal quality of treatment.",
            'work_skill_polite_and_approachable': "Provided an approachable, polite, and professional attitude towards all patrons.",
            'work_skill_friendly': "Ensured that all customers were met with a bubbly and friendly service.",
            'work_skill_enthusiastic': "Approached work with an enthusiastic, can-do, and positive attitude, with a willingness to undertake a variety of tasks.",
            'work_skill_confidence': "Provided excellent hospitality with a confident and well-poised approach.",
            'work_skill_works_well_under_pressure': "Worked well under pressure and responded positively to stressful situations whilst effectively managing deadlines and time sensitive tasks.",
            'work_skill_teamwork': "Demonstrated excellent collaboration skills whilst working as part of a team, as well as being able to work independently when required.",
            'work_skill_motivational': "Adopted an energetic approach to motivate and encourage colleagues, keeping morale high.",
            'work_skill_independent': "Worked independently to manage deliverables whilst also being able to work well as part of a team.",
            'work_skill_disciplined_time': "Maintained a high level of self-discipline, including excellent organisation and time management skills to ensure operations ran smoothly.",
            'work_skill_disciplined': "Displayed discipline and diligence whilst following instructions and ensured appropriate conduct in all situations.",
            'work_skill_organisation': "Demonstrated high levels of organisational skills whilst working hard to ensure that customer expectations were met in a timely and punctual manner.",
            'work_skill_language': "Communicated with customers from a range of diverse backgrounds, changing the engagement approach according to the situation whilst ensuring equal quality of treatment for all customers.",
            'work_skill_flexible_in_work': "Worked with flexiblity and the willingness to undertake a variety of tasks as and when required.",
            'work_skill_trustworthy': "Consistently delivered on responsibilities with trust, reliability, and regularity.",
            'work_skill_attention_to_detail': "Worked in an attentive and alert manner, displaying high awareness to observe the environment with high attention to detail.",
            'work_skill_problem_solving': "Practised the ability to solve unique problems as they arise.",
        }

    html = template.render(context)
    css = [
        '/home/domvdp/cv-generator/pdf/static/cv_template.css', # 'pdf/static/cv_template.css',
    ]

    # Save Resume as PDF within project
    pdfkit.from_string(html, 'CV Output.pdf', css=css, configuration=config)

    # Assign variable that allows PDF to be viewed by user on website
    pdf = pdfkit.from_string(html, False, css=css, configuration=config)

    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')

        return response
    return HttpResponse("Not found")


def construction_resume(request):
    # wkhtmltopdf lives and functions differently depending on Windows or Linux.
    # We need to support both since we develop on windows but deploy on Heroku,
    # which uses Linux.
    if platform.system() == "Windows":
        config = pdfkit.configuration(wkhtmltopdf=os.environ.get('WKHTMLTOPDF_BINARY', 'wkhtmltopdf\\bin\\wkhtmltopdf.exe'))
    else:
        os.environ['PATH'] += os.pathsep + os.path.dirname(sys.executable)

        WKHTMLTOPDF_CMD = subprocess.Popen(['which', os.environ.get('WKHTMLTOPDF_BINARY', 'wkhtmltopdf-pack')], stdout=subprocess.PIPE).communicate()[0].strip()

        config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_CMD)

    #config = pdfkit.configuration(wkhtmltopdf="..\\myapp\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")

    template = get_template('construction_template.html')
    profile = Profile.objects.all()

    for profile in profile:
        context = {
            'sum_1': profile.sum_1,

            'construction_sum_1': profile.construction_sum_1,
            'construction_sum_2': profile.construction_sum_2,
            'construction_sum_3': profile.construction_sum_3,
            'construction_sum_4': profile.construction_sum_4,
            'construction_sum_5': profile.construction_sum_5,

            'company_1': profile.company_1,
            'job_1': profile.job_1,
            'work_start_1': profile.work_start_1,
            'work_end_1': profile.work_end_1,
            'work_1a': profile.work_1a,
            'work_1c': profile.work_1c,
            'work_1e': profile.work_1e,

            'company_2': profile.company_2,
            'job_2': profile.job_2,
            'work_start_2': profile.work_start_2,
            'work_end_2': profile.work_end_2,
            'work_2a': profile.work_2a,
            'work_2c': profile.work_2c,
            'work_2e': profile.work_2e,

            'company_3': profile.company_3,
            'job_3': profile.job_3,
            'work_start_3': profile.work_start_3,
            'work_end_3': profile.work_end_3,
            'work_3a': profile.work_3a,
            'work_3c': profile.work_3c,
            'work_3e': profile.work_3e,

            'company_4': profile.company_4,
            'job_4': profile.job_4,
            'work_start_4': profile.work_start_4,
            'work_end_4': profile.work_end_4,
            'work_4a': profile.work_4a,
            'work_4c': profile.work_4c,
            'work_4e': profile.work_4e,

            'college_name': profile.college_name,
            'college_course_type': profile.college_course_type,
            'college_course_name': profile.college_course_name,
            'college_start': profile.college_start,
            'college_grade': profile.college_grade,
            'college_end': profile.college_end,
            'college_modules': profile.college_modules,
            'college_notable': profile.college_notable,
            'college_societies': profile.college_societies,

            'upper_school_name': profile.upper_school_name,

            'upper_school_start': profile.upper_school_start,
            'upper_school_end': profile.upper_school_end,

            'upper_school_subject_type_1': profile.upper_school_subject_type_1,
            'upper_school_subject_name_1': profile.upper_school_subject_name_1,
            'upper_school_subject_grade_1': profile.upper_school_subject_grade_1,

            'upper_school_subject_type_2': profile.upper_school_subject_type_2,
            'upper_school_subject_name_2': profile.upper_school_subject_name_2,
            'upper_school_subject_grade_2': profile.upper_school_subject_grade_2,

            'upper_school_subject_type_3': profile.upper_school_subject_type_3,
            'upper_school_subject_name_3': profile.upper_school_subject_name_3,
            'upper_school_subject_grade_3': profile.upper_school_subject_grade_3,

            'upper_school_subject_type_4': profile.upper_school_subject_type_4,
            'upper_school_subject_name_4': profile.upper_school_subject_name_4,
            'upper_school_subject_grade_4': profile.upper_school_subject_grade_4,

            'upper_school_subject_type_5': profile.upper_school_subject_type_5,
            'upper_school_subject_name_5': profile.upper_school_subject_name_5,
            'upper_school_subject_grade_5': profile.upper_school_subject_grade_5,

            'upper_school_clubs': profile.upper_school_clubs,

            'lower_school_name': profile.lower_school_name,

            'lower_school_start': profile.lower_school_start,
            'lower_school_end': profile.lower_school_end,

            'lower_school_subject_type_1': profile.lower_school_subject_type_1,
            'lower_school_subject_name_1': profile.lower_school_subject_name_1,
            'lower_school_subject_grade_1': profile.lower_school_subject_grade_1,

            'lower_school_subject_type_2': profile.lower_school_subject_type_2,
            'lower_school_subject_name_2': profile.lower_school_subject_name_2,
            'lower_school_subject_grade_2': profile.lower_school_subject_grade_2,

            'lower_school_subject_type_3': profile.lower_school_subject_type_3,
            'lower_school_subject_name_3': profile.lower_school_subject_name_3,
            'lower_school_subject_grade_3': profile.lower_school_subject_grade_3,

            'lower_school_subject_type_4': profile.lower_school_subject_type_4,
            'lower_school_subject_name_4': profile.lower_school_subject_name_4,
            'lower_school_subject_grade_4': profile.lower_school_subject_grade_4,

            'lower_school_subject_type_5': profile.lower_school_subject_type_5,
            'lower_school_subject_name_5': profile.lower_school_subject_name_5,
            'lower_school_subject_grade_5': profile.lower_school_subject_grade_5,

            'lower_school_subject_type_6': profile.lower_school_subject_type_6,
            'lower_school_subject_name_6': profile.lower_school_subject_name_6,
            'lower_school_subject_grade_6': profile.lower_school_subject_grade_6,

            'lower_school_subject_type_7': profile.lower_school_subject_type_7,
            'lower_school_subject_name_7': profile.lower_school_subject_name_7,
            'lower_school_subject_grade_7': profile.lower_school_subject_grade_7,

            'lower_school_subject_type_8': profile.lower_school_subject_type_8,
            'lower_school_subject_name_8': profile.lower_school_subject_name_8,
            'lower_school_subject_grade_8': profile.lower_school_subject_grade_8,

            'lower_school_subject_type_9': profile.lower_school_subject_type_9,
            'lower_school_subject_name_9': profile.lower_school_subject_name_9,
            'lower_school_subject_grade_9': profile.lower_school_subject_grade_9,

            'lower_school_subject_type_10': profile.lower_school_subject_type_10,
            'lower_school_subject_name_10': profile.lower_school_subject_name_10,
            'lower_school_subject_grade_10': profile.lower_school_subject_grade_10,

            'lower_school_subject_type_11': profile.lower_school_subject_type_11,
            'lower_school_subject_name_11': profile.lower_school_subject_name_11,
            'lower_school_subject_grade_11': profile.lower_school_subject_grade_11,

            'lower_school_clubs': profile.lower_school_clubs,

            'cert_1': profile.cert_1,
            'cert_date_1': profile.cert_date_1,
            'cert_2': profile.cert_2,
            'cert_date_2': profile.cert_date_2,
            'cert_3': profile.cert_3,
            'cert_date_3': profile.cert_date_3,

            'activity_1': profile.activity_1,

            'tech_skills': profile.tech_skills,

            'language_1': profile.language_1,
            'fluency_1': profile.fluency_1,
            'language_2': profile.language_2,
            'fluency_2': profile.fluency_2,
            'language_3': profile.language_3,
            'fluency_3': profile.fluency_3,
            'language_4': profile.language_4,
            'fluency_4': profile.fluency_4,

            'work_1_list': [profile.work_1a, profile.work_1c, profile.work_1e],
            'work_2_list': [profile.work_2a, profile.work_2c, profile.work_2e],
            'work_3_list': [profile.work_3a, profile.work_3c, profile.work_3e],
            'work_4_list': [profile.work_4a, profile.work_4c, profile.work_4e],

            'work_skill_plumbing_commercial': "Skilled in installing, repairing and maintaining commercial and/or industrial plumbing fixtures.",
            'work_skill_plumbing_domestic': "Skilled in installing, repairing and maintaining domestic plumbing fixtures.",
            'work_skill_plumbing_domestic_and_commercial': "Skilled in installing, repairing and maintaining domestic, commercial and/or industrial plumbing fixtures.",
            'work_skill_demolition': "Skilled in efficient, safe and quick demolition and removal.",
            'work_skill_carpentry_expertise': "Experienced tradesmen in residential carpentry.",
            'work_skill_construction_machinery_operation': "Skilled in operating specialist construction machinery.",
            'work_skill_drywalling': "Experienced in ceiling and wall drywalling.",
            'work_skill_hvac_equipment_and_ductwork': "Experienced in HVAC equipment use and ductwork.",
            'work_skill_appliance_installations': "Skilled in installing residential appliances.",
            'work_skill_driver': "Experienced driver with a full and valid UK license.",
            'work_skill_problem_solving': "Practised the ability to solve unique problems as they arise.",
            'work_skill_interpersonal_skills': "Displayed excellent interpersonal skills when dealing with customers to provide the best possible service.",
            'work_skill_enthusiastic': "Approached work with an enthusiastic, can-do, and positive attitude, with a willingness to undertake a variety of tasks.",
            'work_skill_customer_service': "Communicated with customers regularly to ensure the delivery of excellent service and quality of treatment.",
            'work_skill_works_well_under_pressure': "Worked well under pressure and responded positively to stressful situations whilst effectively managing deadlines and time sensitive tasks.",
            'work_skill_teamwork': "Demonstrated excellent collaboration skills whilst working as part of a team, as well as being able to work independently when required.",
            'work_skill_motivational': "Adopted an energetic approach to motivate and encourage colleagues, keeping morale high.",
            'work_skill_independent': "Worked independently to manage deliverables whilst also being able to work well as part of a team.",
            'work_skill_disciplined_time': "Maintained a high level of self-discipline, including excellent organisation and time management skills to ensure operations ran smoothly.",
            'work_skill_disciplined': "Displayed discipline and diligence whilst following instructions and ensured appropriate conduct in all situations.",
            'work_skill_organisation': "Demonstrated high levels of organisational skills whilst working hard to ensure that customer expectations were met in a timely and punctual manner.",
            'work_skill_flexible_in_work': "Worked with flexiblity and the willingness to undertake a variety of tasks as and when required.",
            'work_skill_trustworthy': "Consistently delivered on responsibilities with trust, reliability, and regularity.",
            'work_skill_attention_to_detail': "Worked in an attentive and alert manner, displaying high awareness to observe the environment with high attention to detail.",
        }

    html = template.render(context)
    css = [
        '/home/domvdp/cv-generator/pdf/static/cv_template.css', # 'pdf/static/cv_template.css',
    ]

    # Save Resume as PDF within project
    pdfkit.from_string(html, 'CV Output.pdf', css=css, configuration=config)

    # Assign variable that allows PDF to be viewed by user on website
    pdf = pdfkit.from_string(html, False, css=css, configuration=config)

    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')

        return response
    return HttpResponse("Not found")


def security_resume(request):
    # wkhtmltopdf lives and functions differently depending on Windows or Linux.
    # We need to support both since we develop on windows but deploy on Heroku,
    # which uses Linux.
    if platform.system() == "Windows":
        config = pdfkit.configuration(wkhtmltopdf=os.environ.get('WKHTMLTOPDF_BINARY', 'wkhtmltopdf\\bin\\wkhtmltopdf.exe'))
    else:
        os.environ['PATH'] += os.pathsep + os.path.dirname(sys.executable)

        WKHTMLTOPDF_CMD = subprocess.Popen(['which', os.environ.get('WKHTMLTOPDF_BINARY', 'wkhtmltopdf-pack')], stdout=subprocess.PIPE).communicate()[0].strip()

        config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_CMD)

    #config = pdfkit.configuration(wkhtmltopdf="..\\myapp\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")

    template = get_template('security_template.html')
    profile = Profile.objects.all()

    for profile in profile:
        context = {
            'sum_1': profile.sum_1,
            'sum_2': profile.sum_2,

            'security_sum_1': profile.security_sum_1,

            'company_1': profile.company_1,
            'job_1': profile.job_1,
            'work_start_1': profile.work_start_1,
            'work_end_1': profile.work_end_1,
            'work_1a': profile.work_1a,
            'work_1c': profile.work_1c,
            'work_1e': profile.work_1e,

            'company_2': profile.company_2,
            'job_2': profile.job_2,
            'work_start_2': profile.work_start_2,
            'work_end_2': profile.work_end_2,
            'work_2a': profile.work_2a,
            'work_2c': profile.work_2c,
            'work_2e': profile.work_2e,

            'company_3': profile.company_3,
            'job_3': profile.job_3,
            'work_start_3': profile.work_start_3,
            'work_end_3': profile.work_end_3,
            'work_3a': profile.work_3a,
            'work_3c': profile.work_3c,
            'work_3e': profile.work_3e,

            'company_4': profile.company_4,
            'job_4': profile.job_4,
            'work_start_4': profile.work_start_4,
            'work_end_4': profile.work_end_4,
            'work_4a': profile.work_4a,
            'work_4c': profile.work_4c,
            'work_4e': profile.work_4e,

            'college_name': profile.college_name,
            'college_course_type': profile.college_course_type,
            'college_course_name': profile.college_course_name,
            'college_start': profile.college_start,
            'college_grade': profile.college_grade,
            'college_end': profile.college_end,
            'college_modules': profile.college_modules,
            'college_notable': profile.college_notable,
            'college_societies': profile.college_societies,

            'upper_school_name': profile.upper_school_name,

            'upper_school_start': profile.upper_school_start,
            'upper_school_end': profile.upper_school_end,

            'upper_school_subject_type_1': profile.upper_school_subject_type_1,
            'upper_school_subject_name_1': profile.upper_school_subject_name_1,
            'upper_school_subject_grade_1': profile.upper_school_subject_grade_1,

            'upper_school_subject_type_2': profile.upper_school_subject_type_2,
            'upper_school_subject_name_2': profile.upper_school_subject_name_2,
            'upper_school_subject_grade_2': profile.upper_school_subject_grade_2,

            'upper_school_subject_type_3': profile.upper_school_subject_type_3,
            'upper_school_subject_name_3': profile.upper_school_subject_name_3,
            'upper_school_subject_grade_3': profile.upper_school_subject_grade_3,

            'upper_school_subject_type_4': profile.upper_school_subject_type_4,
            'upper_school_subject_name_4': profile.upper_school_subject_name_4,
            'upper_school_subject_grade_4': profile.upper_school_subject_grade_4,

            'upper_school_subject_type_5': profile.upper_school_subject_type_5,
            'upper_school_subject_name_5': profile.upper_school_subject_name_5,
            'upper_school_subject_grade_5': profile.upper_school_subject_grade_5,

            'upper_school_clubs': profile.upper_school_clubs,

            'lower_school_name': profile.lower_school_name,

            'lower_school_start': profile.lower_school_start,
            'lower_school_end': profile.lower_school_end,

            'lower_school_subject_type_1': profile.lower_school_subject_type_1,
            'lower_school_subject_name_1': profile.lower_school_subject_name_1,
            'lower_school_subject_grade_1': profile.lower_school_subject_grade_1,

            'lower_school_subject_type_2': profile.lower_school_subject_type_2,
            'lower_school_subject_name_2': profile.lower_school_subject_name_2,
            'lower_school_subject_grade_2': profile.lower_school_subject_grade_2,

            'lower_school_subject_type_3': profile.lower_school_subject_type_3,
            'lower_school_subject_name_3': profile.lower_school_subject_name_3,
            'lower_school_subject_grade_3': profile.lower_school_subject_grade_3,

            'lower_school_subject_type_4': profile.lower_school_subject_type_4,
            'lower_school_subject_name_4': profile.lower_school_subject_name_4,
            'lower_school_subject_grade_4': profile.lower_school_subject_grade_4,

            'lower_school_subject_type_5': profile.lower_school_subject_type_5,
            'lower_school_subject_name_5': profile.lower_school_subject_name_5,
            'lower_school_subject_grade_5': profile.lower_school_subject_grade_5,

            'lower_school_subject_type_6': profile.lower_school_subject_type_6,
            'lower_school_subject_name_6': profile.lower_school_subject_name_6,
            'lower_school_subject_grade_6': profile.lower_school_subject_grade_6,

            'lower_school_subject_type_7': profile.lower_school_subject_type_7,
            'lower_school_subject_name_7': profile.lower_school_subject_name_7,
            'lower_school_subject_grade_7': profile.lower_school_subject_grade_7,

            'lower_school_subject_type_8': profile.lower_school_subject_type_8,
            'lower_school_subject_name_8': profile.lower_school_subject_name_8,
            'lower_school_subject_grade_8': profile.lower_school_subject_grade_8,

            'lower_school_subject_type_9': profile.lower_school_subject_type_9,
            'lower_school_subject_name_9': profile.lower_school_subject_name_9,
            'lower_school_subject_grade_9': profile.lower_school_subject_grade_9,

            'lower_school_subject_type_10': profile.lower_school_subject_type_10,
            'lower_school_subject_name_10': profile.lower_school_subject_name_10,
            'lower_school_subject_grade_10': profile.lower_school_subject_grade_10,

            'lower_school_subject_type_11': profile.lower_school_subject_type_11,
            'lower_school_subject_name_11': profile.lower_school_subject_name_11,
            'lower_school_subject_grade_11': profile.lower_school_subject_grade_11,

            'lower_school_clubs': profile.lower_school_clubs,

            'cert_1': profile.cert_1,
            'cert_date_1': profile.cert_date_1,
            'cert_2': profile.cert_2,
            'cert_date_2': profile.cert_date_2,
            'cert_3': profile.cert_3,
            'cert_date_3': profile.cert_date_3,

            'activity_1': profile.activity_1,

            'tech_skills': profile.tech_skills,

            'language_1': profile.language_1,
            'fluency_1': profile.fluency_1,
            'language_2': profile.language_2,
            'fluency_2': profile.fluency_2,
            'language_3': profile.language_3,
            'fluency_3': profile.fluency_3,
            'language_4': profile.language_4,
            'fluency_4': profile.fluency_4,

            'work_1_list': [profile.work_1a, profile.work_1c, profile.work_1e],
            'work_2_list': [profile.work_2a, profile.work_2c, profile.work_2e],
            'work_3_list': [profile.work_3a, profile.work_3c, profile.work_3e],
            'work_4_list': [profile.work_4a, profile.work_4c, profile.work_4e],

            'work_skill_interpersonal_skills': "Displayed excellent interpersonal skills when dealing with customers to provide the best possible service.",
            'work_skill_verbal_and_written_communication': "Demonstrated effective levels of verbal and written communication in all levels of engagement.",
            'work_skill_security_equipment': "Experienced in security related technical equipment such as walkie-talkies, closed-circuit televisions, and CCTV.",
            'work_skill_deal_with_difficult_customers': "Dealt with difficult customer complaints in a patient and friendly manner whilst working to ensure an appropriate and timely resolution.",
            'work_skill_enthusiastic': "Approached work with an enthusiastic, can-do, and positive attitude, with a willingness to undertake a variety of tasks.",
            'work_skill_confidence': "Provided excellent hospitality with a confident and well-poised approach.",
            'work_skill_works_well_under_pressure': "Worked well under pressure and responded positively to stressful situations whilst effectively managing deadlines and time sensitive tasks.",
            'work_skill_teamwork': "Demonstrated excellent collaboration skills whilst working as part of a team, as well as being able to work independently when required.",
            'work_skill_independent': "Worked independently to manage deliverables whilst also being able to work well as part of a team.",
            'work_skill_disciplined_time': "Maintained a high level of self-discipline, including excellent organisation and time management skills to ensure operations ran smoothly.",
            'work_skill_disciplined': "Displayed discipline and diligence whilst following instructions and ensured appropriate conduct in all situations.",
            'work_skill_flexible_in_work': "Worked with flexiblity and the willingness to undertake a variety of tasks as and when required.",
            'work_skill_trustworthy': "Consistently delivered on responsibilities with trust, reliability, and regularity.",
            'work_skill_attention_to_detail': "Worked in an attentive and alert manner, displaying high awareness to observe the environment with high attention to detail.",
            'work_skill_problem_solving': "Practised the ability to solve unique problems as they arise.",
        }

    html = template.render(context)
    css = [
        '/home/domvdp/cv-generator/pdf/static/cv_template.css', # 'pdf/static/cv_template.css',
    ]

    # Save Resume as PDF within project
    pdfkit.from_string(html, 'CV Output.pdf', css=css, configuration=config)

    # Assign variable that allows PDF to be viewed by user on website
    pdf = pdfkit.from_string(html, False, css=css, configuration=config)

    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')

        return response
    return HttpResponse("Not found")
