from petals.constants import PUBLIC_INITIAL_PEERS

from data_structures import ModelInfo

INITIAL_PEERS = /ip4/49.194.161.134/tcp/31337/p2p/QmNbWmdMF4mrHYBZvaX1aWmEHw1i6Sh7E1sVZdqE1LFbFm

MODELS = [
    ModelInfo(
        dht_prefix="StableBeluga2-hf",
        repository="https://huggingface.co/petals-team/StableBeluga2",
        num_blocks=80,
    ),
    ModelInfo(
        dht_prefix="falcon-180B-chat",
        repository="https://huggingface.co/tiiuae/falcon-180B-chat",
        num_blocks=80,
        limited=True,
    ),
    ModelInfo(
        dht_prefix="CodeLlama-34b-Instruct-hf",
        repository="https://huggingface.co/codellama/CodeLlama-34b-Instruct-hf",
        num_blocks=80,
    ),
    ModelInfo(
        dht_prefix="Llama-2-70b-hf",
        repository="https://huggingface.co/meta-llama/Llama-2-70b-hf",
        num_blocks=80,
    ),
]

UPDATE_PERIOD = 15
