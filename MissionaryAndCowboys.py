from __future__ import annotations
from typing import List, Optional
from GenericSearch import Node, bfs, node_to_path

MAX_NUM = 3

class MCState:
    def __init__(self, missionaries: int, cannibals: int, boat: bool) -> None:
        self.westMissionaries= missionaries
        self.westCannibals = cannibals
        self.eastMissionaries = MAX_NUM - self.westMissionaries
        self.eastCannibals = MAX_NUM - self.westCannibals
        self.boat = boat

    def __str__(self) -> str:
        return ("No oeste temos {} Missionários e {} Canibais;\n"
                "No leste temos {} Missionários e {} Canibais.\n"
                "O barco está no {}"\
                .format(self.westMissionaries, self.westCannibals, self.eastMissionaries, self.eastCannibals, ("Oeste" if self.boat else "Leste")))

    @property
    def is_legal(self) -> bool:
        if self.westCannibals > self.westMissionaries and self.westMissionaries > 0:
            return False
        if self.eastCannibals > self.eastMissionaries and self.eastMissionaries > 0:
            return False
        return True

    def goal_test(self) -> bool:
        return self.is_legal and self.eastCannibals == MAX_NUM and self.eastMissionaries == MAX_NUM

    def successors(self) -> List[MCState]:
        successList : List[MCState] = []

        if self.boat:
            if self.westMissionaries > 1:
                successList.append(MCState(self.westMissionaries - 2, self.westCannibals, not self.boat))
            if self.westMissionaries > 0:
                successList.append(MCState(self.westMissionaries - 1, self.westCannibals, not self.boat))
            if self.westCannibals > 1:
                successList.append(MCState(self.westMissionaries,self.westCannibals - 2, not self.boat))
            if self.westCannibals > 0 :
                successList.append(MCState( self.westMissionaries,self.westCannibals - 1, not self.boat))
            if (self.westMissionaries > 0) and (self.westCannibals > 0):
                successList.append(MCState( self.westMissionaries -1 , self.westCannibals -1, not self.boat))
        else:
            if self.eastMissionaries > 1:
                successList.append(MCState(self.westMissionaries + 2, self.westCannibals, not self.boat))
            if self.eastMissionaries > 0:
                successList.append(MCState(self.westMissionaries +1, self.westCannibals, not self.boat))
            if self.eastCannibals > 1:
                successList.append(MCState( self.westMissionaries, self.westCannibals + 2, not self.boat))
            if self.eastCannibals > 0:
                successList.append(MCState( self.westMissionaries, self.westCannibals + 1, not self.boat))
            if (self.eastMissionaries > 0) and (self.eastCannibals):
                successList.append(MCState( self.westMissionaries + 1, self.westCannibals +1 , not self.boat))

        return (x for x in successList if x.is_legal)

def display_solution(path : List[MCState]):
    if len(path) == 0:
        return

    old_state: MCState = path[0]

    print(path)

    for current_state in path[1:]:
        if current_state.boat:
            print("{} Missionarios e {} Canibais foram movidos do leste para o oeste\n"\
                .format(old_state.eastMissionaries - current_state.eastMissionaries, old_state.eastCannibals - current_state.eastCannibals))
                    
        else:
            print("{} Missionarios e {} Canibais foram movidos do oeste para o leste\n"\
                 .format(old_state.westMissionaries - current_state.westMissionaries, old_state.westCannibals - current_state.westCannibals))
                     

        print(current_state)
        old_state = current_state

start: MCState = MCState(MAX_NUM, MAX_NUM, True)
solution: Optional[Node[MCState]] = bfs(start, MCState.goal_test, MCState.successors)

if solution is None:
    print("Sem solução amigo")

else:
    path: List[MCState] = node_to_path(solution)
    display_solution(path)