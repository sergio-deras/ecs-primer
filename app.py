#!/usr/bin/env python3

from aws_cdk import core

from ecs_primer.ecs_primer_stack import EcsPrimerStack


app = core.App()
EcsPrimerStack(app, "ecs-primer")

app.synth()
