from django.shortcuts import render
from .forms import ReportForm, ProblemReportedForm

# Create your views here.
def report_view(request):
    form = ReportForm
    pform = ProblemReportedForm

    context = {
        'form':form,
        'pform':pform
    }
    return render(request, 'reports/report.html', context)