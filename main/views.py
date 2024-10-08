from django.shortcuts import render,redirect
from django.contrib.auth import logout,login,authenticate
from django.contrib import messages
from main.models import User,Questionary

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']

        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged in successfully")
            return redirect('add_question')
        else:
            messages.error(request,"Username or password invalid")

    return render(request,'user_login.html')

def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password']
        createUser = User.objects.create_user(username,email,pass1)
        createUser.first_name = username
        createUser.save()
        messages.success(request,"Your account has been created successfully")
        return redirect('user_login')
    return render(request,'user_register.html')

def logout(request):
    logout(request)
    return redirect('user_login')

def add_questions(request):
    if request.method == 'POST':
        title = request.POST['title']
        questions = request.POST['questions']
        option1 = request.POST['option1']
        option2 = request.POST['option2']
        option3 = request.POST['option3']
        option4 = request.POST['option4']
        correct_ans = request.POST['correct_ans']

        questions = Questionary.objects.create(activeuser=request.user, title=title, questions=questions, option1=option1, option2=option2, option3=option3, option4=option4, correct_ans=correct_ans)
        questions.save()
        return redirect('quiz')
    return render(request,'add_questions.html')

def quiz(request):
    questions = Questionary.objects.all()

    if request.method == 'POST':
        correct_count = 0
        total_questions = questions.count()

        # Loop through each question and validate the user's answer
        for question in questions:
            selected_answer = request.POST.get(f'question_{question.id}')
            if selected_answer == question.correct_ans:
                correct_count += 1

        # Calculate score percentage
        score_percentage = round((correct_count / total_questions) * 100, 2)

        # Redirect to the scorecard with the calculated score
        return redirect(f'/score_card/?score={score_percentage}')

    return render(request, 'give_test.html', {'questions': questions})

def score_card_view(request):
    score = request.GET.get('score')
    return render(request, 'score_card.html', {'score': score})
