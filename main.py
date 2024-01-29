import requests
import flask
import json

#Handle errors such as invalid genre inputs, API errors, or empty responses

#Fetch a list of all movies with an API call

#Filter the movies based on genre (determined by the genre parameter)

#Get additional details for each movie using a separate API call

#Calculate the total run time of the movies in the genre

#Calculate the average rating for the movies in the genre

#For each movie store:
  #Title, Genre, Rating, Relative Rating (rating minues the avg rating in the genre), Runtime (runtime in a human friendly format)

#Sort the movies based on relative rating (highest first) and trim to the first N records (set by the limit parameter)

#Return all data in JSON format
