from rest_framework import serializers

from reviews.models import Review


SCORE_ERROR = 'Оценка должна быть целым числом в пределах от 1 до 10!'
MAX_VALUE_SCORE_VALIDATOR = 10
MIN_VALUE_SCORE_VALIDATOR = 1


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    def validate_score(self, score):
        if self.context.get('request').method == 'POST':
            if (
                type(score) != int
                or (score < MIN_VALUE_SCORE_VALIDATOR
                    or score > MAX_VALUE_SCORE_VALIDATOR)
            ):
                raise serializers.ValidationError(SCORE_ERROR)
        return score

    class Meta:
        fields = ('id', 'text', 'author', 'score', 'pub_date')
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Review
