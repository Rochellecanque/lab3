from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('index.html/', views.login, name='index'),
    path('analytics.html/', views.analytics_view, name='analytics'),
    path('reports-sales.html/', views.reports_sales, name='reports_sales'),
    path('reports-leads.html/', views.reports_leads, name='reports_leads'),
    path('reports-project.html/', views.reports_project, name='reports_project'),
    path('reports-timesheets.html/', views.reports_timesheets, name='reports_timesheets'),
    path('apps-chat.html/', views.apps_chat, name='apps_chat'),
    path('apps-email.html/', views.apps_email, name='apps_email'),
    path('apps-tasks.html/', views.apps_tasks, name='apps_tasks'),
    path('apps-notes.html/', views.apps_notes, name='apps_notes'),
    path('apps-storage.html/', views.apps_storage, name='apps_storage'),
    path('apps-calendar.html/', views.apps_calendar, name='apps_calendar'),
     # Catch-all redirect to index.html
    path('<path:path>/', RedirectView.as_view(url='', permanent=True)),
    path('<path:path>/index.html', RedirectView.as_view(url='/index.html', permanent=True)),
    # Add more paths as needed
]
