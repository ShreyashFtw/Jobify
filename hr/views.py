from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hr.models import JobPost, CandidateApplications, SelectCandidateJob
from django.contrib import messages


@login_required
def hrHome(request):
    jobposts = JobPost.objects.filter(user=request.user)
    return render(request, 'hr/hrdashboard.html', {'jobposts': jobposts})


@login_required
def hrCandidateDetails(request, id):
    if JobPost.objects.filter(id=id).exists():
        jobpost = JobPost.objects.get(id=id)
        jobapplys = CandidateApplications.objects.filter(job=jobpost)
        selectedCandidates = SelectCandidateJob.objects.filter(job=jobpost)
        acceptedCandidates = selectedCandidates.filter(candidate__status='accepted')
        return render(request, 'hr/candidate.html', {'jobapplys': jobapplys, 'jobpost': jobpost, 'acceptedCandidates': acceptedCandidates})
    else:
        return render(request, 'hr/hrdashboard.html')



@login_required
def postJobs(request):
    if request.method == 'POST':
        job_title = request.POST.get('job-title')
        address = request.POST.get('address')
        company_name = request.POST.get('company-name')
        salary_low = request.POST.get('salary-low')
        salary_high = request.POST.get('salary-high')
        last_date = request.POST.get('last-date')

        jobpost = JobPost(user=request.user, title=job_title, address=address, companyName=company_name, salaryLow=salary_low, salaryHigh=salary_high, lastDateToApply=last_date)
        jobpost.save()
        msg = "Job Upload Done.."
        return render(request, 'hr/postjob.html', {'msg': msg})
    return render(request, 'hr/postjob.html')


def updateSelectedCandidateJobs(candidate, jobpost, status):
    selected_candidate_jobs = SelectCandidateJob.objects.filter(candidate=candidate, job=jobpost)
    for sc in selected_candidate_jobs:
        sc.status = status
        sc.save(update_fields=['status'])




def acceptApplication(request):
    if request.method != 'POST':
        return redirect('hrdash')

    candidateid = request.POST.get('candidateid')
    jobpostid = request.POST.get('jobpostid')
    action = request.POST.get('action')

    try:
        candidate = CandidateApplications.objects.select_for_update().get(id=candidateid)
    except CandidateApplications.DoesNotExist:
        return redirect('hrdash')
    else:
        if candidate.status != 'pending':
            messages.warning(request, "Application is already processed or rejected.")
            return redirect(f'/candidatedetails/{jobpostid}/')

    if action == 'accept':
        candidate.status = 'accepted'
    elif action == 'reject':
        candidate.status = 'rejected'

    candidate.save(update_fields=['status'])

    try:
        jobpost = JobPost.objects.select_for_update().get(id=jobpostid)
    except JobPost.DoesNotExist:
        return redirect('hrdash')

    updateSelectedCandidateJobs(candidate, jobpost, action)

    return redirect(f'/candidatedetails/{jobpostid}/')

@login_required
def rejectApplication(request):
    if request.method != 'POST':
        return redirect('hrdash')

    candidateid = request.POST.get('candidateid')
    jobpostid = request.POST.get('jobpostid')

    try:
        candidate = CandidateApplications.objects.select_for_update().get(id=candidateid)
    except CandidateApplications.DoesNotExist:
        return redirect('hrdash')
    else:
        if candidate.status != 'pending':
            messages.warning(request, "Application is already processed or rejected.")
            return redirect(f'/candidatedetails/{jobpostid}/')

    candidate.status = 'rejected'
    candidate.save(update_fields=['status'])

    try:
        jobpost = JobPost.objects.select_for_update().get(id=jobpostid)
    except JobPost.DoesNotExist:
        return redirect('hrdash')

    updateSelectedCandidateJobs(candidate, jobpost, 'reject')

    return redirect(f'/candidatedetails/{jobpostid}/')

