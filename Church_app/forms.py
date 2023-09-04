from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, DateInput, TextInput, Select, forms, ChoiceField, ModelChoiceField, RadioSelect, \
    EmailInput, Textarea, IntegerField
from .models import Ward, Event, Hall, Hall_Booking, type_donation, Donation, Family_details, deceased_persons, \
    Personal_details, Baptism_details, confirmation_details, Marriage_details, payment


class Ward_Form(ModelForm):
    class Meta:
        model=Ward
        fields=['ward_num','ward_name','area_name','ward_president','notes']

        widgets = {

            'ward_num': TextInput(
                                    attrs={'class': 'form-control'}),
            'ward_name': TextInput(
                attrs={'class': 'form-control'}) ,
            'area_name': TextInput(
                                    attrs={'class': 'form-control'}),
            'ward_president': TextInput(
                attrs={'class': 'form-control'}),
            'notes': Textarea(
                attrs={'class': 'form-control'}),

        }


class Event_Form(ModelForm):
    class Meta:
        model=Event
        fields=['event_name','start_date','end_date','notes']
        widgets = {
            'event_name': TextInput(
                attrs={'class': 'form-control'}),
            'start_date': DateInput(format=('%Y-%m-%d'),
                                       attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'end_date': DateInput(format=('%Y-%m-%d'),
                                    attrs={ 'class': 'form-control','placeholder': 'Select a date', 'type': 'date'}),
            'notes': Textarea(
                attrs={'class': 'form-control'}),
        }

class hall_Form(ModelForm):
    class Meta:
        model=Hall
        fields=['Hall_name']
        widgets = {

            'Hall_name': TextInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Add Hall Name'})

        }



class Booking_hall_form(ModelForm):

    class Meta:
        model = Hall_Booking
        fields = ['hall','event_name','start_date','time','notes']

        widgets = {
            'hall': Select(
                attrs={'class': 'form-control','placeholder': 'Select Hall'}),
            'event_name': TextInput(
                attrs={'class': 'form-control'}),

                    'start_date':DateInput(format=('%Y-%m-%d'),attrs={'class': 'form-control','placeholder': 'Select a date','type': 'date'}),

            'end_date': DateInput(format=('%Y-%m-%d'),
                                       attrs={'class': 'form-control','placeholder': 'Select a date', 'type': 'date'}),
            'notes': Textarea(
                attrs={'class': 'form-control'}),
            'time': Select(attrs={'class': 'form-control'}),

        }

        def clean(self):
            cleaned_data = super().clean()
            time = cleaned_data.get('time')

            # Check if a booking already exists for the provided date and time
            existing_booking = Hall_Booking.objects.filter(time=time).first()
            if existing_booking:
                raise forms.ValidationError('A booking already exists for this date and time.')

            return cleaned_data



    # Define choices for the dropdown field

class Donation_type(ModelForm):
    class Meta:
        model=type_donation
        fields=['donation_name']
        widgets = {

            'donation_name': TextInput(
                                    attrs={ 'class': 'form-control','placeholder': 'Add Donation Type'})

        }

class Donation_form(ModelForm):
    class Meta:
        model=Donation
        fields=['donation','name','rupees']
        widgets = {

            'donation': Select(
                attrs={'class': 'form-control','placeholder': 'Select Donation Type'}),

            'name': TextInput(
                attrs={'class': 'form-control'}),


            'rupees': TextInput(
                attrs={'class': 'form-control'})

        }


class NewUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class Family_details_form(ModelForm):
    class Meta:
        model=Family_details
        fields=['book_name','page_number','diocese','parish','ward_name','house_name','place','post_office','pincode','tel',
                'mob','head_of_family','female_head','joining_date','seperated_year_family','income_status','number_of_priests','number_of_sisters']
        widgets = {
            'book_name': TextInput(attrs={'class': 'form-control'}),
            'page_number': TextInput(attrs={'class': 'form-control'}),
            'diocese': TextInput(attrs={'class': 'form-control'}),
            'parish': TextInput(attrs={'class': 'form-control'}),
            'ward_name': Select(attrs={'class': 'form-control'}),
            'house_name': TextInput(attrs={'class': 'form-control'}),
            'place': TextInput(attrs={'class': 'form-control'}),
            'post_office': TextInput(attrs={'class': 'form-control'}),
            'pincode': TextInput(attrs={'class': 'form-control'}),
            'tel': TextInput(attrs={'class': 'form-control'}),
            'mob': TextInput(attrs={'class': 'form'
                                             '-control'}),
            'head_of_family': TextInput(attrs={'class': 'form-control'}),
            'female_head': TextInput(attrs={'class': 'form-control'}),
            'joining_date': TextInput(attrs={'class': 'form-control'}),
            'seperated_year_family': TextInput(attrs={'class': 'form-control'}),
            'income_status': TextInput(attrs={'class': 'form-control'}),
            'number_of_priests': TextInput(attrs={'class': 'form-control'}),
            'number_of_sisters': TextInput(attrs={'class': 'form-control'}),

        }
class Deceased_persons_form_details(ModelForm):

    class Meta:
        model = deceased_persons
        fields = ['name','baptism_name','relation','birthdate','deathdate','funeral_date','placeofcymetry']


        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'baptism_name': TextInput(attrs={'class': 'form-control'}),

            'birthdate': DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control','placeholder': 'Select a date', 'type': 'date'}),

            'deathdate': DateInput(format=('%Y-%m-%d'),
                                  attrs={'class': 'form-control','placeholder': 'Select a date', 'type': 'date'}),
            'funeral_date': DateInput(format=('%Y-%m-%d'),
                                   attrs={'class': 'form-control','placeholder': 'Select a date', 'type': 'date'}),
            'relation': Select(attrs={'class': 'form-control'}),
            'placeofcymetry': TextInput(attrs={'class': 'form-control'}),
        }


class Personal_details_form(ModelForm):

    class Meta:
        model = Personal_details
        fields = ['name','gender','father_name','mother_name','marital_status','relation','Land_no','Mob_no',
                  'email','blood_group','Qualification','working_status','place']

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'father_name': TextInput(attrs={'class': 'form-control'}),
            'mother_name': TextInput(attrs={'class': 'form-control'}),

            'gender':RadioSelect ( attrs={'aria-label':'Title','aria-describedby':'add-btn'} ),

            'marital_status': Select(attrs={'class': 'form-control','aria-label': 'Title', 'aria-describedby': 'add-btn'
                                         }),

            'relation': Select(attrs={'class': 'form-control'}),
            'Land_no': TextInput(attrs={'class': 'form-control'}),
            'Mob_no': TextInput(attrs={'class': 'form-control'}),

            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email ID ', 'aria-label': 'Title',
                                       'aria-describedby': 'add-btn', 'id': 'txt_email'}),
            'blood_group': Select(attrs={'class': 'form-control'}),

            'Qualification': Select(attrs={'class': 'form-control'}),
            'working_status': Select(attrs={'class': 'form-control'}),
            'place': TextInput(attrs={'class': 'form-control'}),

        }

class Baptism_form_details(ModelForm):

    class Meta:
        model = Baptism_details
        fields = ['Baptism_name','Reg_number','baptism_date','baptism_place','celebrant','godfather_name','gf_baptism_name','gf_diocese',
                  'gf_parish','gf_house_name','godmother_name','gm_baptism_name','gm_diocese','gm_parish','gm_house_name']

        widgets = {
            'Baptism_name': TextInput(attrs={'class': 'form-control'}),
            'Reg_number': TextInput(attrs={'class': 'form-control'}),
            'baptism_place': TextInput(attrs={'class': 'form-control'}),
            'celebrant': TextInput(attrs={'class': 'form-control'}),
            'godfather_name': TextInput(attrs={'class': 'form-control'}),
            'gf_baptism_name': TextInput(attrs={'class': 'form-control'}),
            'gf_diocese': TextInput(attrs={'class': 'form-control'}),
            'gf_parish': TextInput(attrs={'class': 'form-control'}),
            'gf_house_name': TextInput(attrs={'class': 'form-control'}),
            'godmother_name': TextInput(attrs={'class': 'form-control'}),
            'gm_baptism_name': TextInput(attrs={'class': 'form-control'}),
            'gm_diocese': TextInput(attrs={'class': 'form-control'}),
            'gm_parish': TextInput(attrs={'class': 'form-control'}),
            'gm_house_name': TextInput(attrs={'class': 'form-control'}),
            'baptism_date': DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control','placeholder': 'Select a date', 'type': 'date'}),


        }

class confirmation_form(ModelForm):
    class Meta:
        model=confirmation_details
        fields=['confirmation_date','confirmation_place','celebrant','godfather_name']
        widgets = {
            'confirmation_place': TextInput(attrs={'class': 'form-control'}),
            'celebrant': TextInput(attrs={'class': 'form-control'}),
            'godfather_name': TextInput(attrs={'class': 'form-control'}),

            'confirmation_date': DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control','placeholder': 'Select a date', 'type': 'date'}),

        }

class marriage_form_details(ModelForm):
    class Meta:
        model=Marriage_details
        fields=['Reg_number','marriage_date','partner_name','p_baptism_name','p_house_name','p_diocese','p_parish',
                'p_father_name','p_mother_name','p_birth_date','p_baptism_date','celebrant',
                'marriage_palce','witness_name1','w_baptism_name1','w_diocese1','w_parish1',
                'w_house_name1','w_father_name1','witness_name2','w_baptism_name2','w_diocese2','w_parish2',
                'w_house_name2','w_father_name2']
        widgets = {
            'Reg_number': TextInput(attrs={'class': 'form-control'}),
            'partner_name': TextInput(attrs={'class': 'form-control'}),
            'p_baptism_name': TextInput(attrs={'class': 'form-control'}),
            'p_house_name': TextInput(attrs={'class': 'form-control'}),
            'p_diocese': TextInput(attrs={'class': 'form-control'}),
            'p_parish': TextInput(attrs={'class': 'form-control'}),
            'p_father_name': TextInput(attrs={'class': 'form-control'}),
            'p_mother_name': TextInput(attrs={'class': 'form-control'}),
            'celebrant': TextInput(attrs={'class': 'form-control'}),
            'marriage_palce': TextInput(attrs={'class': 'form-control'}),
            'witness_name1': TextInput(attrs={'class': 'form-control'}),
            'w_baptism_name1': TextInput(attrs={'class': 'form-control'}),
            'w_diocese1': TextInput(attrs={'class': 'form-control'}),
            'w_parish1': TextInput(attrs={'class': 'form-control'}),
            'w_house_name1': TextInput(attrs={'class': 'form-control'}),
            'w_father_name1': TextInput(attrs={'class': 'form-control'}),
            'witness_name2': TextInput(attrs={'class': 'form-control'}),
            'w_baptism_name2': TextInput(attrs={'class': 'form-control'}),
            'w_diocese2': TextInput(attrs={'class': 'form-control'}),
            'w_parish2': TextInput(attrs={'class': 'form-control'}),
            'w_house_name2': TextInput(attrs={'class': 'form-control'}),
            'w_father_name2': TextInput(attrs={'class': 'form-control'}),

            'marriage_date': DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control','placeholder': 'Select a date', 'type': 'date'}),

            'p_birth_date': DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control','placeholder': 'Select a date', 'type': 'date'}),
            'p_baptism_date': DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control','placeholder': 'Select a date', 'type': 'date'}),

        }
class Month_Payment_form(ModelForm):
    class Meta:
        model=payment
        fields=['year','month','rupees']
        widgets = {
            'month': Select(attrs={'class': 'form-control'}),
            'rupees':TextInput(attrs={'class': 'form-control'}),
            'year': Select(attrs={'class': 'form-control'}),

        }

class BookSearchForm(ModelForm):
    class Meta:
        model = payment
        fields = ['year', 'month', 'rupees']