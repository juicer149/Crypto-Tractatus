from typing import Callable, Dict, List, TypeVar

T = TypeVar("T")

# Internt register
TRANSFORM_REGISTRY: Dict[str, Callable[[List[T]], List[T]]] = {}

def register(name: str):
    def decorator(func: Callable[[List[T]], List[T]]):
        if name in TRANSFORM_REGISTRY:
            raise ValueError(f"Transform '{name}' is already registered.")
        TRANSFORM_REGISTRY[name] = func
        return func
    return decorator

def get_transform(name: str) -> Callable[[List[T]], List[T]]:
    if name not in TRANSFORM_REGISTRY:
        raise ValueError(f"Transform '{name}' is not registered.")
    return TRANSFORM_REGISTRY[name]

def list_transforms() -> List[str]:
    return list(TRANSFORM_REGISTRY.keys())

