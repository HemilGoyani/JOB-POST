from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import jobs, UserProposal
from .forms import JobForm, UserProposalForm
from django.contrib import messages

# List all jobs
def job_list(request):
    all_jobs = jobs.objects.all()
    return render(request, 'jobs.html', {'jobs': all_jobs})


# Create a new job (for admin or company user)
@login_required
def create_job(request):
    if not request.user.is_superuser:
        messages.error(request, "You do not have permission to create a job.")
        return redirect('job_list')
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Job created successfully.")
            return redirect('job_list')
    else:
        form = JobForm()
    return render(request, 'job_post.html', {'form': form})


# Job detail + proposal form
@login_required
def job_detail(request, job_id):
    job = get_object_or_404(jobs, id=job_id)

    # Check if user already submitted a proposal
    existing_proposal = UserProposal.objects.filter(user=request.user, job=job).first()

    if request.method == 'POST':
        if existing_proposal:
            messages.warning(request, "You have already submitted a proposal for this job.")
            return redirect('job_detail', job_id=job_id)

        form = UserProposalForm(request.POST)
        if form.is_valid():
            proposal = form.save(commit=False)
            proposal.user = request.user
            proposal.job = job
            proposal.save()
            messages.success(request, "Your proposal has been submitted.")
            return redirect('job_list')
    else:
        form = UserProposalForm()

    return render(request, 'job_detail.html', {
        'job': job,
        'form': form,
        'existing_proposal': existing_proposal
    })


def delete_job(request, job_id):
    job = get_object_or_404(jobs, id=job_id)
    if request.user.is_superuser:
        job.delete()
        messages.success(request, "Job deleted successfully.")
    else:
        messages.error(request, "You do not have permission to delete this job.")
    return redirect('job_list')