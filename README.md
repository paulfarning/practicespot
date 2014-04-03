Practice Spot
============

Practice Spot is a Python script to read the contents of a directory's subdirectories containing mp3s
and generate a static html page to list the directory names, file names and file lengths.

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

### Full usage + bash scripts
Here are two ways to use this with the included bash scripts. One version runs a local script while the other is a two step process of upload and then run a remote script.

#### Local script.

1. Create a local directory with mp3 files.
2. Run push.sh locally:

		$ bash push.sh user@host dirname

#### Two step with remote script.

1. Create a local directory with mp3 files.
2. Upload the files:

		$ scp -r local/path/to/dirname user@host:remote/path/to/dirname

3. SSH to server.
4. Run add.sh on remote server:

		$ bash add.sh dirname


### Bash scripts
__push.sh__ takes a host name and a new directory name as arguments or prompt, uploads the directory, prepares it and regenerates the listing.

1. Directory is uploaded using scp.
2. `.DS_Store` files are removed.
3. The directory is zipped and that zip is added to the directory.
4. Listing is regenerated.

__add.sh__ takes a new directory name as an argument or prompt, prepares it and regenerates the listing.

1. `.DS_Store` files are removed.
2. The directory is zipped and that zip is added to the directory.
3. Listing is regenerated.

