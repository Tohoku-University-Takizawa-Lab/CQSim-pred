# CQSim-pred - a predicted runtime based job scheduling simulator

## CQSim
CQSim-pred is developed based on [CQSim](https://github.com/SPEAR-UIC/CQSim). 

## Features
Except for the original features of [CQSim](https://github.com/SPEAR-UIC/CQSim), CQSim-pred can use a predicted runtime to backfill the jobs submitted to it. After that, it can evaluate the scheduling results. 

## Modules
The added and modified modules to the original [CQSim](https://github.com/SPEAR-UIC/CQSim) simulator is as follows: 
- Combine_predicted.py (Newly Designed)
  - Add the predicted runtime to the log as an extra column in the `.swf` file.
- Filter_job_SWF.py, Job_trace.py, Cqsim_sim.py (Modified)
  - Transfer the added predicted runtime to scheduler.
- Backfill.py (Modified)
  - Schedule jobs use the predicted runtime.
- Evaluate.py (Newly Designed)
  - Evaluate the scheduling results.

## Usage
```
./schedule_evaluate.sh $log$ $predicted_runtime$ 
```
