from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ward(models.Model):
    ward_num = models.IntegerField()
    ward_name = models.CharField(max_length=150, null=True)  
    area_name = models.CharField(max_length=150, null=True) 
    ward_president =models.CharField(max_length=150, null=True)
    notes = models.TextField(max_length=150, null=True)

    def __str__(self):
        return self.ward_name


class Event(models.Model):
    event_name = models.CharField(max_length=150, null=True)
    start_date = models.DateField(max_length=150, null=True)
    end_date = models.DateField(max_length=150, null=True)
    notes = models.TextField(max_length=150, null=True)

class Hall(models.Model):
    Hall_name = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.Hall_name

class Hall_Booking(models.Model):
    hall =models.ForeignKey(Hall,on_delete=models.CASCADE,null=True,)
    event_name = models.CharField(max_length=150, null=True)
    start_date = models.DateField(max_length=150, null=True)
    time = models.CharField(max_length=150,null=True)
    notes = models.TextField(max_length=150, null=True)


class type_donation(models.Model):
    donation_name = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.donation_name

class Donation(models.Model):
    donation =models.ForeignKey(type_donation,on_delete=models.CASCADE,null=True,default='select Donation')
    name = models.CharField(max_length=150, null=True)
    rupees = models.CharField(max_length=150, null=True)



class Family_details(models.Model):
    book_name = models.CharField(max_length=150, null=True)
    page_number = models.CharField(max_length=150, null=True)
    diocese = models.CharField(max_length=150, null=True)
    parish = models.CharField(max_length=150, null=True)
    ward_name=models.ForeignKey(Ward,on_delete=models.CASCADE,null=True,default='bbb')
    house_name = models.CharField(max_length=150, null=True)
    place = models.CharField(max_length=150, null=True)
    post_office = models.CharField(max_length=150, null=True)
    pincode = models.IntegerField(null=True)
    tel = models.IntegerField(null=True)
    mob = models.IntegerField(null=True)
    head_of_family = models.CharField(max_length=150, null=True)
    female_head = models.CharField(max_length=150, null=True)
    seperated_year_family = models.IntegerField(null=True)
    joining_date=models.IntegerField(null=True)
    income_status=models.CharField(max_length=150, null=True)
    number_of_priests=models.IntegerField(null=True)
    number_of_sisters=models.IntegerField(null=True)





class deceased_persons(models.Model):
    family=models.ForeignKey(Family_details,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=150, null=True)
    baptism_name = models.CharField(max_length=150, null=True)
    choice = [('Female_head', 'Female_head'), ('Son', 'Son'), ('Daughter', 'Daughter'),('Grand Son', 'Grand Son'),('Grand Daughter', 'Grand Daughter')]
    relation = models.CharField(max_length=150,choices=choice,null=True)
    birthdate = models.DateField(max_length=150, null=True)
    deathdate = models.DateField(max_length=150, null=True)
    funeral_date = models.DateField(max_length=150, null=True)

    placeofcymetry = models.CharField(max_length=150, null=True)

class Personal_details(models.Model):
    family=models.ForeignKey(Family_details,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=150, null=True)
    choice1 = [('Male', 'Male'), ('Female', 'Female'),('Others','Others')]
    gender = models.CharField(max_length=10, choices=choice1, default='Male')
    father_name = models.CharField(max_length=150, null=True)
    mother_name = models.CharField(max_length=150, null=True)
    choice2 = [('Married', 'Married'),('Unmarried', 'Unmarried',),('Divorced', 'Divorced',),('Widow/Widower', 'Widow/Widower',)]
    marital_status = models.CharField(max_length=150,choices=choice2,default='Married')
    choice3 = [('Family Head Male', 'Family Head Male'),('Family Head Female', 'Family Head Female',),('Son', 'son',),('Daughter', 'Daughter',),('Son in Law', 'Son in Law',),
                ('Daughter in Law', 'Daughter in Law',),('Grand Son', 'Grand Son',),('Grand Daughter', 'Grand Daughter',)]
    relation = models.CharField(max_length=150, choices=choice3, null=True,default='Family Head Male')
    Land_no=models.CharField(max_length=150, null=True)
    Mob_no=models.CharField(max_length=150, null=True)
    email=models.CharField(max_length=150, null=True)
    choice4 = [('A+', 'A+'),('O+', 'O+',),('B+', 'B+',),('AB+', 'AB+',),('A-', 'A-',),('B-', 'B-',),('O-', 'O-',),('AB-', 'AB-',)]
    blood_group=models.CharField(max_length=150,choices=choice4,default='A+', null=True)
    choice5 = [('Below SSLC', 'Below SSLC'),('SSLC', 'SSLC',),('Diploma', 'Diploma',),('Graduate', 'Graduate',),('Above Graduate', 'Above Graduate')]
    Qualification=models.CharField(max_length=150,choices=choice5,default='Degree')
    choice6 = [('Govt Job', 'Govt Job'),('Private Job', 'Private Job',),('Business', 'Business',),('Abroad', 'Abroad',),('Studying', 'Studying',),('Others','Others',)]
    working_status=models.CharField(max_length=150,choices=choice6,null=True,default='Private Job')
    place=models.CharField(max_length=150, null=True)


class Baptism_details(models.Model):
    person=models.ForeignKey(Personal_details,on_delete=models.CASCADE,null=True)
    Baptism_name=models.CharField(max_length=150,null=True)
    Reg_number=models.CharField(max_length=150,null=True)
    baptism_date=models.DateField(max_length=150, null=True)
    baptism_place=models.CharField(max_length=150, null=True)
    celebrant=models.CharField(max_length=150, null=True)
    godfather_name=models.CharField(max_length=150, null=True)
    gf_baptism_name=models.CharField(max_length=150, null=True)
    gf_diocese=models.CharField(max_length=150, null=True)
    gf_parish=models.CharField(max_length=150, null=True)
    gf_house_name=models.CharField(max_length=150, null=True)
    godmother_name=models.CharField(max_length=150, null=True)
    gm_baptism_name=models.CharField(max_length=150, null=True)
    gm_diocese=models.CharField(max_length=150, null=True)
    gm_parish=models.CharField(max_length=150, null=True)
    gm_house_name=models.CharField(max_length=150, null=True)

class confirmation_details(models.Model):
    person=models.ForeignKey(Personal_details,on_delete=models.CASCADE,null=True)
    confirmation_date=models.CharField(max_length=150, null=True)
    confirmation_place=models.CharField(max_length=150, null=True)
    celebrant=models.CharField(max_length=150, null=True)
    godfather_name=models.CharField(max_length=150, null=True)

class Marriage_details(models.Model):
    person = models.ForeignKey(Personal_details, on_delete=models.CASCADE, null=True)
    Reg_number = models.CharField(max_length=150,null=True)
    marriage_date = models.DateField(max_length=150, null=True)
    partner_name = models.CharField(max_length=150, null=True)
    p_baptism_name = models.CharField(max_length=150, null=True)
    p_house_name = models.CharField(max_length=150, null=True)
    p_diocese = models.CharField(max_length=150, null=True)
    p_parish = models.CharField(max_length=150, null=True)
    p_father_name = models.CharField(max_length=150, null=True)
    p_mother_name = models.CharField(max_length=150, null=True)
    p_birth_date = models.DateField(max_length=150, null=True)
    p_baptism_date = models.DateField(max_length=150, null=True)
    celebrant = models.CharField(max_length=150, null=True)
    marriage_palce = models.CharField(max_length=150, null=True)
    witness_name1 = models.CharField(max_length=150, null=True)
    w_baptism_name1 = models.CharField(max_length=150, null=True)
    w_diocese1 = models.CharField(max_length=150, null=True)
    w_parish1 = models.CharField(max_length=150, null=True)
    w_house_name1 = models.CharField(max_length=150, null=True)
    w_father_name1 = models.CharField(max_length=150, null=True)
    witness_name2 = models.CharField(max_length=150, null=True)
    w_baptism_name2 = models.CharField(max_length=150, null=True)
    w_diocese2 = models.CharField(max_length=150, null=True)
    w_parish2 = models.CharField(max_length=150, null=True)
    w_house_name2 = models.CharField(max_length=150, null=True)
    w_father_name2 = models.CharField(max_length=150, null=True)


class payment(models.Model):
    family=models.ForeignKey(Family_details,on_delete=models.CASCADE,null=True)
    choice = [('2020', '2020'), ('2021', '2021',), ('2022', '2022',),
              ('2023', '2023',), ('2024', '2024',), ('2025', '2025',),
              ('2026', '2026',), ('2027', '2027',), ('2028', '2028',),
              ('2029', '2029',), ('2030', '2023',),]
    year = models.CharField(max_length=150, choices=choice, default='2023')

    choice = [('January', 'January'), ('February', 'February',), ('March', 'March',),
               ('April', 'April',),('May', 'May',),('June', 'June',),
               ('July', 'July',),('August', 'August',),('September', 'September',),
               ('October', 'October',),('November', 'November',),('December', 'December',)]
    month = models.CharField(max_length=150, choices=choice, default='January')
    rupees = models.CharField(max_length=150, default=50)
