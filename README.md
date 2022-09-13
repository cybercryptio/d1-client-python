# Python Client Packages for CYBERCRYPT D1

Python client packages for
* [CYBERCRYPT D1 Generic](https://github.com/cybercryptio/d1-service-generic)
* [CYBERCRYPT D1 Storage](https://github.com/cybercryptio/d1-service-storage)

## D1 Generic Client

In order to use the D1 Generic client, you will need credentials for a user. If you are using the built in Standalone ID Provider you can refer to the Getting Started (insert reference) guide for details on how to obtain these. If you are using an OIDC provider you will need to obtain an ID Token in the usual way.

The client can be configured such that the access token is automatically attached to every request as shown in the following example (assuming an insecure channel is preferred):
```python
import grpc

header_adder_interceptor = interceptor.header_adder_interceptor(
        'authorization', f'bearer {access_token}')

channel = grpc.intercept_channel(
    grpc.insecure_channel('localhost:9000'), header_adder_interceptor)

client = generic.GenericClient(channel)
```

Otherwise, the access token should be given as metadata in every request, and in this case the client can be initialized as shown in the following example (assuming an insecure channel is preferred):
```python
import grpc

channel = grpc.insecure_channel('localhost:9000')

client = generic.GenericClient(channel)
```

## D1 Storage Client

In order to use the D1 Storage client, you will need credentials for a user. If you are using the built in Standalone ID Provider you can refer to the Getting Started (insert reference) guide for details on how to obtain these. If you are using an OIDC provider you will need to obtain an ID Token in the usual way.

The client can be configured such that the access token is automatically attached to every request as shown in the following example (assuming an insecure channel is preferred):
```python
import grpc

header_adder_interceptor = interceptor.header_adder_interceptor(
        'authorization', f'bearer {access_token}')

channel = grpc.intercept_channel(
    grpc.insecure_channel('localhost:9000'), header_adder_interceptor)

client = storage.StorageClient(channel)
```

Otherwise, the access token should be given as metadata in every request, and in this case the client can be initialized as shown in the following example (assuming an insecure channel is preferred):
```python
import grpc

channel = grpc.insecure_channel('localhost:9000')

client = storage.StorageClient(channel)
```

## License

The software in the CYBERCRYPT d1-client-python repository is licensed under the Apache License 2.0.
