# http://www.djangosnippets.org/snippets/331/
# based on the implementation by Sean Patrick Hogan: http://code.djangoproject.net/ticket/4604 

class Flash(dict):
    # make two commonly used flashes available as attributes
    error = property(lambda s: s.get('error', ""), lambda s, v: s.update({'error': v}))
    notice = property(lambda s: s.get('notice', ""), lambda s, v: s.update({'notice': v}))
    
    # if used as a string, return the first message found
    def __str__(self):        
        if len(self) > 0:
            return self.values()[0]
        return ""
    
    # allow {% for msg in flash %}{{ msg.type }}: {{ msg.msg }}{% endfor %}
    # this may not be necessary in newer versions of django where you should be
    # able to do: {% for key, value in flash %}{{ key }}: {{ value }}{% endfor %}
    def __iter__(self):
        for item in self.keys():
            yield {'type': item, 'msg': self[item]}
    
    # evaluate to True if there is at least one non-empty message
    def __nonzero__(self):
        return len(str(self)) > 0

# Add to MIDDLEWARE_CLASSES
class Middleware:
    def process_response(self, request, response):        
        try:
            # make sure we never override an existing flash with an empty one.
            # otherwise non-pageview requests (like views.static.serve) will
            # override a previously set flash with the empty object created in
            # process_request(). Note that we use len(), so it is still possible
            # to clear a flash by setting the dict-item to ""
            if len(request.flash):
                request.session['flash'] = request.flash            
        except:
            pass
        return response
    
    def process_request(self, request): 
        # Initialize a Flash dict that can be used in views      
        request.flash = Flash()

# Add to TEMPLATE_CONTEXT_PROCESSORS
def context_processor(request):
    if 'flash' in request.session:        
        flash = request.session['flash']
        del request.session['flash']
        return {'flash': flash}
    return {'flash': None}