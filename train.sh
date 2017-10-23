#!/bin/bash
./common/word2vec/bin/word2vec -train train_data -output model.bin -cbow 0 -size 200 -window 5 -negative 0 -hs 1 -sample 1e-3 -threads 12 -binary 1
