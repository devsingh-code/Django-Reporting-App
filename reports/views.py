from django.shortcuts import render, get_object_or_404
from .forms import ReportForm, ProblemReportedForm
from .models import Report
from areas.models import ProductionLine

# Create your views here.
def report_view(request, production_line):
    form = ReportForm(request.POST or None)
    pform = ProblemReportedForm(request.POST or None)
    queryset = Report.objects.filter(production_line__name = production_line )
    
    if 'submitpform' in request.POST:
        r_id = request.POST.get("report_id")
        print("r id is:",r_id)

        if pform.is_valid():
            report = Report.objects.get(id = r_id)
            obj = pform.save(commit = False)
            obj.user = request.user
            obj.report = report
            print(report)
            obj.save()
            form = ReportForm()
            pform = ProblemReportedForm()

    elif 'submitform' in request.POST:
        if form.is_valid():
            line = get_object_or_404(ProductionLine, name = production_line )
            obj = form.save(commit =False)
            obj.user = request.user
            obj.production_line = line 
            obj.save()
            form = ReportForm()
            pform = ProblemReportedForm()
    
    context = {
        'form':form,
        'pform':pform,
        'object_list': queryset
    }
    return render(request, 'reports/report.html', context)




