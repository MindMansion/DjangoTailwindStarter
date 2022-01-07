"""DjangoTailwindStarter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.views.generic import TemplateView

#  Just a mock data can be removed
moc_data = [
    {
        "author": '(C.A.R. Hoare)',
        "quote": '“There are two ways of constructing a software design.  One way is to make it so simple that there'
                 'are obviously no deficiencies. And the other way is to make it so complicated that there are no '
                 'obvious deficiencies.”'
    },
    {
        "author": '(Ray Ozzie)',
        "quote": '“Complexity kills.  It sucks the life out of developers, it makes products difficult to plan, '
                 'build and test, it introduces security challenges, a '
    },
    {
        "author": '(Walter Mossberg)',
        "quote": '“Just remember: you’re not a ‘dummy,’ no matter what those computer books claim.  The real dummies '
                 'are the people who–though technically expert–couldn’t design hardware and software that’s usable by '
                 'normal consumers if their lives depended upon it.” '
    }
]

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html', extra_context={'moc_data': moc_data})),
    path('admin/', admin.site.urls),
]
