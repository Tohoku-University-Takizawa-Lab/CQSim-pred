# pred-CQSim - predicted runtime based job scheduling simulator

pred-CQsim is modified job scheduling simulator based on [CQSim](https://github.com/SPEAR-UIC/CQSim). 

#### modules
The added features to the original simulator is as follows: 
- combine_predicted.py
  - add the predicted runtime to the log data as an extra column in the data file.
- Filter_job_SWF.py, Job_trace.py, Cqsim_sim.py
  - transfer newly added `predicted_runtime` to scheduler.
- Backfill.py
  - schedule jobs using predicted runtime.
- evaluate.py
  - evaluate the scheduling results.

# Getting started: Run A Simple Example
```
./schedule_evaluate.sh $log$ $predicted_runtime$ 
```
