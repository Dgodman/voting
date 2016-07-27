from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from vote.forms import UserForm, ProfileForm
from votelist import us_states, get_absentee, us_states_dict


def index(request):
    # already registered
    if user_auth(request):
        return HttpResponseRedirect('/vote/account/')
    return HttpResponseRedirect('/vote/register/')


@login_required
def account(request):
    return render(request, 'vote/account.html', {})


def register(request, state_id=""):
    # already registered?
    if user_auth(request):
        return HttpResponseRedirect('/vote/account/')

    # no state?
    if state_id not in us_states_dict.keys():
        return HttpResponseRedirect('/vote/states/')

    # init flags
    registered = False

    # get state data
    state_data = us_states_dict[state_id]
    context_dict = {'state_id': state_id,
                    'state_long': state_data['name_long'],
                    'absentee_type': state_data['absentee_type'],
                    }

    # form stuff
    if request.method == 'POST':
        # grab info from form
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)

        # check if valid
        if user_form.is_valid() and profile_form.is_valid():
            # save the user's form data to database
            user = user_form.save()

            # hash the password with the set_password method
            user.set_password(user.password)
            user.save()

            # save profile
            profile = profile_form.save(commit=False)
            profile.user = user


            # registration successful
            registered = True
        else:
            print user_form.errors
    else:
        # start user form
        user_form = UserForm()
        # start profile form and set state_id
        profile_form = ProfileForm(initial={'state_home': state_id})
        # add forms to context
        context_dict['user_form'] = user_form
        context_dict['profile_form'] = profile_form

    context_dict['registered'] = registered
    # render template
    return render(request, 'vote/register.html', context_dict)


def states(request):
    # already registered
    if user_auth(request):
        return HttpResponseRedirect('/vote/account/')
    else:
        return render(request, 'vote/states.html', {})


def user_login(request):
    context_dict = {}
    if request.method == 'POST':
        # get username and password from login form
        username = request.POST.get('username')
        password = request.POST.get('password')

        # verify
        user = authenticate(username=username, password=password)

        # if user object, the details are correct
        if user:
            # is it active
            if user.is_active:
                # log user in
                login(request, user)
                return HttpResponseRedirect('/vote/')
            else:
                # inactive account
                return HttpResponse("Your account is disabled.")
        else:
            # bad login credentials
            context_dict['error_msg'] = "Invalid login details."
            print "Invalid login details: {0}, {1}".format(username, password)

    return render(request, 'vote/login.html', context_dict)


def user_auth(request):
    return request.user.is_authenticated()


@login_required
def user_logout(request):
    # log user out
    logout(request)
    # return to home
    return HttpResponseRedirect('/vote/')