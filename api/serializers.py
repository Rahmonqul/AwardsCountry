from .models import *
from rest_framework.serializers import ModelSerializer, SerializerMethodField, IntegerField, CharField
from .paginator import *

class AwardSerializer(ModelSerializer):

    class Meta:
        model = Award
        fields = ['id','name', 'image', 'code']



class PartnerSerializer(ModelSerializer):
    count_award = SerializerMethodField()  # Количество наград у партнера
    fio = CharField(source='name')  # Полное имя партнера
    image = SerializerMethodField()  # URL изображения партнера

    class Meta:
        model = Partner
        fields = ['id','fio', 'image', 'count_award']

    def get_image(self, obj):
        # Возвращаем абсолютный URL изображения партнера, если есть
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None

    def get_count_award(self, obj):
        # Считаем количество наград, связанных с данным партнером
        return AwardPartner.objects.filter(partner=obj).count()


class AwardDetailSerializer(ModelSerializer):
    partners = SerializerMethodField()  # Список партнеров
    partner_count = SerializerMethodField()  # Общее количество партнеров

    class Meta:
        model = Award
        fields = ['id','name', 'image', 'description', 'partner_count', 'partners']

    def get_partners(self, obj):
        # Получаем партнеров, связанных с данной наградой
        award_partners = AwardPartner.objects.filter(award=obj).select_related('partner')
        partners = [ap.partner for ap in award_partners]
        return PartnerSerializer(partners, many=True, context=self.context).data

    def get_partner_count(self, obj):
        # Считаем количество уникальных партнеров, связанных с наградой
        return AwardPartner.objects.filter(award=obj).count()




class AwardPartnerSerializer(ModelSerializer):
    class Meta:
        model = AwardPartner
        fields = ['id','award_id', 'decision_id', 'date', 'partner_id']

class DecisionSerializer(ModelSerializer):
    class Meta:
        model=Decision
        fields=['id', 'name', 'link']


class AwardPartnerDetailSerializer(ModelSerializer):
    partner = PartnerSerializer()

    class Meta:
        model = AwardPartner
        fields = ['id','award_id', 'decision_id', 'date', 'partner']  # Поле



class PartnerSearchSerializer(ModelSerializer):
    count_award = SerializerMethodField()  # Количество наград у партнера
    fio = CharField(source='name')  # Полное имя партнера
    image = SerializerMethodField()  # URL изображения партнера
    awards = SerializerMethodField()  # Список наград партнера с пагинацией

    class Meta:
        model = Partner
        fields = ['id','fio', 'image', 'biography', 'position', 'count_award', 'awards']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None

    def get_count_award(self, obj):
        # Получаем количество наград для партнера
        return obj.award_partners.count()

    def get_awards(self, obj):
        # Получаем все награды партнера с пагинацией
        awards = Award.objects.filter(award_partners__partner=obj)

        # Используем пагинатор
        paginator = AwardPagination()
        result_page = paginator.paginate_queryset(awards, self.context['request'])
        return paginator.get_paginated_response(AwardSerializer(result_page, many=True, context=self.context).data).data


class PartnerDetailSerializer(ModelSerializer):
    count_award = SerializerMethodField()  # Количество наград у партнера
    fio = CharField(source='name')  # Полное имя партнера
    image = SerializerMethodField()  # URL изображения партнера
    awards = SerializerMethodField()  # Список наград партнера с пагинацией

    class Meta:
        model = Partner
        fields = ['id','fio', 'image', 'biography', 'position', 'count_award', 'awards']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None

    def get_count_award(self, obj):
        # Получаем количество наград для партнера
        return obj.award_partners.count()

    def get_awards(self, obj):
        # Получаем все награды партнера с пагинацией
        awards = Award.objects.filter(award_partners__partner=obj)

        # Используем пагинатор
        paginator = AwardPagination()
        result_page = paginator.paginate_queryset(awards, self.context['request'])
        return paginator.get_paginated_response(AwardSerializer(result_page, many=True, context=self.context).data).data


class AwardPartnerFilterSerializer(ModelSerializer):
    fio = SerializerMethodField()
    owner_image = SerializerMethodField()
    awards = SerializerMethodField()

    class Meta:
        model = AwardPartner
        fields = ['id','fio', 'owner_image', 'awards']

    def get_fio(self, obj):
        return obj.partner.name

    def get_owner_image(self, obj):
        # Проверяем наличие изображения у партнера
        if obj.partner.image:
            return obj.partner.image.url
        return None

    def get_awards(self, obj):
        return {
            "name": obj.award.name,
            "image": obj.award.image.url if obj.award.image else None,
            "date_awarded": obj.date.strftime('%Y-%m-%d'),  # Используем дату напрямую
        }
