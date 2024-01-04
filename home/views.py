import json

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.response import Response

from home.models import Books
from home.serializers import BooksSerializer

# Create your views here.

weekDays = ["Tuesday", "Wednesday"]


class HomeView(APIView):
    def post(self, request):
        print(type(request))
        data = request.data
        serial = BooksSerializer(data=data)
        if serial.is_valid():
            print("True")
            serial.save()
            print(data)
            return Response({"data": serial.data})

        return Response({"message": "invalid data"})

    def get(self, request):
        book_id = request.query_params.get("book_id")

        if book_id:
            book = Books.objects.get(pk=book_id)
            serial = BooksSerializer(book)
            return Response({"data": serial.data})

        books = Books.objects.all()
        serial = BooksSerializer(books, many=True)

        return Response({"data": serial.data})


def hello_world(requests):
    print("req")
    print(requests)
    print("bject is creating")
    obj1 = Books(3, "Harry potter", 3000, "J K Rowly", False)
    obj1.save()
    print("books record saved")
    return HttpResponse("<h1>Heading 1</h1>")


def nav_bar(requests):
    return render(requests, "home/home.html", {"days": weekDays})


def get_books(request, id):
    book = Books.objects.get(pk=id)
    serail = BooksSerializer(book)
    # book = book.first()
    print(serail.data)
    # print(book.id)
    return HttpResponse(serail.data)


@csrf_exempt
def create_book(request):
    if request.method == "POST":
        body_uncode = request.body.decode("utf-8")
        print(body_uncode)
        body = json.loads(body_uncode)
        print(body)
        serail = BooksSerializer(data=body)
        if serail.is_valid():
            print("true")
            serail.save()
        return HttpResponse("this is post")

    return HttpResponse("not post")
