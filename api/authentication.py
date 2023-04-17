from tastypie.authentication import ApiKeyAuthentication


class CustomAuthentication(ApiKeyAuthentication):
    # создаем подкласс CustomAuthentication, чтобы исключить аутентификацию при 'GET' запросе
    def is_authenticated(self, request, **kwargs):
        if request.method == 'GET':
            return True
        return super().is_authenticated(request, **kwargs)
