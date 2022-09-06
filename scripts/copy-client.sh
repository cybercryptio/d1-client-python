#!/bin/bash
# TODO: rewrite that script in Python3
set -euo pipefail

temp=$(mktemp -d tmp.d1-client-python.XXXXXXXXXX)

# TODO: tag
git clone --depth=1 git@github.com:cybercryptio/d1-service-generic.git "$temp"

rm -rf d1_client
mkdir d1_client
cp -v $temp/protobuf/*.proto d1_client

python3 -m grpc_tools.protoc -I d1_client --python_out=d1_client --grpc_python_out=d1_client d1_client/*.proto

sed -E -i.bak 's/^(import .*_pb2 as)/from . \1/' d1_client/*_pb2*.py
rm d1_client/*_pb2*.py.bak

rm -rf "$temp"
echo '[+] ALL DONE'