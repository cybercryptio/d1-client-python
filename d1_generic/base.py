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

import datetime

import protobuf_generic.authn_pb2_grpc
import protobuf_generic.authz_pb2_grpc
import protobuf_generic.version_pb2_grpc


class BaseClient:  # pylint: disable=too-few-public-methods
    """BaseClient represents the shared functionality between various D1 services."""

    def __init__(self, channel):

        self._version_stub = protobuf_generic.version_pb2_grpc.VersionStub(
            channel)
        self._authn_stub = protobuf_generic.authn_pb2_grpc.AuthnStub(channel)
        self._authz_stub = protobuf_generic.authz_pb2_grpc.AuthzStub(channel)
        self.user_id = None
        self.password = None
        self._access_token = None
        self._token_expiry = None

    def _token_expired(self, token_expiry):
        return int((datetime.datetime.utcnow() +
                    datetime.timedelta(minutes=1)).timestamp()) > token_expiry

    def _create_metadata(self, access_token):
        if not access_token:
            if self._token_expired(self._token_expiry):
                self.login_user_set_token(self.user_id, self.password)
            else:
                access_token = self._access_token

        return (
            ('authorization', f'bearer {access_token}'),
        )

    def create_user(self, scopes, access_token=None):
        "Create user request."
        metadata = self._create_metadata(access_token)

        return self._authn_stub.CreateUser(protobuf_generic.authn_pb2.CreateUserRequest
                                           (scopes=scopes), metadata=metadata)

    def login_user_set_token(self, user_id, password):
        "New per rpc token saves the access token from the login user response."
        response = self._authn_stub.LoginUser(protobuf_generic.authn_pb2.LoginUserRequest
                                              (user_id=user_id, password=password))

        self.user_id = user_id
        self.password = password
        self._access_token = response.access_token
        self._token_expiry = response.expiry_time

    def login_user(self, user_id, password):
        "Login user request."

        return self._authn_stub.LoginUser(protobuf_generic.authn_pb2.LoginUserRequest
                                          (user_id=user_id, password=password))

    def remove_user(self, user_id, access_token=None):
        "Remove user request."
        metadata = self._create_metadata(access_token)

        return self._authn_stub.RemoveUser(protobuf_generic.authn_pb2.RemoveUserRequest
                                           (user_id=user_id), metadata=metadata)

    def create_group(self, scopes, access_token=None):
        "Create group request."
        metadata = self._create_metadata(access_token)

        return self._authn_stub.CreateGroup(protobuf_generic.authn_pb2.CreateGroupRequest
                                            (scopes=scopes), metadata=metadata)

    def add_user_to_groups(self, user_id, group_ids, access_token=None):
        "Add user to groups request."
        metadata = self._create_metadata(access_token)

        return self._authn_stub.AddUserToGroups(protobuf_generic.authn_pb2.AddUserToGroupsRequest
                                                (user_id=user_id, group_ids=group_ids),
                                                metadata=metadata)

    def remove_user_from_groups(self, user_id, group_ids, access_token=None):
        "Remove user from groups request."
        metadata = self._create_metadata(access_token)

        return self._authn_stub.RemoveUserFromGroups(
            protobuf_generic.authn_pb2.RemoveUserFromGroupsRequest
            (user_id=user_id, group_ids=group_ids),
            metadata=metadata)

    def get_permissions(self, object_id, access_token=None):
        "Get permissions request."
        metadata = self._create_metadata(access_token)

        return self._authz_stub.GetPermissions(protobuf_generic.authz_pb2.GetPermissionsRequest
                                               (object_id=object_id), metadata=metadata)

    def add_permission(self, object_id, group_ids, access_token=None):
        "Add permission request."
        metadata = self._create_metadata(access_token)

        return self._authz_stub.AddPermission(protobuf_generic.authz_pb2.AddPermissionRequest
                                              (object_id=object_id, group_ids=group_ids),
                                              metadata=metadata)

    def remove_permission(self, object_id, group_ids, access_token=None):
        "Remove permission request."
        metadata = self._create_metadata(access_token)

        return self._authz_stub.RemovePermission(protobuf_generic.authz_pb2.RemovePermissionRequest
                                                 (object_id=object_id, group_ids=group_ids),
                                                 metadata=metadata)

    def check_permission(self, object_id, access_token=None):
        "Check permission request."
        metadata = self._create_metadata(access_token)

        return self._authz_stub.CheckPermission(protobuf_generic.authz_pb2.CheckPermissionRequest
                                                (object_id=object_id), metadata=metadata)

    def version(self, access_token=None):
        "Version request."
        metadata = self._create_metadata(access_token)

        return self._version_stub.Version(protobuf_generic.version_pb2.VersionRequest(),
                                          metadata=metadata)
