from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup(request):
    if request.method == 'POST':
        fn = request.POST.get('fn')
        ln = request.POST.get('ln')
        em = request.POST.get('email')
        un = request.POST.get('un')
        pw = request.POST.get('pw')

        # to validate the unique username
        if User.objects.filter(username = un).exists():
            messages.error(request, "Username is already existing..")
            return redirect('signup')

        # to validate unique email
        if User.objects.filter(email = em).exists():
            messages.error(request, "Email already exists...")
            return redirect('signup')

        # registration of user details in the 'User' model as a user
        User.objects.create_user(first_name = fn, last_name = ln, email = em, username = un, password = pw)
        messages.success(request, "Signed Up Successfully...")
        return redirect('signin')
    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')

        # to authenticate the signin credentials with the registered data of the user
        user = authenticate(request,
                            username = un,
                            password = pw)
        if user:
            messages.success(request, "Signin Successful...")
            login(request, user)
            return redirect('create')
        else:
            messages.error(request, "Credentials does not match...")
            return redirect('signin')
    return render(request, 'signin.html')

@login_required(login_url='signin')
def profile(request):
    return render(request, 'profile.html')

@login_required(login_url='signin')
def update_det(request):
    user = request.user
    if request.method == 'POST':
        fn = request.POST.get('fn')
        ln = request.POST.get('ln')
        em = request.POST.get('email')
        un = request.POST.get('un')

        # to check whether email has been updated or not
        if user.email != em:
            # to check whether updated email id is unique
            if User.objects.filter(email = em).exists():
                messages.error(request, "Email is not available...")
                return redirect('update_det')
        # to check whether username has been updated or not
        if user.username != un:
            # to check whether username is unique
            if User.objects.filter(username = un).exists():
                messages.error(request, 'Username is not available...')
                return redirect('update_det')
            
        # update the details
        user.username = un
        user.email = em
        user.first_name = fn
        user.last_name = ln

        # save the details
        user.save()

        messages.success(request, 'Details Updated Successfully...')
        return redirect('profile')
    return render(request, 'update_det.html')

@login_required(login_url='signin')
def update_pw(request):
    user = request.user # current signed-in user
    if request.method == 'POST':
        # extract the data from submitted HTML form
        old = request.POST.get('old_pw')
        new = request.POST.get('new_pw')
        confirm = request.POST.get('confirm_pw')

        # old password with existing password
        if not user.check_password(old):
            messages.error(request, "Old Password does not match...")
            return redirect('update_pw')

        # old password should not be equal to new password
        if old == new:
            messages.error(request, "New password cannot be same as Old password...")
            return redirect('update_pw')

        # new password should be equal to confirm password
        if new != confirm:
            messages.error(request, "New password does not match with Confirm password...")
            return redirect('update_pw')
        
        # encrypt and update password
        user.set_password(new)
        
        # save the password
        user.save()

        # update the session and keep the user logged in
        update_session_auth_hash(request, user)

        messages.success(request, "Password Updated Successfully...")
        return redirect('profile')
    return render(request, 'update_pw.html')

@login_required(login_url='signin')
def signout(request):
    if request.method == 'POST':
        # signout user from the session
        logout(request)
        messages.success(request, "Signed Out Successfully...")
        return redirect('signin')
    return render(request, 'signout.html')