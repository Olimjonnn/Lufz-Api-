from main.models import *
from rest_framework import serializers

lala =serializers.ModelSerializer

class SliderSerializer(lala):
    class Meta:
        model = Slider
        fields = "__all__"
        

class InfoSerializer(lala):
    class Meta:
        model = Info
        fields = "__all__"

class PracticesAreasSerializer(lala):
    class Meta:
        model = PracticesAreas
        fields = "__all__"

class OurExpertiseSerializer(lala):
    class Meta:
        model = OurExpertise
        fields = "__all__"

class FlaticationSerializer(lala):
    expertise = OurExpertiseSerializer(read_only=True)
    class Meta:
        model = Flatication
        fields = "__all__"

class BlogSerializer(lala):
    class Meta:
        model = Blog
        fields = "__all__"

class TeamMembersSerializer(lala):
    class Meta:
        model = TeamMembers
        fields = "__all__"

class AboutUsSerializer(lala):
    class Meta:
        model = AboutUs
        fields = "__all__"

class ContactUSSerializer(lala):
    class Meta:
        model = ContactUS
        fields = "__all__"

class NewsletterSerializer(lala):
    class Meta:
        model = Newsletter
        fields = "__all__" 