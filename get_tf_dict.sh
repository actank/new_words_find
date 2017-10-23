#!/bin/bash
cat train_data | awk -F ' ' '{for(i=1;i<NF;i++){print $i}}' | sort | uniq -c | awk -F ' ' '{if($1>5){print $2}}' > tf_dict
