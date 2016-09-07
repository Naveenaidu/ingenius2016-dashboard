from datetime import datetime
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from notifs.models import Notification
def index(request):
	now = datetime.now()
	notif_obj = Notification.objects.order_by('created_at')
	return render(request, 'notifs/index.html', {'notif_obj': notif_obj})
