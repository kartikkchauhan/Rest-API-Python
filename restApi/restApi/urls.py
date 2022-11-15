"""restApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from tests.api import *
from tests.kinaway_api import *
from tests.bbf_api import *

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^api/auth/$', UserAuth.as_view(), name="auth"),

    url(r'^api/company_list/$', CompanyList.as_view(), name="company_list"),
    url(r'^api/company_list_bbf/$', CompanyListBbf.as_view(), name="company_list_bbf"),
    url(r'^api/company_list_kinaway/$', CompanyListKinaway.as_view(), name="company_list_kinaway"),

    url(r'^api/add_company/$', AddCompany.as_view(), name="add_company"),

    url(r'^api/contacted_list_kinaway/$', ContactedCompanyListKinaway.as_view(), name="contacted_list_kinaway"),
    url(r'^api/non_contacted_list_kinaway/$', NonContactedCompanyListKinaway.as_view(), name="non_contacted_list_kinaway"),
    url(r'^api/contacted_list_bbf/$', ContactedCompanyListBbf.as_view(), name="contacted_list_bbf"),
    url(r'^api/non_contacted_list_bbf/$', NonContactedCompanyListBbf.as_view(), name="non_contacted_list_bbf"),

    url(r'^api/intersected_list_kinaway/$', IntersectedCompanyListKinaway.as_view(), name="intersected_list_kinaway"),
    url(r'^api/non_intersected_list_kinaway/$', NonIntersectedCompanyListKinaway.as_view(), name="non_intersected_list_kinaway"),
    url(r'^api/intersected_list_bbf/$', IntersectedCompanyListBbf.as_view(), name="intersected_list_bbf"),
    url(r'^api/non_intersected_list_bbf/$', NonIntersectedCompanyListBbf.as_view(), name="non_intersected_list_bbf"),

    url(r'^api/contacted/(?P<company_abn>\d+)$', CompanyContacted.as_view(), name="contacted"),
    url(r'^api/intersected/(?P<company_abn>\d+)$', CompanyIntersected.as_view(), name="intersected"),


    url(r'^kinaway_api/add_company/$', AddKinawayCompany.as_view(), name="add_company"),
    url(r'^kinaway_api/company_list/$', KinawayList.as_view(), name="company_list"),
    url(r'^kinaway_api/company_details/(?P<company_abn>\d+)$', KinawayCompanyInfo.as_view(), name="company_details"),

    url(r'^bbf_api/add_company/$', AddBbfCompany.as_view(), name="add_company"),
    url(r'^bbf_api/company_list/$', BbfList.as_view(), name="company_list"),
    url(r'^bbf_api/company_details/(?P<company_abn>\d+)$', BbfCompanyInfo.as_view(), name="company_details"),
]
