
from typing import (Any, Callable, Dict, Generic, Iterator, List, Optional, Sequence, Tuple, Type,
                    TypeVar, Union, Sized, overload)
from numpy import _ArrayLike, ndarray, AxesType

def cond(x: _ArrayLike[Any], p: str=None) -> float: ...
@overload
def norm(x: float, ord: Union[str, float]=None, axis: AxesType=None, keepdims: bool=False) -> float: ...
@overload
def norm(x: _ArrayLike[Any], ord: Union[str, float]=None, axis: AxesType=None, keepdims: bool=False) -> ndarray[float]: ...

def qr(a: _ArrayLike[Any], mode: str='reduced') -> Tuple[ndarray[Any], ndarray[Any], ndarray[Any]]: ...
def svd(a: _ArrayLike[Any], full_matrices: bool=True, compute_uv: bool=True) -> Tuple[ndarray[Any],
        ndarray[Any], ndarray[Any]]: ...
def pinv(a: _ArrayLike[Any], rcond: float=1e-15) -> ndarray[Any]: ...
