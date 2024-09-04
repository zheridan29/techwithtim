from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

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

# define a function for abort, if the video_id does not exist in our videos dictionary
# 404 - does not exists
def abort_if_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, message="Video ID does not valid...")

# define a function to test if a video exist in the dictionary using a video_id
# 409 - conflict with running the request in the server
def abort_if_video_id_exists(video_id):
    if video_id in videos:
        abort(409, message="Video already exists with that ID...")

class Video(Resource):
    def get(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return videos[video_id]
    
    def put(self, video_id):
        abort_if_video_id_exists(video_id)
        args = video_put_args.parse_args()
        # This is how you store data from the forms tru the args
        # from the request data is save to the empty dictionary named: videos
        videos[video_id] = args
        # returns a web status code
        return videos[video_id], 201
    
    # 204 - meaning deleted successfully
    def delete(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        del videos[video_id]
        return '', 204

class Welcome(Resource):
    def get(self):
        return {"data":"Welcome to RestAPI"}


api.add_resource(Video, "/video/<int:video_id>")
api.add_resource(Welcome, "/welcome")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
    # app.run(debug=True)
