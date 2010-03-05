from django.http import HttpResponse
from django.utils import simplejson
from django.utils.encoding import force_unicode
from django.utils.functional import Promise


class LazyEncoder(simplejson.JSONEncoder):
    """
    Convert lazy translations before being passed on to simplejson's encoder
    """
    def default(self, obj):
        if isinstance(obj, Promise):
            return force_unicode(obj)

        return obj


def JSONResponse(message, status=0, content={}):
    """
    Returns an HttpResponse in JSON format.
        message -- required, it will be added to the content as "message".
                    In many cases this message will be viewed by the end user.
        status  -- optional, default is 0 is for successful responses.
                    Use a different status code for unsuccessful responses.
        content -- optional, additional infomation to be sent via JSON
    """
    content["message"] = message
    content["status"] = status

    json_content = simplejson.dumps(content, cls=LazyEncoder, ensure_ascii=False)

    return HttpResponse(json_content, content_type="application/json")
