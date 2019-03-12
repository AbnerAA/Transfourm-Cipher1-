import cipher
import threensform
import IO

block_length = 12
iterations = 16

def main():
	encrypt = IO.request_mode()
	if encrypt:
		text = IO.request_plaintext()
	else:
		text = IO.request_ciphertext()

	mode = IO.request_feistel_mode()

	#coba buat mode ECB

	external_key = IO.request_key()

	new_text = cipher.block_cipher(text, external_key, threensform.threensform, block_length, iterations, mode, encrypt)
	

	if encrypt:
		IO.output_ciphertext(new_text)
	else:
		IO.output_plaintext(new_text)

if __name__ == "__main__":
	main()