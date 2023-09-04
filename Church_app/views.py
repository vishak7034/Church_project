from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from Church_app.forms import Ward_Form, Event_Form, hall_Form, Donation_type, Donation_form, \
    Booking_hall_form, NewUserForm, Family_details_form, Deceased_persons_form_details, Personal_details_form, \
confirmation_form, marriage_form_details, Month_Payment_form, Baptism_form_details
from Church_app.models import Family_details, deceased_persons, Personal_details, payment, Baptism_details, \
    confirmation_details, Marriage_details, Donation, Event, Ward, Hall_Booking, Hall




def login_view(request):
    return render(request,'admin/index.html')




def ward_reg(request):
    form = Ward_Form()
    if request.method == 'POST':
        form = Ward_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '')

            return redirect('Indexview',)

    return render(request, 'admin/church_ward_reg.html', {'form': form})


def add_events(request):
    form = Event_Form()
    if request.method == 'POST':
        form = Event_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Added Successfull')
            return redirect('add_events')

    return render(request, 'admin/events.html', {'form': form})

def add_hall(request):
    form = hall_Form()
    if request.method == 'POST':
        form = hall_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Added Successfull')


    return render(request, 'admin/add_hall.html', {'form': form})


def hall_Booking(request):
    st=Hall.objects.all()
    if request.method == 'POST':
        hallname=request.POST['hallname']
        eventname = request.POST['eventname']
        sdate=request.POST['sdate']
        time=request.POST['time']
        note=request.POST['note']
        if Hall_Booking.objects.filter(start_date=sdate,time=time,hall_id=hallname):
            return render(request, 'admin/index.html',{'message':" This slot is already taken"})
        else:
            x = Hall_Booking()
            x.hall_id = hallname
            x.event_name = eventname
            x.time = time
            x.start_date = sdate
            x.notes = note
            x.save()
            return render(request, 'admin/index.html', {'message':" Successfully added",'st': st})

    else:
        return render(request, 'admin/hall_booking.html', {'st': st})

def add_type_donation(request):
    form = Donation_type()
    if request.method == 'POST':
        form = Donation_type(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Added Successfull')

            return redirect('add_type_donation')

    return render(request, 'admin/donation_type.html', {'form': form})


def add_donation(request):
    form = Donation_form()
    if request.method == 'POST':
        form = Donation_form(request.POST)
        if form.is_valid():
            form.save()

            return redirect('Indexview')

    return render(request, 'admin/add_donation.html', {'form': form})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("main:homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
        form = NewUserForm()
    return render (request=request, template_name="register.html", context={"form":form})


def Family_information(request):
    form = Family_details_form()
    if request.method == 'POST':
        form = Family_details_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_Family_details')

    return render(request, 'admin/family_details.html', {'form': form})


def view_Family_details(request):
    students=Family_details.objects.all()
    return render(request, 'admin/view_family_details.html',{'stu':students})

def add_deceased_persons(request,id):
    form = Deceased_persons_form_details()
    if request.method == 'POST':
        form = Deceased_persons_form_details(request.POST)
        print('ytyfuyfufu')

        if form.is_valid():
            de = form.save(commit=False)
            de.family_id=id
            de.save()
            print('ytyfuyfufu')

            return redirect('Indexview')


    return render(request, 'admin/deceased_persons_details.html', {'form': form})


def Personal_details_one(request,id):
    form = Personal_details_form()
    if request.method == 'POST':
        form = Personal_details_form(request.POST)
        print('ytyfuyfufu')

        if form.is_valid():
            de = form.save(commit=False)
            de.family_id = id
            de.save()
            print('ytyfuyfufu')

            return redirect('Indexview')

    return render(request, 'admin/personal_details.html',{'form':form})

def view_members(request,id):
    students=Personal_details.objects.filter(family_id=id)
    return render(request, 'admin/view_members_details.html',{'stu':students})

def Baptism_details_one(request,id):
    form = Baptism_form_details()
    if request.method == 'POST':
        form = Baptism_form_details(request.POST)
        print('unniiiiiiii')
        if form.is_valid():
            de = form.save(commit=False)
            de.person_id = id
            de.save()
            print('ytyfuyfufu')
            return redirect('Indexview')

    return render(request, 'admin/baptism_details.html',{'form':form})


def confirmation_details_one(request,id):
    form = confirmation_form()
    if request.method == 'POST':
        form = confirmation_form(request.POST)
        print('ytyfuyfufu')

        if form.is_valid():
            de = form.save(commit=False)
            de.person_id = id
            de.save()
            print('ytyfuyfufu')

            return redirect('Indexview')



    return render(request, 'admin/confirmation_details.html',{'form':form})


def marriage_details_one(request,id):
    form = marriage_form_details()
    if request.method == 'POST':
        form = marriage_form_details(request.POST)
        print('ytyfuyfufu')
        if form.is_valid():
            de = form.save(commit=False)
            de.person_id = id
            de.save()
            print('ytyfuyfufu')
            return redirect('Indexview')

    return render(request, 'admin/marriage_details.html',{'form':form})


def monthly_payment(request,id):
    students=payment.objects.filter(family_id=id)

    form = Month_Payment_form()
    if request.method == 'POST':
        form = Month_Payment_form(request.POST)
        print('ytyfuyfufu')

        if form.is_valid():
            de = form.save(commit=False)
            de.family_id = id
            de.save()
            print('ytyfuyfufu')
            messages.success(request, "Message sent.")
            return render(request, 'admin/payment.html', {'form': form, 'stu': students})

    return render(request, 'admin/payment.html',{'form':form,'stu':students})

def view_member_details(request,id):
    students=Personal_details.objects.get(id=id)
    st=confirmation_details.objects.get(person_id=id)
    em=Baptism_details.objects.get(person_id=id)
    rm=Marriage_details.objects.get(person_id=id)

    return render(request, 'admin/view_member.html',{'form':students,'st':st,'em':em,'rm':rm})

def view_family_details(request,id):
    students=Family_details.objects.get(id=id)

    return render(request, 'admin/view_family.html',{'form':students})

def view_donation(request):
    students=Donation.objects.all()

    return render(request, 'admin/view_donation.html',{'form':students})

def view_events(request):
    students=Event.objects.all()

    return render(request, 'admin/view_events.html',{'form':students})


def view_ward(request):
    students=Ward.objects.all()

    return render(request, 'admin/view_ward.html',{'form':students})


def view_Hall_booking(request):
    students=Hall_Booking.objects.all()

    return render(request, 'admin/view_hall_booking.html',{'st':students})