from django.db import models

# Create your models here.

class Show(models.Model):
    # Fields

    name = models.CharField(max_length=100, help_text='Enter name of the show.')
    description = models.TextField(blank=True, help_text='Enter description of the show.')
    slug = models.SlugField(max_length=100, unique=True, null=False, help_text='Enter a url-safe, unique, lower-case version of the show.')

    # Metadata

    class Meta:
        ordering = ['name']

    # Methods
    
    def __str__(self):
        return self.name

class Episode(models.Model):
    # Fields

    show = models.ForeignKey(Show, on_delete=models.SET_NULL, blank=True, null=True, help_text='Enter show that includes the episode.')
    title = models.CharField(max_length=100, help_text='Enter title of the episode.')
    host = models.ForeignKey(Person, related_name='%(app_label)s_%(class)s_host_related', related_query_name='%(app_label)s_%(class)ss_host', on_delete=models.SET_NULL, null=True, blank=True, help_text='Enter person who hosts the episode.')
    featuring = models.ManyToManyField(Person, related_name='%(app_label)s_%(class)s_featuring_related', related_query_name='%(app_label)s_%(class)ss_featuring', blank=True, help_text='Enter people who feature in the episode (NOT including the host).')
    youtube_video = models.ForeignKey(YouTubeVideo, blank=True, null=True, on_delete=models.SET_NULL, help_text='Enter YouTube video of the episode.')
    external_links = models.ManyToManyField(ExternalLink, blank=True, verbose_name='External Links', help_text='Enter any external URL links (NOT including YouTube video).')
    headings = models.JSONField(null=True, blank=True, help_text='Enter JSON of different headings with key being the heading title and value being the content.')
    slug = models.SlugField(max_length=100, unique=True, null=False, help_text='Enter a url-safe, unique, lower-case version of the episode.')

    # Metadata

    class Meta:
        pass

    # Methods

    def __str__(self):
        return self.title

    def display_featuring(self):
        return ', '.join( person.__str__() for person in self.featuring.all()[:3] )

    display_featuring.short_description = 'Featuring'
