from polls.models import Choice, Question
Question.objects.all() # Question要素の取得

from django.utils import timezone 
q = Question(question_text="What's new?", pub_date=timezone.now())
q.save()
q.id
q.question_text
q.pub_date
q.question_text = "What's up?"
q.save()
Question.objects.all()
