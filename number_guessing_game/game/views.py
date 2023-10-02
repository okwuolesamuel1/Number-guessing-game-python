from django.shortcuts import render
import random

def home(request):
    context = {}
    if request.method == 'POST':
        guess = int(request.POST.get('guess'))
        random_number = request.session.get('random_number')
        attempts_left = request.session.get('attempts_left', 5)

        if guess == random_number:
            context['message'] = 'Congratulations! You guessed the correct number.'
            attempts_left = 0  # Reset attempts_left to 0 when the guess is correct
        elif guess < random_number:
            context['message'] = 'Wrong guess. The number is greater than what you guessed.'
        else:
            context['message'] = 'Wrong guess. The number is smaller than what you guessed.'

        attempts_left -= 1
        request.session['attempts_left'] = attempts_left
        context['attempts_left'] = attempts_left

        if attempts_left == 0:
            context['message'] = 'Game over. You have used all your attempts. The number was {}.'.format(random_number)

    else:
        random_number = random.randint(0, 999)
        request.session['random_number'] = random_number
        request.session['attempts_left'] = 15
        context['attempts_left'] = 15

    return render(request, 'game/home.html', context)

