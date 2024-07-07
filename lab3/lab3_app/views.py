from django.shortcuts import render

def index(request):
    return render(request, 'lab3_app/index.html')

def login(request):
    return render(request, 'lab3_app/auth-login-creative.html')

def analytics_view(request):
    # Your view logic goes here
    return render(request, 'lab3_app/analytics.html')

def reports_sales(request):
    # Your view logic goes here
    return render(request, 'lab3_app/reports-sales.html')

def reports_leads(request):
    # Your view logic goes here
    return render(request, 'lab3_app/reports-leads.html')

def reports_project(request):
    # Your view logic goes here
    return render(request, 'lab3_app/reports-project.html')

def reports_timesheets(request):
    # Your view logic goes here
    return render(request, 'lab3_app/reports-timesheets.html')

def apps_chat(request):
    # Your view logic goes here
    return render(request, 'lab3_app/apps-chat.html')

def apps_email(request):
    # Your view logic goes here
    return render(request, 'lab3_app/apps-email.html')

def apps_tasks(request):
    # Your view logic goes here
    return render(request, 'lab3_app/apps-tasks.html')

def apps_notes(request):
    # Your view logic goes here
    return render(request, 'lab3_app/apps-notes.html')

def apps_storage(request):
    # Your view logic goes here
    return render(request, 'lab3_app/apps-storage.html')

def apps_calendar(request):
    # Your view logic goes here
    return render(request, 'lab3_app/apps-calendar.html')
# Add more views as needed
