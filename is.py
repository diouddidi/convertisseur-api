import requests

# Remplace par ta propre clé API obtenue sur ExchangeRate-API
API_KEY = "b66b3c2662aee4ed1c6feff7"
BASE_URL = "https://v6.exchangerate-api.com/v6"

def convert_currency(from_currency, to_currency, amount):
    """Convertit un montant d'une devise à une autre."""
    url = f"{BASE_URL}/{API_KEY}/pair/{from_currency}/{to_currency}/{amount}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200 and data.get("conversion_result"):
            result = data["conversion_result"]
            print(f"{amount} {from_currency} = {result} {to_currency}")
        else:
            print("Erreur lors de la conversion :", data.get("error-type", "Inconnue"))
    
    except requests.exceptions.RequestException as e:
        print("Une erreur s'est produite lors de la requête :", e)

# Interface utilisateur
def main():
    print("=== Convertisseur de devises ===")
    from_currency = input("Entrez la devise de départ (par exemple, USD) : ").upper()
    to_currency = input("Entrez la devise cible (par exemple, EUR) : ").upper()
    try:
        amount = float(input("Entrez le montant à convertir : "))
        convert_currency(from_currency, to_currency, amount)
    except ValueError:
        print("Veuillez entrer un montant valide.")

if __name__ == "__main__":
    main()
