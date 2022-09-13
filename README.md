# Python Client Packages for CYBERCRYPT D1

Python client packages for
* [CYBERCRYPT D1 Generic](https://github.com/cybercryptio/d1-service-generic)
* [CYBERCRYPT D1 Storage](https://github.com/cybercryptio/d1-service-storage)

## D1 Generic Client

In order to use the D1 Generic client, you will need credentials for a user. If you are using the built in Standalone ID Provider you can refer to the Getting Started (insert reference) guide for details on how to obtain these. If you are using an OIDC provider you will need to obtain an ID Token in the usual way.

```python
client = generic.GenericClient(endpoint)
```

## D1 Storage Client

In order to use the D1 Storage client, you will need credentials for a user. If you are using the built in Standalone ID Provider you can refer to the Getting Started (insert reference) guide for details on how to obtain these. If you are using an OIDC provider you will need to obtain an ID Token in the usual way.

```python
client = storage.StorageClient(endpoint)
```

## License

The software in the CYBERCRYPT d1-client-python repository is licensed under the Apache License 2.0.
