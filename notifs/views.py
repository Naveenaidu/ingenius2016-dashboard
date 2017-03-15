from datetime import datetime, timedelta
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect

from notifs.models import Notification, StartTime

def index(request):
	context = {}
	now = datetime.now()

	q = request.GET.get("q", None)
	s = StartTime.objects.all()
	
	if not q:
		if s.count() == 0:
			context['started_already'] = False
			context['just_started'] = False
		else:
			_s = StartTime.objects.all()[0]		
			end_date = _s.time + timedelta(days=1,seconds=14)
			context['started_already'] = True
			context['just_started'] = False
			context['end_date'] = end_date.strftime("%m/%d/%Y %H:%M:%S")
	else:
		if q == "getSetHack":
			if s.count() == 0:
				_s = StartTime.objects.create(time=datetime.now())
				_s.save()
				end_date = _s.time + timedelta(days=1,seconds=14)
				context['started_already'] = False
				context['just_started'] = True
				context['end_date'] = end_date.strftime("%m/%d/%Y %H:%M:%S")
			else:
				_s = StartTime.objects.all()[0]
				end_date = _s.time + timedelta(days=1,seconds=14)
				context['started_already'] = True
				context['just_started'] = False
				context['end_date'] = end_date.strftime("%m/%d/%Y %H:%M:%S")				

		else:
			if s.count() == 0:
				context['started_already'] = False
				context['just_started'] = False
			else:
				_s = StartTime.objects.all()[0]
				end_date = _s.time + timedelta(days=1,seconds=14)
				context['started_already'] = True
				context['just_started'] = False
				context['end_date'] = end_date.strftime("%m/%d/%Y %H:%M:%S")



	notif_obj = Notification.objects.order_by('-created_at')
	context['notif_obj'] = notif_obj
	return render(request, 'notifs/index.html', context)



	 
