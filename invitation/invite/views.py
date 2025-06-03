from django.shortcuts import render, redirect, HttpResponse
# Create your views here.
def show(request):
    return render(request, 'base.html')

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import PreRegisteredUser
from django.contrib import messages

from django.contrib import messages
from django.shortcuts import redirect, render
from .models import PreRegisteredUser

def pre_register_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile_no = request.POST.get('mobile')

        # Basic validation
        if not name or not email or not mobile_no:
            messages.error(request, "All fields are required.")
            return redirect('home')

        # Check for duplicates
        if PreRegisteredUser.objects.filter(email=email).exists() or PreRegisteredUser.objects.filter(mobile_no=mobile_no).exists():
            messages.warning(request, "You have already pre-registered.")
            return redirect('home')

        # Count current registered users
        current_count = PreRegisteredUser.objects.count()

        # Determine eligibility based on count
        if current_count < 5000:
            eligibility_status = "eligible"
        else:
            eligibility_status = "not eligible"

        # Save user with eligibility status
        PreRegisteredUser.objects.create(
            name=name,
            email=email,
            mobile_no=mobile_no,
            eligibility=eligibility_status
        )

        if eligibility_status == "eligible":
            messages.success(request, "Pre-registration successful! You are eligible.")
        else:
            messages.info(request, "Pre-registration received. Unfortunately, the quota has been reached and you are currently not eligible.")

        return redirect('home')

    return render(request, 'base.html')

