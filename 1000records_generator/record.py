import random

# Provided input records
input_records = [
    "[NEW] tcp 6 120 SYN_SENT src=10.1.2.3 dst=203.0.113.47 sport=47800 dport=21 [UNREPLIED] src=203.0.113.47 dst=198.51.100.32 sport=21 dport=47800 helper=ftp",
    "[UPDATE] tcp 6 60 SYN_RECV src=10.1.2.3 dst=203.0.113.47 sport=47800 dport=21 src=203.0.113.47 dst=198.51.100.32 sport=21 dport=47800 helper=ftp",
    "[UPDATE] tcp 6 432000 ESTABLISHED src=10.1.2.3 dst=203.0.113.47 sport=47800 dport=21 src=203.0.113.47 dst=198.51.100.32 sport=21 dport=47800 [ASSURED] helper=ftp"
]

# Function to generate a single record similar to the provided input
def generate_record(dst_ip1, dst_ip2, state):
    src_ip = '10.1.2.3'
    sport = random.randint(1024, 65535)
    dport = random.randint(1024, 65535)

    record = f"[{state}] tcp 6 120 {state} src={src_ip} dst={dst_ip1} sport={sport} dport={dport} [{state}] src={dst_ip1} dst={dst_ip2} sport={dport} dport={sport} helper=ftp\n"
    return record

# Generate 1000 records
records = []
dst_ip1 = '203.0.113.47'
dst_ip2 = '198.51.100.32'

for _ in range(1000):
    # Use the provided input text based on the state
    state = random.choice(['SYN_SENT', 'SYN_RECV', 'ESTABLISHED'])
    record = generate_record(dst_ip1, dst_ip2, state)
    records.append(record)

    # Update dst_ip1 and dst_ip2 based on the last digits
    last_digit1 = int(dst_ip1.split('.')[-1])
    last_digit2 = int(dst_ip2.split('.')[-1])
    dst_ip1 = '.'.join(dst_ip1.split('.')[:-1] + [str(last_digit1 + 1 + random.randint(1, 5))])
    dst_ip2 = '.'.join(dst_ip2.split('.')[:-1] + [str(last_digit2 + 1 + random.randint(1, 5))])

# Write records to a file
with open('output_records.txt', 'w') as f:
    f.writelines(input_records + records)

print("Records generated and written to 'output_records.txt'")
