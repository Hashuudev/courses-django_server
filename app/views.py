
        
from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from .models import Courses,CoursesDetails,Playlist,Comments
from django.http import HttpResponseRedirect



class Home(View):
    def get(self,request):
        if request.user.is_anonymous:
            return redirect("login")
        all_courses = Courses.objects.all()
        data = {
            'all_courses':all_courses
        }
        return render(request,'index.html',data)


class WatchVideo(View):
    def get(self,request,id):
        if request.user.is_anonymous:
            return redirect("login")
        all_courses = CoursesDetails.objects.get(courses_id=id)
        all_comments = Comments.objects.filter(commentid=all_courses.id)
        print(all_comments)
        data = {
            'all_courses':all_courses,
            'all_comments':all_comments
        }
        return render(request,'watch-video.html',data)
        
class PlaylistView(View):
    def get(self,request,id):
        if request.user.is_anonymous:
            return redirect("login")
        all_courses = Playlist.objects.filter(courses_id=id)
        data = {
            'all_courses':all_courses
        }
        return render(request,'playlist.html',data)
        

class Comment(View):

    def get(self,request,id):
        Comments.objects.get(id=id).delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
    def post(self,request):
        user_id = request.user
        id = request.POST['id']
        comment = request.POST['comment']
        Comments(commentid_id=id,comments=comment,user_id=user_id).save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 


class About(View):
    def get(self,request):
        return render(request,'about.html')