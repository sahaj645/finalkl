from django.db import models

# Models for the News client application

# Story Model
class Story(models.Model):
    story_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    category_choices = (
        ('top', 'Top'),
        ('new', 'New'),
        ('best', 'Best')
    )
    category = models.CharField(max_length=10, choices=category_choices)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Comment Model
class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    content = models.TextField()
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment #{self.comment_id} on {self.story.title}"

# User Profile Model
class UserProfile(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    submissions = models.ManyToManyField(Story, related_name='submissions')
    comments = models.ManyToManyField(Comment, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    karma_points = models.IntegerField(default=0)

    def __str__(self):
        return self.username
