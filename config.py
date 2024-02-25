from petals.constants import PUBLIC_INITIAL_PEERS

from data_structures import ModelInfo

INITIAL_PEERS = ['/ip4/192.168.1.29/tcp/31337/p2p/QmXWbuJQTs1eQiwV6SpPdup4hXXvKmNZCpX5XrRYk3EgVj']

MODELS = [
    ModelInfo(
        dht_prefix="StableBeluga2-hf",
        repository="https://huggingface.co/petals-team/StableBeluga2",
        num_blocks=80,
    ),
    ModelInfo(
        dht_prefix="CodeLlama-34b-Instruct-hf",
        repository="https://huggingface.co/codellama/CodeLlama-34b-Instruct-hf",
        num_blocks=80,
    ),
]

UPDATE_PERIOD = 15
