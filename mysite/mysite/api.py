from rest_framework import routers
from polls import views as polls_views

router = routers.DefaultRouter()
router.register(r'question', polls_views.QuestionViewSet)
router.register(r'choice', polls_views.ChoiceViewSet)
