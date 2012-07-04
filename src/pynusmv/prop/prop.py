from ..nusmv.prop import prop as nsprop

from ..fsm.fsm import BddFsm
from ..node.node import Node
from ..utils.wrap import PointerWrapper

class Prop(PointerWrapper):
    """
    Python class for prop structure.
    
    The Prop class contains a pointer to a prop in NuSMV and provides a set
    of operations on this prop.
    """
    
    def __init__(self, ptr):
        """
        Create a new prop with ptr.
        
        ptr -- the pointer to the NuSMV prop.
        """
        super().__init__(ptr)
        
    @property
    def type(self):
        """The type of this prop."""
        return nsprop.Prop_get_type(self._ptr)
        
    @property
    def name(self):
        """The name of this prop."""
        return Node(nsprop.Prop_get_name(self._ptr))
        
    @property
    def strname(self):
        """The name of this prop, as a string."""
        return nsprop.Prop_get_name_as_string(self._ptr)
        
    @property
    def expr(self):
        """The expression of this prop."""
        return Node(nsprop.Prop_get_expr(self._ptr))
        
    @property
    def exprcore(self):
        """The core expression of this prop."""
        return Node(nsprop.Prop_get_expr_core(self._ptr))
        
    @property
    def bddfsm(self):
        """The fsm of this prop, into BddFsm format."""
        return BddFsm(nsprop.Prop_get_bdd_fsm(self._ptr))