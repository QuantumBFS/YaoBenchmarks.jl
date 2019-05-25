# Benchmark Report for *YaoArrayRegister*

## Job Properties
* Time of benchmarks:
    - Target: 24 May 2019 - 22:56
    - Baseline: 25 May 2019 - 00:06
* Package commits:
    - Target: 69e218
    - Baseline: 2f785b
* Julia commits:
    - Target: 80516c
    - Baseline: 80516c
* Julia command flags:
    - Target: `-O3`
    - Baseline: `-O3`
* Environment variables:
    - Target: `JULIA_NUM_THREADS => 4`
    - Baseline: `JULIA_NUM_THREADS => 1`

## Results
A ratio greater than `1.0` denotes a possible regression (marked with :x:), while a ratio less
than `1.0` denotes a possible improvement (marked with :white_check_mark:). Only significant results - results
that indicate possible regressions or improvements - are shown below (thus, an empty table means that all
benchmark results remained invariant between builds).

| ID                                                                                                                                                       | time ratio                   | memory ratio                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|------------------------------|
| `["matrices", "contiguous", "ordered", "(1, \"Complex{Float64}\", \"Array{Complex{Float64},2}\")"]`                                                      |                2.86 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "contiguous", "ordered", "(1, \"Complex{Float64}\", \"Diagonal{Complex{Float64},Array{Complex{Float64},1}}\")"]`                           |                3.08 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "contiguous", "ordered", "(1, \"Complex{Float64}\", \"MArray{Tuple{2,2},Complex{Float64},2,4}\")"]`                                        |                3.18 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "contiguous", "ordered", "(1, \"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\")"]`    |               13.00 (5%) :x: |                 Inf (1%) :x: |
| `["matrices", "contiguous", "ordered", "(1, \"Complex{Float64}\", \"SArray{Tuple{2,2},Complex{Float64},2,4}\")"]`                                        |                2.35 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "contiguous", "ordered", "(1, \"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\")"]`                                        |                2.11 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "contiguous", "ordered", "(3, \"Complex{Float64}\", \"Array{Complex{Float64},2}\")"]`                                                      | 0.95 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "contiguous", "ordered", "(3, \"Complex{Float64}\", \"Diagonal{Complex{Float64},Array{Complex{Float64},1}}\")"]`                           | 0.94 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "contiguous", "ordered", "(3, \"Complex{Float64}\", \"MArray{Tuple{8,8},Complex{Float64},2,64}\")"]`                                       | 0.94 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "contiguous", "ordered", "(3, \"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\")"]`    | 0.94 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "contiguous", "ordered", "(3, \"Complex{Float64}\", \"SArray{Tuple{8,8},Complex{Float64},2,64}\")"]`                                       | 0.93 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "contiguous", "ordered", "(3, \"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\")"]`                                        |                   0.96 (5%)  |                1.03 (1%) :x: |
| `["matrices", "contiguous", "ordered", "(5, \"Complex{Float64}\", \"Diagonal{Complex{Float64},Array{Complex{Float64},1}}\")"]`                           | 0.95 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "contiguous", "ordered", "(5, \"Complex{Float64}\", \"MArray{Tuple{32,32},Complex{Float64},2,1024}\")"]`                                   | 0.94 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "contiguous", "ordered", "(5, \"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\")"]`    | 0.93 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "contiguous", "ordered", "(5, \"Complex{Float64}\", \"SArray{Tuple{32,32},Complex{Float64},2,1024}\")"]`                                   | 0.89 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "contiguous", "ordered", "(5, \"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\")"]`                                        | 0.94 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "contiguous", "ordered", "(7, \"Complex{Float64}\", \"Array{Complex{Float64},2}\")"]`                                                      | 0.95 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "contiguous", "ordered", "(7, \"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\")"]`    | 0.94 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "contiguous", "ordered", "(7, \"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\")"]`                                        | 0.93 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "contiguous", "ordered", "(9, \"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\")"]`    | 0.91 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "contiguous", "ordered", "(9, \"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\")"]`                                        | 0.94 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "contiguous", "random", "(1, \"Complex{Float64}\", \"Array{Complex{Float64},2}\")"]`                                                       |                2.90 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "contiguous", "random", "(1, \"Complex{Float64}\", \"Diagonal{Complex{Float64},Array{Complex{Float64},1}}\")"]`                            |                3.08 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "contiguous", "random", "(1, \"Complex{Float64}\", \"MArray{Tuple{2,2},Complex{Float64},2,4}\")"]`                                         |                3.14 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "contiguous", "random", "(1, \"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\")"]`     |               13.05 (5%) :x: |                 Inf (1%) :x: |
| `["matrices", "contiguous", "random", "(1, \"Complex{Float64}\", \"SArray{Tuple{2,2},Complex{Float64},2,4}\")"]`                                         |                3.16 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "contiguous", "random", "(1, \"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\")"]`                                         |                2.40 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "contiguous", "random", "(3, \"Complex{Float64}\", \"Array{Complex{Float64},2}\")"]`                                                       | 0.95 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "contiguous", "random", "(3, \"Complex{Float64}\", \"MArray{Tuple{8,8},Complex{Float64},2,64}\")"]`                                        | 0.94 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "contiguous", "random", "(3, \"Complex{Float64}\", \"SArray{Tuple{8,8},Complex{Float64},2,64}\")"]`                                        | 0.94 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "contiguous", "random", "(3, \"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\")"]`                                         |                   0.97 (5%)  | 0.93 (1%) :white_check_mark: |
| `["matrices", "contiguous", "random", "(5, \"Complex{Float64}\", \"MArray{Tuple{32,32},Complex{Float64},2,1024}\")"]`                                    | 0.93 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "contiguous", "random", "(5, \"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\")"]`     | 0.93 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "contiguous", "random", "(5, \"Complex{Float64}\", \"SArray{Tuple{32,32},Complex{Float64},2,1024}\")"]`                                    | 0.94 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "contiguous", "random", "(5, \"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\")"]`                                         |                   0.96 (5%)  |                1.02 (1%) :x: |
| `["matrices", "contiguous", "random", "(7, \"Complex{Float64}\", \"Array{Complex{Float64},2}\")"]`                                                       |                1.26 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "contiguous", "random", "(7, \"Complex{Float64}\", \"Diagonal{Complex{Float64},Array{Complex{Float64},1}}\")"]`                            | 0.92 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "contiguous", "random", "(7, \"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\")"]`     | 0.93 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "contiguous", "random", "(7, \"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\")"]`                                         |                1.28 (5%) :x: | 0.98 (1%) :white_check_mark: |
| `["matrices", "contiguous", "random", "(9, \"Complex{Float64}\", \"Array{Complex{Float64},2}\")"]`                                                       | 0.79 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "contiguous", "random", "(9, \"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\")"]`     | 0.92 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "contiguous", "random", "(9, \"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\")"]`                                         |                1.33 (5%) :x: |                   1.01 (1%)  |
| `["matrices", "controlled", "ordered", "(1, 3, \"Complex{Float64}\", \"Diagonal{Complex{Float64},Array{Complex{Float64},1}}\")"]`                        | 0.94 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "ordered", "(1, 3, \"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\")"]` | 0.90 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "ordered", "(1, 3, \"Complex{Float64}\", \"SArray{Tuple{2,2},Complex{Float64},2,4}\")"]`                                     | 0.94 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "ordered", "(1, 3, \"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\")"]`                                     | 0.89 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "ordered", "(1, 5, \"Complex{Float64}\", \"Diagonal{Complex{Float64},Array{Complex{Float64},1}}\")"]`                        | 0.95 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "ordered", "(1, 5, \"Complex{Float64}\", \"SArray{Tuple{2,2},Complex{Float64},2,4}\")"]`                                     | 0.94 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "ordered", "(1, 5, \"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\")"]`                                     | 0.90 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "ordered", "(3, 3, \"Complex{Float64}\", \"Diagonal{Complex{Float64},Array{Complex{Float64},1}}\")"]`                        | 0.90 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "ordered", "(3, 3, \"Complex{Float64}\", \"SArray{Tuple{8,8},Complex{Float64},2,64}\")"]`                                    | 0.89 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "ordered", "(3, 3, \"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\")"]`                                     | 0.92 (5%) :white_check_mark: |                1.03 (1%) :x: |
| `["matrices", "controlled", "ordered", "(3, 5, \"Complex{Float64}\", \"MArray{Tuple{8,8},Complex{Float64},2,64}\")"]`                                    | 0.89 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "ordered", "(3, 5, \"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\")"]` | 0.90 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "ordered", "(3, 5, \"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\")"]`                                     | 0.94 (5%) :white_check_mark: | 0.99 (1%) :white_check_mark: |
| `["matrices", "controlled", "ordered", "(5, 3, \"Complex{Float64}\", \"SArray{Tuple{32,32},Complex{Float64},2,1024}\")"]`                                | 0.90 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "ordered", "(5, 5, \"Complex{Float64}\", \"Array{Complex{Float64},2}\")"]`                                                   | 0.94 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "ordered", "(5, 5, \"Complex{Float64}\", \"Diagonal{Complex{Float64},Array{Complex{Float64},1}}\")"]`                        | 0.94 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "ordered", "(5, 5, \"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\")"]` | 0.88 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "ordered", "(7, 3, \"Complex{Float64}\", \"Diagonal{Complex{Float64},Array{Complex{Float64},1}}\")"]`                        | 0.88 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "ordered", "(7, 5, \"Complex{Float64}\", \"Array{Complex{Float64},2}\")"]`                                                   |                1.07 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "controlled", "ordered", "(7, 5, \"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\")"]` |                1.06 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "controlled", "ordered", "(7, 5, \"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\")"]`                                     |                1.06 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "controlled", "ordered", "(9, 3, \"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\")"]` |                1.06 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "controlled", "ordered", "(9, 3, \"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\")"]`                                     | 0.90 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "ordered", "(9, 5, \"Complex{Float64}\", \"Array{Complex{Float64},2}\")"]`                                                   | 0.94 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "ordered", "(9, 5, \"Complex{Float64}\", \"Diagonal{Complex{Float64},Array{Complex{Float64},1}}\")"]`                        | 0.87 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "ordered", "(9, 5, \"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\")"]` | 0.94 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "ordered", "(9, 5, \"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\")"]`                                     | 0.88 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "random", "(1, 3, \"Complex{Float64}\", \"Array{Complex{Float64},2}\")"]`                                                    |                1.08 (5%) :x: |                   1.01 (1%)  |
| `["matrices", "controlled", "random", "(1, 3, \"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\")"]`  | 0.93 (5%) :white_check_mark: |                   0.99 (1%)  |
| `["matrices", "controlled", "random", "(1, 3, \"Complex{Float64}\", \"SArray{Tuple{2,2},Complex{Float64},2,4}\")"]`                                      | 0.93 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "random", "(1, 3, \"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\")"]`                                      | 0.95 (5%) :white_check_mark: |                   0.99 (1%)  |
| `["matrices", "controlled", "random", "(1, 5, \"Complex{Float64}\", \"Array{Complex{Float64},2}\")"]`                                                    | 0.92 (5%) :white_check_mark: |                   0.99 (1%)  |
| `["matrices", "controlled", "random", "(1, 5, \"Complex{Float64}\", \"Diagonal{Complex{Float64},Array{Complex{Float64},1}}\")"]`                         | 0.94 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "random", "(1, 5, \"Complex{Float64}\", \"MArray{Tuple{2,2},Complex{Float64},2,4}\")"]`                                      | 0.94 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "random", "(1, 5, \"Complex{Float64}\", \"SArray{Tuple{2,2},Complex{Float64},2,4}\")"]`                                      | 0.89 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "random", "(1, 5, \"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\")"]`                                      | 0.93 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "random", "(3, 3, \"Complex{Float64}\", \"Diagonal{Complex{Float64},Array{Complex{Float64},1}}\")"]`                         | 0.88 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "random", "(3, 3, \"Complex{Float64}\", \"MArray{Tuple{8,8},Complex{Float64},2,64}\")"]`                                     | 0.94 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "random", "(3, 3, \"Complex{Float64}\", \"SArray{Tuple{8,8},Complex{Float64},2,64}\")"]`                                     |                1.07 (5%) :x: |                1.20 (1%) :x: |
| `["matrices", "controlled", "random", "(3, 3, \"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\")"]`                                      |                   0.96 (5%)  |                1.13 (1%) :x: |
| `["matrices", "controlled", "random", "(3, 5, \"Complex{Float64}\", \"Array{Complex{Float64},2}\")"]`                                                    | 0.89 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "random", "(3, 5, \"Complex{Float64}\", \"MArray{Tuple{8,8},Complex{Float64},2,64}\")"]`                                     | 0.94 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "random", "(3, 5, \"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\")"]`  |                   0.98 (5%)  |                1.04 (1%) :x: |
| `["matrices", "controlled", "random", "(3, 5, \"Complex{Float64}\", \"SArray{Tuple{8,8},Complex{Float64},2,64}\")"]`                                     |                   1.01 (5%)  |                1.21 (1%) :x: |
| `["matrices", "controlled", "random", "(5, 3, \"Complex{Float64}\", \"Array{Complex{Float64},2}\")"]`                                                    | 0.94 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "random", "(5, 3, \"Complex{Float64}\", \"SArray{Tuple{32,32},Complex{Float64},2,1024}\")"]`                                 | 0.95 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "random", "(5, 3, \"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\")"]`                                      | 0.95 (5%) :white_check_mark: | 0.97 (1%) :white_check_mark: |
| `["matrices", "controlled", "random", "(5, 5, \"Complex{Float64}\", \"Array{Complex{Float64},2}\")"]`                                                    | 0.92 (5%) :white_check_mark: |                   1.01 (1%)  |
| `["matrices", "controlled", "random", "(5, 5, \"Complex{Float64}\", \"Diagonal{Complex{Float64},Array{Complex{Float64},1}}\")"]`                         | 0.91 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "random", "(5, 5, \"Complex{Float64}\", \"MArray{Tuple{32,32},Complex{Float64},2,1024}\")"]`                                 | 0.86 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "random", "(5, 5, \"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\")"]`  | 0.92 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "random", "(5, 5, \"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\")"]`                                      | 0.94 (5%) :white_check_mark: | 0.98 (1%) :white_check_mark: |
| `["matrices", "controlled", "random", "(7, 3, \"Complex{Float64}\", \"Array{Complex{Float64},2}\")"]`                                                    | 0.94 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "random", "(7, 3, \"Complex{Float64}\", \"Diagonal{Complex{Float64},Array{Complex{Float64},1}}\")"]`                         | 0.93 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "random", "(7, 3, \"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\")"]`  | 0.87 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "random", "(7, 3, \"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\")"]`                                      |                   1.04 (5%)  |                1.01 (1%) :x: |
| `["matrices", "controlled", "random", "(7, 5, \"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\")"]`  | 0.90 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "random", "(7, 5, \"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\")"]`                                      |                1.16 (5%) :x: |                1.03 (1%) :x: |
| `["matrices", "controlled", "random", "(9, 3, \"Complex{Float64}\", \"Array{Complex{Float64},2}\")"]`                                                    |                1.14 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "controlled", "random", "(9, 3, \"Complex{Float64}\", \"Diagonal{Complex{Float64},Array{Complex{Float64},1}}\")"]`                         |                1.12 (5%) :x: |                1.01 (1%) :x: |
| `["matrices", "controlled", "random", "(9, 3, \"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\")"]`  | 0.90 (5%) :white_check_mark: |                   0.99 (1%)  |
| `["matrices", "controlled", "random", "(9, 3, \"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\")"]`                                      | 0.91 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "random", "(9, 5, \"Complex{Float64}\", \"Array{Complex{Float64},2}\")"]`                                                    |            47692.08 (5%) :x: |               25.78 (1%) :x: |
| `["matrices", "controlled", "random", "(9, 5, \"Complex{Float64}\", \"Diagonal{Complex{Float64},Array{Complex{Float64},1}}\")"]`                         |                   0.96 (5%)  |                1.02 (1%) :x: |
| `["matrices", "controlled", "random", "(9, 5, \"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\")"]`  | 0.92 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "controlled", "random", "(9, 5, \"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\")"]`                                      |                1.05 (5%) :x: |                   1.01 (1%)  |
| `["matrices", "in-contiguous", "ordered", "(1, \"Complex{Float64}\", \"Array{Complex{Float64},2}\")"]`                                                   |                1.36 (5%) :x: |                 Inf (1%) :x: |
| `["matrices", "in-contiguous", "ordered", "(1, \"Complex{Float64}\", \"Diagonal{Complex{Float64},Array{Complex{Float64},1}}\")"]`                        |                1.83 (5%) :x: |                 Inf (1%) :x: |
| `["matrices", "in-contiguous", "ordered", "(1, \"Complex{Float64}\", \"MArray{Tuple{2,2},Complex{Float64},2,4}\")"]`                                     |                1.36 (5%) :x: |                 Inf (1%) :x: |
| `["matrices", "in-contiguous", "ordered", "(1, \"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\")"]` |               54.60 (5%) :x: |                 Inf (1%) :x: |
| `["matrices", "in-contiguous", "ordered", "(1, \"Complex{Float64}\", \"SArray{Tuple{2,2},Complex{Float64},2,4}\")"]`                                     |                1.32 (5%) :x: |                 Inf (1%) :x: |
| `["matrices", "in-contiguous", "ordered", "(1, \"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\")"]`                                     |                1.34 (5%) :x: |                 Inf (1%) :x: |
| `["matrices", "in-contiguous", "ordered", "(2, \"Complex{Float64}\", \"Array{Complex{Float64},2}\")"]`                                                   | 0.91 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "in-contiguous", "ordered", "(2, \"Complex{Float64}\", \"Diagonal{Complex{Float64},Array{Complex{Float64},1}}\")"]`                        | 0.87 (5%) :white_check_mark: | 0.99 (1%) :white_check_mark: |
| `["matrices", "in-contiguous", "ordered", "(2, \"Complex{Float64}\", \"MArray{Tuple{4,4},Complex{Float64},2,16}\")"]`                                    | 0.88 (5%) :white_check_mark: |                   1.01 (1%)  |
| `["matrices", "in-contiguous", "ordered", "(2, \"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\")"]` | 0.87 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "in-contiguous", "ordered", "(2, \"Complex{Float64}\", \"SArray{Tuple{4,4},Complex{Float64},2,16}\")"]`                                    | 0.88 (5%) :white_check_mark: |                   0.99 (1%)  |
| `["matrices", "in-contiguous", "ordered", "(2, \"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\")"]`                                     | 0.84 (5%) :white_check_mark: | 0.98 (1%) :white_check_mark: |
| `["matrices", "in-contiguous", "ordered", "(3, \"Complex{Float64}\", \"Array{Complex{Float64},2}\")"]`                                                   | 0.91 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "in-contiguous", "ordered", "(3, \"Complex{Float64}\", \"Diagonal{Complex{Float64},Array{Complex{Float64},1}}\")"]`                        | 0.88 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "in-contiguous", "ordered", "(3, \"Complex{Float64}\", \"MArray{Tuple{8,8},Complex{Float64},2,64}\")"]`                                    | 0.88 (5%) :white_check_mark: |                   1.01 (1%)  |
| `["matrices", "in-contiguous", "ordered", "(3, \"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\")"]` | 0.93 (5%) :white_check_mark: |                1.02 (1%) :x: |
| `["matrices", "in-contiguous", "ordered", "(3, \"Complex{Float64}\", \"SArray{Tuple{8,8},Complex{Float64},2,64}\")"]`                                    | 0.90 (5%) :white_check_mark: |                   1.01 (1%)  |
| `["matrices", "in-contiguous", "ordered", "(3, \"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\")"]`                                     | 0.81 (5%) :white_check_mark: | 0.93 (1%) :white_check_mark: |
| `["matrices", "in-contiguous", "random", "(1, \"Complex{Float64}\", \"Array{Complex{Float64},2}\")"]`                                                    |                   1.05 (5%)  |                 Inf (1%) :x: |
| `["matrices", "in-contiguous", "random", "(1, \"Complex{Float64}\", \"Diagonal{Complex{Float64},Array{Complex{Float64},1}}\")"]`                         |                1.96 (5%) :x: |                 Inf (1%) :x: |
| `["matrices", "in-contiguous", "random", "(1, \"Complex{Float64}\", \"MArray{Tuple{2,2},Complex{Float64},2,4}\")"]`                                      |                1.27 (5%) :x: |                 Inf (1%) :x: |
| `["matrices", "in-contiguous", "random", "(1, \"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\")"]`  |               49.39 (5%) :x: |                 Inf (1%) :x: |
| `["matrices", "in-contiguous", "random", "(1, \"Complex{Float64}\", \"SArray{Tuple{2,2},Complex{Float64},2,4}\")"]`                                      |                1.33 (5%) :x: |                 Inf (1%) :x: |
| `["matrices", "in-contiguous", "random", "(1, \"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\")"]`                                      |                1.44 (5%) :x: |                 Inf (1%) :x: |
| `["matrices", "in-contiguous", "random", "(2, \"Complex{Float64}\", \"Array{Complex{Float64},2}\")"]`                                                    | 0.90 (5%) :white_check_mark: |                1.04 (1%) :x: |
| `["matrices", "in-contiguous", "random", "(2, \"Complex{Float64}\", \"Diagonal{Complex{Float64},Array{Complex{Float64},1}}\")"]`                         | 0.90 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "in-contiguous", "random", "(2, \"Complex{Float64}\", \"MArray{Tuple{4,4},Complex{Float64},2,16}\")"]`                                     | 0.88 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "in-contiguous", "random", "(2, \"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\")"]`  | 0.89 (5%) :white_check_mark: | 0.98 (1%) :white_check_mark: |
| `["matrices", "in-contiguous", "random", "(2, \"Complex{Float64}\", \"SArray{Tuple{4,4},Complex{Float64},2,16}\")"]`                                     | 0.79 (5%) :white_check_mark: | 0.86 (1%) :white_check_mark: |
| `["matrices", "in-contiguous", "random", "(2, \"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\")"]`                                      | 0.82 (5%) :white_check_mark: | 0.91 (1%) :white_check_mark: |
| `["matrices", "in-contiguous", "random", "(3, \"Complex{Float64}\", \"Array{Complex{Float64},2}\")"]`                                                    | 0.88 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "in-contiguous", "random", "(3, \"Complex{Float64}\", \"Diagonal{Complex{Float64},Array{Complex{Float64},1}}\")"]`                         | 0.88 (5%) :white_check_mark: |                   1.01 (1%)  |
| `["matrices", "in-contiguous", "random", "(3, \"Complex{Float64}\", \"MArray{Tuple{8,8},Complex{Float64},2,64}\")"]`                                     | 0.86 (5%) :white_check_mark: | 0.98 (1%) :white_check_mark: |
| `["matrices", "in-contiguous", "random", "(3, \"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\")"]`  | 0.88 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "in-contiguous", "random", "(3, \"Complex{Float64}\", \"SArray{Tuple{8,8},Complex{Float64},2,64}\")"]`                                     | 0.88 (5%) :white_check_mark: |                   1.00 (1%)  |
| `["matrices", "in-contiguous", "random", "(3, \"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\")"]`                                      | 0.89 (5%) :white_check_mark: | 0.94 (1%) :white_check_mark: |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"Array{Complex{Float64},2}\", 1)"]`                                                    |                2.85 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"Array{Complex{Float64},2}\", 13)"]`                                                   | 0.68 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"Array{Complex{Float64},2}\", 17)"]`                                                   | 0.34 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"Array{Complex{Float64},2}\", 21)"]`                                                   | 0.77 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"Array{Complex{Float64},2}\", 25)"]`                                                   | 0.83 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"Array{Complex{Float64},2}\", 5)"]`                                                    |                1.96 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"Array{Complex{Float64},2}\", 9)"]`                                                    |                1.08 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"Diagonal{Complex{Float64},Array{Complex{Float64},1}}\", 1)"]`                         |                2.55 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"Diagonal{Complex{Float64},Array{Complex{Float64},1}}\", 13)"]`                        |                   1.01 (5%)  |                 Inf (1%) :x: |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"Diagonal{Complex{Float64},Array{Complex{Float64},1}}\", 17)"]`                        | 0.37 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"Diagonal{Complex{Float64},Array{Complex{Float64},1}}\", 21)"]`                        | 0.60 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"Diagonal{Complex{Float64},Array{Complex{Float64},1}}\", 25)"]`                        | 0.94 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"Diagonal{Complex{Float64},Array{Complex{Float64},1}}\", 5)"]`                         |                1.32 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"Diagonal{Complex{Float64},Array{Complex{Float64},1}}\", 9)"]`                         |                1.18 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"MArray{Tuple{2,2},Complex{Float64},2,4}\", 1)"]`                                      |                2.71 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"MArray{Tuple{2,2},Complex{Float64},2,4}\", 13)"]`                                     | 0.67 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"MArray{Tuple{2,2},Complex{Float64},2,4}\", 17)"]`                                     | 0.28 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"MArray{Tuple{2,2},Complex{Float64},2,4}\", 21)"]`                                     | 0.88 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"MArray{Tuple{2,2},Complex{Float64},2,4}\", 25)"]`                                     | 0.90 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"MArray{Tuple{2,2},Complex{Float64},2,4}\", 5)"]`                                      |                1.77 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"MArray{Tuple{2,2},Complex{Float64},2,4}\", 9)"]`                                      |                1.16 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\", 1)"]`  |                6.54 (5%) :x: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\", 13)"]` | 0.92 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\", 17)"]` | 0.37 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\", 21)"]` | 0.91 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\", 25)"]` | 0.94 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\", 5)"]`  |                3.92 (5%) :x: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\", 9)"]`  |                1.37 (5%) :x: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"SArray{Tuple{2,2},Complex{Float64},2,4}\", 1)"]`                                      |                2.75 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"SArray{Tuple{2,2},Complex{Float64},2,4}\", 13)"]`                                     | 0.60 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"SArray{Tuple{2,2},Complex{Float64},2,4}\", 17)"]`                                     | 0.30 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"SArray{Tuple{2,2},Complex{Float64},2,4}\", 21)"]`                                     | 0.85 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"SArray{Tuple{2,2},Complex{Float64},2,4}\", 25)"]`                                     | 0.55 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"SArray{Tuple{2,2},Complex{Float64},2,4}\", 5)"]`                                      |                1.85 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"SArray{Tuple{2,2},Complex{Float64},2,4}\", 9)"]`                                      |                1.10 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\", 1)"]`                                      |                2.14 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\", 13)"]`                                     | 0.74 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\", 17)"]`                                     |                1.24 (5%) :x: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\", 21)"]`                                     | 0.79 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\", 25)"]`                                     | 0.80 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\", 5)"]`                                      |                1.69 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "single qubit", "ordered", "(\"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\", 9)"]`                                      |                1.31 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"Array{Complex{Float64},2}\", 1)"]`                                                     |                2.88 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"Array{Complex{Float64},2}\", 13)"]`                                                    | 0.66 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"Array{Complex{Float64},2}\", 17)"]`                                                    | 0.35 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"Array{Complex{Float64},2}\", 21)"]`                                                    | 0.92 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"Array{Complex{Float64},2}\", 25)"]`                                                    | 0.90 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"Array{Complex{Float64},2}\", 5)"]`                                                     |                2.06 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"Array{Complex{Float64},2}\", 9)"]`                                                     |                1.30 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"Diagonal{Complex{Float64},Array{Complex{Float64},1}}\", 1)"]`                          |                2.50 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"Diagonal{Complex{Float64},Array{Complex{Float64},1}}\", 13)"]`                         |                   0.98 (5%)  |                 Inf (1%) :x: |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"Diagonal{Complex{Float64},Array{Complex{Float64},1}}\", 17)"]`                         | 0.39 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"Diagonal{Complex{Float64},Array{Complex{Float64},1}}\", 21)"]`                         | 0.92 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"Diagonal{Complex{Float64},Array{Complex{Float64},1}}\", 25)"]`                         |                   0.96 (5%)  |                 Inf (1%) :x: |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"Diagonal{Complex{Float64},Array{Complex{Float64},1}}\", 5)"]`                          |                1.28 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"MArray{Tuple{2,2},Complex{Float64},2,4}\", 1)"]`                                       |                2.90 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"MArray{Tuple{2,2},Complex{Float64},2,4}\", 13)"]`                                      | 0.62 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"MArray{Tuple{2,2},Complex{Float64},2,4}\", 17)"]`                                      | 0.35 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"MArray{Tuple{2,2},Complex{Float64},2,4}\", 21)"]`                                      | 0.84 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"MArray{Tuple{2,2},Complex{Float64},2,4}\", 25)"]`                                      | 0.82 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"MArray{Tuple{2,2},Complex{Float64},2,4}\", 5)"]`                                       |                1.97 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"MArray{Tuple{2,2},Complex{Float64},2,4}\", 9)"]`                                       |                1.20 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\", 1)"]`   |                6.53 (5%) :x: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\", 13)"]`  |                   1.01 (5%)  |                 Inf (1%) :x: |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\", 17)"]`  | 0.32 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\", 21)"]`  | 0.93 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\", 25)"]`  |                   0.95 (5%)  |                 Inf (1%) :x: |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\", 5)"]`   |                3.92 (5%) :x: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"PermMatrix{Complex{Float64},Int64,Array{Complex{Float64},1},Array{Int64,1}}\", 9)"]`   |                1.91 (5%) :x: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"SArray{Tuple{2,2},Complex{Float64},2,4}\", 1)"]`                                       |                2.92 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"SArray{Tuple{2,2},Complex{Float64},2,4}\", 13)"]`                                      | 0.65 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"SArray{Tuple{2,2},Complex{Float64},2,4}\", 17)"]`                                      | 0.35 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"SArray{Tuple{2,2},Complex{Float64},2,4}\", 21)"]`                                      | 0.52 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"SArray{Tuple{2,2},Complex{Float64},2,4}\", 25)"]`                                      | 0.82 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"SArray{Tuple{2,2},Complex{Float64},2,4}\", 5)"]`                                       |                1.75 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"SArray{Tuple{2,2},Complex{Float64},2,4}\", 9)"]`                                       |                1.56 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\", 1)"]`                                       |                2.20 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\", 13)"]`                                      | 0.71 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\", 17)"]`                                      | 0.44 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\", 21)"]`                                      | 0.79 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\", 25)"]`                                      | 0.77 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\", 5)"]`                                       |                1.60 (5%) :x: |                   1.00 (1%)  |
| `["matrices", "single qubit", "random", "(\"Complex{Float64}\", \"SparseMatrixCSC{Complex{Float64},Int64}\", 9)"]`                                       |                1.24 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi control", "(\"S\", 12, 2:12, (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))"]`                                                            | 0.52 (5%) :white_check_mark: |                1.12 (1%) :x: |
| `["specialized", "multi control", "(\"S\", 16, 2:16, (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))"]`                                            | 0.28 (5%) :white_check_mark: |                1.10 (1%) :x: |
| `["specialized", "multi control", "(\"S\", 20, 2:20, (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))"]`                            | 0.26 (5%) :white_check_mark: |                1.09 (1%) :x: |
| `["specialized", "multi control", "(\"S\", 24, 2:24, (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))"]`            | 0.26 (5%) :white_check_mark: |                1.08 (1%) :x: |
| `["specialized", "multi control", "(\"S\", 4, 2:4, (2, 3, 4))"]`                                                                                         |                1.21 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi control", "(\"Sdag\", 12, 2:12, (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))"]`                                                         | 0.52 (5%) :white_check_mark: |                1.12 (1%) :x: |
| `["specialized", "multi control", "(\"Sdag\", 16, 2:16, (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))"]`                                         | 0.31 (5%) :white_check_mark: |                1.10 (1%) :x: |
| `["specialized", "multi control", "(\"Sdag\", 20, 2:20, (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))"]`                         | 0.25 (5%) :white_check_mark: |                1.09 (1%) :x: |
| `["specialized", "multi control", "(\"Sdag\", 24, 2:24, (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))"]`         | 0.28 (5%) :white_check_mark: |                1.08 (1%) :x: |
| `["specialized", "multi control", "(\"Sdag\", 4, 2:4, (2, 3, 4))"]`                                                                                      |                1.25 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi control", "(\"Sdag\", 8, 2:8, (2, 3, 4, 5, 6, 7, 8))"]`                                                                          |                1.16 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi control", "(\"T\", 12, 2:12, (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))"]`                                                            | 0.63 (5%) :white_check_mark: |                1.12 (1%) :x: |
| `["specialized", "multi control", "(\"T\", 16, 2:16, (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))"]`                                            | 0.41 (5%) :white_check_mark: |                1.10 (1%) :x: |
| `["specialized", "multi control", "(\"T\", 20, 2:20, (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))"]`                            | 0.41 (5%) :white_check_mark: |                1.09 (1%) :x: |
| `["specialized", "multi control", "(\"T\", 24, 2:24, (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))"]`            | 0.25 (5%) :white_check_mark: |                1.08 (1%) :x: |
| `["specialized", "multi control", "(\"T\", 4, 2:4, (2, 3, 4))"]`                                                                                         |                1.34 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi control", "(\"T\", 8, 2:8, (2, 3, 4, 5, 6, 7, 8))"]`                                                                             |                1.25 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi control", "(\"Tdag\", 12, 2:12, (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))"]`                                                         | 0.52 (5%) :white_check_mark: |                1.12 (1%) :x: |
| `["specialized", "multi control", "(\"Tdag\", 16, 2:16, (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))"]`                                         | 0.19 (5%) :white_check_mark: |                1.10 (1%) :x: |
| `["specialized", "multi control", "(\"Tdag\", 20, 2:20, (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))"]`                         | 0.17 (5%) :white_check_mark: |                1.09 (1%) :x: |
| `["specialized", "multi control", "(\"Tdag\", 24, 2:24, (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))"]`         | 0.23 (5%) :white_check_mark: |                1.08 (1%) :x: |
| `["specialized", "multi control", "(\"Tdag\", 4, 2:4, (2, 3, 4))"]`                                                                                      |                1.27 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi control", "(\"Tdag\", 8, 2:8, (2, 3, 4, 5, 6, 7, 8))"]`                                                                          |                1.17 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi control", "(\"X\", 12, 2:12, (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))"]`                                                            | 0.48 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi control", "(\"X\", 16, 2:16, (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))"]`                                            | 0.28 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi control", "(\"X\", 20, 2:20, (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))"]`                            | 0.26 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi control", "(\"X\", 24, 2:24, (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))"]`            | 0.25 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi control", "(\"X\", 4, 2:4, (2, 3, 4))"]`                                                                                         |                2.28 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi control", "(\"X\", 8, 2:8, (2, 3, 4, 5, 6, 7, 8))"]`                                                                             |                1.73 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi control", "(\"Y\", 12, 2:12, (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))"]`                                                            | 0.49 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi control", "(\"Y\", 16, 2:16, (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))"]`                                            | 0.30 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi control", "(\"Y\", 20, 2:20, (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))"]`                            | 0.27 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi control", "(\"Y\", 24, 2:24, (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))"]`            | 0.18 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi control", "(\"Y\", 4, 2:4, (2, 3, 4))"]`                                                                                         |                2.21 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi control", "(\"Y\", 8, 2:8, (2, 3, 4, 5, 6, 7, 8))"]`                                                                             |                1.39 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi control", "(\"Z\", 12, 2:12, (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))"]`                                                            | 0.51 (5%) :white_check_mark: |                1.12 (1%) :x: |
| `["specialized", "multi control", "(\"Z\", 16, 2:16, (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))"]`                                            | 0.28 (5%) :white_check_mark: |                1.10 (1%) :x: |
| `["specialized", "multi control", "(\"Z\", 20, 2:20, (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))"]`                            | 0.16 (5%) :white_check_mark: |                1.09 (1%) :x: |
| `["specialized", "multi control", "(\"Z\", 24, 2:24, (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))"]`            | 0.24 (5%) :white_check_mark: |                1.08 (1%) :x: |
| `["specialized", "multi control", "(\"Z\", 4, 2:4, (2, 3, 4))"]`                                                                                         |                1.35 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi control", "(\"Z\", 8, 2:8, (2, 3, 4, 5, 6, 7, 8))"]`                                                                             |                1.19 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi qubit multi control", "(\"S\", 12, 4)"]`                                                                                         | 0.78 (5%) :white_check_mark: |                1.15 (1%) :x: |
| `["specialized", "multi qubit multi control", "(\"S\", 16, 5)"]`                                                                                         | 0.30 (5%) :white_check_mark: |                1.15 (1%) :x: |
| `["specialized", "multi qubit multi control", "(\"S\", 20, 6)"]`                                                                                         | 0.26 (5%) :white_check_mark: |                1.14 (1%) :x: |
| `["specialized", "multi qubit multi control", "(\"S\", 24, 8)"]`                                                                                         | 0.27 (5%) :white_check_mark: |                1.13 (1%) :x: |
| `["specialized", "multi qubit multi control", "(\"S\", 4, 2)"]`                                                                                          |                1.35 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi qubit multi control", "(\"S\", 8, 3)"]`                                                                                          |                1.24 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi qubit multi control", "(\"Sdag\", 12, 4)"]`                                                                                      | 0.63 (5%) :white_check_mark: |                1.15 (1%) :x: |
| `["specialized", "multi qubit multi control", "(\"Sdag\", 16, 5)"]`                                                                                      | 0.27 (5%) :white_check_mark: |                1.15 (1%) :x: |
| `["specialized", "multi qubit multi control", "(\"Sdag\", 20, 6)"]`                                                                                      | 0.25 (5%) :white_check_mark: |                1.14 (1%) :x: |
| `["specialized", "multi qubit multi control", "(\"Sdag\", 24, 8)"]`                                                                                      | 0.27 (5%) :white_check_mark: |                1.13 (1%) :x: |
| `["specialized", "multi qubit multi control", "(\"Sdag\", 4, 2)"]`                                                                                       |                1.33 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi qubit multi control", "(\"Sdag\", 8, 3)"]`                                                                                       |                1.17 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi qubit multi control", "(\"T\", 12, 4)"]`                                                                                         | 0.64 (5%) :white_check_mark: |                1.15 (1%) :x: |
| `["specialized", "multi qubit multi control", "(\"T\", 16, 5)"]`                                                                                         | 0.40 (5%) :white_check_mark: |                1.15 (1%) :x: |
| `["specialized", "multi qubit multi control", "(\"T\", 20, 6)"]`                                                                                         | 0.31 (5%) :white_check_mark: |                1.14 (1%) :x: |
| `["specialized", "multi qubit multi control", "(\"T\", 24, 8)"]`                                                                                         | 0.38 (5%) :white_check_mark: |                1.13 (1%) :x: |
| `["specialized", "multi qubit multi control", "(\"T\", 4, 2)"]`                                                                                          |                1.39 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi qubit multi control", "(\"T\", 8, 3)"]`                                                                                          |                1.30 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi qubit multi control", "(\"Tdag\", 12, 4)"]`                                                                                      | 0.63 (5%) :white_check_mark: |                1.15 (1%) :x: |
| `["specialized", "multi qubit multi control", "(\"Tdag\", 16, 5)"]`                                                                                      | 0.29 (5%) :white_check_mark: |                1.15 (1%) :x: |
| `["specialized", "multi qubit multi control", "(\"Tdag\", 20, 6)"]`                                                                                      | 0.30 (5%) :white_check_mark: |                1.14 (1%) :x: |
| `["specialized", "multi qubit multi control", "(\"Tdag\", 24, 8)"]`                                                                                      | 0.26 (5%) :white_check_mark: |                1.13 (1%) :x: |
| `["specialized", "multi qubit multi control", "(\"Tdag\", 4, 2)"]`                                                                                       |                1.33 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi qubit multi control", "(\"X\", 12, 4)"]`                                                                                         | 0.72 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit multi control", "(\"X\", 16, 5)"]`                                                                                         | 0.32 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit multi control", "(\"X\", 20, 6)"]`                                                                                         | 0.24 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit multi control", "(\"X\", 24, 8)"]`                                                                                         | 0.30 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit multi control", "(\"X\", 4, 2)"]`                                                                                          |                2.30 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi qubit multi control", "(\"X\", 8, 3)"]`                                                                                          |                1.88 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi qubit multi control", "(\"Y\", 12, 4)"]`                                                                                         | 0.64 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit multi control", "(\"Y\", 16, 5)"]`                                                                                         | 0.32 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit multi control", "(\"Y\", 20, 6)"]`                                                                                         | 0.28 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit multi control", "(\"Y\", 24, 8)"]`                                                                                         | 0.30 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit multi control", "(\"Y\", 4, 2)"]`                                                                                          |                2.05 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi qubit multi control", "(\"Y\", 8, 3)"]`                                                                                          |                1.47 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi qubit multi control", "(\"Z\", 12, 4)"]`                                                                                         | 0.82 (5%) :white_check_mark: |                1.15 (1%) :x: |
| `["specialized", "multi qubit multi control", "(\"Z\", 16, 5)"]`                                                                                         | 0.30 (5%) :white_check_mark: |                1.15 (1%) :x: |
| `["specialized", "multi qubit multi control", "(\"Z\", 20, 6)"]`                                                                                         | 0.23 (5%) :white_check_mark: |                1.14 (1%) :x: |
| `["specialized", "multi qubit multi control", "(\"Z\", 24, 8)"]`                                                                                         | 0.21 (5%) :white_check_mark: |                1.13 (1%) :x: |
| `["specialized", "multi qubit multi control", "(\"Z\", 4, 2)"]`                                                                                          |                1.32 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi qubit multi control", "(\"Z\", 8, 3)"]`                                                                                          |                1.29 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi qubit", "(\"SWAP\", 12)"]`                                                                                                       | 0.69 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit", "(\"SWAP\", 16)"]`                                                                                                       | 0.31 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit", "(\"SWAP\", 20)"]`                                                                                                       | 0.81 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit", "(\"SWAP\", 24)"]`                                                                                                       | 0.84 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit", "(\"SWAP\", 4)"]`                                                                                                        |                2.60 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi qubit", "(\"SWAP\", 8)"]`                                                                                                        |                1.30 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi qubit", "(\"SWAP\", \"random\", 12)"]`                                                                                           | 0.55 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit", "(\"SWAP\", \"random\", 16)"]`                                                                                           | 0.31 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit", "(\"SWAP\", \"random\", 20)"]`                                                                                           | 0.40 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit", "(\"SWAP\", \"random\", 24)"]`                                                                                           | 0.60 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit", "(\"SWAP\", \"random\", 4)"]`                                                                                            |                2.71 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi qubit", "(\"SWAP\", \"random\", 8)"]`                                                                                            |                1.29 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi qubit", "(\"S\", 12)"]`                                                                                                          | 0.31 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit", "(\"S\", 16)"]`                                                                                                          | 0.28 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit", "(\"S\", 20)"]`                                                                                                          | 0.28 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit", "(\"S\", 24)"]`                                                                                                          | 0.31 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit", "(\"S\", 4)"]`                                                                                                           |                1.44 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi qubit", "(\"S\", 8)"]`                                                                                                           |                1.13 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi qubit", "(\"Sdag\", 12)"]`                                                                                                       | 0.37 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit", "(\"Sdag\", 16)"]`                                                                                                       | 0.31 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit", "(\"Sdag\", 20)"]`                                                                                                       | 0.28 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit", "(\"Sdag\", 24)"]`                                                                                                       | 0.28 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit", "(\"Sdag\", 4)"]`                                                                                                        |                1.86 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi qubit", "(\"Sdag\", 8)"]`                                                                                                        |                1.14 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi qubit", "(\"T\", 12)"]`                                                                                                          | 0.32 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit", "(\"T\", 16)"]`                                                                                                          | 0.27 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit", "(\"T\", 20)"]`                                                                                                          | 0.27 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit", "(\"T\", 24)"]`                                                                                                          | 0.29 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit", "(\"T\", 4)"]`                                                                                                           |                1.63 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi qubit", "(\"T\", 8)"]`                                                                                                           |                1.08 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi qubit", "(\"Tdag\", 12)"]`                                                                                                       | 0.36 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit", "(\"Tdag\", 16)"]`                                                                                                       | 0.27 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit", "(\"Tdag\", 20)"]`                                                                                                       | 0.26 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit", "(\"Tdag\", 24)"]`                                                                                                       | 0.29 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit", "(\"Tdag\", 4)"]`                                                                                                        |                1.66 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi qubit", "(\"Tdag\", 8)"]`                                                                                                        |                1.09 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi qubit", "(\"X\", 12)"]`                                                                                                          |                   1.01 (5%)  |                 Inf (1%) :x: |
| `["specialized", "multi qubit", "(\"X\", 16)"]`                                                                                                          | 0.31 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit", "(\"X\", 20)"]`                                                                                                          | 0.43 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit", "(\"X\", 24)"]`                                                                                                          | 0.93 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit", "(\"X\", 4)"]`                                                                                                           |                2.69 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi qubit", "(\"X\", 8)"]`                                                                                                           |                1.25 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi qubit", "(\"Y\", 12)"]`                                                                                                          | 0.51 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit", "(\"Y\", 16)"]`                                                                                                          | 0.28 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit", "(\"Y\", 20)"]`                                                                                                          | 0.44 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit", "(\"Y\", 24)"]`                                                                                                          | 0.56 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit", "(\"Y\", 4)"]`                                                                                                           |                2.26 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi qubit", "(\"Y\", 8)"]`                                                                                                           |                1.21 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi qubit", "(\"Z\", 12)"]`                                                                                                          | 0.60 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit", "(\"Z\", 16)"]`                                                                                                          | 0.25 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit", "(\"Z\", 20)"]`                                                                                                          | 0.62 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit", "(\"Z\", 24)"]`                                                                                                          | 0.84 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "multi qubit", "(\"Z\", 4)"]`                                                                                                           |                2.55 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "multi qubit", "(\"Z\", 8)"]`                                                                                                           |                1.10 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single control", "(\"S\", 12, (2,), (1,))"]`                                                                                           | 0.88 (5%) :white_check_mark: |                5.00 (1%) :x: |
| `["specialized", "single control", "(\"S\", 16, (2,), (1,))"]`                                                                                           | 0.35 (5%) :white_check_mark: |                5.00 (1%) :x: |
| `["specialized", "single control", "(\"S\", 20, (2,), (1,))"]`                                                                                           | 0.80 (5%) :white_check_mark: |                5.00 (1%) :x: |
| `["specialized", "single control", "(\"S\", 24, (2,), (1,))"]`                                                                                           | 0.85 (5%) :white_check_mark: |                5.00 (1%) :x: |
| `["specialized", "single control", "(\"S\", 4, (2,), (1,))"]`                                                                                            |                2.02 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single control", "(\"S\", 8, (2,), (1,))"]`                                                                                            |                1.51 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single control", "(\"Sdag\", 12, (2,), (1,))"]`                                                                                        |                   0.99 (5%)  |                5.00 (1%) :x: |
| `["specialized", "single control", "(\"Sdag\", 16, (2,), (1,))"]`                                                                                        | 0.35 (5%) :white_check_mark: |                5.00 (1%) :x: |
| `["specialized", "single control", "(\"Sdag\", 20, (2,), (1,))"]`                                                                                        | 0.76 (5%) :white_check_mark: |                5.00 (1%) :x: |
| `["specialized", "single control", "(\"Sdag\", 24, (2,), (1,))"]`                                                                                        | 0.87 (5%) :white_check_mark: |                5.00 (1%) :x: |
| `["specialized", "single control", "(\"Sdag\", 4, (2,), (1,))"]`                                                                                         |                1.67 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single control", "(\"Sdag\", 8, (2,), (1,))"]`                                                                                         |                1.57 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single control", "(\"T\", 12, (2,), (1,))"]`                                                                                           |                1.07 (5%) :x: |                5.00 (1%) :x: |
| `["specialized", "single control", "(\"T\", 16, (2,), (1,))"]`                                                                                           | 0.37 (5%) :white_check_mark: |                5.00 (1%) :x: |
| `["specialized", "single control", "(\"T\", 20, (2,), (1,))"]`                                                                                           | 0.85 (5%) :white_check_mark: |                5.00 (1%) :x: |
| `["specialized", "single control", "(\"T\", 24, (2,), (1,))"]`                                                                                           | 0.88 (5%) :white_check_mark: |                5.00 (1%) :x: |
| `["specialized", "single control", "(\"T\", 4, (2,), (1,))"]`                                                                                            |                2.01 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single control", "(\"T\", 8, (2,), (1,))"]`                                                                                            |                1.57 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single control", "(\"Tdag\", 12, (2,), (1,))"]`                                                                                        |                   0.96 (5%)  |                5.00 (1%) :x: |
| `["specialized", "single control", "(\"Tdag\", 16, (2,), (1,))"]`                                                                                        | 0.34 (5%) :white_check_mark: |                5.00 (1%) :x: |
| `["specialized", "single control", "(\"Tdag\", 20, (2,), (1,))"]`                                                                                        | 0.81 (5%) :white_check_mark: |                5.00 (1%) :x: |
| `["specialized", "single control", "(\"Tdag\", 24, (2,), (1,))"]`                                                                                        | 0.86 (5%) :white_check_mark: |                5.00 (1%) :x: |
| `["specialized", "single control", "(\"Tdag\", 4, (2,), (1,))"]`                                                                                         |                2.00 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single control", "(\"Tdag\", 8, (2,), (1,))"]`                                                                                         |                1.47 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single control", "(\"X\", 12, (2,), (1,))"]`                                                                                           |                   0.97 (5%)  |                5.00 (1%) :x: |
| `["specialized", "single control", "(\"X\", 16, (2,), (1,))"]`                                                                                           | 0.31 (5%) :white_check_mark: |                5.00 (1%) :x: |
| `["specialized", "single control", "(\"X\", 20, (2,), (1,))"]`                                                                                           | 0.76 (5%) :white_check_mark: |                5.00 (1%) :x: |
| `["specialized", "single control", "(\"X\", 24, (2,), (1,))"]`                                                                                           | 0.86 (5%) :white_check_mark: |                5.00 (1%) :x: |
| `["specialized", "single control", "(\"X\", 4, (2,), (1,))"]`                                                                                            |                1.66 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single control", "(\"X\", 8, (2,), (1,))"]`                                                                                            |                1.37 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single control", "(\"Y\", 12, (2,), (1,))"]`                                                                                           | 0.76 (5%) :white_check_mark: |                5.00 (1%) :x: |
| `["specialized", "single control", "(\"Y\", 16, (2,), (1,))"]`                                                                                           | 0.33 (5%) :white_check_mark: |                5.00 (1%) :x: |
| `["specialized", "single control", "(\"Y\", 20, (2,), (1,))"]`                                                                                           | 0.71 (5%) :white_check_mark: |                5.00 (1%) :x: |
| `["specialized", "single control", "(\"Y\", 24, (2,), (1,))"]`                                                                                           | 0.81 (5%) :white_check_mark: |                5.00 (1%) :x: |
| `["specialized", "single control", "(\"Y\", 4, (2,), (1,))"]`                                                                                            |                1.87 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single control", "(\"Y\", 8, (2,), (1,))"]`                                                                                            |                1.41 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single control", "(\"Z\", 12, (2,), (1,))"]`                                                                                           |                1.22 (5%) :x: |                5.00 (1%) :x: |
| `["specialized", "single control", "(\"Z\", 16, (2,), (1,))"]`                                                                                           | 0.39 (5%) :white_check_mark: |                5.00 (1%) :x: |
| `["specialized", "single control", "(\"Z\", 20, (2,), (1,))"]`                                                                                           | 0.83 (5%) :white_check_mark: |                5.00 (1%) :x: |
| `["specialized", "single control", "(\"Z\", 24, (2,), (1,))"]`                                                                                           | 0.86 (5%) :white_check_mark: |                5.00 (1%) :x: |
| `["specialized", "single control", "(\"Z\", 4, (2,), (1,))"]`                                                                                            |                2.04 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single control", "(\"Z\", 8, (2,), (1,))"]`                                                                                            |                1.60 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single qubit multi control", "(\"S\", 12, 4)"]`                                                                                        | 0.77 (5%) :white_check_mark: |                1.15 (1%) :x: |
| `["specialized", "single qubit multi control", "(\"S\", 16, 5)"]`                                                                                        | 0.32 (5%) :white_check_mark: |                1.15 (1%) :x: |
| `["specialized", "single qubit multi control", "(\"S\", 20, 6)"]`                                                                                        | 0.28 (5%) :white_check_mark: |                1.14 (1%) :x: |
| `["specialized", "single qubit multi control", "(\"S\", 24, 8)"]`                                                                                        | 0.27 (5%) :white_check_mark: |                1.13 (1%) :x: |
| `["specialized", "single qubit multi control", "(\"S\", 4, 2)"]`                                                                                         |                1.29 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single qubit multi control", "(\"S\", 8, 3)"]`                                                                                         |                1.21 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single qubit multi control", "(\"Sdag\", 12, 4)"]`                                                                                     | 0.61 (5%) :white_check_mark: |                1.15 (1%) :x: |
| `["specialized", "single qubit multi control", "(\"Sdag\", 16, 5)"]`                                                                                     | 0.30 (5%) :white_check_mark: |                1.15 (1%) :x: |
| `["specialized", "single qubit multi control", "(\"Sdag\", 20, 6)"]`                                                                                     | 0.25 (5%) :white_check_mark: |                1.14 (1%) :x: |
| `["specialized", "single qubit multi control", "(\"Sdag\", 24, 8)"]`                                                                                     | 0.26 (5%) :white_check_mark: |                1.13 (1%) :x: |
| `["specialized", "single qubit multi control", "(\"Sdag\", 4, 2)"]`                                                                                      |                1.45 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single qubit multi control", "(\"Sdag\", 8, 3)"]`                                                                                      |                1.08 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single qubit multi control", "(\"T\", 12, 4)"]`                                                                                        | 0.89 (5%) :white_check_mark: |                1.15 (1%) :x: |
| `["specialized", "single qubit multi control", "(\"T\", 16, 5)"]`                                                                                        | 0.40 (5%) :white_check_mark: |                1.15 (1%) :x: |
| `["specialized", "single qubit multi control", "(\"T\", 20, 6)"]`                                                                                        | 0.31 (5%) :white_check_mark: |                1.14 (1%) :x: |
| `["specialized", "single qubit multi control", "(\"T\", 24, 8)"]`                                                                                        | 0.38 (5%) :white_check_mark: |                1.13 (1%) :x: |
| `["specialized", "single qubit multi control", "(\"T\", 4, 2)"]`                                                                                         |                1.33 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single qubit multi control", "(\"T\", 8, 3)"]`                                                                                         |                1.20 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single qubit multi control", "(\"Tdag\", 12, 4)"]`                                                                                     | 0.47 (5%) :white_check_mark: |                1.15 (1%) :x: |
| `["specialized", "single qubit multi control", "(\"Tdag\", 16, 5)"]`                                                                                     | 0.32 (5%) :white_check_mark: |                1.15 (1%) :x: |
| `["specialized", "single qubit multi control", "(\"Tdag\", 20, 6)"]`                                                                                     | 0.32 (5%) :white_check_mark: |                1.14 (1%) :x: |
| `["specialized", "single qubit multi control", "(\"Tdag\", 24, 8)"]`                                                                                     | 0.25 (5%) :white_check_mark: |                1.13 (1%) :x: |
| `["specialized", "single qubit multi control", "(\"Tdag\", 4, 2)"]`                                                                                      |                1.40 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single qubit multi control", "(\"X\", 12, 4)"]`                                                                                        | 0.64 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "single qubit multi control", "(\"X\", 16, 5)"]`                                                                                        | 0.33 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "single qubit multi control", "(\"X\", 20, 6)"]`                                                                                        | 0.23 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "single qubit multi control", "(\"X\", 24, 8)"]`                                                                                        | 0.29 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "single qubit multi control", "(\"X\", 4, 2)"]`                                                                                         |                2.14 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single qubit multi control", "(\"X\", 8, 3)"]`                                                                                         |                1.54 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single qubit multi control", "(\"Y\", 12, 4)"]`                                                                                        | 0.58 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "single qubit multi control", "(\"Y\", 16, 5)"]`                                                                                        | 0.30 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "single qubit multi control", "(\"Y\", 20, 6)"]`                                                                                        | 0.31 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "single qubit multi control", "(\"Y\", 24, 8)"]`                                                                                        | 0.28 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "single qubit multi control", "(\"Y\", 4, 2)"]`                                                                                         |                2.09 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single qubit multi control", "(\"Y\", 8, 3)"]`                                                                                         |                1.48 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single qubit multi control", "(\"Z\", 12, 4)"]`                                                                                        | 0.61 (5%) :white_check_mark: |                1.15 (1%) :x: |
| `["specialized", "single qubit multi control", "(\"Z\", 16, 5)"]`                                                                                        | 0.33 (5%) :white_check_mark: |                1.15 (1%) :x: |
| `["specialized", "single qubit multi control", "(\"Z\", 20, 6)"]`                                                                                        | 0.24 (5%) :white_check_mark: |                1.14 (1%) :x: |
| `["specialized", "single qubit multi control", "(\"Z\", 24, 8)"]`                                                                                        | 0.30 (5%) :white_check_mark: |                1.13 (1%) :x: |
| `["specialized", "single qubit multi control", "(\"Z\", 4, 2)"]`                                                                                         |                1.43 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single qubit multi control", "(\"Z\", 8, 3)"]`                                                                                         |                1.12 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single qubit", "(\"S\", 1)"]`                                                                                                          |                2.47 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single qubit", "(\"S\", 13)"]`                                                                                                         | 0.61 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "single qubit", "(\"S\", 17)"]`                                                                                                         | 0.35 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "single qubit", "(\"S\", 21)"]`                                                                                                         | 0.80 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "single qubit", "(\"S\", 25)"]`                                                                                                         | 0.78 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "single qubit", "(\"S\", 5)"]`                                                                                                          |                1.93 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single qubit", "(\"S\", 9)"]`                                                                                                          |                1.14 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single qubit", "(\"Sdag\", 1)"]`                                                                                                       |                2.75 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single qubit", "(\"Sdag\", 13)"]`                                                                                                      | 0.77 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "single qubit", "(\"Sdag\", 17)"]`                                                                                                      | 0.36 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "single qubit", "(\"Sdag\", 21)"]`                                                                                                      | 0.79 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "single qubit", "(\"Sdag\", 25)"]`                                                                                                      | 0.83 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "single qubit", "(\"Sdag\", 5)"]`                                                                                                       |                2.06 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single qubit", "(\"Sdag\", 9)"]`                                                                                                       |                1.22 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single qubit", "(\"T\", 1)"]`                                                                                                          |                2.77 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single qubit", "(\"T\", 13)"]`                                                                                                         | 0.78 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "single qubit", "(\"T\", 17)"]`                                                                                                         | 0.36 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "single qubit", "(\"T\", 21)"]`                                                                                                         | 0.80 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "single qubit", "(\"T\", 25)"]`                                                                                                         | 0.86 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "single qubit", "(\"T\", 5)"]`                                                                                                          |                2.04 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single qubit", "(\"T\", 9)"]`                                                                                                          |                1.19 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single qubit", "(\"Tdag\", 1)"]`                                                                                                       |                2.69 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single qubit", "(\"Tdag\", 13)"]`                                                                                                      | 0.81 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "single qubit", "(\"Tdag\", 17)"]`                                                                                                      | 0.35 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "single qubit", "(\"Tdag\", 21)"]`                                                                                                      | 0.77 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "single qubit", "(\"Tdag\", 25)"]`                                                                                                      | 0.83 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "single qubit", "(\"Tdag\", 5)"]`                                                                                                       |                1.99 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single qubit", "(\"Tdag\", 9)"]`                                                                                                       |                1.23 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single qubit", "(\"X\", 1)"]`                                                                                                          |                3.33 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single qubit", "(\"X\", 13)"]`                                                                                                         | 0.65 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "single qubit", "(\"X\", 17)"]`                                                                                                         | 0.30 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "single qubit", "(\"X\", 21)"]`                                                                                                         | 0.83 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "single qubit", "(\"X\", 25)"]`                                                                                                         | 0.85 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "single qubit", "(\"X\", 5)"]`                                                                                                          |                2.41 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single qubit", "(\"X\", 9)"]`                                                                                                          |                1.09 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single qubit", "(\"Y\", 1)"]`                                                                                                          |                2.92 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single qubit", "(\"Y\", 13)"]`                                                                                                         | 0.39 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "single qubit", "(\"Y\", 17)"]`                                                                                                         | 0.24 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "single qubit", "(\"Y\", 21)"]`                                                                                                         | 0.55 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "single qubit", "(\"Y\", 25)"]`                                                                                                         | 0.66 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "single qubit", "(\"Y\", 5)"]`                                                                                                          |                1.73 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single qubit", "(\"Y\", 9)"]`                                                                                                          |                1.17 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single qubit", "(\"Z\", 1)"]`                                                                                                          |                2.60 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single qubit", "(\"Z\", 13)"]`                                                                                                         | 0.89 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "single qubit", "(\"Z\", 17)"]`                                                                                                         | 0.39 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "single qubit", "(\"Z\", 21)"]`                                                                                                         | 0.84 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "single qubit", "(\"Z\", 25)"]`                                                                                                         | 0.86 (5%) :white_check_mark: |                 Inf (1%) :x: |
| `["specialized", "single qubit", "(\"Z\", 5)"]`                                                                                                          |                2.23 (5%) :x: |                   1.00 (1%)  |
| `["specialized", "single qubit", "(\"Z\", 9)"]`                                                                                                          |                1.23 (5%) :x: |                   1.00 (1%)  |

## Benchmark Group List
Here's a list of all the benchmark groups executed by this job:

- `["matrices", "contiguous", "ordered"]`
- `["matrices", "contiguous", "random"]`
- `["matrices", "controlled", "ordered"]`
- `["matrices", "controlled", "random"]`
- `["matrices", "in-contiguous", "ordered"]`
- `["matrices", "in-contiguous", "random"]`
- `["matrices", "single qubit", "ordered"]`
- `["matrices", "single qubit", "random"]`
- `["specialized", "multi control"]`
- `["specialized", "multi qubit multi control"]`
- `["specialized", "multi qubit"]`
- `["specialized", "single control"]`
- `["specialized", "single qubit multi control"]`
- `["specialized", "single qubit"]`

## Julia versioninfo

### Target
```
Julia Version 1.1.0
Commit 80516ca202 (2019-01-21 21:24 UTC)
Platform Info:
  OS: macOS (x86_64-apple-darwin18.5.0)
  uname: Darwin 18.6.0 Darwin Kernel Version 18.6.0: Thu Apr 25 23:16:27 PDT 2019; root:xnu-4903.261.4~2/RELEASE_X86_64 x86_64 i386
  CPU: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz: 
              speed         user         nice          sys         idle          irq
       #1  2800 MHz     258423 s          0 s      91344 s    1271437 s          0 s
       #2  2800 MHz      14322 s          0 s       7966 s    1598840 s          0 s
       #3  2800 MHz     221813 s          0 s      58207 s    1341109 s          0 s
       #4  2800 MHz      14544 s          0 s       5768 s    1600815 s          0 s
       #5  2800 MHz     202017 s          0 s      45211 s    1373900 s          0 s
       #6  2800 MHz      14789 s          0 s       5085 s    1601252 s          0 s
       #7  2800 MHz     193871 s          0 s      37446 s    1389811 s          0 s
       #8  2800 MHz      17268 s          0 s       4643 s    1599216 s          0 s
       
  Memory: 16.0 GB (1602.1015625 MB free)
  Uptime: 297831.0 sec
  Load Avg:  4.51953125  3.6650390625  3.42822265625
  WORD_SIZE: 64
  LIBM: libopenlibm
  LLVM: libLLVM-6.0.1 (ORCJIT, skylake)
```

### Baseline
```
Julia Version 1.1.0
Commit 80516ca202 (2019-01-21 21:24 UTC)
Platform Info:
  OS: macOS (x86_64-apple-darwin18.5.0)
  uname: Darwin 18.6.0 Darwin Kernel Version 18.6.0: Thu Apr 25 23:16:27 PDT 2019; root:xnu-4903.261.4~2/RELEASE_X86_64 x86_64 i386
  CPU: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz: 
              speed         user         nice          sys         idle          irq
       #1  2800 MHz     270328 s          0 s      93310 s    1299686 s          0 s
       #2  2800 MHz      14521 s          0 s       8069 s    1640658 s          0 s
       #3  2800 MHz     231977 s          0 s      59712 s    1371560 s          0 s
       #4  2800 MHz      14702 s          0 s       5849 s    1642696 s          0 s
       #5  2800 MHz     211666 s          0 s      46537 s    1405045 s          0 s
       #6  2800 MHz      14950 s          0 s       5161 s    1643136 s          0 s
       #7  2800 MHz     203183 s          0 s      38613 s    1421452 s          0 s
       #8  2800 MHz      17448 s          0 s       4713 s    1641086 s          0 s
       
  Memory: 16.0 GB (2646.421875 MB free)
  Uptime: 302043.0 sec
  Load Avg:  1.56689453125  1.75439453125  1.853515625
  WORD_SIZE: 64
  LIBM: libopenlibm
  LLVM: libLLVM-6.0.1 (ORCJIT, skylake)
```