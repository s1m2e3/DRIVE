import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from communication.transceiver import Transceiver
import pytest

def test_transceiver_init():
    transceiver = Transceiver()
    assert transceiver.receivers == []
    assert transceiver.senders == []
def test_transceiver_add_messengers():
    transceiver = Transceiver()
    transceiver.add_messengers('../../config/communicationConfig.json')
    assert len(transceiver.receivers) == 2
    assert len(transceiver.senders) == 4
