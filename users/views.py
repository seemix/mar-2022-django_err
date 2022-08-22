from rest_framework.views import APIView
from rest_framework.response import Response


class TestView(APIView):
    def get(self, request):
        return Response("method get")

    def post(self, request):
        return Response("method post")

    def put(self, request):
        return Response("method put")

    def patch(self, request):
        return Response("method patch")

    def delete(self, request):
        return Response("method delete")


users = [
    {'id': 1, 'name': 'max', 'age': 15},
    {'id': 2, 'name': 'kira', 'age': 25},
    {'id': 3, 'name': 'karina', 'age': 19},
    {'id': 4, 'name': 'oleh', 'age': 30},
]


class UserListCreateView(APIView):
    def get(self, request):
        return Response(users)

    def post(self, *args, **kwargs):
        params_dict = self.request.query_params.dict()
        print(params_dict)
        new_user = self.request.data
        users.append(new_user)
        return Response(new_user)


class UserRetrieveUpdateDestroy(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        for user in users:
            if user['id'] == pk:
                return Response(user)
        return Response('Not Found')
