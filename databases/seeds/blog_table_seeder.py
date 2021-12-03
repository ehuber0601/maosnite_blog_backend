"""BlogTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Blog import Blog

class BlogTableSeeder(Seeder):
    def run(self):
        Blog.create({"title":"My Life", "body":"I live in a tree"})
        Blog.create({"title":"Hello", "body":"My name is Phil"})
        Blog.create({"title":"How to make a cake", "body":"1. eggs 2. flour 3. milk"})