def customheader(request):
    x = {}
    x['learning'] = 'Django' # string:string
    x['speed'] = 55          # string:integer
    
    return HttpResponse(headers=x)  # adds our custom headers to the response

def customcode(request):
    return HttpResponse("Working on that", status=201)  # return teh response code 201 "created"

