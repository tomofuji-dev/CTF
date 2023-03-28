import hashlib
key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_e584b363"
username_trial = b"SCHOFIELD"

print(hashlib.sha256(username_trial),
      hashlib.sha256(username_trial),
      hashlib.sha256(username_trial),
      hashlib.sha256(username_trial),
      hashlib.sha256(username_trial),
      hashlib.sha256(username_trial),
      hashlib.sha256(username_trial),
      hashlib.sha256(username_trial))

print(hashlib.sha256(username_trial).hexdigest(),
	  hashlib.sha256(username_trial).hexdigest(),
	  hashlib.sha256(username_trial).hexdigest(),
	  hashlib.sha256(username_trial).hexdigest(),
	  hashlib.sha256(username_trial).hexdigest(),
	  hashlib.sha256(username_trial).hexdigest(),
	  hashlib.sha256(username_trial).hexdigest(),
	  hashlib.sha256(username_trial).hexdigest())

h = hashlib.sha256(username_trial).hexdigest()
print(h[4],h[5],h[3],h[6],h[2],h[7],h[1],h[8])