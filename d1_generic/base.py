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

import protobuf_generic.authn_pb2_grpc
import protobuf_generic.authn_pb2
import protobuf_generic.authz_pb2_grpc
import protobuf_generic.version_pb2_grpc


class BaseClient:  # pylint: disable=too-few-public-methods
    """BaseClient represents the shared functionality between various D1 services."""

    def __init__(self, channel):

        self.version_stub = protobuf_generic.version_pb2_grpc.VersionStub(
            channel)
        self.authn_stub = protobuf_generic.authn_pb2_grpc.AuthnStub(channel)
        self.authz_stub = protobuf_generic.authz_pb2_grpc.AuthzStub(channel)

    def create_user(self, scopes, metadata=None):
        "Create user request."
        return self.authn_stub.CreateUser(protobuf_generic.authn_pb2.CreateUserRequest
                                          (scopes=scopes), metadata=metadata)

    def login_user(self, user_id, password, metadata=None):
        "Login user request."
        return self.authn_stub.LoginUser(protobuf_generic.authn_pb2.LoginUserRequest
                                         (user_id=user_id, password=password), metadata=metadata)

    def remove_user(self, user_id, metadata=None):
        "Remove user request."
        return self.authn_stub.RemoveUser(protobuf_generic.authn_pb2.RemoveUserRequest
                                          (user_id=user_id), metadata=metadata)

    def create_group(self, scopes, metadata=None):
        "Create group request."
        return self.authn_stub.CreateGroup(protobuf_generic.authn_pb2.CreateGroupRequest
                                           (scopes=scopes), metadata=metadata)

    def add_user_to_groups(self, user_id, group_ids, metadata=None):
        "Add user to groups request."
        return self.authn_stub.AddUserToGroups(protobuf_generic.authn_pb2.AddUserToGroupsRequest
                                               (user_id=user_id, group_ids=group_ids),
                                               metadata=metadata)

    def remove_user_from_groups(self, user_id, group_ids, metadata=None):
        "Remove user from groups request."
        return self.authn_stub.RemoveUserFromGroups(
            protobuf_generic.authn_pb2.RemoveUserFromGroupsRequest
            (user_id=user_id, group_ids=group_ids),
            metadata=metadata)

    def get_permissions(self, object_id, metadata=None):
        "Get permissions request."
        return self.authz_stub.GetPermissions(protobuf_generic.authz_pb2.GetPermissionsRequest
                                              (object_id=object_id), metadata=metadata)

    def add_permission(self, object_id, group_ids, metadata=None):
        "Add permission request."
        return self.authz_stub.AddPermission(protobuf_generic.authz_pb2.AddPermissionRequest
                                             (object_id=object_id, group_ids=group_ids),
                                             metadata=metadata)

    def remove_permission(self, object_id, group_ids, metadata=None):
        "Remove permission request."
        return self.authz_stub.RemovePermission(protobuf_generic.authz_pb2.RemovePermissionRequest
                                                (object_id=object_id, group_ids=group_ids),
                                                metadata=metadata)

    def check_permission(self, object_id, metadata=None):
        "Check permission request."
        return self.authz_stub.CheckPermission(protobuf_generic.authz_pb2.CheckPermissionRequest
                                               (object_id=object_id), metadata=metadata)

    def version(self, metadata=None):
        "Version request."
        return self.version_stub.Version(protobuf_generic.version_pb2.VersionRequest(),
                                         metadata=metadata)
