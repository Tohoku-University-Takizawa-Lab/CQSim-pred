# combine predicted runtime
python3 Interface/combin_predict.py "$1.swf" "$2.log"

# regulate the modified log file
python3 ../data/InputFiles/regulate.py "$1_$2.swf" "$1_$2_regulate.swf"

# schedule the jobs 
# modify config_sys.set for choosing backfilling mode
# 0: No Backfilling
# 1: EASY Backfilling
# 2: Conservative Backfilling
python3 cqsim.py -j "$1_$2_regulate.swf" -n "$1_$2_regulate.swf"

# evaluate the scheduling result
python3 ResultAnalysis/evaluate.py "$1_$2_regulate"