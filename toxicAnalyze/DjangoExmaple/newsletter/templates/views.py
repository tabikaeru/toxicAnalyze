from django.shortcuts import render

from .forms import SignupForm
from .forms import texts
from  .forms import status
from newsletter.templates.controll import controllerAnalyzeText
from newsletter.templates.controll import controllerUserAnalyze
from django.http import HttpResponse

# Create your views here.

def view_plot(image):
    response = HttpResponse(content_type="image/png")
    image.save(response, "PNG")
    return response

def signupform(request):
    # if form is submitted
    if request.method == 'POST':
        if "form" in request.POST:
            # will handle the request later
            # result_status = status(request.POST)
            form = SignupForm(request.POST)
            #  checking the form is valid or not
            if form.is_valid():
                # if valid rendering new view with values
                # the form values contains in cleaned_data dictionary
                results = controllerUserAnalyze(form.cleaned_data['twitterID'])

                return render(request, 'resultSentence.html', {
                    'twitterID': form.cleaned_data['twitterID'],
                    'identity_hate': results[0],
                    'obscene': results[1],
                    'threat': results[2],
                    'insult': results[3],
                    'severe_toxic': results[4],
                    'toxic': results[5]
                })

        if "analyse_text" in request.POST:
            # will handle the request later
            #result_status = status(request.POST)
            analyse_text = texts(request.POST)
            #  checking the form is valid or not
            if analyse_text.is_valid():
                # if valid rendering new view with values
                # the form values contains in cleaned_data dictionary
                #analyse_text.cleaned_data['sentence'] = controller(analyse_text.cleaned_data['sentence'])
                #results = []

                results = controllerAnalyzeText(analyse_text.cleaned_data['sentence'])


                return render(request, 'resultSentence.html', {
                    'identity_hate': results[0],
                    'obscene': results[1],
                    'threat': results[2],
                    'insult': results[3],
                    'severe_toxic': results[4],
                    'toxic': results[5]
                })

    else:
        # creating a new form
        form = SignupForm()
        analyse_text = texts()
        # returning form
        return render(request, 'signupform.html', {'form': form, 'analyse_text': analyse_text})
