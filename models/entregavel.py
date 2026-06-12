"""
Modelo de dados para Entregável.
Representa uma execução de processo RPA.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Entregavel:
    """Representa um entregável/execução de processo RPA"""

    id_disparo: str
    nome_processo: str
    nome_fluxo: str
    frequencia_disparo: str
    horarios_disparo: str
    tipo_fluxo: str
    data_inicio: datetime
    data_fim: datetime
    duracao: str
    tipo_arquivo: Optional[str]
    status: str
    erros: Optional[str]
    progresso: int
    resultado_esperado: int
    resultado_entregue: int
    tipo_esperado: Optional[str]
    dados_adicionais: Optional[str]
    em_producao: bool

    @property
    def area_sigla(self) -> str:
        """Extrai a sigla da área do nome do processo"""
        return self.nome_processo.split('-')[0].lower() if '-' in self.nome_processo else 'outros'

    @property
    def concluido(self) -> bool:
        """Verifica se o processo foi concluído com sucesso"""
        return self.status.lower() == 'concluído'

    @property
    def percentual_atingimento(self) -> float:
        """Calcula o percentual de atingimento"""
        if self.resultado_esperado == 0:
            return 0.0
        return (self.resultado_entregue / self.resultado_esperado) * 100
