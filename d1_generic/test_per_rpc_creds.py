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

"""A test of an example Generic Client where the access token is given as channel metadata."""

import os

from d1_generic import generic
import protobuf_generic.generic_pb2
import protobuf_generic.authn_pb2

access_token = os.environ['access_token']


def test_per_rpc_creds():
    """Create a new Storage Client and verify that a plaintext and associated_data can be 
    stored and retrieved correctly."""

    client = generic.GenericClient(
        'localhost:9000', access_token=access_token)

    plaintext = b'Darkwingduck'

    response = client.generic_stub.Encrypt(protobuf_generic.generic_pb2.EncryptRequest(
        plaintext=plaintext))

    response = client.generic_stub.Decrypt(protobuf_generic.generic_pb2.DecryptRequest(
        ciphertext=response.ciphertext, object_id=response.object_id))

    assert plaintext == response.plaintext
