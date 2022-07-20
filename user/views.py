from rest_framework import generics,mixins,viewsets
from rest_framework.response import Response
from .models import CustomUser,UserImage
from .serializers import CustomUserSerializer,UserImagesSerializer,addUserSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def userNearByMe(request):
    """ fid the data accroging to queryset """
    data = request.data
    age_min = data['age_min']
    age_max = data['age_max']
    fb_id = data['fb_id']
    gender = data['gender']
    version = data['version']
    lat_long = data['lat_long']
    device = data['device']
    distance = data['distance']
    obj=get_object_or_404(CustomUser,fbId=fb_id)    
    if obj is not 'Not found.':
        if gender is 'all':
            queryset = CustomUser.objects.filter(age__gte=age_min,age__lte=age_max)
        else:
            print(gender)
            queryset = CustomUser.objects.filter(age__gte=age_min,age__lte=age_max,gender=gender)
            data=CustomUserSerializer(queryset,many=True).data
            return Response(data)


@api_view(['GET'])
def getUserbyid(request):
    data=request.data
    fb_id = data['fbid']
    alreadyExists = CustomUser.objects.filter(fbId=fb_id).exists()
    if alreadyExists:
        obj=CustomUser.objects.get(fbId=fb_id)
        data=CustomUserSerializer(obj,many=False).data
    else:
        content = {'detail': 'user not exist'}
        return Response(content) 
    return Response(data)


@api_view(['POST'])
def userMixinView(request):
    data=request.data
    fbId=data['fbId']
    serializer=addUserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        alreadyExists = CustomUser.objects.filter(fbId=fbId).exists()
        if alreadyExists:
            serializer=UserImagesSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                obj=CustomUser.objects.get(fbId=fbId)
                data=CustomUserSerializer(obj,many=False).data
    return Response(data)


@api_view(['DELETE'])
def user_delete_view(request):
    data=request.data
    fb_id = data['fb_id']
    obj=get_object_or_404(CustomUser,fbId=fb_id)

    CustomUser.objects.filter(fbId=fb_id).delete()
    content = {'detail': 'Successfully deleted'}
    return Response(content)


@api_view(['DELETE'])
def profile_delete_view(request):
    data=request.data
    fb_id = data['fb_id']
    image=data['image']
    obj=get_object_or_404(UserImage,fbId=fb_id,image=image)
    UserImage.objects.filter(fbId=fb_id,image=image).delete()
    content = {'detail': 'Successfully deleted'}
    return Response(content)


@api_view(['PUT'])
def user_update_view(request):
    data = request.data
    fbid=data['fbId']
    alreadyExists = CustomUser.objects.filter(fbId=fbid).exists()
    if alreadyExists:
        user = CustomUser.objects.get(fbId=fbid)
        user.firstName = data['firstName']
        user.lastName = data['lastName']
        user.gender = data['gender']
        user.age = data['age']
        user.jobTitle = data['jobTitle']
        user.location = data['location']    
        user.school = data['school']
        user.save()
        Customuser = CustomUserSerializer(user, many=False)
    else:
        content = {'detail': 'user not exist'}
        return Response(content)
    return Response(Customuser.data)


@api_view(['POST'])
def add_image(request):
    data = request.data
    fbId=data['fbId']
    alreadyExists = CustomUser.objects.filter(fbId=fbId).exists()
    if alreadyExists:
        serializer = UserImagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    content = {'detail': 'user not exist'}
    return Response(content)


# @api_view(['GET'])
# def upload_image(request):
#     all_entries = UserImage.objects.all()
#     print(all_entries)
#     serializer = UserImagesSerializer(all_entries,many=True)
#     return Response(serializer.data)