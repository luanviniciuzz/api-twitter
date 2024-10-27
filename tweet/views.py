"""
Views for the tweet APIs.
"""
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema, extend_schema_view

from core.models import Tweet
from tweet import serializers

@extend_schema_view(
    list=extend_schema(
        summary="List all tweets.",
        description="Retrieve a list of tweets for the authenticated user."
    ),
    create=extend_schema(
        summary="Create a new tweet.",
        description="Create a new tweet associated with the authenticated user."
    ),
    retrieve=extend_schema(
        summary="Retrieve a tweet.",
        description="Get details of a specific tweet."
    ),
    update=extend_schema(
        summary="Update a tweet.",
        description="Modify an existing tweet."
    ),
    partial_update=extend_schema(
        summary="Partially updates a tweet.",
        description="Partially modify an existing tweet."
    ),
    destroy=extend_schema(
        summary="Delete a tweet.",
        description="Remove a tweet from the platform."
    )
)
class TweetViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TweetDetailSerializer
    queryset = Tweet.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve tweets for authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Return the serializer class for requests."""
        if self.action == 'list':
            return serializers.TweetSerializer

        return self.serializer_class
    
    def perform_create(self, serializer):
        """Create a new tweet."""
        serializer.save(user=self.request.user)


class LikeView(APIView):
    serializer_class = serializers.LikeSerializer
    queryset = Tweet.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Manage likes. Like tweet.",
        description="Manage likes. Like tweet.",
    )
    def post(self, request, tweet_id):
        tweet = Tweet.objects.get(id=tweet_id)
        tweet.likes.add(request.user)
        return Response({'message':'Tweet liked.'}, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Remove like from previously liked tweet.",
        description="Remove like from previously liked tweet.",
    )
    def delete(self, request, tweet_id):
        tweet = Tweet.objects.get(id=tweet_id)
        tweet.likes.remove(request.user)
        return Response({'message':'Like is removed.'}, status=status.HTTP_200_OK)