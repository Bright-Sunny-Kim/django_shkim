from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.ManyToManyField('Author')
    publisher=models.ForeignKey('Publisher', on_delete=models.CASCADE)
    publication_date=models.DateField()

    def __str__(self):
        return self.title
    # 테이블간 관계를 나타내는 필드 타입
    # ForeignKey  N:1
    # ManyToManyField  N:N
    # OneToOneField   1:1
    # on_delete 옵션 : ForeignKey 필드를 사용할 때 필수로 지정해야하는 옵션
    # CASCADE:Publisher 테이블의 특정 레코드가 삭제되면, 그 레코드에 연결된 Book테이블의 레코드도 삭제된다는 의미
    
class Author(models.Model):
    name=models.CharField(max_length=50)
    salutation=models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    website=models.URLField()

    def __str__(self):
        return self.name

