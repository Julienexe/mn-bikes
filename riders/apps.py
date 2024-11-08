from django.apps import AppConfig


class RidersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'riders'
    verbose_name = "MN Transport"
    
    def ready(self):
        import riders.signals