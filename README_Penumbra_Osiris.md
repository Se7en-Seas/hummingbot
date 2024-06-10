## Penumbra Osiris
The [penumbra osiris bot](https://github.com/Se7en-Seas/hummingbot/blob/penunumbra-integration/scripts/penumbra_osiris.py) aims to be an approximate parity to its [rust counterpart](https://github.com/penumbra-zone/osiris/) and function as an abstraction to allow new users to interact with the penumbra protocol without needing to understand the underlying mechanics.

## First time setup
1. Clone this [repo and checkout this branch](https://github.com/Se7en-Seas/hummingbot/tree/penunumbra-integration/)
```bash
git clone https://github.com/Se7en-Seas/hummingbot/tree/penunumbra-integration/
cd hummingbot
git fetch --all
git checkout penunumbra-integration
```
2. Set up pclientd and have it running with any releveant test funds. You'll know you're good to go when you can run the following command and get a response
```bash
grpcurl -plaintext -d '{"account_filter": {"account": 0}}'     127.0.0.1:8081 penumbra.view.v1.ViewService/Balances
```
3. Install Anaconda w/ Python 3.7+ along with relevant dependencies, this is a requirement to compile the hummingbot repo
```bash
apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6
wget https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh
bash Anaconda3-2023.09-0-Linux-x86_64.sh # Accept the lisence agreement and install
# install miniconda
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
~/miniconda3/bin/conda init bash
```

3.5 Set up conda for your terminal, here is a minimal bash example
```bash
export PATH=/root/anaconda3/bin:$PATH
source ~/.bashrc
conda init bash
conda activate hummingbot
```

4. Compile hummingbot (this will take a while) & activate the conda environment (if you haven't already)
```bash
make install
./compile # Assuming you're still in the base hummingbot repo directory
conda activate hummingbot
```

5. Start hummingbot and run the penumbra osiris bot :3
```bash 
./start # If it's your first time running hummingbot, you'll need to follow the on screen instructions to set up your configurations
# Now that you're in the terminal, you'll need to set up the penumbra connector by specifying the pclientd url (typically localhost:8081) and the gateway url (typically localhost:15888 note the gateway is currently not used and so the URL is a formality but not relevant to the osiris script)
connect penumbra # Note this is only necessary for the first time setup
start --script penumbra_osiris.py # This will start the penumbra osiris bot
# Note your terminal may appear to hang, this is normal as the bot is submitting orders in the background and cannot render logging at the same time
# To see your account's status
status
# If you wish to stop the bot, just type in stop, or exit to exit the hummingbot terminal
```


Notes:

To check the logs you can look at the logs directory
```bash
cat ./logs/logs_penumbra_osiris.log 
```

If you wish to add more logging in the log file, you must do:
```python
logging.getLogger().info("<TEXT_HERE>")
```
however if you wish to print to the terminal, you must do:
```python
print("<TEXT_HERE>")
```


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
