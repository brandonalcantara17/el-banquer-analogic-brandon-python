class Client:
    def __init__(self, nom, saldo_inicial=0):
        self.nom = nom
        self.saldo = saldo_inicial

    def ingressar(self, quantitat):
        if quantitat > 0:
            self.saldo += quantitat
            print(f"{self.nom}: Has ingressat {quantitat} €. Saldo actual: {self.saldo} €.")
        else:
            print(f"{self.nom}: La quantitat ha de ser positiva.")

    def retirar(self, quantitat):
        comissio = quantitat * 0.01
        total_a_restar = quantitat + comissio
        if total_a_restar > self.saldo:
            print(f"{self.nom}: Saldo insuficient. Saldo actual: {self.saldo} €.")
        else:
            self.saldo -= total_a_restar
            print(f"{self.nom}: Has retirat {quantitat} € (comissió: {comissio:.2f} €). Saldo actual: {self.saldo:.2f} €.")

class BancAnalogic:
    def __init__(self):
        self.clients = {}

    def afegir_client(self, nom, saldo_inicial=0):
        if nom in self.clients:
            print(f"El client {nom} ja existeix.")
        else:
            self.clients[nom] = Client(nom, saldo_inicial)
            print(f"S'ha afegit el client {nom} amb un saldo inicial de {saldo_inicial} €.")

    def gestionar_client(self, nom):
        return self.clients.get(nom, print(f"El client {nom} no existeix.") or None)
    
def main():
    banc = BancAnalogic()
    
    while True:
        action = input("Acció (afegir, gestionar, sortir): ").strip().lower()
        
        if action == "afegir":
            nom = input("Nom del client: ")
            try:
                saldo_inicial = float(input("Saldo inicial: "))
            except ValueError:
                print("El saldo inicial ha de ser un número.")
                continue
            banc.afegir_client(nom, saldo_inicial)
        
        elif action == "gestionar":
            client = banc.gestionar_client(input("Nom del client: "))
            
            while client:
                operacio = input(f"Operació per a {client.nom} (ingressar, retirar, tornar): ").strip().lower()
                if operacio == "ingressar":
                    try:
                        client.ingressar(float(input("Quantitat a ingressar: ")))
                    except ValueError:
                        print("La quantitat ha de ser un número.")
                elif operacio == "retirar":
                    try:
                        client.retirar(float(input("Quantitat a retirar: ")))
                    except ValueError:
                        print("La quantitat ha de ser un número.")
                elif operacio == "tornar":
                    break
        
        elif action == "sortir":
            break

if __name__ == "__main__":
    main()