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

"""Base Client..."""

import grpc

import protobuf_generic.authn_pb2_grpc
import protobuf_generic.authz_pb2_grpc
import protobuf_generic.version_pb2_grpc


class BaseClient:
    """BaseClient..."""

    def __init__(self, endpoint):
        channel = grpc.insecure_channel(endpoint)

        self.version_stub = protobuf_generic.version_pb2_grpc.VersionStub(
            channel)
        self.authn_stub = protobuf_generic.authn_pb2_grpc.AuthnStub(channel)
        self.authz_stub = protobuf_generic.authz_pb2_grpc.AuthzStub(channel)
