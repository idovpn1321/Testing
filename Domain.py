import sublist3r
import sys
import os

def find_subdomains(domain):
    # Menggunakan Sublist3r untuk menemukan subdomain
    engines = 'Google,Bing,Yahoo'  # Menggunakan string yang dipisahkan koma
    subdomains = sublist3r.main(domain, 40, None, None, False, True, False, engines)
    
    # Menentukan path untuk menyimpan hasil
    output_file_path = f'/storage/shared/{domain}_subdomains.txt'  # Menggunakan path yang benar
    
    # Menyimpan hasil ke dalam file
    with open(output_file_path, 'w') as f:
        for subdomain in subdomains:
            f.write(f"{subdomain}\n")
    
    print(f"Subdomain untuk {domain} telah ditemukan dan disimpan ke {output_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Penggunaan: python subdomain_finder.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    find_subdomains(domain)
