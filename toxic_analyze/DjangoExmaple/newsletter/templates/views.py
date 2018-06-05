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
                # analyse_text.cleaned_data['sentence'] = controller(analyse_text.cleaned_data['sentence'])
                # hoge = []
                """
                for line in range(6):
                    hoge.append(line)
                """

                # result_status.cleaned_data['identity_hate'], result_status.cleaned_data['obscene'], result_status.cleaned_data['threat'], result_status.cleaned_data['insult'], result_status.cleaned_data['severe_toxic'], result_status.cleaned_data['toxic'] = controller(analyse_text.cleaned_data['sentence'])
                hoge = controllerUserAnalyze(form.cleaned_data['twitterID'])

                """
                result_status.cleaned_data['identity_hate'], result_status.cleaned_data['obscene'], \
                    result_status.cleaned_data['threat'], result_status.cleaned_data['insult'], result_status.cleaned_data['severe_toxic'], result_status.cleaned_data['toxic'] = hoge[0], hoge[1], hoge[2], hoge[3], hoge[4], hoge[5]
                """
                # hoge = controllerAnalyzeText(analyse_text.cleaned_data['sentence'])
                """
                return render(request, 'resultSentence.html', {
                    'identity_hate': result_status.cleaned_data['identity_hate'], 'obscene': result_status.cleaned_data['obscene'], 'threat': result_status.cleaned_data['threat'], 'insult': result_status.cleaned_data['insult'], 'severe_toxic': result_status.cleaned_data['severe_toxic'], 'toxic': result_status.cleaned_data['toxic']
                """

                return render(request, 'resultSentence.html', {
                    'twitterID': form.cleaned_data['twitterID'],
                    'identity_hate': hoge[0],
                    'obscene': hoge[1],
                    'threat': hoge[2],
                    'insult': hoge[3],
                    'severe_toxic': hoge[4],
                    'toxic': hoge[5]
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
                #hoge = []
                """
                for line in range(6):
                    hoge.append(line)
                """

                #result_status.cleaned_data['identity_hate'], result_status.cleaned_data['obscene'], result_status.cleaned_data['threat'], result_status.cleaned_data['insult'], result_status.cleaned_data['severe_toxic'], result_status.cleaned_data['toxic'] = controller(analyse_text.cleaned_data['sentence'])
                hoge = controllerAnalyzeText(analyse_text.cleaned_data['sentence'])

                """
                result_status.cleaned_data['identity_hate'], result_status.cleaned_data['obscene'], \
                    result_status.cleaned_data['threat'], result_status.cleaned_data['insult'], result_status.cleaned_data['severe_toxic'], result_status.cleaned_data['toxic'] = hoge[0], hoge[1], hoge[2], hoge[3], hoge[4], hoge[5]
                """
                #hoge = controllerAnalyzeText(analyse_text.cleaned_data['sentence'])
                """
                return render(request, 'resultSentence.html', {
                    'identity_hate': result_status.cleaned_data['identity_hate'], 'obscene': result_status.cleaned_data['obscene'], 'threat': result_status.cleaned_data['threat'], 'insult': result_status.cleaned_data['insult'], 'severe_toxic': result_status.cleaned_data['severe_toxic'], 'toxic': result_status.cleaned_data['toxic']
                """

                return render(request, 'resultSentence.html', {
                    'identity_hate': hoge[0],
                    'obscene': hoge[1],
                    'threat': hoge[2],
                    'insult': hoge[3],
                    'severe_toxic': hoge[4],
                    'toxic': hoge[5]
                })

    else:
        # creating a new form
        form = SignupForm()
        analyse_text = texts()
        # returning form
        return render(request, 'signupform.html', {'form': form, 'analyse_text': analyse_text})
