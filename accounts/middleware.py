from django.http import JsonResponse
from django.core.cache import cache


class RateLimitingMiddleware:
    def __init__(self,get_response,rate_limit=20, window=10):
        self.get_response = get_response
        self.rate_limit = rate_limit
        self.window = window
    
    def __call__(self, request):
        # Generate a unique identifier for the client (e.g., using IP address)
        client_identifier = self.get_client_identifier(request)

        # Get the current request count for the client from cache
        request_count = cache.get(client_identifier, 0)

        # If the request count exceeds the rate limit, return a Forbidden response
        if request_count >= self.rate_limit:
            return JsonResponse({'status':208,'error':"Too many requests. Please try again later."})

        # Increment the request count and set it back in cache
        cache.set(client_identifier, request_count + 1, self.window)

        # Continue with the regular request/response handling
        response = self.get_response(request)

        return response
    
    def get_client_identifier(self, request):
        # For simplicity, let's use the client's IP address as the identifier
        return request.META.get('REMOTE_ADDR')
        