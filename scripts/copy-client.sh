#!/bin/bash
# TODO: rewrite that script in Python3
set -euo pipefail

SCRIPT=$(basename "$0")
CLIENT=$1

temp=$(mktemp -d tmp.d1-client-python.XXXXXXXXXX)

# TODO: tag
git clone --depth=1 git@github.com:cybercryptio/d1-service-$CLIENT.git "$temp"

rm -rf protobuf_$CLIENT
mkdir protobuf_$CLIENT
cp -v $temp/protobuf/*.proto protobuf_$CLIENT

python3 -m grpc_tools.protoc -I protobuf_$CLIENT --python_out=protobuf_$CLIENT --grpc_python_out=protobuf_$CLIENT protobuf_$CLIENT/*.proto

sed -E -i.bak 's/^(import .*_pb2 as)/from . \1/' protobuf_$CLIENT/*_pb2*.py
rm protobuf_$CLIENT/*_pb2*.py.bak

rm -rf "$temp"
echo '[+] ALL DONE'
