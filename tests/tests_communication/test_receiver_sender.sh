#!/bin/bash
pytest test_receiver_sender.py -k test_receiver_sender_off;
python run_sender.py & sleep 1 ; pytest test_receiver_sender.py -k test_receiver_sender_on ;kill %1