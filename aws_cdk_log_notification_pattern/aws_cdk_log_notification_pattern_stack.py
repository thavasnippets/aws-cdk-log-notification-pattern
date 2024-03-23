from aws_cdk import (
    aws_lambda as _lambda,
    aws_sns as sns,
    aws_sns_subscriptions as subscriptions,
    aws_iam as iam,
    aws_logs as logs,
    Stack
)

from constructs import Construct
from .tags import CustomTags


class AwsCdkLogNotificationPatternStack(Stack):

    def __init__(self, scope: Construct, id: str, log_group_names: list, email: str, env: str, cost_center: str, contact: str, **kwargs) -> None:
        super().__init__(scope, f"{id}", **kwargs)

        # Apply tags to the construct
        CustomTags.apply_tags(self, env, cost_center, contact)

        # Create SNS topic for email notifications
        error_topic = sns.Topic(self, f"{env}-error-topic")

        # Apply tags to the SNS topic
        CustomTags.apply_tags(error_topic, env, cost_center, contact)

        # Create Lambda function
        lambda_function = _lambda.Function(self, f"{env}-LogConsumer",
                                           runtime=_lambda.Runtime.PYTHON_3_8,
                                           handler="app.lambda_handler",
                                           code=_lambda.Code.from_asset(
                                               "lambda"),
                                           environment={
            'SNS_TOPIC_ARN': error_topic.topic_arn
        })

        # Add IAM policy for CloudWatch Logs
        lambda_function.add_to_role_policy(
            statement=iam.PolicyStatement(

                actions=["sns:Publish",
                         "logs:CreateLogGroup",
                         "logs:CreateLogStream",
                         "logs:PutLogEvents",
                         "logs:DescribeLogStreams"],
                resources=["*"]
            )
        )

        lambda_function.add_permission(
            f"AllowInvocationFromCloudWatchLogs",
            principal=iam.ServicePrincipal('logs.amazonaws.com'),
            action='lambda:InvokeFunction'

        )

        # Add email subscription to SNS topic
        error_topic.add_subscription(subscriptions.EmailSubscription(email))

        for log_group_name in log_group_names:

            # Create CloudWatch subscription filter
            logs.CfnSubscriptionFilter(
                self, f"{env}-ErrorLogFilter-{log_group_name}",
                log_group_name=log_group_name,
                filter_pattern="ERROR",
                destination_arn=lambda_function.function_arn
            )
