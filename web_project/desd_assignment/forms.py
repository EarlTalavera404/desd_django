from django import forms
from desd_assignment.models import ClubRep


#This is for the register form (CREATE)
class RegisterClubRepForm(forms.ModelForm):
    class Meta:
        model = ClubRep
        fields = ("repNumber","firstName","lastName","password","dob",)




#This is for the update form (UPDATE)
class UpdateForm(forms.ModelForm):
    class Meta:
            model = ClubRep # table data in and out
            fields = ("repNumber","firstName","lastName","password","dob",)

