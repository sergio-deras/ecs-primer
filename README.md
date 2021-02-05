
# (CDK + Python) + (ESC + TS)

## Deploy an ECS cluster with CDK + Python served by a TS app

```
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ cdk synth
$ cdk bootstrap
$ cdk deploy
```

The stack is defined in ./ecs_primer/ecs_primer_stack.py
The TS app definition is inside ./app/


If you want to create the app content by yourself, copy the content of the app.ts and the Dockerfile, but execute these first:
```
$ mkdir app
$ cd app
$ npm init -y
$ npm install express typescript @types/express --save
$ npx tsc --init --outDir dist
```
