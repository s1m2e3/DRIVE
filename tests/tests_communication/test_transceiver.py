import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from communication.transceiver import Transceiver
import pytest
import asyncio

def test_transceiver_init():
    transceiver = Transceiver()
    assert transceiver.receivers == []
    assert transceiver.senders == []
def test_transceiver_add_messengers():
    transceiver = Transceiver()
    transceiver.add_messengers('../../config/communicationConfig.json')
    assert len(transceiver.receivers) == 2
    assert len(transceiver.senders) == 4
def test_get_bsm_receiver():
    transceiver = Transceiver()
    transceiver.add_messengers('../../config/communicationConfig.json')
    bsm_index = transceiver.identify_bsm_receiver()
    assert len(bsm_index)==1
def test_get_psm_receiver():
    transceiver = Transceiver()
    transceiver.add_messengers('../../config/communicationConfig.json')
    psm_index = transceiver.identify_psm_receiver()
    assert len(psm_index)==1
def test_get_tim_sender():
    transceiver = Transceiver()
    transceiver.add_messengers('../../config/communicationConfig.json')
    tim_index = transceiver.identify_tim_sender()
    assert len(tim_index)==2
def test_get_psm_sender():
    transceiver = Transceiver()
    transceiver.add_messengers('../../config/communicationConfig.json')
    psm_index = transceiver.identify_psm_sender()
    assert len(psm_index)==2
def test_start_bsm_receiver():
    transceiver = Transceiver()
    transceiver.add_messengers('../../config/communicationConfig.json')
    async def run_bsm_receivers(transceiver: Transceiver,stop_event:asyncio.Event):
        await transceiver.start_bsm_receiver(stop_event)
    async def collect_bsm_messages(transceiver: Transceiver,stop_event:asyncio.Event):
        indexes = transceiver.identify_bsm_receiver()
        await asyncio.sleep(2)
        messages = [transceiver.receivers[index].message == "Hello from BSM!" for index in indexes]
        assert all(messages) 
        stop_event.set()
    async def main():
        stop_event = asyncio.Event()
        tasks = [asyncio.create_task(run_bsm_receivers(transceiver,stop_event)), asyncio.create_task(collect_bsm_messages(transceiver,stop_event))]
        await stop_event.wait()
        await asyncio.gather(*tasks)

    asyncio.run(main())  