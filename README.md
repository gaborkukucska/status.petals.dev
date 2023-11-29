# Petals Health Monitor

## Installation

You can run this app on your server using these commands:

```bash
git clone https://github.com/gaborkukucska/status.petals.dev
cd status.petals.dev
pip install -r requirements.txt
flask run --host=0.0.0.0 --port=46266
```

In production, we recommend using gunicorn instead of the Flask dev server:

```bash
gunicorn app:app --bind 0.0.0.0:46266 --worker-class gthread --threads 10 --timeout 120
```

<details>
<summary><b>Running with Docker</b></summary>

```bash
git clone https://github.com/gaborkukucska/status.petals.dev
cd status.petals.dev
docker-compose up --build -d
```
</details>

### Monitoring private swarm

To monitor your private swarm instead of the public one, please replace `PUBLIC_INITIAL_PEERS` with a list of multiaddresses of your swarm's **initial peers** in [config.py](config.py). Example:

```python
INITIAL_PEERS = ['/ip4/49.194.161.134/tcp/31337/p2p/QmNbWmdMF4mrHYBZvaX1aWmEHw1i6Sh7E1sVZdqE1LFbFm']
```

## HTTP API

- **GET /api/v1/state**

    Note that we regularly update the info shown there, so the response format may change at any time. We expect most changes to be minor.
    If this is still an issue for you, you can clone this repository and launch your own API endpoint with a fixed version of the code.
    Alternatively, you can use Python API directly from your script (see below).

- **GET /api/v1/is_reachable/`<peer_id>`**

    Check if the health monitor can reach a libp2p node with given `peer_id`.
    Petals servers use this call to ping themselves and ensure that they are reachable before announcing their ONLINE status to the swarm.
    For example, if the server is located behind NAT without ports forwarded,
    this ensures that libp2p has successfully found a relay needed for NAT traversal.

    Returns (JSON):

    - **ok** (bool) - whether the node is reachable
    - **message** (str) - an error message if `ok == False`
    - **your_ip** (str) - the IP address of the caller

## Python API

You can clone this repository and access the health monitor state directly from Python by running a `hivemind.DHT` client:

```python
# git clone https://github.com/petals-infra/health.petals.dev
# cd health.petals.dev

from pprint import pprint
import hivemind
from petals.constants import PUBLIC_INITIAL_PEERS
from health import fetch_health_state

dht = hivemind.DHT(initial_peers=PUBLIC_INITIAL_PEERS, client_mode=True, start=True)
pprint(fetch_health_state(dht))
```
