from conversor import ConversorBase

class ConversorDistancia(ConversorBase):
    def metros_a_centimetros(self, cantidad_metros):
        self.operacion = "conversión"
        self.cantidad_original = cantidad_metros
        self.unidad_origen = "metros"
        self.unidad_destino = "centimetros"
        self._valor_convertido = cantidad_metros * 100
        return self._mostrar_resultado()

    def centimetros_a_metros(self, cantidad_centimetros):
        self.operacion = "conversión"
        self.cantidad_original = cantidad_centimetros
        self.unidad_origen = "centimetros"
        self.unidad_destino = "metros"
        self._valor_convertido = cantidad_centimetros / 100
        return self._mostrar_resultado()

    def centimetros_a_kilometros(self, cantidad_centimetros):
        self.operacion = "conversión"
        self.cantidad_original = cantidad_centimetros
        self.unidad_origen = "centimetros"
        self.unidad_destino = "kilometros"
        self._valor_convertido = cantidad_centimetros / 100000
        return self._mostrar_resultado()