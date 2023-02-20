# Generated by Django 3.1.5 on 2021-04-16 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum_1', models.CharField(default='', max_length=100)),
                ('sum_2', models.CharField(default='', max_length=100)),
                ('sum_3', models.CharField(default='', max_length=100)),
                ('sum_4', models.CharField(default='', max_length=100)),
                ('language_1', models.CharField(default='', max_length=100)),
                ('fluency_1', models.CharField(default='', max_length=100)),
                ('language_2', models.CharField(default='', max_length=100)),
                ('fluency_2', models.CharField(default='', max_length=100)),
                ('language_3', models.CharField(default='', max_length=100)),
                ('fluency_3', models.CharField(default='', max_length=100)),
                ('language_4', models.CharField(default='', max_length=100)),
                ('fluency_4', models.CharField(default='', max_length=100)),
                ('company_1', models.CharField(default='', max_length=100)),
                ('job_1', models.CharField(default='', max_length=100)),
                ('work_start_1', models.CharField(default='', max_length=100)),
                ('work_end_1', models.CharField(default='', max_length=100)),
                ('work_1a', models.CharField(default='', max_length=100)),
                ('work_1b', models.CharField(default='', max_length=100)),
                ('work_1c', models.CharField(default='', max_length=100)),
                ('work_1d', models.CharField(default='', max_length=100)),
                ('work_1e', models.CharField(default='', max_length=100)),
                ('work_1f', models.CharField(default='', max_length=100)),
                ('work_1g', models.CharField(default='', max_length=100)),
                ('work_1h', models.CharField(default='', max_length=100)),
                ('company_2', models.CharField(default='', max_length=100)),
                ('job_2', models.CharField(default='', max_length=100)),
                ('work_start_2', models.CharField(default='', max_length=100)),
                ('work_end_2', models.CharField(default='', max_length=100)),
                ('work_2a', models.CharField(default='', max_length=100)),
                ('work_2b', models.CharField(default='', max_length=100)),
                ('work_2c', models.CharField(default='', max_length=100)),
                ('work_2d', models.CharField(default='', max_length=100)),
                ('work_2e', models.CharField(default='', max_length=100)),
                ('work_2f', models.CharField(default='', max_length=100)),
                ('work_2g', models.CharField(default='', max_length=100)),
                ('work_2h', models.CharField(default='', max_length=100)),
                ('company_3', models.CharField(default='', max_length=100)),
                ('job_3', models.CharField(default='', max_length=100)),
                ('work_start_3', models.CharField(default='', max_length=100)),
                ('work_end_3', models.CharField(default='', max_length=100)),
                ('work_3a', models.CharField(default='', max_length=100)),
                ('work_3b', models.CharField(default='', max_length=100)),
                ('work_3c', models.CharField(default='', max_length=100)),
                ('work_3d', models.CharField(default='', max_length=100)),
                ('work_3e', models.CharField(default='', max_length=100)),
                ('work_3f', models.CharField(default='', max_length=100)),
                ('work_3g', models.CharField(default='', max_length=100)),
                ('work_3h', models.CharField(default='', max_length=100)),
                ('company_4', models.CharField(default='', max_length=100)),
                ('job_4', models.CharField(default='', max_length=100)),
                ('work_start_4', models.CharField(default='', max_length=100)),
                ('work_end_4', models.CharField(default='', max_length=100)),
                ('work_4a', models.CharField(default='', max_length=100)),
                ('work_4b', models.CharField(default='', max_length=100)),
                ('work_4c', models.CharField(default='', max_length=100)),
                ('work_4d', models.CharField(default='', max_length=100)),
                ('work_4e', models.CharField(default='', max_length=100)),
                ('work_4f', models.CharField(default='', max_length=100)),
                ('work_4g', models.CharField(default='', max_length=100)),
                ('work_4h', models.CharField(default='', max_length=100)),
                ('college_course_name', models.CharField(default='', max_length=100)),
                ('college_course_type', models.CharField(default='', max_length=100)),
                ('college_name', models.CharField(default='', max_length=100)),
                ('college_start', models.CharField(default='', max_length=100)),
                ('college_grade', models.CharField(default='', max_length=100)),
                ('college_end', models.CharField(default='', max_length=100)),
                ('college_modules', models.CharField(default='', max_length=100)),
                ('college_notable', models.CharField(default='', max_length=100)),
                ('college_societies', models.CharField(default='', max_length=100)),
                ('upper_school_start', models.CharField(default='', max_length=100)),
                ('upper_school_end', models.CharField(default='', max_length=100)),
                ('upper_school_subject_type_1', models.CharField(default='', max_length=100)),
                ('upper_school_subject_name_1', models.CharField(default='', max_length=100)),
                ('upper_school_subject_grade_1', models.CharField(default='', max_length=100)),
                ('upper_school_subject_type_2', models.CharField(default='', max_length=100)),
                ('upper_school_subject_name_2', models.CharField(default='', max_length=100)),
                ('upper_school_subject_grade_2', models.CharField(default='', max_length=100)),
                ('upper_school_subject_type_3', models.CharField(default='', max_length=100)),
                ('upper_school_subject_name_3', models.CharField(default='', max_length=100)),
                ('upper_school_subject_grade_3', models.CharField(default='', max_length=100)),
                ('upper_school_subject_type_4', models.CharField(default='', max_length=100)),
                ('upper_school_subject_name_4', models.CharField(default='', max_length=100)),
                ('upper_school_subject_grade_4', models.CharField(default='', max_length=100)),
                ('upper_school_subject_type_5', models.CharField(default='', max_length=100)),
                ('upper_school_subject_name_5', models.CharField(default='', max_length=100)),
                ('upper_school_subject_grade_5', models.CharField(default='', max_length=100)),
                ('upper_school_clubs', models.CharField(default='', max_length=100)),
                ('lower_school_start', models.CharField(default='', max_length=100)),
                ('lower_school_end', models.CharField(default='', max_length=100)),
                ('lower_school_subject_type_1', models.CharField(default='', max_length=100)),
                ('lower_school_subject_name_1', models.CharField(default='', max_length=100)),
                ('lower_school_subject_grade_1', models.CharField(default='', max_length=100)),
                ('lower_school_subject_type_2', models.CharField(default='', max_length=100)),
                ('lower_school_subject_name_2', models.CharField(default='', max_length=100)),
                ('lower_school_subject_grade_2', models.CharField(default='', max_length=100)),
                ('lower_school_subject_type_3', models.CharField(default='', max_length=100)),
                ('lower_school_subject_name_3', models.CharField(default='', max_length=100)),
                ('lower_school_subject_grade_3', models.CharField(default='', max_length=100)),
                ('lower_school_subject_type_4', models.CharField(default='', max_length=100)),
                ('lower_school_subject_name_4', models.CharField(default='', max_length=100)),
                ('lower_school_subject_grade_4', models.CharField(default='', max_length=100)),
                ('lower_school_subject_type_5', models.CharField(default='', max_length=100)),
                ('lower_school_subject_name_5', models.CharField(default='', max_length=100)),
                ('lower_school_subject_grade_5', models.CharField(default='', max_length=100)),
                ('lower_school_subject_type_6', models.CharField(default='', max_length=100)),
                ('lower_school_subject_name_6', models.CharField(default='', max_length=100)),
                ('lower_school_subject_grade_6', models.CharField(default='', max_length=100)),
                ('lower_school_subject_type_7', models.CharField(default='', max_length=100)),
                ('lower_school_subject_name_7', models.CharField(default='', max_length=100)),
                ('lower_school_subject_grade_7', models.CharField(default='', max_length=100)),
                ('lower_school_subject_type_8', models.CharField(default='', max_length=100)),
                ('lower_school_subject_name_8', models.CharField(default='', max_length=100)),
                ('lower_school_subject_grade_8', models.CharField(default='', max_length=100)),
                ('lower_school_subject_type_9', models.CharField(default='', max_length=100)),
                ('lower_school_subject_name_9', models.CharField(default='', max_length=100)),
                ('lower_school_subject_grade_9', models.CharField(default='', max_length=100)),
                ('lower_school_subject_type_10', models.CharField(default='', max_length=100)),
                ('lower_school_subject_name_10', models.CharField(default='', max_length=100)),
                ('lower_school_subject_grade_10', models.CharField(default='', max_length=100)),
                ('lower_school_subject_type_11', models.CharField(default='', max_length=100)),
                ('lower_school_subject_name_11', models.CharField(default='', max_length=100)),
                ('lower_school_subject_grade_11', models.CharField(default='', max_length=100)),
                ('lower_school_clubs', models.CharField(default='', max_length=100)),
                ('cert_1', models.CharField(default='', max_length=100)),
                ('cert_date_1', models.CharField(default='', max_length=100)),
                ('cert_2', models.CharField(default='', max_length=100)),
                ('cert_date_2', models.CharField(default='', max_length=100)),
                ('cert_3', models.CharField(default='', max_length=100)),
                ('cert_date_3', models.CharField(default='', max_length=100)),
                ('activity_1', models.CharField(default='', max_length=100)),
            ],
        ),
    ]