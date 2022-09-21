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

"""Tests of an example Storage Client."""

import os
import grpc

from d1_storage import storage

uid = os.environ['D1_UID']
password = os.environ['D1_PASS']


class TestStorageClass:
    """Tests of Storage Class."""

    def test_storage_client(self):
        """Create a new Storage Client and verify that a plaintext and associated_data can be
        stored and retrieved correctly."""

        with grpc.insecure_channel('localhost:9000') as channel:
            client = storage.StorageClient(channel)

            response = client.login_user(uid, password)

            access_token = response.access_token

            plaintext = b'Darkwingduck'
            associated_data = b'Associated data'

            response = client.store(plaintext, associated_data, access_token)

            response = client.retrieve(response.object_id, access_token)

            assert plaintext == response.plaintext
            assert associated_data == response.associated_data

    def test_login_set_token(self):
        """Create a new Storage Client and verify that a plaintext
        can be stored and retrieved correctly."""

        with grpc.insecure_channel('localhost:9000') as channel:
            client = storage.StorageClient(channel)

            client.login_user_set_token(uid, password)

            plaintext = b'Darkwingduck'
            associated_data = b'Associated data'

            response = client.store(plaintext, associated_data)

            response = client.retrieve(response.object_id)

            assert plaintext == response.plaintext
            assert associated_data == response.associated_data

    def test_set_token(self):
        """Create a new Storage Client and verify that an access
        token can be set without calling a login method."""

        access_token = os.environ['D1_TOKEN']

        with grpc.insecure_channel('localhost:9000') as channel:
            client = storage.StorageClient(channel)

            client.set_access_token(access_token)

            plaintext = b'Darkwingduck'
            associated_data = b'Associated data'

            response = client.store(plaintext, associated_data)

            response = client.retrieve(response.object_id)

            assert plaintext == response.plaintext
            assert associated_data == response.associated_data
