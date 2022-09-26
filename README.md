# Python Client Packages for CYBERCRYPT D1

Python client packages for
* [CYBERCRYPT D1 Generic](https://github.com/cybercryptio/d1-service-generic)
* [CYBERCRYPT D1 Storage](https://github.com/cybercryptio/d1-service-storage)

## D1 Generic Client

In order to use the D1 Generic client, you will need credentials for a user. If you are using the built in Standalone ID Provider you can refer to the Getting Started (insert reference) guide for details on how to obtain these. If you are using an OIDC provider you will need to obtain an ID Token in the usual way.

In all the examples below, an insecure channel is used for simplicity.

The client can be configured such that the access token is automatically set and attached to every request as shown in the following example:
```python
import grpc

with grpc.insecure_channel('localhost:9000') as channel:
    client = generic.GenericClient(channel)

    client.login_user_set_token(<user_id>, <password>)

    plaintext = b'Darkwingduck'

    response = client.encrypt(plaintext)
```

The access token can also be set be the end-user and then automatically attached to every request:
```python
import grpc

with grpc.insecure_channel('localhost:9000') as channel:
    client = generic.GenericClient(channel)

    client.set_access_token(<access_token>)

    plaintext = b'Darkwingduck'

    response = client.encrypt(plaintext)
```

Finally, the access token can be given as metadata in every request:
```python
with grpc.insecure_channel('localhost:9000') as channel:
    client = generic.GenericClient(channel)

    response = client.login_user(<user_id>, <password>)

    access_token = response.access_token

    plaintext = b'Darkwingduck'

    response = client.encrypt(plaintext, access_token)
```

## D1 Storage Client

In order to use the D1 Storage client, you will need credentials for a user. If you are using the built in Standalone ID Provider you can refer to the Getting Started (insert reference) guide for details on how to obtain these. If you are using an OIDC provider you will need to obtain an ID Token in the usual way.

In all the examples below, an insecure channel is used for simplicity.

The client can be configured such that the access token is automatically set and attached to every request as shown in the following example:
```python
import grpc

with grpc.insecure_channel('localhost:9000') as channel:
    client = storage.StorageClient(channel)

    client.login_user_set_token(<user_id>, <password>)

    plaintext = b'Darkwingduck'
    associated_data = b'Associated data'

    response = client.store(plaintext, associated_data)
```

The access token can also be set be the end-user and then automatically attached to every request:
```python
import grpc

with grpc.insecure_channel('localhost:9000') as channel:
    client = storage.StorageClient(channel)

    client.set_access_token(<access_token>)

    plaintext = b'Darkwingduck'
    associated_data = b'Associated data'

    response = client.store(plaintext, associated_data)
```

Finally, the access token can be given as metadata in every request:
```python
with grpc.insecure_channel('localhost:9000') as channel:
    client = storage.StorageClient(channel)

    response = client.login_user(<user_id>, <password>)

    access_token = response.access_token
    
    plaintext = b'Darkwingduck'
    associated_data = b'Associated data'

    response = client.store(plaintext, associated_data, access_token)
```

## License

The software in the CYBERCRYPT d1-client-python repository is licensed under the Apache License 2.0.
