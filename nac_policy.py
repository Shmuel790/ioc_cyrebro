def generate_fortigate_script(ip_addresses):
    config_template = """
config user nac-policy

{address_entries}

end
"""
    address_entry_template = """
edit "MAC_{mac}"
    set mac "{mac}"
    set ssid-policy "{mac}"
next
"""

    addresses = []

    for ip in ip_addresses:
        address_entry = address_entry_template.format(ip=ip, comment="NAC_Policy")
        addresses.append(address_entry)

    address_entries = "\n".join(addresses)
    full_script = config_template.format(address_entries=address_entries)

    return full_script

if __name__ == "__main__":
    ip_addresses = [
        "1.14.63.190",

    ]

    fortigate_script = generate_fortigate_script(ip_addresses)
    print(fortigate_script)