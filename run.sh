#!/bin/bash
python clean.py
sh train.sh
sh get_tf_dict.sh
python predict.py > tmp
