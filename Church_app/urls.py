from django.urls import path

from Church_app import views

urlpatterns = [
    path('ward_reg',views.ward_reg,name='ward_reg'),
    path('Add_events',views.add_events,name='add_events'),
    path('add_hall',views.add_hall,name='add_hall'),
    path('hall_Booking',views.hall_Booking,name='hall_Booking'),
    path('add_type_donation',views.add_type_donation,name='add_type_donation'),
    path('add_donation',views.add_donation,name='add_donation'),
    path('Family_information',views.Family_information,name='Family_information'),
    path('view_Family_details',views.view_Family_details,name='view_Family_details'),
    path('add_deceased_persons/<int:id>',views.add_deceased_persons,name='add_deceased_persons'),
    path('Personal_details_one/<int:id>',views.Personal_details_one,name='Personal_details_one'),
    path('Baptism_details_one/<int:id>',views.Baptism_details_one,name='Baptism_details_one'),
    path('view_members/<int:id>',views.view_members,name='view_members'),
    path('confirmation_details_one/<int:id>',views.confirmation_details_one,name='confirmation_details_one'),
    path('marriage_details_one/<int:id>',views.marriage_details_one,name='marriage_details_one'),
    path('monthly_payment/<int:id>',views.monthly_payment,name='monthly_payment'),
    path('view_member_details/<int:id>',views.view_member_details,name='view_member_details'),
    path('view_family_details/<int:id>',views.view_family_details,name='view_family_details'),
    path('view_donation',views.view_donation,name='view_donation'),
    path('view_events',views.view_events,name='view_events'),
    path('view_ward',views.view_ward,name='view_ward'),
    path('view_Hall_booking',views.view_Hall_booking,name='view_Hall_booking')
]

