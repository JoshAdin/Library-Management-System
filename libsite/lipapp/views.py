# import necessary classes
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from lipapp.models import Book, Dvd, Libuser, Libitem, Suggestion
from .forms import SuggestionForm, SearchlibForm, LoginForm, RegisterForm
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import datetime
from random import randint
from django.views import generic


# @login_required
# class IndexView(generic.ListView):
#     template_name = 'lipapp/index.html'
#     context_object_name = 'itemlist'
#
#     def get_queryset(self, request):
#         value = 0
#         if 'luckynum' in request.session:
#             value = request.session['luckynum']
#         itemlist = Libitem.objects.all().order_by('title')[:10]
#         return render(request, 'lipapp/index.html', {'itemlist': itemlist, 'user': request.user, 'value': value})


@login_required
def index(request):
    value = 0
    if 'luckynum' in request.session:
        value = request.session['luckynum']
    itemlist = Libitem.objects.all().order_by('title')[:10]
    return render(request, 'lipapp/index.html', {'itemlist': itemlist, 'user': request.user, 'value': value})


def about(request):
    visits = int(request.COOKIES.get('visits', '0'))
    response = render(request, 'lipapp/about.html', {'user': request.user, 'visits': visits})

    # Does the cookie last_visit exist?
    if 'about_visits' in request.COOKIES:
        # Get the cookie's value.
        about_visits = request.COOKIES['about_visits']
        # Cast the value to a Python date/time object.
        about_visits_time = datetime.strptime(about_visits[:-7], "%Y-%m-%d %H:%M:%S")

        # Set time to 5 minutes = 300 seconds
        if (datetime.now() - about_visits_time).seconds > 300:
            # ...reassign the value of the cookie to +1 of what it was before...
            response.set_cookie('visits', visits + 1)
            # ...and update the last visit cookie, too.
            response.set_cookie('about_visits', datetime.now())
    else:
        # Cookie last_visit doesn't exist, so create it to the current date/time.
        response.set_cookie('about_visits', datetime.now())

    # Return response back to the user, updating any cookies that need changed.
    return response


@login_required
def detail(request, item_id):
    libitem = get_object_or_404(Libitem, pk=item_id)
    itemtype = libitem.__getattribute__('itemtype')

    if itemtype == 'Book':
        author = Book.objects.get(pk=item_id).__getattribute__('author')
        category = Book.objects.get(pk=item_id).__getattribute__('category')
        context = {'libitem': libitem, 'author': author, 'category': category, 'user': request.user}
        return render(request, 'lipapp/detail.html', context)

    elif itemtype == 'DVD':
        maker = Dvd.objects.get(pk=item_id).__getattribute__('maker')
        duration = Dvd.objects.get(pk=item_id).__getattribute__('duration')
        rating = Dvd.objects.get(pk=item_id).__getattribute__('rating')
        context = {'libitem': libitem, 'maker': maker, 'duration': duration, 'rating': rating, 'user': request.user}
        return render(request, 'lipapp/detail.html', context)


@login_required
def suggestions(request):
    suggestionlist = Suggestion.objects.all()[:10]
    return render(request, 'lipapp/suggestions.html', {'itemlist': suggestionlist, 'user': request.user})


def suggestiondetail(request, item_id):
    suggestion = get_object_or_404(Suggestion, pk=item_id)
    return render(request, 'lipapp/suggestiondetail.html', {'suggestion': suggestion})



@login_required
def newitem(request):
    suggestions = Suggestion.objects.all()
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            suggestion = form.save(commit=False)
            suggestion.num_interested = 1
            suggestion.save()
            return HttpResponseRedirect(reverse('lipapp:suggestions'))
        else:
            return render(request, 'lipapp/newitem.html', {'form':form, 'suggestions':suggestions})
    else:
        form = SuggestionForm()
        return render(request, 'lipapp/newitem.html', {'form':form, 'suggestions':suggestions})


@login_required
def searchlib(request):
    results = []
    if request.method == 'GET':
        form = SearchlibForm()

    else:
        form = SearchlibForm(request.POST)
        if form.is_valid():
            title_query = form.cleaned_data['title']
            author_query = form.cleaned_data['author']

            if title_query != '' and author_query != '':
                results = Book.objects.filter(title__icontains=title_query, author__icontains=author_query)
                if not results:
                    return render(request, 'lipapp/searchlib.html',
                                  {'form': form, 'message': "No Match Found", 'user': request.user})

            elif title_query != '':
                results = Libitem.objects.filter(title__icontains=title_query)
                if not results:
                    return render(request, 'lipapp/searchlib.html',
                                  {'form': form, 'message': "No Match Found", 'user': request.user})

            elif author_query != '':
                results = Book.objects.filter(author__icontains=author_query)
                if not results:
                    return render(request, 'lipapp/searchlib.html',
                                  {'form': form, 'message': "No Match Found", 'user': request.user})

            else:  # title_query == '' and author_query == ''
                return render(request, 'lipapp/searchlib.html',
                              {'form': form, 'message': "Please submit a search term"})

    return render(request, 'lipapp/searchlib.html', {'form': form, 'results': results, 'user': request.user})


def user_login(request):
    random_number = randint(1, 9)
    request.session['luckynum'] = random_number
    request.session.set_expiry(3600)

    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('lipapp:index'))
            else:
                return render(request, 'lipapp/login.html', {'error_message': 'Your account has been disabled'})

        elif not user and (username != '' and password != ''):
            return render(request, 'lipapp/login.html', {'form': form, 'error_message': 'Invalid login details.'})

        else:
            return render(request, 'lipapp/login.html', {'form': form})
        # return render(request, 'music/login.html', {'error_message': 'Invalid login'})
    else:
        form = LoginForm()
        return render(request, 'lipapp/login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('lipapp:index'))


@login_required
def myitems(request):
    user = Libuser.objects.get(username=request.user.username)
    if user:
        itemlist = Libitem.objects.filter(checked_out=True, user=user)
        return render(request, 'lipapp/myitems.html', {'itemlist': itemlist, 'user': request.user})
    else:
        return HttpResponse('You are not a Libuser')


def register(request):
    return render(request, 'lipapp/register.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = None
            try:
                user = Libuser.objects.get(username=form.cleaned_data['username'])
            except Exception as e:
                print(e)
            if user is not None:
                message = "User name is currently in use"
                return render(request, 'lipapp/register.html', {'form': form, 'error_message': message})

            try:
                user = Libuser.objects.get(email=form.cleaned_data['email'])
            except Exception as e:
                print(e)
            if user is not None:
                message = "Email already registered"
                return render(request, 'lipapp/register.html', {'form': form, 'error_message': message})

            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            if password2 != password:
                message = "Passwords don't match"
                return render(request, 'lipapp/register.html', {'form': form, 'error_message': message})

            user = Libuser.objects.create_user(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                email=form.cleaned_data['email'],
                last_name=form.cleaned_data['last_name'],
                password=form.cleaned_data['password'],
            )
            user.save()
            message = "Registration Successful! "
            form = RegisterForm()
            return render(request, 'lipapp/register.html', {'form': form, 'success_message': message})
        else:
            return render(request, 'lipapp/register.html', {'form': form})
    else:
        form = RegisterForm()
        return render(request, 'lipapp/register.html', {'form': form})















