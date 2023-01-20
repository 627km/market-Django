from rest_framework import serializers
from .models import Product, Comment
from rest_framework.exceptions import ValidationError

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentCreateSerializer(serializers.ModelSerializer):
    member = serializers.HiddenField(
        default = serializers.CurrentUserDefault(),
        required = False
    )

    # def validate(self, attrs):
    #     request = self.context['request']
    #     if request.user.is_authenticated:
    #         attrs['member'] = request.user
    #     else: 
    #         raise ValidationError("member is required")
    #     return attrs
    
    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {'member': { 'required': False}}
