from django.urls import  path
from .views import *

urlpatterns=[
    path("awards/", AwardView.as_view(), name="apiawards"),
    path("awards/<int:pk>/", AwardDetailView.as_view(), name="apidetailawards"),
    path("awards/<int:id>/<int:year>/decision/", AwardDetailYearDecisionAPIView.as_view(), name="apidecision"),
    path('decision-user/<int:id>/<int:year>/<int:award_id>/', DecisionUserAwardAPIView.as_view(), name="apidecisionuser"),
    path('search-user/', SearchUserApiView.as_view(), name='apisearchuser'),
    path('user/<int:pk>/', DetailUserApiView.as_view(), name='apidetail'),
    path('user-filter/', PartnerFilterAPIView.as_view(), name='apifilter')
    # path("users/", UsersApiView.as_view(), name="apiusers"),
    # path("users/search/", AwardOwnerSearchApiView.as_view(), name="apiuserssearch"),
    # path("decree/", PresidentDecreeApiView.as_view(), name="apidecree"),
    # path("decree/year/", PresidentDecreeYearApiView.as_view(), name="apidecreeyear"),
    # path("decree/filter/", AwardOwnerFilterApiView.as_view(), name="apifilter"),
    # path("order/", AwardOrderApiView.as_view(), name="apiorder"),
    # path("decree/filter/year", AwardFilterYearApiview.as_view(), name="apifilteryear"),
]