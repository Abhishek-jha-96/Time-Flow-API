from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from apps.core.db_layer import db_create_record
from apps.task.models import Task
from apps.task.utils import classify_task_priority
from apps.task.settings import Status


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('priority', 'status')
    
    def validate_status(self, status):
        if not self.instance:
            if status != Status.UPCOMING:
                raise ValidationError("Cannot create task with status other than UPCOMING.")
    
    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user if request else None

        title = validated_data.get('title')
        description = validated_data.get('description', '')
        try:
            priority = classify_task_priority(title, description)
        except Exception as e:
            raise ValidationError(f"Error while make request to Hugging Face Inference endpoint with: {e}")
        task_data = {
            "title": validated_data["title"],
            "description": validated_data["description"],
            "deadline": validated_data["deadline"],
            "created_by": user,
            "priority": priority,
        }
        task = db_create_record(model=Task, data=task_data)

        return task

class TaskUpdateSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ("is_completed", )
    
    def validate_is_completed(self, is_completed):
        if self.instance.is_completed and is_completed:
            raise ValidationError("Task is already marked as completed.")
        return is_completed
    
    def update(self, instance, validated_data):
        if validated_data.get("is_completed"):
            validated_data["status"] = Status.COMPLETED
        return super().update(instance, validated_data)