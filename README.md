# Complexity Measures Throughout Training

This repository contains the results of running a large number on Network-in-Network models, and calculating 
interesting generalization measures throughout the course of training. This data was generated for my MSc thesis 
(which can be found at https://github.com/le-big-mac/msc_diss), and is provided here for use by anyone else 
who is interested in how generalization measures evolve over the course of training.

The data can be loaded by importing Run from run.py, and then loading the file of interest with pickle. 
The file named "all-0.pickle" contain a list of Run objects, each of which contains the values of generalization measures 
computed throughout the course of training a model. These models have varying depths, learning rates, batch sizes and 
dropout probabilities. Files "all-17.pickle" and "all-43.pickle" contain repeats of these runs with different random seeds.
Files named "no-dropout-{seed}.pickle" contain only the runs in "all-{seed}.pickle" trained with a dropout probability of zero.

The measures computed during training include:

- VC dimension
- Spectral-complexity [https://arxiv.org/abs/1706.08498]
- Path norm [https://arxiv.org/abs/1506.02617]
- PAC-Bayesian flatness [https://arxiv.org/abs/1703.11008]

For a more exhaustive list see the theis at https://github.com/le-big-mac/msc_diss.
