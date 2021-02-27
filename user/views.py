from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from product.models import *
from user.models import *
from order.models import *
from product.models import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, authenticate, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from user.forms import Signupform, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return HttpResponse('userapp')

def loginform(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                current_user=request.user
                userprofile=UserProfile.objects.get(user_id=current_user.id)
                request.session['userimage']=userprofile.image.url
                messages.info(request, f"You are now logged in as {username}")
                return HttpResponseRedirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    category=Category.objects.all()
    context={'category':category,'form':form}
    return render(request,'login_form.html',context)

def logout_func(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return HttpResponseRedirect('/')


def signupform(request):
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            user = form.save()
            login(request, user)
            current_user = request.user
            data=UserProfile()
            data.user_id=current_user.id
            data.image="images/users/user.png"
            data.save()
            messages.success(request, 'Your account has been created!')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,form.errors)
            return HttpResponseRedirect('/signup')
    form = Signupform()
    category=Category.objects.all()
    context={
        'category':category,
        'form':form}
    return render(request,'signup_form.html',context)


@login_required(login_url='/login') # Check login
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user) # request.user is user  data
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return HttpResponseRedirect('/user')
    else:
        category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile) #"userprofile" model -> OneToOneField relatinon with user
        context = {
            'category': category,
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'user_update.html', context)

@login_required(login_url='/login') # Check login
def user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect('/user')
        else:
            messages.error(request, 'Please correct the error below.<br>'+ str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        return render(request, 'user_password.html', {'form': form,'category': category})
@login_required(login_url='/login')
def user_orders(request):
    category=Category.objects.all()
    current_user=request.user
    orders=Order.objects.filter(user_id=current_user.id)
    context={
        'category':category,
        'orders':orders}
    return render(request,'user_orders.html',context)
@login_required(login_url='/login')
def user_orderdetail(request,id):
    category=Category.objects.all()
    current_user=request.user
    order=Order.objects.filter(user_id=current_user.id, id=id)
    orderitems=OrderProduct.objects.filter(order_id=id)
    context={
        'category':category,
        'order':order,
        'orderitems':orderitems}
    return render(request,'user_order_detail.html',context)
@login_required(login_url='/login')
def user_orderproduct(request):
    category=Category.objects.all()
    current_user=request.user
    orderitems=OrderProduct.objects.filter(user_id=current_user.id)
    context={
        'category':category,
        'orderitems':orderitems}
    return render(request,'user_order_product.html',context)
@login_required(login_url='/login')
def user_comments(request):
    category=Category.objects.all()
    current_user=request.user
    comments=Comment.objects.filter(user_id=current_user.id)
    context={
        'category':category,
        'comments':comments}
    return render(request,'user_comments.html',context)
@login_required(login_url='/login')
def deletecomments(request,id):
    current_user=request.user
    Comment.objects.filter(id=id,user_id=current_user.id).delete()
    messages.success(request, 'Your comment was deleted successfully!')
    return HttpResponseRedirect('/user/user_comments')
