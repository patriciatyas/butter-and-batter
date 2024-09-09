from django.shortcuts import render

def show_main(request):
    context = {
        'tagline': "Your Daily Dose of Sweetness",
        'description': "Welcome to Butter & Batter — where every bite is a blissful journey of flavors."
    }

    return render(request, 'main.html', context)