# from typing_extensions import Required
from flask import Flask
from flask_restful import Resource,Api, reqparse
from werkzeug.exceptions import abort

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str,help="Name Of The Video is required",required=True)
video_put_args.add_argument("views", type=int,help="View Of The Video",required=True)
video_put_args.add_argument("likes", type=int,help="Like Of The Video",required=True)
videos = {}



Names = {"Mayur":{"age":25,"gender":"male"},
        "Yash":{"age":45,"gender":"male"}}
# class demo(Resource):
#     def get(self):
#         return {"Hello":"Mayur"}


    # def post(self):
    #     return {"Mydata":"Mayur Information data posted Successfully!!!"}  

    # def get(self,name,test):
    #     return {"name":name,"test":test}

    # def get(self,name):
        # return Names[name]
        # # OUTPUT:{'age': 25, 'gender': 'male'}
        # # OUTPUT{'age': 45, 'gender': 'male'}


    #####################################################
    # Rest-api Request Argument parser
    
def abort_if_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, message="Could not find video...")    
class Video(Resource):

    def get(self,video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return videos[video_id]

    def put(self,video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201
        


  
  

# api.add_resource(demo,"/demo/<string:name>/<int:test>")       
# api.add_resource(demo,"/demo/<string:name>")
#Video api
api.add_resource(Video,"/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
