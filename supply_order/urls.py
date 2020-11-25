from django.urls import path
from supply_order import views
from django.urls import path


app_name = 'supply_order'


urlpatterns = [

    path('details/', views.SupplyOrderListCreateAPIView.as_view(), name='supply_order_list_create'),
    path('count/', views.supply_order_count, name='supply_order_list_count'),

    # path('feedbacks/myfeedbacks/', feedback.MyFeedbackListAPIView.as_view(), name='my_workplace_feedback_list'),
    #
    # path('feedbacks/<str:uuid>/', feedback.FeedbackRetrieveUpdateDestroyAPIView.as_view(), name='workplace_feedback_manipulate'),
    # path('reacts/<str:uuid>/', reaction.ReactionListCreateAPIView.as_view(), name='reaction_list_create'),
    # path('choices/reaction', choices.ReactionChoiceListView.as_view(), name='reaction choices'),

]