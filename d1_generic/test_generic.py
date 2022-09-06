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

import os

import d1_generic.generic as generic
import protobuf_generic.generic_pb2
import protobuf_generic.authn_pb2


def test_generic_client():
    client = generic.GenericClient('localhost:9000')

    user_id = os.environ['D1_UID']
    password = os.environ['D1_PASS']

    response = client.authn_stub.LoginUser(protobuf_generic.authn_pb2.LoginUserRequest(
        user_id=user_id, password=password))

    accessToken = response.access_token

    metadata = (
        ('authorization', f'bearer {accessToken}'),
    )

    response = client.authn_stub.CreateUser(protobuf_generic.authn_pb2.CreateUserRequest(
        scopes=['READ', 'CREATE']), metadata=metadata)

    response = client.authn_stub.LoginUser(protobuf_generic.authn_pb2.LoginUserRequest(
        user_id=response.user_id, password=response.password))

    accessToken = response.access_token

    metadata = (
        ('authorization', f'bearer {accessToken}'),
    )

    plaintext = b'Darkwingduck'

    response = client.generic_stub.Encrypt(protobuf_generic.generic_pb2.EncryptRequest(
        plaintext=plaintext), metadata=metadata)

    response = client.generic_stub.Decrypt(protobuf_generic.generic_pb2.DecryptRequest(
        ciphertext=response.ciphertext, object_id=response.object_id), metadata=metadata)

    assert plaintext == response.plaintext
