#two.py
import one

print("TOP IN LEVEL TWO.PY")

one.func()

if __name__ == '__main__':
	print("TWO.PY is being run directly!")
else:
	print("TWO.PY HAS BEEN imported!")	
	pass