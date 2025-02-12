# Proiect Python - Gestionare Produse și Coș de Cumpărături

Acest proiect Python simulează gestionarea unui inventar de produse și adăugarea produselor într-un coș de cumpărături. Proiectul include următoarele funcționalități:

## Clase

### 1. **Product**
Clasa `Product` reprezintă un produs din inventar. Atributele acestei clase sunt:
- `name`: Numele produsului
- `price`: Prețul produsului
- `quantity`: Cantitatea disponibilă a produsului

Metode:
- `display_info()`: Afișează informații despre produs
- `update_quantity(amount)`: Actualizează cantitatea produsului (poate adăuga sau reduce cantitatea)

### 2. **ProductManager**
Clasa `ProductManager` gestionează lista de produse. Atributele acestei clase sunt:
- `products`: O listă cu obiecte de tip `Product`

Metode:
- `add_product(product)`: Adaugă un produs la inventar
- `display_all_products()`: Afișează toate produsele din inventar
- `total_inventory_value()`: Calculează valoarea totală a inventarului

### 3. **Cart**
Clasa `Cart` reprezintă coșul de cumpărături al unui client. Atributele acestei clase sunt:
- `cart_items`: O listă cu produsele adăugate în coș (sub formă de dicționare care conțin produsul și cantitatea acestuia)

Metode:
- `add_to_cart(product, quantity)`: Adaugă un produs în coșul de cumpărături
- `calculate_total()`: Calculează valoarea totală a coșului de cumpărături
- `display_cart()`: Afișează produsele din coșul de cumpărături

## Funcționalități

- **Adăugare produse**: Produsele pot fi adăugate în inventar de către un manager de produse.
- **Coș de cumpărături**: Produsele pot fi adăugate într-un coș de cumpărături, iar valoarea totală a coșului poate fi calculată.
- **Actualizarea cantităților**: Cantitățile produselor din inventar pot fi actualizate pe baza adăugării sau eliminării acestora din coș.

## Tehnologii folosite:
- Python 3.x

## Cum să folosești acest proiect:
1. Clonează repository-ul:
   ```bash
   git clone https://github.com/username/proiectul-meu.git
