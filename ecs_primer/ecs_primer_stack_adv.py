from typing import Mapping

from aws_cdk import core
import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_ecs as ecs
import aws_cdk.aws_ecs_patterns as ecs_patterns


class EcsPrimerStackAdv(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        myVpc = ec2.Vpc(self, "MyVPC", max_azs=2)
        # cdk deploy
        myCluster = ecs.Cluster(self, "MyCluster", vpc=myVpc)
        # cdk diff
        fargateService = ecs_patterns. \
            ApplicationLoadBalancedFargateService(
                self,
                "MyFargateApp",
                cluster=myCluster,
                listener_port=80,  # the default container port is port 80
                memory_limit_mib=1024,
                task_image_options=
                ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                    image=ecs.ContainerImage.from_asset("./app/"),
                    environment=dict(ENV_VAR1="test environment variable 1 value",
                                     ENV_VAR2="test environment variable 1 value")
                )

            )
        # cdk bootstrap

        # Tags.of(service.loadBalancer).add("alb", "Special value");
        # Tags.of(service).add("common", "value");

        # Base: https: // www.youtube.com / watch?v = bz4jTx4v - l8
