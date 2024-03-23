# Implementing AWS CDK Log Notification Pattern for Error Logs

## Abstract
The one common pattern is to set up log monitoring and notification for error logs in AWS services like AWS Lambda using Amazon CloudWatch Logs and Amazon SNS. In this article, we'll explore how to implement this pattern using AWS CDK, allowing you to automatically detect errors in your application logs and receive email notifications.

## Design
Monitoring logs for errors is crucial for maintaining the reliability and performance of cloud-based applications. AWS offers services like CloudWatch Logs for log management and Amazon SNS for notification delivery. By combining these services, you can set up automated error detection and notification systems, ensuring that you're promptly alerted to any issues in your applications.

## How to Use This Pattern
To utilize this AWS CDK log notification pattern for error logs in your own AWS environment, follow these steps:

### Prerequisites
- Make sure you have the AWS CDK installed and configured on your local machine.
- Ensure you have Python 3 installed.

### Example Code
```python
#!/usr/bin/env python3
import aws_cdk as cdk

from aws_cdk_log_notification_pattern.aws_cdk_log_notification_pattern_stack import AwsCdkLogNotificationPatternStack

app = cdk.App()

log_group_names = ["/logs/sample1", "/logs/sample2"]
AwsCdkLogNotificationPatternStack(
    app,
    "dev",
    log_group_names=log_group_names,
    email="mailme@email.com",
    env="tst",
    cost_center="AX0339",
    contact="Users@abcd.com"
)

app.synth()
```
Replace the log_group_names, email, env, cost_center, and contact parameters with your desired values.

Happy Coding!
