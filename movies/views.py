from django.shortcuts import render
from django.views.generic import View
from movies.models import Movie
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import requests, json

apikey = "e99e474e"
omdbendpoint = "http://www.omdbapi.com/?"

class MoviesView(View):
   def get(self, request, id=None):
      response = {}
      if(id):
         try:
            movie = Movie.objects.get(id=id)
         except:
            response["status"] = 400
            response["info"] = "Id does not exist"
            return JsonResponse(response)

         title = movie.title
         url = "%sapikey=%s&t=%s&y=&plot=short&r=json" %(omdbendpoint, apikey, title)
         results = requests.get(url)
         data = json.loads(results.text)
         response["id"] = id
         response["title"] = title
         response["rating"] = movie.rating
         for ratings in data["Ratings"]:
            if ratings["Source"] == "Internet Movie Database":
               response["imdbRating"] = ratings["Value"]
            elif(ratings["Source"] == "Metacritic"):
               response["metascore"] = ratings["Value"]
         return JsonResponse(response)
      else:
         movies = Movie.objects.all().values("title", "rating")
         return JsonResponse(list(movies), safe=False)

   def post(self, request, id=None):
      response = {}
      try:
         data = json.loads(request.body)
      except ValueError as e:
         response["status"] = 400
         response["info"] = "Failed to load JSON"
         return JsonResponse(response)
      if("title" in data.keys() and "rating" in data.keys()):
         try:
            movie = Movie(title=data["title"],rating=data["rating"])
            movie.save()
            response["status"] = 200
            response["info"] = "Success"
            return JsonResponse(response)
         except Exception as e:
            print(e)
            response["status"] = 400
            response["info"] = "Unable to store information"
            return JsonResponse(response)
      else:
         response["status"] = 400
         response["info"] = "Please use the following keys: title and rating"
         return JsonResponse(response)

   def put(self, request, id=None):
      response = {}
      try:
         data = json.loads(request.body)
      except ValueError as e:
         response["status"] = 400
         response["info"] = "Failed to load JSON"
         return JsonResponse(response)
      if("title" in data.keys() and "rating" in data.keys()):
         try:
            try: 
               movie = Movie.objects.get(title=data["title"])
            except:
               response["status"] = 400
               response["info"] = "Title does not exist"
               return JsonResponse(response)
            movie.rating = data["rating"]
            movie.save()
            response["status"] = 200
            response["info"] = "Success"
            return JsonResponse(response)
         except Exception as e:
            print(e)
            response["status"] = 400
            response["info"] = "Unable to store information"
            return JsonResponse(response)
      else:
         response["status"] = 400
         response["info"] = "Please use the following keys: title and rating"
         return JsonResponse(response)