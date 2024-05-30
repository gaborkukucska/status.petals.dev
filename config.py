from petals.constants import PUBLIC_INITIAL_PEERS

from data_structures import ModelInfo

INITIAL_PEERS = ['/dns/ai.gettingitalldone.com/tcp/31337/p2p/QmTbqDrBxCioZMYCjTUHu5GLVERw369VkY7fBTMiKFFDXu']

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
