class ConversorBase:
    def __init__(self):
        self._valor_convertido = None
        self.unidad_origen = None
        self.unidad_destino = None
        self.cantidad_original = None
        self.operacion = ""

    def _mostrar_resultado(self):
        if self._valor_convertido is not None:
            return f"{self.operacion}: {self.cantidad_original} {self.unidad_origen} = {self._valor_convertido} {self.unidad_destino}"
        return "No se ha realizado ninguna conversión."