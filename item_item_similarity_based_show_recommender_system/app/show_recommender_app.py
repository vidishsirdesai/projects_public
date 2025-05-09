from flask import Flask, request, jsonify
from sklearn.neighbors import NearestNeighbors
import numpy as np
import pandas as pd
import pickle


app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Show Recommender App</h1>"

# reading the trained model's pickle file
model = open("../artifacts/recommender_system_cosine_similarity.pkl", "rb")

# loading the model
model = pickle.load(model)

pivot_table = pd.read_csv("../artifacts/pivot_table.csv")
# df = pd.read_csv("../artifacts/df.csv")
# # creating a pivot table of movie titles and user id and imputing the NaN values
# pivot_table = pd.pivot_table(df, index = "user_id", columns = "title", values = "rating", aggfunc = "mean")
# # imputing the NaN with 0
# pivot_table.fillna(0, inplace = True)

@app.route("/recommedations", methods = ["POST"])
def recommendations():
    recommend_request = request.get_json()

    movie_name = recommend_request["movie_name"]

    distances, indices = model.kneighbors(pivot_table[movie_name].values.reshape(1, -1), n_neighbors = 11)
    recommendations = pd.DataFrame(columns = ["rank", "movie", "distance"])
    for i in range(0, len(distances.flatten())):
        if i == 0:
            continue
        new_row = pd.DataFrame({"rank": [i], "movie": [pivot_table.columns[indices.flatten()[i]]], "distance": [distances.flatten()[i]]})
        recommendations = pd.concat([recommendations, new_row], ignore_index = True)

    recommendations = dict(recommendations["movie"])

    # recommendations = jsonify(recommendations.to_dict(orient = "records"))
    return recommendations