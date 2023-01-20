from rest_framework import serializers

from .models import Product, Comment, Like

class ProductSerializer(serializers.ModelSerializer):
    comment_count = serializers.SerializerMethodField() # methodfield : 함수를 만들어서 정의 
    like_count = serializers.SerializerMethodField()

    def get_comment_count(self, obj): # get_필드명 (약속)
        return obj.comment_set.all().count()    # 모델명_set (= 모델명.objects)
        # return Comment.objects.filter(product=obj).count()
    def get_like_count(self,obj):
        return obj.like_set.all().count()
    
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
    
    def validate_member(self, value):
        if not value.is_authenticated:
            raise serializers.ValidationError('member is required')
        return value

    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {'member': { 'required': False}}


class LikeCreateSerializer(serializers.ModelSerializer):
# 로그인한 사용자가 자동으로 들어가도록 하는 코드 
    member = serializers.HiddenField(
        default = serializers.CurrentUserDefault(),
        required = False
    )

    # 로그인 에러에 대해 response 해주는 메소드 (유효성 검사)
    def validate_member(self, value):
        if not value.is_authenticated:
            raise serializers.ValidationError('member is required')
        return value
# 여기까지

    class Meta:
        model = Like
        fields = '__all__'
        extra_kwargs = {'member': { 'required': False}}