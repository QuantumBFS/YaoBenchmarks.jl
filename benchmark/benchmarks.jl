using Yao, YaoArrayRegister, YaoBlocks, BenchmarkTools
using PkgBenchmark

function bench(block)
    N = nqubits(block)
    r = rand_state(N)
    return @benchmarkable apply!($r, $block)
end

const SUITE = BenchmarkGroup()

SUITE["gates"] = BenchmarkGroup()
SUITE["random circuits"] = BenchmarkGroup()

for G in [:X, :Y, :Z, :S, :T, :Sdag, :Tdag]
    GT = Expr(:(.), :ConstGate, QuoteNode(Symbol(G, :Gate)))
    GN = Expr(:(.), :ConstGate, QuoteNode(G))

    SUITE["gates"][string(G)] = BenchmarkGroup()
    for n in 1:4:25
        SUITE["gates"][string(G)][n] = @eval bench(repeat($n, $GN))
    end
end
