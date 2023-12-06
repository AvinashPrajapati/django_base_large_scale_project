from django.contrib.sitemaps import Sitemap
# from _core.models import Post


# class PostSitemap(Sitemap):
#     changefreq = "weekly"
#     priority = 0.9

#     def items(self):
#         return Post.objects.filter(status="published", is_approved=True, visibility='forall').distinct()

#     def lastmod(self, obj):
#         return obj.updated
    
#     def location(self, obj):
#         return obj.get_unauthorized_url()
  