### To reproduce:

The following assumes that the [`aws-sam-cli`](https://github.com/aws/aws-sam-cli)
[PR #2458](https://github.com/ramosbugs/aws-sam-cli/tree/develop-operation-name) branch has been
checked out into `../aws-sam-cli` and that a `virtualenv` has been initialized properly.

To start the API:
```
$ python ../aws-sam-cli/samcli local start-api
```

Actual output:
```
$ curl http://127.0.0.1:3000/foo
{"message": "routed to handler getFoo"}
$ curl -X POST http://127.0.0.1:3000/foo
{"message": "routed to handler getFoo"}
```
Note that both requests are supplied an `operationName` of `getFoo`. The latter request should be
`postFoo`.

Expected output:
```
$ curl http://127.0.0.1:3000/foo
{"message": "routed to handler getFoo"}
$ curl -X POST http://127.0.0.1:3000/foo
{"message": "routed to handler postFoo"}
```
