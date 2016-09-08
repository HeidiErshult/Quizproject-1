from django.shortcuts import render
def startpage(request):
	return render(request, "quiz/startsida.html")
def quiz(request):
	return render(request, "quiz/Quiz.html")
def question(request):
	return render(request, "quiz/Question.html")
def completed(request):
	return render(request, "quiz/Results.html")

# Create your views here.
