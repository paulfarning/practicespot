Practicespot
============

Simple Python script to read the contents of a directory's subdirectories containing mp3s
and generating a static html page to list the directory names, file names and file lengths.

Designed to make sharing of band practice recordings easy and is limited based on
those needs.

I'm not a Python developer. Don't use this code as examples of good coding practices.

### Dependencies

* [`mpeg1audio`](http://github.com/Ciantic/mpeg1audio/)

### Basic usage
Put directories containing mp3s in `audio` and upload entire package to server. To build, run:

	$ python lib/build.py

This will create a file named index.html. Page title, directory name and template location
can be changed in `lib/build.py`. If changing the audio directory name and using the Bash script,
it must be changed there as well.

Directories are sorted in reverse. The intended naming convention is `YYMMDD`, ex 130908.

### Shared hosting usage
I run this on Dreamhost. This is how I installed and use mpeg1audio in that environment.

1. Clone the [repo](http://github.com/Ciantic/mpeg1audio/).
2. Install to home directory: `$ python setup.py install --home=~`
3. Add path to `build.py` by adding these lines before `import mpeg1audio`:

		import sys
		import os
		sys.path.append(os.environ['HOME'] + '/lib/python')

### Full usage + bash script
Here's how I use this with the included bash script to add a session.

1. Create a local directory with mp3 files.
2. Upload the files:

		$ scp -r local/path/to/dirname user@host:remote/path/to/dirname

3. SSH to server.
4. Run bash script:

		$ bash add.sh dirname


### Bash script
This script takes a new directory name as an argument or prompt, prepares it and regenerates the listing.

1. `.DS_Store` files are removed.
2. The directory is zipped and that zip is added to the directory.
3. Listing is regenerated.

