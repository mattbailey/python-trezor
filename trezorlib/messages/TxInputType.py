# Automatically generated by pb2py
from __future__ import absolute_import
from .. import protobuf as p
from .MultisigRedeemScriptType import MultisigRedeemScriptType


class TxInputType(p.MessageType):
    FIELDS = {
        1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
        2: ('prev_hash', p.BytesType, 0),  # required
        3: ('prev_index', p.UVarintType, 0),  # required
        4: ('script_sig', p.BytesType, 0),
        5: ('sequence', p.UVarintType, 0),  # default=4294967295
        6: ('script_type', p.UVarintType, 0),  # default=0
        7: ('multisig', MultisigRedeemScriptType, 0),
        8: ('amount', p.UVarintType, 0),
    }
