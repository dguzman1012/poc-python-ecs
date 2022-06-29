import boto3
import datetime
import json

client = boto3.client('events')

response = client.put_events(
    Entries=[
        {
            'Source': 'run.task.definition',
            'DetailType': "ECS Task definition triggered",
            'Detail': json.dumps({
                "ecs-task-definition": "poc-python-ecs-task-definition"
            }),
            'EventBusName': 'cor-enterprise-bus-service-staging'
        }
    ]
)

print(response)