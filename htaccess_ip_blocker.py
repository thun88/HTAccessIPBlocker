input_file = "list_ip.txt"
output_file = ".htaccess"

with open(input_file, "r") as ip_list:
    ip_addresses = ip_list.readlines()
htaccess_code = "#######   HTAccessIPBlocker BEGIN    #######\n"
htaccess_code += "<IfModule mod_rewrite.c>\n    RewriteEngine On\n\n"

for ip_address in ip_addresses:
    ip_address = ip_address.strip()
    htaccess_code += f"    RewriteCond %{{REMOTE_ADDR}} ^{ip_address}$ [OR]\n"

# Remove the last [OR] from the last condition
htaccess_code = htaccess_code.rstrip("[OR]\n")

htaccess_code += "\n    RewriteRule ^ - [F]\n</IfModule>"
htaccess_code += "\n#######   HTAccessIPBlocker END    #######"

with open(output_file, "w") as htaccess:
    htaccess.write(htaccess_code)

print(f"Generated {output_file} with IP blocking rules.")
