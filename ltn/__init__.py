from ltn.core import Variable, Predicate, Constant, Function, Connective, diag, undiag, Quantifier, \
    LTNObject, process_ltn_objects, LambdaModel
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")