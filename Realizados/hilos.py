import threading

class ContadorHilos:
    def __init__(self, hilosAGenerar):
        self.ubicacionHilos = []
        self.hilosAGenerar = hilosAGenerar

    def contadorDePaso(self, paso, numeroDeHilo):
        print(f"Hilo {numeroDeHilo}, paso: {paso}")

    def conteo(self, numeroDehilo):
        print(f"Yo soy el hilo Nro {numeroDehilo}")
        for paso in range(1, 11):
            self.contadorDePaso(paso, numeroDehilo)
        print(f"Fin del conteo del hilo Nro {numeroDehilo}")

    def iniciarProceso(self):
        print("Comenzando el proceso")

        for numeroHilo in range(1, self.hilosAGenerar + 1):
            hilo = threading.Thread(target=self.conteo, args=(numeroHilo,))
            self.ubicacionHilos.append(hilo)
            hilo.start()

        for hilo in self.ubicacionHilos:
            hilo.join()

        print("El proceso ha terminado.")


contadorHilos = ContadorHilos(4)
contadorHilos.iniciarProceso()