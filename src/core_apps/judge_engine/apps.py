from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class JudgeEngineConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.judge_engine"
    verbose_name = "Judge Engine"
    verbose_name_plural = "Judge Engines"
