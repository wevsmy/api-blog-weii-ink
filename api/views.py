from django.http import JsonResponse
from rest_framework.views import APIView


# Create your views here.
class GetMessageView(APIView):
    # get 请求
    def get(self, request):
        # 获取参数数据
        get = request.GET
        # 获取参数 a
        a = get.get('a')
        print(a)
        # 返回信息
        d = {
            'status': 200,
            'message': 'success',
            'data': get
        }
        return JsonResponse(d)
