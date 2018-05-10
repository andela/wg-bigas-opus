from import_export import resources

from .models import WorkoutLog

class WorkoutLogResources(resources.ModelResource):
    class Meta:
        model : WorkoutLog