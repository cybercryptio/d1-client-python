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
import grpc

from d1_generic import generic
import d1_generic.header_manipulator_client_interceptor as interceptor

access_token = os.environ['access_token']


def test_per_rpc_creds():
    """Create a new Storage Client and verify that a plaintext and associated_data can be 
    stored and retrieved correctly."""

    header_adder_interceptor = interceptor.header_adder_interceptor(
        'authorization', f'bearer {access_token}')

    channel = grpc.intercept_channel(
        grpc.insecure_channel('localhost:9000'), header_adder_interceptor)

    client = generic.GenericClient(channel)

    plaintext = b'Darkwingduck'

    response = client.encrypt(plaintext)

    response = client.decrypt(
        response.ciphertext, response.object_id)

    assert plaintext == response.plaintext
