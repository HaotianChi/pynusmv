%module(package="pynusmv.nusmv.ltl.ltl2smv") ltl2smv

%{
#include "../../../../nusmv/src/utils/defs.h"
#include "../../../../nusmv/src/ltl/ltl2smv/ltl2smv.h" 
%}

%include ../../../../nusmv/src/utils/defs.h
%include ../../../../nusmv/src/ltl/ltl2smv/ltl2smv.h