import re
import ipaddress


def extract_cidrs_from_file(file_path):
    # Define the regex pattern for matching CIDR blocks
    cidr_pattern = re.compile(
        r'\bCidr: (?:[0-9]{1,3}\.){3}[0-9]{1,3}\/(?:[0-2]?[0-9]|3[0-2])\b'
    )

    cidrs_found = []

    # Read the file
    with open(file_path, 'r') as file:
        for line in file:
            # Find all CIDR blocks in the line
            matches = cidr_pattern.findall(line)
            cidrs_found.extend(matches)

    return cidrs_found


# Example usage
file_path = 'path/to/cfn.template'

cidr_blocks = [cidr.split(':')[1].strip() for cidr in extract_cidrs_from_file(file_path)]

sorted_cidr_blocks = sorted(cidr_blocks, key=lambda cidr: ipaddress.ip_network(cidr, strict=False))

# Print the sorted CIDR blocks
print(len(sorted_cidr_blocks))
for cidr in sorted_cidr_blocks:
    print(cidr)
