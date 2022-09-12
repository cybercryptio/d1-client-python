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

"""A test of an example Generic Client."""

import os

from d1_generic import generic

uid = os.environ['D1_UID']
password = os.environ['D1_PASS']


def test_generic_client():
    """Create a new Generic Client and verify that a plaintext can be encrypted and decrypted correctly."""

    client = generic.GenericClient('localhost:9000')

    response = client.login_user(uid, password)

    access_token = response.access_token

    metadata = (
        ('authorization', f'bearer {access_token}'),
    )

    plaintext = b'Darkwingduck'

    response = client.encrypt(plaintext, metadata)

    response = client.decrypt(
        response.ciphertext, response.object_id, metadata)

    assert plaintext == response.plaintext
