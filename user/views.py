"""
Views for the user API.
"""

from rest_framework import generics, authentication, permissions, viewsets, status
from rest_framework.settings import api_settings
from user.serializers import UserSerializer,  FollowSerializer, UserImageSerializer#, AuthTokenSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from drf_spectacular.utils import extend_schema


@extend_schema(
        summary="Create a new user in the system.",
        description="Create a new user in the system.",
    )
class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class AuthTokenView(ObtainAuthToken):
    @extend_schema(
        summary="Create a new auth token for user.",
        description="Create a new auth token for user.",
    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

@extend_schema(
        summary="Manage the authenticated user. Retrieve and return the authenticated user.",
        description="Manage the authenticated user. Retrieve and return the authenticated user.",
    )
class ManageUserView(generics.RetrieveUpdateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = get_user_model().objects.all()
    def get_object(self):
        return self.request.user


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        summary="Manage following users. List follows.",
        description="Manage following users. List follows",
    )
    def list(self, request):
        follows = request.user.follows.all().order_by('-id')
        serializer = FollowSerializer(follows, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Manage following users. Follow user.",
        description="Manage following users. Follow user.",
    )
    def follow(self, request):
        follow_id = request.data.get('id')
        user_to_be_followed = get_user_model().objects.get(id=follow_id)
        request.user.follows.add(user_to_be_followed)
        return Response({"message": "Followed."}, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Manage following users. Unfollow user.",
        description="Manage following users. Unfollow user.",
    )
    def unfollow(self, request):
        unfollow_id = request.data.get('id')
        user_to_be_unfollowed = get_user_model().objects.get(id=unfollow_id)
        request.user.follows.remove(user_to_be_unfollowed)
        return Response({"message": "Unfollowed."},status=status.HTTP_200_OK)


class UploadProfilePictureView(APIView):
    serializer_class = UserImageSerializer
    queryset = get_user_model().objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        summary="Manage profile picture. Upload a profile image.",
        description="Manage profile picture. Upload a profile image.",
    )
    def post(self, request, pk=None):
        user = self.request.user
        serializer = UserImageSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)