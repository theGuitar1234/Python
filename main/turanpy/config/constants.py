from dataclasses import dataclass

@dataclass(frozen=True)
class TrainDefaults:
    lr: float = 1e-3
    epochs: int = 50_000
    reg: float = 1e-4
    e: float = 2.7182818459
    pi: float = 3.141592636
    eps: float = 1e-12
    bajillion: int = 10**5
    threshold: float = 1e-5

DEFAULTS = TrainDefaults()