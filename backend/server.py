import os
from dotenv import load_dotenv
import argparse
from flask import Flask, jsonify, request
from waitress import serve
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from hacker_news_scraper import get_top_links

# Load environment variables from the .env file
load_dotenv()

# creating the flask app
app = Flask(__name__)

# Allow Cross-origin resource requests
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# creating an API object
api = Api(app)


# Just used by test scripts to see if connection from client to server works
class Test(Resource):

    def get(self):
        return jsonify({'Message': 'hello world'})


# The actual resource. This returns a list of news links from Hacker News given four parameters
class NewsLinks(Resource):

    def get(self):
        # Extract the parameters and convert to the proper type as needed
        num_links = int(request.args.get('num_links'))
        num_pages = int(request.args.get('num_pages'))
        search_term = request.args.get('search_term')
        min_points = int(request.args.get('min_points'))

        # The call to the scraper to get the links
        news_links = get_top_links(num_links, num_pages, search_term, min_points)

        # Convert the news_links from a list of objects to list of dictionaries so jsonify will work
        news_links_as_dict = []
        for news_link in news_links:
            news_links_as_dict.append(vars(news_link))

        # Return these links
        return jsonify({'NewsLinks': news_links_as_dict})


# adding the defined resources along with their corresponding urls
api.add_resource(Test, '/test')
api.add_resource(NewsLinks, '/')

# Run the app when this file is called directly
if __name__ == '__main__':
    # Set up argument parser to ensure user selected whether to run in development or production
    parser = argparse.ArgumentParser(description='Run the Flask application.')
    parser.add_argument('--env', type=str, choices=['development', 'production'], required=True,
                        help="Choose the environment: 'development' or 'production'")

    args = parser.parse_args()

    if args.env == 'development':
        # Run Flask in development mode
        port = int(os.getenv("VITE_BACKEND_PORT_DEV", 5000))  # Default to 5000 if not found
        app.run(host='0.0.0.0', port=port, debug=True)  # Debug=True enables hot reloading and better error messages
    elif args.env == 'production':
        # Run Flask using Waitress in production mode
        port = int(os.getenv("VITE_BACKEND_PORT_PROD", 8080))  # Default to 8080 if not found
        print('Running server on port', port)
        serve(app, host='0.0.0.0', port=port)

