import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_cdk_log_notification_pattern.aws_cdk_log_notification_pattern_stack import AwsCdkLogNotificationPatternStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_cdk_log_notification_pattern/aws_cdk_log_notification_pattern_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsCdkLogNotificationPatternStack(app, "aws-cdk-log-notification-pattern")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
