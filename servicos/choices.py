from django.db.models import TextChoices

class ChoicesCategoriaManutencao(TextChoices):
    TROCAR_VALVULA_MOTOR = "TVM", "Trocar válcula do motor"
    TROCAR_OLEO = "TO", "Troca de óleo"
    BALANCEAMENTO = "B", "Balanceamento"
    REVISAO_FREIOS = "RF", "Revisão dos freios"
    LIMPEZA_AR_CONDICIONADO = "LAC", "Limpeza do sistema de ar condicionado"
    TROCA_PASTILHAS_FREIO = "TPF", "Troca das pastilhas de freio"