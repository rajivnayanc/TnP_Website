from django.shortcuts import render
from django.db.models import Avg, Max, Min
from . import models
from recruiters.models import CompanyType, Recruiter
from . import models

# Create your views here.
def general_statistics(students_list):
    statistics = students_list.aggregate(average=Avg('salary'),maximum = Max('salary'), Minimum = Min('salary'))
    return statistics

def branch_wise_statistics(branch_list,students_list):
    branch_statistics = {}
    for branch in branch_list:
        students = students_list.filter(branch=branch)
        if(len(students)>0):
            branch_statistics[branch.branch_name] = general_statistics(students)
    return branch_statistics

def get_statistics(branch_list,students_list):
    total_statistics = general_statistics(students_list)
    branch_wise_stats = branch_wise_statistics(branch_list,students_list)
    statistics = {}
    for key,value in total_statistics.items():
        statistics[key] = {}
        statistics[key]['total']=value
    
    for key,stats in branch_wise_stats.items():
        for type,value in stats.items():
            statistics[type][key] = value
    return statistics

def get_company_student_list(companies,student_list):
    company_students_list = {}
    for company in companies:
        students = student_list.filter(company=company)
        if(len(students)>0):
            company_students_list[company.name] = students
    return company_students_list

def get_job_roles_students_list(job_descriptions,students_list):
    job_roles_students_list = {}
    for jd in job_descriptions:
        students = students_list.filter(Job_description=jd)
        if(len(students)>0):
            job_roles_students_list[jd.type] = students
    return job_roles_students_list

def get_company_type_students_list(company_types, students_list):
    company_type_students_list={}
    for type in company_types:
        students = students_list.filter(company__type = type)
        if(len(students)>0):
            company_type_students_list[type.type] = students
    return company_type_students_list

def index(request,id):
    batch = models.Batch.objects.get(pk=id)
    students_list = batch.student_of_batch.all()
    branch_lists = models.Branch.objects.all()

    statistics = get_statistics(branch_lists,students_list)
    
    companies = Recruiter.objects.all()
    company_students_list = get_company_student_list(companies,students_list)

    jd = models.JobDescription.objects.all()
    job_roles_students_list = get_job_roles_students_list(jd,students_list)

    company_types = CompanyType.objects.all()
    company_type_students_list = get_company_type_students_list(company_types,students_list)
    context = {
        'height':len(company_students_list)*60,
        'batch':batch.batch_name,
        'statistics':statistics,
        'companies':company_students_list,
        'job_roles':job_roles_students_list,
        'company_type': company_type_students_list
    }
    return render(request,'placements/index.html',context)
