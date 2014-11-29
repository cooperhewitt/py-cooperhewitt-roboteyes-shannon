# py-cooperhewitt-roboteyes-shannon

Functions for calculating and deriving properties using Shannon entropy for an image.

## Usage

	import sys
	import Image
        import pprint

	import cooperhewitt.roboteyes.shannon as shannon

	path = sys.argv[1]
	im = Image.open(path)

	entropy = shannon.entropy(im)
	print pprint.pformat(entropy)

	tiles = shannon.focalpoint(im)
	print pprint.pformat(tiles)

## See also

* http://labs.cooperhewitt.org/2013/default-sort-or-what-would-shannon-do/
