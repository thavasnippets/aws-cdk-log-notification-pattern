#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aws_cdk_log_notification_pattern.aws_cdk_log_notification_pattern_stack import AwsCdkLogNotificationPatternStack


app = cdk.App()

log_group_names = ["/logs/sample1", "/logs/sample2"]
AwsCdkLogNotificationPatternStack(app, "dev", log_group_names=log_group_names,
                                  email="mailme@email.com", env="tst", cost_center="AX0339", contact="Users@abcd.com")

app.synth()
