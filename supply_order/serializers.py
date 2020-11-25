
"""
.. module:: Feedback Serializer

   :synopsis: All serializer related to Feedback are provided here
.. moduleauthor:: Masum Rahman
"""

from django.contrib.auth import get_user_model
from django.db.models import Count
from rest_framework import serializers
from supply_order import models


class SupplyOrderSerializer(serializers.ModelSerializer):
    """
    Serializer class for supply order.
    """
    # institute_detail = InstituteSerializer(source='institute', required=False)
    # author_detail = FeedbackAuthorSerializer(source='author', required=False)
    # react_detail = serializers.SerializerMethodField()
    # post_uuid = serializers.CharField(source='uuid', read_only=True)
    # my_reaction = serializers.SerializerMethodField()

    class Meta:
        model = models.SupplyOrder
        fields = '__all__'

        # exclude = ['reacts', 'id', 'uuid', 'last_modified']
        # extra_kwargs = {
        #     'anonymity': {'write_only': True},
        #     'author_work': {'write_only': True}
        # }
        # read_only_fields = ['creation_date', 'last_modified', 'author']

    # def get_react_detail(self, obj):
    #     queryset = obj.post_ref.values('react').exclude(react=ReactsChoices.NONE).annotate(
    #         count=Count('react')
    #     )
    #     return ReactSerializer(queryset, many=True).data  # serializing reaction queryset
    #
    # def get_my_reaction(self, obj):
    #     user = self.context['request'].user
    #     if not user.is_authenticated:
    #         return ReactsChoices.NONE
    #     my_react = ReactsChoices.NONE
    #     try:
    #         my_react = obj.post_ref.get(user=user).react
    #     except:
    #         pass
    #     return my_react
    #
    # #
    # def to_internal_value(self, data):
    #     """
    #     called before serializer validation.
    #     converts institute's uuid to id
    #     """
    #     # data['author_work'] = WorkModel.works.get(uuid=data['author_work']).id
    #     data['institute'] = WorkplaceModel.workplaces.get(uuid=data['institute']).id
    #     return super(WorkPlaceFeedbackSerializer, self).to_internal_value(data)
    #
    # def create(self, validated_data):
    #     """
    #       set request's user as feedback's author
    #     """
    #     feedback = Feedback.objects.create(author=self.context['request'].user,
    #                                        **validated_data)
    #     return feedback
    #
    # def to_representation(self, obj):
    #     representation = super(WorkPlaceFeedbackSerializer, self).to_representation(obj)
    #     # baseurl, uuid = representation['url'].rsplit('/', 1)
    #     # representation['url'] = baseurl + '/' + uuid.UUID(uuid).hex
    #     representation.pop('author')
    #     representation.pop('institute')
    #     if obj.anonymity is True:
    #         representation.pop('author_detail')
    #
    #     return representation

