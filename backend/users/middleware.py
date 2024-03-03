from django.utils.deprecation import MiddlewareMixin

class DisableCsrfCheck(MiddlewareMixin):
    def process_request(self, request):
        api_prefix = '/users/'
        if request.path.startswith(api_prefix):
            setattr(request, '_dont_enforce_csrf_checks', True)