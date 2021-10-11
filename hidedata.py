
from PIL import Image

def genData(data):

		newd = []

		for i in data:
			newd.append(format(ord(i), '08b'))
		return newd


def main():
	a = int(input(":: Welcome to Steganography ::\n"
						"1. Encode\n2. Decode\n"))
	if (a == 1):
		encode()

	elif (a == 2):
		print("Decoded Word : " + decode())
	else:
		raise Exception("Enter correct input")
	    
def modPix(pix, data):



	
def encode_enc(newimg, data):





	


def encode():
	img = input("Enter image name(with extension) : ")
	image = Image.open(img, 'r')

	data = input("Enter data to be encoded : ")
	if (len(data) == 0):
		raise ValueError('Data is empty')

	newimg = image.copy()
	encode_enc(newimg, data)

	new_img_name = input("Enter the name of new image(with extension) : ")
	newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))

	main()


def decode():
























	

# Main Function


# Driver Code
if __name__ == '__main__' :

	# Calling main function
	main()
