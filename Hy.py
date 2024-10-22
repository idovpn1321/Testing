import sublist3r
import sys

def find_subdomains(domain):
    # Menggunakan Sublist3r untuk menemukan subdomain
    # Menyediakan argumen yang diperlukan
    engines = 'Google,Bing,Yahoo'  # Menggunakan string yang dipisahkan koma
    subdomains = sublist3r.main(domain, 40, None, None, False, True, False, engines)
    
    # Menyimpan hasil ke dalam file
    with open(f'{domain}_subdomains.txt', 'w') as f:
        for subdomain in subdomains:
            f.write(f"{subdomain}\n")
    
    print(f"Subdomain untuk {domain} telah ditemukan dan disimpan ke {domain}_subdomains.txt")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Penggunaan: python subdomain_finder.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    find_subdomains(domain)
