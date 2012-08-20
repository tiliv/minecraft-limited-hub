from django.db import models

from taggit.managers import TaggableManager

# class GameMode(models.Model):
#     name = models.CharField(max_length=100, blank=False, \
#             help_text="Minecraft game type name.")
#     description = models.CharField(max_length=200, blank=False, \
#             help_text="Simple mode description.")
# 
class Server(models.Model):
    name = models.CharField(max_length=200, blank=False, \
            help_text="Server name")
    description = models.TextField(blank=False, \
            help_text="Public description of the server's features and gameplay type.")
    address = models.CharField(max_length=200, blank=False, \
            help_text="Address and port information, exactly as required by a Minecraft client.")
    
    # Through the use of standard tag names, the game details can be communicated for easy search and directory features.
    tags = TaggableManager()
    

