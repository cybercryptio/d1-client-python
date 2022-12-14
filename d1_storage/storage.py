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

# pylint: disable=E1101

"""This module contains the StorageClient class."""

from d1_generic import base
import protobuf_storage.storage_pb2_grpc


class StorageClient(base.BaseClient):
    """Storage Client can be used to make calls to a D1 Storage service."""

    def __init__(self, channel):
        base.BaseClient.__init__(self, channel)

        self._storage_stub = protobuf_storage.storage_pb2_grpc.StorageStub(
            channel)

    def store(self, plaintext, associated_data, group_ids, access_token=None):
        "Store request."
        metadata = self._create_metadata(access_token)

        return self._storage_stub.Store(protobuf_storage.storage_pb2.StoreRequest
            (plaintext=plaintext, associated_data=associated_data, group_ids=group_ids),
            metadata=metadata)

    def retrieve(self, object_id, access_token=None):
        "Retrieve request."
        metadata = self._create_metadata(access_token)

        return self._storage_stub.Retrieve(protobuf_storage.storage_pb2.RetrieveRequest
                                           (object_id=object_id), metadata=metadata)

    def update(self, plaintext, associated_data, object_id, access_token=None):
        "Update request."
        metadata = self._create_metadata(access_token)

        return self._storage_stub.Update(protobuf_storage.storage_pb2.UpdateRequest
            (plaintext=plaintext, associated_data=associated_data, object_id=object_id),
            metadata=metadata)

    def delete(self, object_id, access_token=None):
        "Delete request."
        metadata = self._create_metadata(access_token)

        return self._storage_stub.Delete(protobuf_storage.storage_pb2.DeleteRequest
                                         (object_id=object_id), metadata=metadata)
