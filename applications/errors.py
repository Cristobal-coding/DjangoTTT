from django.forms.utils import ErrorList

class DivErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ''
        return '<div class="errorlist mt-0 pt-0 d-inline mx-2">%s</div>' % ''.join(['<small class="text-danger fs-6">*%s*</small>' % e for e in self])
    # def as_divs(self):
    #     if not self:
    #         return ''
    #     return '<div class="error alert alert-danger"><span>Solucione los siguientes errores:</span>%s</div>' % ''.join(['<li>%s</li>' % e for e in self])