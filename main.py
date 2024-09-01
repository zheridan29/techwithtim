from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

# this will check if the request follows are guideline
# this will validate if the data is sent correctly
video_put_args = reqparse.RequestParser() 
# help = error / help string if they dont send the valid argument
video_put_args.add_argument("name", type=str, help="Name of the video", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the video", required=True)
# here the request must have 3 data with it
# this is how we create a request parser that has 3 mandatory arguments



videos = {

}

class Video(Resource):
    def get(self, video_id):
        return videos[video_id]
    
    def put(self, video_id):
        args = video_put_args.parse_args()
        return {video_id: args}

api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
    # app.run(debug=True)
