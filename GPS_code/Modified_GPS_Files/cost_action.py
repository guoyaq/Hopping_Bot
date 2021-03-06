#!/usr/bin/env python3

import numpy as np 
import copy
from hyperparameters import Cost_Action

class CostAction():
    def __init__(self):
        #send cost dic in the hyperparams file
        hyperparams = Cost_Action
        config = copy.deepcopy(hyperparams)
        config.update(hyperparams)
        self._hyperparams = config
    
    def eval(self, sample):
        '''
        Evaluate cost function and derivatives on a sample
        Args:
            A single sample (object)
        '''
        sample_u = sample.get_U()
        T = sample.T
        Du = sample.dU
        Dx = sample.dx
        l = 0.5 * np.sum(self._hyperparams['wu'] * (sample_u ** 2), axis=1)
        lu = self._hyperparams['wu'] * sample_u
        lx = np.zeros((T, Dx))
        luu = np.tile(np.diag(self._hyperparams['wu']), [T, 1, 1])
        lxx = np.zeros((T, Dx, Dx))
        lux = np.zeros((T, Du, Dx))
        return l, lx, lu, lxx, luu, lux
