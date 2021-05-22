from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Jop
from .forms import Jop_ApplierForm, AddJopForm
from django.contrib.auth.decorators import login_required
from .filters import JopFilter

# Create your views here.


def jop_list(request):
    jobs_list = Jop.objects.all()

    # filter
    job_filter = JopFilter(request.GET, queryset=jobs_list)
    jobs_list = job_filter.qs

    paginator = Paginator(jobs_list, 3)  # Show 3 jops per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'jobs': page_obj, 'job_filter': job_filter}
    return render(request, 'jop_app/job_list.html', context)


def jop_detail(request, slug):
    job = Jop.objects.get(slug=slug)

    if request.method == "POST":
        # Create a form instance from POST data.
        form = Jop_ApplierForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()=> Creat and Save a new database object from the form's data.
            # form.save(commit=False)=> Creat but not Save a new database object from the form's data.
            myForm = form.save(commit=False)
            myForm.jop = job
            myForm.save()

    else:
        form = Jop_ApplierForm()

    context = {'job': job, 'form': form}
    return render(request, 'jop_app/job_detail.html', context)


@login_required
def add_job(request):
    if request.method == "POST":
        form = AddJopForm(request.POST, request.FILES)
        if form.is_valid():
            myForm = form.save(commit=False)
            myForm.owner = request.user
            myForm.save()
            return redirect(reverse('jobsssss:jobs'))
    else:
        form = AddJopForm()

    context = {'form': form}
    return render(request, 'jop_app/add_job.html', context)
