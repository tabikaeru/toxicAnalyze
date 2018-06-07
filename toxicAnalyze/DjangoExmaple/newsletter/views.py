from django.shortcuts import render
from .forms import SignupForm
from .forms import texts



def signupform(request):
    # if form is submitted
    if request.method == 'POST':
        print("post")
    else:
        # creating a new form
        form = SignupForm()
        analyse_text = texts()
        # returning form
        return render(request, 'index.html', {'form': form, 'analyse_text': analyse_text})
