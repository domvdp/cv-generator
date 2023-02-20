from django.db import models

# Create your models here.
class Profile(models.Model):
    sum_1 = models.CharField(max_length=100, default='')
    sum_2 = models.CharField(max_length=100, default='')
    sum_3 = models.CharField(max_length=100, default='')

    construction_sum_1 = models.CharField(max_length=100, default='')
    construction_sum_2 = models.CharField(max_length=100, default='')
    construction_sum_3 = models.CharField(max_length=100, default='')
    construction_sum_4 = models.CharField(max_length=100, default='')
    construction_sum_5 = models.CharField(max_length=100, default='')

    security_sum_1 = models.CharField(max_length=100, default='')

    company_1 = models.CharField(max_length=100, default='')
    job_1 = models.CharField(max_length=100, default='')
    work_start_1 = models.CharField(max_length=100, default='')
    work_end_1 = models.CharField(max_length=100, default='')
    work_1a = models.CharField(max_length=100, default='')
    work_1c = models.CharField(max_length=100, default='')
    work_1e = models.CharField(max_length=100, default='')

    company_2 = models.CharField(max_length=100, default='')
    job_2 = models.CharField(max_length=100, default='')
    work_start_2 = models.CharField(max_length=100, default='')
    work_end_2 = models.CharField(max_length=100, default='')
    work_2a = models.CharField(max_length=100, default='')
    work_2c = models.CharField(max_length=100, default='')
    work_2e = models.CharField(max_length=100, default='')

    company_3 = models.CharField(max_length=100, default='')
    job_3 = models.CharField(max_length=100, default='')
    work_start_3 = models.CharField(max_length=100, default='')
    work_end_3 = models.CharField(max_length=100, default='')
    work_3a = models.CharField(max_length=100, default='')
    work_3c = models.CharField(max_length=100, default='')
    work_3e = models.CharField(max_length=100, default='')

    company_4 = models.CharField(max_length=100, default='')
    job_4 = models.CharField(max_length=100, default='')
    work_start_4 = models.CharField(max_length=100, default='')
    work_end_4 = models.CharField(max_length=100, default='')
    work_4a = models.CharField(max_length=100, default='')
    work_4c = models.CharField(max_length=100, default='')
    work_4e = models.CharField(max_length=100, default='')

    college_name = models.CharField(max_length=100, default='')
    college_course_type = models.CharField(max_length=100, default='')
    college_course_name = models.CharField(max_length=100, default='')
    college_start = models.CharField(max_length=100, default='')
    college_grade = models.CharField(max_length=100, default='')
    college_end = models.CharField(max_length=100, default='')
    college_modules = models.CharField(max_length=100, default='')
    college_notable = models.CharField(max_length=100, default='')
    college_societies = models.CharField(max_length=100, default='')

    upper_school_name = models.CharField(max_length=100, default='')

    upper_school_start = models.CharField(max_length=100, default='')
    upper_school_end = models.CharField(max_length=100, default='')

    upper_school_subject_type_1 = models.CharField(max_length=100, default='')
    upper_school_subject_name_1 = models.CharField(max_length=100, default='')
    upper_school_subject_grade_1 = models.CharField(max_length=100, default='')

    upper_school_subject_type_2 = models.CharField(max_length=100, default='')
    upper_school_subject_name_2 = models.CharField(max_length=100, default='')
    upper_school_subject_grade_2 = models.CharField(max_length=100, default='')

    upper_school_subject_type_3 = models.CharField(max_length=100, default='')
    upper_school_subject_name_3 = models.CharField(max_length=100, default='')
    upper_school_subject_grade_3 = models.CharField(max_length=100, default='')

    upper_school_subject_type_4 = models.CharField(max_length=100, default='')
    upper_school_subject_name_4 = models.CharField(max_length=100, default='')
    upper_school_subject_grade_4 = models.CharField(max_length=100, default='')

    upper_school_subject_type_5 = models.CharField(max_length=100, default='')
    upper_school_subject_name_5 = models.CharField(max_length=100, default='')
    upper_school_subject_grade_5 = models.CharField(max_length=100, default='')

    upper_school_clubs = models.CharField(max_length=100, default='')

    lower_school_name = models.CharField(max_length=100, default='')

    lower_school_start = models.CharField(max_length=100, default='')
    lower_school_end = models.CharField(max_length=100, default='')

    lower_school_subject_type_1 = models.CharField(max_length=100, default='')
    lower_school_subject_name_1 = models.CharField(max_length=100, default='')
    lower_school_subject_grade_1 = models.CharField(max_length=100, default='')

    lower_school_subject_type_2 = models.CharField(max_length=100, default='')
    lower_school_subject_name_2 = models.CharField(max_length=100, default='')
    lower_school_subject_grade_2 = models.CharField(max_length=100, default='')

    lower_school_subject_type_3 = models.CharField(max_length=100, default='')
    lower_school_subject_name_3 = models.CharField(max_length=100, default='')
    lower_school_subject_grade_3 = models.CharField(max_length=100, default='')

    lower_school_subject_type_4 = models.CharField(max_length=100, default='')
    lower_school_subject_name_4 = models.CharField(max_length=100, default='')
    lower_school_subject_grade_4 = models.CharField(max_length=100, default='')

    lower_school_subject_type_5 = models.CharField(max_length=100, default='')
    lower_school_subject_name_5 = models.CharField(max_length=100, default='')
    lower_school_subject_grade_5 = models.CharField(max_length=100, default='')

    lower_school_subject_type_6 = models.CharField(max_length=100, default='')
    lower_school_subject_name_6 = models.CharField(max_length=100, default='')
    lower_school_subject_grade_6 = models.CharField(max_length=100, default='')

    lower_school_subject_type_7 = models.CharField(max_length=100, default='')
    lower_school_subject_name_7 = models.CharField(max_length=100, default='')
    lower_school_subject_grade_7 = models.CharField(max_length=100, default='')

    lower_school_subject_type_8 = models.CharField(max_length=100, default='')
    lower_school_subject_name_8 = models.CharField(max_length=100, default='')
    lower_school_subject_grade_8 = models.CharField(max_length=100, default='')

    lower_school_subject_type_9 = models.CharField(max_length=100, default='')
    lower_school_subject_name_9 = models.CharField(max_length=100, default='')
    lower_school_subject_grade_9 = models.CharField(max_length=100, default='')

    lower_school_subject_type_10 = models.CharField(max_length=100, default='')
    lower_school_subject_name_10 = models.CharField(max_length=100, default='')
    lower_school_subject_grade_10 = models.CharField(max_length=100, default='')

    lower_school_subject_type_11 = models.CharField(max_length=100, default='')
    lower_school_subject_name_11 = models.CharField(max_length=100, default='')
    lower_school_subject_grade_11 = models.CharField(max_length=100, default='')

    lower_school_clubs = models.CharField(max_length=100, default='')

    cert_1 = models.CharField(max_length=100, default='')
    cert_date_1 = models.CharField(max_length=100, default='')
    cert_2 = models.CharField(max_length=100, default='')
    cert_date_2 = models.CharField(max_length=100, default='')
    cert_3 = models.CharField(max_length=100, default='')
    cert_date_3 = models.CharField(max_length=100, default='')

    activity_1 = models.CharField(max_length=300, default='')

    tech_skills = models.CharField(max_length=300, default='')

    language_1 = models.CharField(max_length=100, default='')
    fluency_1 = models.CharField(max_length=100, default='')
    language_2 = models.CharField(max_length=100, default='')
    fluency_2 = models.CharField(max_length=100, default='')
    language_3 = models.CharField(max_length=100, default='')
    fluency_3 = models.CharField(max_length=100, default='')
    language_4 = models.CharField(max_length=100, default='')
    fluency_4 = models.CharField(max_length=100, default='')
