class Tlacenode:
    """
    A Tlacenode is a TLACE node.
    
    It contains a state, a list of atomic propositions, a list of TLACE branches
    and a list of universal formulas.
    """
    
    def __init__(self, state, atomics=None, branches=None, universals=None):
        """
        Create a new TLACE node.
        
        state -- a State representing the state of the TLACE node
        atomics -- a list of atomic propositions,
                   represented by CTLK AST instances
        branches -- a list of TLACE branches represented by Tlacebranches
        universals -- a list of universal formulas,
                      represented by CTLK AST instances
        """
        self.__state = state
        self.__atomics = atomics or tuple()
        self.__branches = branches or tuple()
        self.__universals = universals or tuple()
    
    @property
    def state(self):
        """state node"""
        return self.__state
        
    @property
    def atomics(self):
        """atomic annotations of this node"""
        return self.__atomics
        
    @property
    def branches(self):
        """branches of this node"""
        return self.__branches
        
    @property
    def universals(self):
        """universal annotations of this node"""
        return self.__universals
        
    def __str__(self):
        pass # TODO


class Tlacebranch:
    """
    A Tlacebranch is a TLACE branch.
    It contains an existential formula.
    This is a generic TLACE branch that must be extended
    to provide an explanation to the existential formula.
    """
    
    def __init__(self, formula):
        """
        Create a new TLACE branch.
        
        formula -- an existential temporal formula,
                   represented by a CTLK AST instance.
        """
        self.__formula = formula      
    
    @property
    def specification(self):
        """The spec of this branch."""
        return self.__formula
        
    def __str__(self):
        pass # TODO
        
        
class TemporalBranch(Tlacebranch):
    """A TLACE branch explaining an existential temporal property."""
    
    def __init__(self, formula, path, loop=None):
        """
        Create a new existential temporal branch.
        
        formula -- the formula this branch explains, as a CTLK AST instance
        path -- the finite path of the explanation,
                as a (state, input, state, ..., input, state) tuple
        loop -- if not None, an (input, state) pair where state belongs to path,
                indicating the start of the loop; input being an input between
                path[-1] and state.
        """
        self.__formula = formula
        self.__path = path
        self.__loop = loop
        
    @property
    def path(self):
        """The path of this branch"""
        return self.__path
        
    @property
    def loop(self):
        """The loop of this branch, possibly None"""
        return self.__loop
    
    
class EpistemicBranch(Tlacebranch):
    """A TLACE branch explaining an existential epistemic property."""
    
    def __init__(self, formula, path):
        """
        Create a new existential epistemic branch.
        
        formula -- the formula this branch explains, as a CTLK AST instance
        path -- the finite path of the explanation,
                as a (s_0, ag_1, s_1, ..., ag_n, state_n) tuple,
                where ag_i is the name of the agents
                for which s_i-1 is equivalent to s_i, for all i : 0 < i <= n.
        """
        self.__formula = formula
        self.__path = path
        
    @property
    def path(self):
        """The path of this branch"""
        return self.__path