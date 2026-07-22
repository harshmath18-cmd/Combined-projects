from flask import Flask, render_template, request

from utils.recommender import recommend

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
    "index.html",
    show_ai_search=False
)


@app.route("/recommend", methods=["GET", "POST"])
def recommend_page():

    print("Request Method:", request.method)

    restaurants = []
    query = ""

    if request.method == "POST":

        query = request.form.get("query", "").strip()

        print("\nQuery Received:", query)

        if query:

            results = recommend(query, top_n=10)

            print("Results Found:", len(results))

            restaurants = results.to_dict(orient="records")

    return render_template(
    "recommend.html",
    restaurants=restaurants,
    query=query,
    show_ai_search=True
)


if __name__ == "__main__":
    app.run(debug=True)