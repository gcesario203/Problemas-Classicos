from typing import Dict
memo: Dict[int, int] = {0:0,1:1}
counter: int  = 0

def fibonacciIterativo(numero: int) -> int:
    if numero == 0:
        return numero

    ultimo:int = 0
    proximo:int = 1

    for _ in range(1,numero):
        ultimo, proximo = proximo, ultimo + proximo

    return proximo

def fibonacciRecursivo(numero: int):
    if numero not in memo:
        memo[numero] = fibonacciRecursivo(numero - 1) + fibonacciRecursivo(numero - 2)
        print('memo atual ---> {0}'.format(memo[numero]))
    return memo[numero]
