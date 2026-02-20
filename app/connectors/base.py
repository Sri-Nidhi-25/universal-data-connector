
from abc import ABC, abstractmethod
from typing import List, Dict, Any

class BaseConnector(ABC):

    @abstractmethod
    def fetch(self, limit: int = 10, **kwargs) -> List[Dict[str, Any]]:
        pass
