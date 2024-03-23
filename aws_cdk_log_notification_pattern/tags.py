from aws_cdk import Tags, CfnResource


class CustomTags:
    @staticmethod
    def apply_tags(resource: CfnResource, env: str, cost_center: str, contact: str) -> None:
        """
        Applies tags to the specified AWS CDK resource.
        """
        Tags.of(resource).add("Environment", env)
        Tags.of(resource).add("CostCenter", cost_center)
        Tags.of(resource).add("Contact", contact)
