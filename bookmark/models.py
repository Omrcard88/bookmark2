from django.db import models

# Create your models here.
# 모델을 작성
# 모델 : 데이터베이스의 묘사 - 어떤 테이블을 만들 것인지, 어떤 컬럼을 만들 것인지, 어떤 제약 조건을 줄 것인지를 작성


# models.Model
# 장고에서 모델은 ORM이란 기능을 통해서 프로그래머가 SQL을 몰라도 데이터베이스를 사용할 수 있도록 도와줍니다.
# models.Model이 실제적인 기능 함수를 가지고 있다.
# 필수는 아니지만 상속받지 않고 ORM을 핸들링 하기는 매우 복잡하다.

#모델까지 만들었을 경우 : 아직 DB에 반영이 안된 상태
# 적용에는 2단계가 필요함
# makemigrations, migrate
# python manage.py makemigrations bookmark
# python manage.py sqlmigrate bookmark 0001 <- 필수는 아님
# python manage.py migrate bookmark 0001
# 데이터베이스에 직접 접근하는 방법 : python manage.py dbshell
# 데이터베이스에 간접적으로 접근하는 방법(모델을 이용해서) : python manage.py shell
class Bookmark(models.Model):
    # 클래스 변수, 속성 : 데이터베이스 컬럼
    # 문자열, 숫자, Boolean, binary는 필드의 종류로 설정 (CharFIeld)
    # 각 필드의 제약 조건 : 컬럼의 제약 조건
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    # 필드 종류 : 프론트 페이지에서 어떤 폼 태그를 사용할 것인지, 폼 태그에서 제약 조건

    def __str__(self):
        # 객체를 출력할 때 나타날 값
        return '이름 : ' + self.site_name + ", 주소 : " + self.url

    #모델 내부의 메서드들은 필드처럼 사용될 수 있다. (예를들면 받아온 변수로 한글인가 영어인가를 구분해서 반환값주는식)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detail', args=[str(self.id)]) #args는 리스트형태


    #다양한 정보를 갖는 클래스
    class Meta:
            ordering = ['site_name']