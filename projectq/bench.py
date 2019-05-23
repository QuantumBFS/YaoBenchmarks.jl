#!/usr/bin/env python
import numpy as np
import time
from contexts import ProjectQContext
from projectq import ops

import mkl
mkl.set_num_threads(1)

import pytest
from functools import wraps

def run_bench(benchmark, G, locs, nbit):
    if nbit==5:
        benchmark.group = "small"
    elif nbit==10:
        benchmark.group = "medium"
    elif nbit==20:
        benchmark.group = "large"
    else:
        raise
    with ProjectQContext(nbit, 'simulate') as cc:
        qureg = cc.qureg
        eng = qureg.engine
        qi = take_locs(qureg, locs)
        benchmark(run_gate, eng, G, qi)

def take_locs(qureg, locs):
    if isinstance(locs, int):
        return qureg[locs]
    elif isinstance(locs, tuple):
        return tuple(qureg[loc] for loc in locs)
    elif isinstance(locs, slice):
        return qureg[sls]
    else:
        raise

def run_gate(eng, G, qi):
    G | qi
    eng.flush()

################### Tests #################
nbit_list = [5, 10, 20]
@pytest.mark.parametrize('nbit', nbit_list)
def test_X(benchmark, nbit):
    run_bench(benchmark, ops.X, 2, nbit)

@pytest.mark.parametrize('nbit', nbit_list)
def test_Y(benchmark, nbit):
    run_bench(benchmark, ops.Y, 2, nbit)

@pytest.mark.parametrize('nbit', nbit_list)
def test_Z(benchmark, nbit):
    run_bench(benchmark, ops.Z, 2, nbit)

@pytest.mark.parametrize('nbit', nbit_list)
def test_H(benchmark, nbit):
    run_bench(benchmark, ops.H, 2, nbit)

@pytest.mark.parametrize('nbit', nbit_list)
def test_Rx(benchmark, nbit):
    run_bench(benchmark, ops.Rx(0.5), 2, nbit)

@pytest.mark.parametrize('nbit', nbit_list)
def test_Ry(benchmark, nbit):
    run_bench(benchmark, ops.Ry(0.5), 2, nbit)

@pytest.mark.parametrize('nbit', nbit_list)
def test_Rz(benchmark, nbit):
    run_bench(benchmark, ops.Rz(0.5), 2, nbit)

@pytest.mark.parametrize('nbit', nbit_list)
def test_CX(benchmark, nbit):
    run_bench(benchmark, ops.CNOT, (2,4), nbit)

@pytest.mark.parametrize('nbit', nbit_list)
def test_CY(benchmark, nbit):
    run_bench(benchmark, ops.C(ops.Y), (2,4), nbit)

@pytest.mark.parametrize('nbit', nbit_list)
def test_CZ(benchmark, nbit):
    run_bench(benchmark, ops.C(ops.Z), (2,4), nbit)

@pytest.mark.parametrize('nbit', nbit_list)
def test_CH(benchmark, nbit):
    run_bench(benchmark, ops.C(ops.H), (2,4), nbit)

@pytest.mark.parametrize('nbit', nbit_list)
def test_Toffoli(benchmark, nbit):
    run_bench(benchmark, ops.Toffoli, (2,3,4), nbit)
