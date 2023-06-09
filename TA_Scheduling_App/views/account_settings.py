import datetime
from django.core.exceptions import PermissionDenied
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views import View
from TA_Scheduling_App.models import User


class AccountSettings(View):
    def get(self, request):
        # check user is logged in - all users can access their own account settings
        if not request.session.get("is_authenticated"):
            return redirect("login")

        # get known profile information for user
        user = User.objects.get(USER_ID=request.session["user_id"])
        return render(request, "account-settings.html", {'user': user})

    def post(self, request):
        # user has requested a profile update
        # verify user is logged in
        if not request.session.get("is_authenticated"):
            raise PermissionDenied("Not logged in.")

        user = User.objects.get(USER_ID=request.session["user_id"])

        # validate information provided by user
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        phone_number = request.POST["phone_number"]
        address = request.POST["address"]
        birth_date = request.POST["birth_date"]
        skills = request.POST["skills"]

        if skills == "":
            skills = None

        status = ""

        try:
            birth_date = datetime.date.fromisoformat(birth_date)

            User(FIRST_NAME=first_name,
                 LAST_NAME=last_name,
                 EMAIL=email,
                 PHONE_NUMBER=phone_number,
                 ADDRESS=address,
                 BIRTH_DATE=birth_date,
                 SKILLS=skills)

            # Information has been validated --> update object.
            user.setFirstName(first_name)
            user.setLastName(last_name)
            user.setEmail(email)
            user.setPhoneNumber(phone_number)
            user.setAddress(address)
            user.setBirthDate(birth_date)
            user.setSkills(skills)

            user.save()

            status = "Your profile changes have been saved."
        except IntegrityError:
            status = "The email is already taken."
        except Exception as e:
            status = e

        return render(request, "account-settings.html", {'user': user, 'status': status})
