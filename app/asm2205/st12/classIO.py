from flask import *


class classIO:
    def responseContext(self, o):
        return request.form.get(o)
