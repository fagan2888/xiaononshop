from django.contrib import admin
from django import forms
import json
from order.models import Job, LineProfile, BentoType, Bento, Area, DistributionPlace, AreaLimitation, Order

admin.site.register(Job)


# --------------------------------------------------------------------------
# LineProfile
class LineProfileAdmin(admin.ModelAdmin):
    list_display = ['line_name', 'email', 'phone', 'job', 'unfollow', 'create_time']
    ordering = ['line_name', 'email', 'phone', 'job', 'unfollow', 'create_time']

admin.site.register(LineProfile)
admin.site.register(BentoType)


# --------------------------------------------------------------------------
# Bento
def make_ready(modeladmin, request, queryset):
    queryset.update(ready=True)
make_ready.short_description = "上架"
def make_non_ready(modeladmin, request, queryset):
    queryset.update(ready=False)
make_non_ready.short_description = "下架"
class BentoModelForm(forms.ModelForm):
    initall_data = dict([(a.area, 100)for a in Area.objects.all()])
    set_limitation_for_all_area = forms.BooleanField(initial=False, label="啟用下面設定限制欄位(注意: 將會同時重設「上限數量」與「剩餘數量」)", required=False)
    limitation_for_all_area = forms.CharField(widget=forms.Textarea, initial=str(initall_data), label="各地區數量限制")
    def save(self, commit=True):
        set_limitation_for_all_area = self.cleaned_data.get('set_limitation_for_all_area')
        limitation_for_all_area_str = self.cleaned_data.get('limitation_for_all_area')
        saved_bento = super(BentoModelForm, self).save()

        if set_limitation_for_all_area:
            limitation_for_all_area_dict = json.loads(limitation_for_all_area_str.replace("\'", "\""))
            for area in Area.objects.all():
                current_limitation = limitation_for_all_area_dict.get(area.area, None)
                current_limitation = int(current_limitation) if current_limitation else 0
                if AreaLimitation.objects.filter(bento=Bento.objects.get(id=saved_bento.id), area=area).exists():
                    current_area_limitation = AreaLimitation.objects.get(bento=Bento.objects.get(id=saved_bento.id), area=area)
                    current_area_limitation.limitation = current_limitation
                    current_area_limitation.remain = current_limitation
                    current_area_limitation.save()
                else:
                    AreaLimitation.objects.create(
                        bento=Bento.objects.get(id=saved_bento.id), 
                        area=area, 
                        limitation = current_limitation,
                        remain = current_limitation)
        return saved_bento

    def save_m2m(self):
        pass

    class Meta:
        model = Bento
        fields = "__all__"

class BentoAdmin(admin.ModelAdmin):
    list_display = ['date', 'bento_type', 'name', 'ready']
    ordering = ['date', 'bento_type', 'name', 'ready']
    actions = [make_ready, make_non_ready]
    form = BentoModelForm

admin.site.register(Bento, BentoAdmin)
admin.site.register(Area)
admin.site.register(DistributionPlace)



# --------------------------------------------------------------------------
# AreaLimitation
class AreaLimitationAdmin(admin.ModelAdmin):
    list_display = ["bento", "area", "limitation", "remain"]
    ordering = ["bento", "area", "limitation", "remain"]

admin.site.register(AreaLimitation, AreaLimitationAdmin)
admin.site.register(Order)




