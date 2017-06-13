from django.shortcuts import render
from .models import JobListing
# Create your views here.


def home(request):

    job_listings = JobListing.objects.all()
    context = {'job_listings': job_listings}

    if request.method == "POST":

        posted_title = request.POST.get("title", "")
        posted_description = request.POST.get("description", "")

        job_listing = JobListing.objects.create(
            title=posted_title,
            description=posted_description
        )
        job_listing.save()

        return render(request, "jobs_app/index.html", context)        



    return render(request, "jobs_app/index.html", context)
