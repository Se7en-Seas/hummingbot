## Penumbra Osiris
The [penumbra osiris bot](https://github.com/Se7en-Seas/hummingbot/blob/penunumbra-integration/scripts/penumbra_osiris.py) aims to be an approximate parity to its [rust counterpart](https://github.com/penumbra-zone/osiris/) and function as an abstraction to allow new users to interact with the penumbra protocol without needing to understand the underlying mechanics.

## First time setup
1. Clone this (repo and branch)[https://github.com/Se7en-Seas/hummingbot/tree/penunumbra-integration/]
2. Set up pclientd and have it running with any releveant test funds. You'll know you're good to go when you can run the following command and get a response
```bash
grpcurl -plaintext -d '{"account_filter": {"account": 0}}'     127.0.0.1:8081 penumbra.view.v1.ViewService/Balances
```
3.



## How to refresh the Penumbra Protos
Note the last proto update was on version 0.75.0
1. Grab all of the relevant [protos](https://github.com/penumbra-zone/penumbra/tree/main/proto)
2. Move everything out of rust-vendored to top level dir so everything is in proto/penumbra and appears as [so](https://github.com/Se7en-Seas/hummingbot/tree/penunumbra-integration/hummingbot/connector/gateway/clob_spot/data_sources/penumbra/proto/penumbra)
3. Wipe the [generated directory](https://github.com/Se7en-Seas/hummingbot/tree/penunumbra-integration/hummingbot/connector/gateway/clob_spot/data_sources/penumbra)
4. Run the following command to generate the protos **from the base repo directory**
```bash 
pip install grpcio-tools

find <ABSOLUTE_PATH_TO_REPO>/hummingbot/hummingbot/hummingbot/connector/gateway/clob_spot/data_sources/penumbra -name "*.proto" | xargs python3.10 -m grpc_tools.protoc  \
    --python_out=<ABSOLUTE_PATH_TO_REPO>/hummingbot/hummingbot/hummingbot/connector/gateway/clob_spot/data_sources/penumbra/generated \
    --grpc_python_out=<ABSOLUTE_PATH_TO_REPO>/hummingbot/hummingbot/hummingbot/connector/gateway/clob_spot/data_sources/penumbra/generated \
    -I<ABSOLUTE_PATH_TO_REPO>/hummingbot/hummingbot/hummingbot/connector/gateway/clob_spot/data_sources/penumbra/proto/penumbra
```
5. Fix all of the import paths to be absolute. Namely, fix all instances of `from penumbra.` imports to be prefixed with `from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.`
6. Update all files that use `grpc.experimental` to contain the import `import grpc.experimental` 