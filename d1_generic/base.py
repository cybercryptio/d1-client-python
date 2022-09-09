#!/usr/bin/enc python3
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

"""This module contains the BaseClient class."""

import grpc

import d1_generic.header_manipulator_client_interceptor as interceptor
import protobuf_generic.authn_pb2_grpc
import protobuf_generic.authz_pb2_grpc
import protobuf_generic.version_pb2_grpc


class BaseClient:
    """BaseClient represents the shared functionality between various D1 services."""

    def __init__(self, endpoint, transport_creds=None, access_token=None):

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

        self.version_stub = protobuf_generic.version_pb2_grpc.VersionStub(
            channel)
        self.authn_stub = protobuf_generic.authn_pb2_grpc.AuthnStub(channel)
        self.authz_stub = protobuf_generic.authz_pb2_grpc.AuthzStub(channel)
