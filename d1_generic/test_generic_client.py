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

"""Tests of an example Generic Client."""

import os
import grpc

from d1_generic import generic


uid = os.environ['D1_UID']
password = os.environ['D1_PASS']


class TestGenericClient:
    "Tests of Generic Client."

    def test_generic_client(self):
        """Create a new Generic Client and verify that a
        plaintext can be encrypted and decrypted correctly."""

        with grpc.insecure_channel('localhost:9000') as channel:
            client = generic.GenericClient(channel)

            response = client.login_user(uid, password)

            access_token = response.access_token

            plaintext = b'Darkwingduck'

            response = client.encrypt(plaintext, access_token)

            response = client.decrypt(
                response.ciphertext, response.object_id, access_token)

            assert plaintext == response.plaintext

    def test_per_rpc_creds(self):
        """Create a new Generic Client and verify that a plaintext
        and associated_data can be stored and retrieved correctly."""

        with grpc.insecure_channel('localhost:9000') as channel:
            client = generic.GenericClient(channel)

            client.login_user_set_token(uid, password)

            plaintext = b'Darkwingduck'

            response = client.encrypt(plaintext)

            response = client.decrypt(
                response.ciphertext, response.object_id)

            assert plaintext == response.plaintext
