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

"""This module contains the GenericClient class."""

from d1_generic import base
import protobuf_generic.generic_pb2_grpc


class GenericClient(base.BaseClient):
    """GenericClient can be used to make calls to a D1 Generic service."""

    def __init__(self, channel):
        base.BaseClient.__init__(self, channel)

        self._generic_stub = protobuf_generic.generic_pb2_grpc.GenericStub(
            channel)

    def encrypt(self, plaintext, associated_data, group_ids, access_token=None):
        "Encrypt request."
        metadata = self._create_metadata(access_token)

        return self._generic_stub.Encrypt(protobuf_generic.generic_pb2.EncryptRequest
            (plaintext=plaintext, associated_data=associated_data, group_ids=group_ids),
            metadata=metadata)

    def decrypt(self, ciphertext, associated_data, object_id, access_token=None):
        "Decrypt request."
        metadata = self._create_metadata(access_token)

        return self._generic_stub.Decrypt(protobuf_generic.generic_pb2.DecryptRequest
            (ciphertext=ciphertext, associated_data=associated_data, object_id=object_id),
            metadata=metadata)
