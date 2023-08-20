input_file = "list_ip.txt"
output_file = ".htaccess"

with open(input_file, "r") as ip_list:
    ip_addresses = ip_list.readlines()

htaccess_code = "#######   HTAccessIPBlocker BEGIN    #######\n"

for ip_address in ip_addresses:
    ip_address = ip_address.strip()
    htaccess_code += f"deny from {ip_address}\n"

htaccess_code += "#######   HTAccessIPBlocker END    #######"

with open(output_file, "w") as htaccess:
    htaccess.write(htaccess_code)

print(f"Generated {output_file} with IP blocking rules.")
