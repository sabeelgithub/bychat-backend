import json
import re
from django.http import HttpResponse,JsonResponse


class EamilCheckingMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        data = json.loads(request.body)
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern,data['email'] ) is not None:
           response = self.get_response(request)
        else:
            return JsonResponse({'status':208,'error':'Middleware Rejected your request,because your email is invalid'})
        # Code to be executed for each request/response after
        # the view is called.
        print('This your result')
        return response
        