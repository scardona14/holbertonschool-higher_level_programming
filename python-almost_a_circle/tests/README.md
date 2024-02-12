# Tests

## Run: `python3 -m unittest discover tests`

## Test Classes

* [Base Model Tests](./test_base.py):

	* CLass #0: `ModelInstances`
		* A class to test instances of Base arguments

	* Class #1: `ModelToJSON`
		* A class that tests modules from other types to JSON strings

	* Class #2: `ModelFromJSON`
		* A class that tests modules from JSON strings to other types

	* Class #3: `SaveModelToFile`
		* A class to save Base models to a file

	* Class #4: `CreateMOdel`
		* A class that defines creation of base models

	* Class #5: `LoadFromFile`
		* A class that loads methods of Base models from a file

	* Class #6: `SaveModelToCSV`
		* A class that saves Base models to CSV files

	* Class #7: `LoadFRomCSV`
		* A class that loads methods of Base models from a CSV file


* [Rectangle Model Tests](./test_rectangle.py)

	* CLass #0: `RectangleInstances`
		* A class that defines instances of the Rectangle model

	* Class #1: `WidthInstances`
		* A class that defines instances for width attribute

	* Class #2: `HeightIstances`
		* A class that defines instances for height attribute

	* Class #3: `XInstances`
		* A class that defines instances for x attribute

	* Class #4: `YINstances`
		* A class that defines instances for y attribute

	* Class #5: `RectangleInitOrder`
		* A class that defines the order of initializing rectabgle instances

	* Class #6: `RectangleArea`
		* A class that defines area of a rectangle

	* Class #7: `DisplayMethodsR`
		* A class that defines the print & display methons of a rectangle

	* Class #8: `RectangleArgs`
		* A class that defines updating *args method for rectangle model

	* Class #9: `RectangleKwargs`
		* A class that defines updating **kwargs method for rectangle model

	* Class #10: `RectangleTodict`
		* A class that defines dictionary representation of rectangles


* [Square Model Tests](./test_square.py)

	* CLass #0: `SquareInstances`
		* A class that defines instances of the Square model

	* Class #1: `SizeInstances`
		* A class that defines instances for size attribute

	* Class #2: `XInstances`
		* A class that defines instances for x attribute

	* Class #3: `YInstances`
		* A class that defines instances for y attribute

	* Class #4: `SquareInitOrder`
		* A class that defines the order of initializing rectabgle instances

	* Class #5: `SquareArea`
		* A class that defines area of a rectangle

	* Class #6: `DisplayMethodsS`
		* A class that defines the print & display methons of a square

	* Class #7: `SquareArgs`
		* A class that defines updating *args method for rectangle model

	* Class #8: `SquareKwargs`
		* A class that defines updating **kwargs method for rectangle model

	* Class #9: `SquareTodict`
		* A class that defines dictionary representation of rectangles