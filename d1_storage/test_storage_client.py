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

"""A test of an example Storage Client."""

import os

from d1_storage import storage

uid = os.environ['D1_UID']
password = os.environ['D1_PASS']


def test_storage_client():
    """Create a new Storage Client and verify that a plaintext and associated_data can be 
    stored and retrieved correctly."""
    client = storage.StorageClient('localhost:9000')

    response = client.login_user(uid, password)

    access_token = response.access_token

    metadata = (
        ('authorization', f'bearer {access_token}'),
    )

    plaintext = b'Darkwingduck'
    associated_data = b'Metadata'

    response = client.store(plaintext, associated_data, metadata)

    response = client.retrieve(response.object_id, metadata)

    assert plaintext == response.plaintext
    assert associated_data == response.associated_data
