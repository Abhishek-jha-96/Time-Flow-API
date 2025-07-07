from django.db.models import TextChoices

from time_flow_api.configurations.env_helpers import get_env_var

TASK_APP =  'apps.task'
TITLE_MAX_LEN = 100
STATUS_MAX_LEN = 10
PRIORITY_MAX_LEN = 10

class Status(TextChoices):
        UPCOMING = 'upcoming', 'Upcoming'
        COMPLETED = 'completed', 'Completed'
        MISSED = 'missed', 'Missed'

class Priority(TextChoices):
        LOW = 'Low', 'Low'
        MEDIUM = 'Medium', 'Medium'
        HIGH = 'High', 'High'
        CRITICAL = 'Critical', 'Critical'

HF_API_TOKEN = get_env_var("HF_API_TOKEN")