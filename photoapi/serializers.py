
from django.forms import widgets
from rest_framework import serializers
from photoapi.models import UserPhoto

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPhoto
        fields = ('id', 'user_id', 'title', 'image')

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.id = attrs.get('id', instance.id)
            instance.user_id = attrs.get('user_id', instance.user_id)
            instance.title = attrs.get('title', instance.title)
            instance.image = attrs.get('image', instance.image)
            
            return instance

        # Create new instance
        return Images(**attrs)
