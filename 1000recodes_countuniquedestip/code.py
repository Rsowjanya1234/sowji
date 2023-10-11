 #Function to check if the last octet of an IP address is in the range 0-255
def is_valid_ip(ip):
    octets = ip.split('.')
    return len(octets) == 4 and all(0 <= int(octet) <= 255 for octet in octets)

# Function to extract unique destination IP addresses from a list of records
def extract_unique_dest_ips(records):
    dest_ip_counts = {}
    for record in records:
        # Split the record and find the destination IP address
        parts = record.split()
        for part in parts:
            if part.startswith("dst="):
                dst_ip = part.split("=")[1]
                if is_valid_ip(dst_ip):
                    if dst_ip in dest_ip_counts:
                        dest_ip_counts[dst_ip] += 1
                    else:
                        dest_ip_counts[dst_ip] = 1
    return dest_ip_counts

# Read records from the 'output_records.txt' file
with open('output_records.txt', 'r') as f:
    records = f.readlines()

# Extract unique destination IP addresses and their counts
dest_ip_counts = extract_unique_dest_ips(records)

# Print each unique destination IP address along with its count
for dst_ip, count in dest_ip_counts.items():
    print(f"Address: {dst_ip} : Count: {count}")

# Print the actual count of unique destination IP addresses
print("COUNT OF UNIQUE DESTINATION IP ADDRESS :")
