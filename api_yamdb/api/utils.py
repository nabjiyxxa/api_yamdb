class CurrentTitleDefault:
    requires_context = True

    def set_context(self, serializer_field):
        self.title = serializer_field.context['request'].data.get('title')

    def __call__(self):
        return self.title
