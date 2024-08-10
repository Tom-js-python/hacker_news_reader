from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from hacker_news_scraper import get_top_links

# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)


# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
class Hello(Resource):

    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    def get(self):
        return jsonify({'Message': 'hello world'})


# another resource to calculate the square of a number
class NewsLinks(Resource):

    def get(self):
        news_links = get_top_links()

        # Convert the news_links from a list of objects to list of dictionaries so jsonify will work
        news_links_as_dict = []
        for news_link in news_links:
            news_links_as_dict.append(vars(news_link))

        return jsonify({'NewsLinks': news_links_as_dict})


# adding the defined resources along with their corresponding urls
api.add_resource(Hello, '/test')
api.add_resource(NewsLinks, '/')

# driver function
if __name__ == '__main__':
    app.run(debug=True)
