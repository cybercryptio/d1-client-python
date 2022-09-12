#!/usr/bin/env python3
# Copyright 2022 CYBERCRYPT
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This module contains the StorageClient class."""

import grpc

from d1_generic import base
import protobuf_storage.storage_pb2_grpc
import protobuf_storage.storage_pb2
import d1_generic.header_manipulator_client_interceptor as interceptor


class StorageClient(base.BaseClient):
    """Storage Client can be used to make calls to a D1 Storage service."""

    def __init__(self, endpoint, transport_creds=None, access_token=None):
        base.BaseClient.__init__(self, endpoint)

        if transport_creds:
            creds = grpc.composite_channel_credentials(
                transport_creds, grpc.access_token_call_credentials(access_token))
            channel = grpc.secure_channel(target=endpoint, credentials=creds)

        else:
            if access_token:
                header_adder_interceptor = interceptor.header_adder_interceptor(
                    'authorization', f'bearer {access_token}')

                channel = grpc.intercept_channel(
                    grpc.insecure_channel(endpoint), header_adder_interceptor)

            else:
                channel = grpc.insecure_channel(endpoint)

        self.storage_stub = protobuf_storage.storage_pb2_grpc.StorageStub(
            channel)

    def store(self, plaintext, associated_data, metadata=None):
        return self.storage_stub.Store(protobuf_storage.storage_pb2.StoreRequest(plaintext=plaintext, associated_data=associated_data), metadata=metadata)

    def retrieve(self, object_id, metadata=None):
        return self.storage_stub.Retrieve(protobuf_storage.storage_pb2.RetrieveRequest(object_id=object_id), metadata=metadata)
