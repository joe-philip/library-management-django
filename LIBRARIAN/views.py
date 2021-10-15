from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from django.contrib import messages
from MAIN.models import User
from LIBRARIAN.decorators import checkLibrarian
from LIBRARIAN.forms import newAuthorForm, newBookCategoryForm, newPublisherForm, newBookForm

# Create your views here.


@checkLibrarian
def activate(request, id):
    if 'email' in request.session:
        user = User.objects.get(email=request.session['email'])
        if user.account_type == User.account_type_choices[1][0]:
            activateLibrarian = User.objects.filter(id=id)
            activateLibrarian.update(is_active=1)
            return redirect('/dashboard')
        else:
            return HttpResponse(
                'Sorry you are not authorized to access this page<br><a href="/">Go Home</a>')
    else:
        return HttpResponse(
            'Login to access this page<br><a href="/login">Go Home</a>')


@checkLibrarian
def deactivate(request, id):
    if 'email' in request.session:
        user = User.objects.get(email=request.session['email'])
        if user.account_type == User.account_type_choices[1][0]:
            deactivateLibrarian = User.objects.filter(id=id)
            deactivateLibrarian.update(is_active=0)
            return redirect('/dashboard')
        else:
            return HttpResponse(
                'Sorry you are not authorized to access this page<br><a href="/">Go Home</a>')
    else:
        return HttpResponse(
            'Login to access this page<br><a href="/login">Go Home</a>')


@checkLibrarian
def delete(request, id):
    if 'email' in request.session:
        user = User.objects.get(email=request.session['email'])
        if user.account_type == User.account_type_choices[1][0]:
            deleteLibrarian = User.objects.filter(id=id)
            deleteLibrarian.delete()
            return redirect('/dashboard')
        else:
            return HttpResponse(
                'Sorry you are not authorized to access this page<br><a href="/">Go Home</a>')
    else:
        return HttpResponse(
            'Login to access this page<br><a href="/login">Go Home</a>')


@checkLibrarian
def addAuthor(request):
    if request.method == 'POST':
        formObject = newAuthorForm(request.POST)
        if formObject.is_valid():
            formObject.save()
            return redirect('/dashboard')
        else:
            messages.error(request, formObject.errors)
            return redirect('/dashboard')
    else:
        context = {
            'form': newAuthorForm(),
            'heading': 'New Author Form',
            'action': '/LIBRARIAN/addAuthor'
        }
        return render(request, 'LIBRARIAN/add.html', context)


@checkLibrarian
def addPublisher(request):
    if request.method == 'POST':
        formObject = newPublisherForm(request.POST)
        if formObject.is_valid():
            formObject.save()
            return redirect('/dashboard')
        else:
            messages.error(request, formObject.errors)
            return redirect('/dashboard')
    else:
        context = {
            'form': newPublisherForm(),
            'heading': 'New Publisher Form',
            'action': '/LIBRARIAN/addPublisher'
        }
        return render(request, 'LIBRARIAN/add.html', context)


@checkLibrarian
def addCategory(request):
    if request.method == 'POST':
        formObject = newBookCategoryForm(request.POST)
        if formObject.is_valid():
            formObject.save()
            return redirect('/dashboard')
        else:
            messages.error(request, formObject.errors)
            return redirect('/dashboard')
    else:
        context = {
            'form': newBookCategoryForm(),
            'heading': 'New Category Form',
            'action': '/LIBRARIAN/addCategory'
        }
        return render(request, 'LIBRARIAN/add.html', context)


@checkLibrarian
def addBook(request):
    if request.method == 'POST':
        formObject = newBookForm(request.POST)
        if formObject.is_valid():
            formObject.save()
            return redirect('/dashboard')
        else:
            messages.error(request, formObject.errors)
            return redirect('/dashboard')
    else:
        context = {
            'form': newBookForm(),
            'heading': 'New Book Form',
            'action': '/LIBRARIAN/addBook'
        }
        return render(request, 'LIBRARIAN/add.html', context)
