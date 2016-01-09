# govtrack-python

A Python library for the GovTrack.us API v2.

Based on https://github.com/markgx/govtrack-node/

For full API docs visit [https://www.govtrack.us/developers/api](https://www.govtrack.us/developers/api)

## Installation

```
pip install govtrack
```

## Usage

### Instantiate the GovTrackClient like so:

```
from govtrack.api import GovTrackClient

client = GovTrackClient()
```

### Calling the API:

##### 1. Choose an endpoint

```
client.bill()
client.cosponsorship()
client.person()
client.role()
client.vote()
client.vote_voter()
```

##### 2a. Filter the results

```
client.person({'lastname': 'Kennedy'})
```

##### 2b. Filter with a 'id' to get a single result (or get none if the 'id' doesn't exist)

```
client.person({'id': 123})
```

##### 2c. Provide an integer to get the same affect as 2b

```
client.person(123)
```

##### 3. Receive a response

Single response if you used an 'id':
```
{
    'id': 65,
    'bill_type': 'resolution',
    'congress': 113
}
```

Multiple response if you used filters:
```
{
    'meta': {
        'some_meta_key_1': 123,
        'some_meta_key_2': 'abc'
    },
    'objects': [
        {
            'id': 65,
            'bill_type: 'resolution',
            'congress': 113
        },
        {
            'id': 66,
            'bill_type': 'resolution',
            'congress': 114
        }
    ]
}
```
