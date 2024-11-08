from django.http import JsonResponse
from django.core.files import File as DjangoFile
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout as logout_user
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
from .forms import LeaseForm, RiderForm
from .models import CustomUser, Lease,Rider

def home(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def login_user(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            rider = user.rider
            return render(request, "riders/dashboard.html", {"rider": rider})
    return render(request, "riders/login.html")

def logout(request):
    logout_user(request)
    return redirect("riders:home")

@login_required
def riderDashboard(request):
    rider = request.user.rider
    lease = Lease.objects.get(rider=rider)
    documents_missing=True

    missing = get_missing_fields(lease)
    if len(missing) == 0:
        documents_missing = False
    form = LeaseForm(instance=lease)
 
    
    return render(request,"riders/dashboard.html",{"rider":rider,"documents_missing":documents_missing,"missing":missing,"form":form})

@require_POST
def update_lease(request):
    rider = request.user.rider
    lease = Lease.objects.get(rider=rider)
    field_name = request.POST.get('field_name')
    db_field = "next_of_kin" if field_name =="next of kin national id" else field_name.replace(' ', '_')
    file = request.FILES.get('file')

    if field_name and file:
        setattr(lease, db_field, DjangoFile(file))
        lease.save()
        return JsonResponse({'success': True,"missing":True if len(get_missing_fields(lease))>0 else False})
    return JsonResponse({'success': False, 'error': 'Invalid field or file'})

def signUp(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        form = RiderForm(request.POST, request.FILES)
        if form.is_valid():
            # create user from email and password
            user = CustomUser.objects.create_user(email=email, password=password)
            
            rider = form.save(commit=False)
            rider.user = user
            rider.save()

            # log user in
            new_user = authenticate(email=email, password=password)
            if new_user is not None:
                login(request, new_user)
                return render(request, "riders/dashboard.html", {"rider": rider})
    else:
        form = RiderForm()
    return render(request, "riders/signup.html", {"form": form})



def get_missing_fields(lease):
    missing_fields = []
    if not lease.national_id:
        missing_fields.append("national id")
    if not lease.driving_license:
        missing_fields.append("driving license")
    if not lease.introduction_letter:
        missing_fields.append("introduction letter")
    if not lease.passport_photo:
        missing_fields.append("passport photo")
    if not lease.next_of_kin:
        missing_fields.append("next of kin national id")
    return missing_fields