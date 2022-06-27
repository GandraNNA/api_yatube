from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import PostViewSet, CommentViewSet, GroupViewSet


router = SimpleRouter()

router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router.register(
    r'groups',
    GroupViewSet,
    basename='groups'
)
router.register(
    r'posts',
    PostViewSet,
    basename='posts'
)

urlpatterns = [
    path('v1/', include(router.urls)),
]
