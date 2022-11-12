from rest_framework import serializers

from posts.models import Group, Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author',
                  'created', 'post', )


class PostSerializer(serializers.ModelSerializer):
    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(),
                                               required=False)
    comment = CommentSerializer(read_only=True, many=True)
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')

    class Meta:
        fields = ('id', 'text', 'author', 'image',
                  'pub_date', 'group', 'comment')
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(read_only=True,
                                               many=True,
                                               )

    class Meta:
        model = Group
        fields = ('title', 'slug', 'posts')
