# py-cooperhewitt-roboteyes-shannon

## Usage

	import sys
	import Image
        import pprint

	import cooperhewitt.roboteyes.shannon as shannon

	path = sys.argv[1]
	im = Image.open(path)

	tiles = shannon.focalpoint(im)
	print pprint.pformat(tiles)

## See also
