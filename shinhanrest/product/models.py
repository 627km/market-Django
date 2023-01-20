from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name='상품명')
    price = models.IntegerField(verbose_name='가격')
    product_type = models.CharField(max_length=8, verbose_name='상품유형',
        choices = (
            ('단품', '단품'),   # ('값(db)', '보여주는 값')
            ('세트', '세트'),   # ('값(db)', '보여주는 값')
        )
    )
    tstamp = models.DateTimeField(auto_now_add=True, verbose_name='등록일시')

    class Meta:
        db_table = 'shinhan_product'
        verbose_name = '상품'
        verbose_name_plural = '상품'


# 댓글 모델만들기
# 사용자 외래키, 상품 외래키, 댓글내용, timestamp
# 관라지 페이지에 등록해서
# 관리자 페이지 통해서 댓글 3개 달기
class Comment(models.Model):
    member = models.ForeignKey('member.Member', on_delete=models.CASCADE, verbose_name='회원')  # 모델을 가르키기위해 'app.model이름'
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='상품')
    content = models.TextField(verbose_name='댓글내용')
    tstamp = models.DateTimeField(auto_now_add=True, verbose_name='등록일시')

    class Meta:
        db_table = 'shinhan_product_comment'
        verbose_name = '상품 댓글'
        verbose_name_plural = '상품 댓글'