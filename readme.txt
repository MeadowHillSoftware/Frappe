I N S T A L L A T I O N

LINUX (32-BIT & 64-BIT)

	To install Frappe, extract the folder (or just the files, if you like) to a place of your choosing.

	Frappe has a number of dependencies that must be installed. Installing PyGTK with your package manager should automatically install GTK+, Python, PyCairo, and PyGObject as dependencies.
	
	To run the program, open a terminal and type:
	
		python Frappe-0.9.0.py
	
	If you get an error like "No such file or directory," the python script (Frappe-0.9.0.py) is probably not in your path.  You can try one of the following:
	
		You can try typing the full path of the script, such as:
		
			python /home/user/Frappe/Frappe-0.9.0.py
	
		You can change directory into the python script's folder and execute the file, such as:
	
			cd /home/user/Frappe
			python Frappe-0.9.0.py
	
	If the program still doesn't work, make sure the dependencies (GTK+, Python, PyCairo, PyGObject, and PyGTK) are all installed.
	
	If the program still doesn't work, open up your file manager, find the python script, right click it, and make sure the script is listed as executable.
	


WINDOWS (2000, XP, VISTA, & 7)

	To install Frappe, extract the folder (or just the files, if you like) to a place of your choosing.
	
	Frappe has a number of dependencies that must be installed in order for the program to run.  Follow the instructions below for their installation.
	
	Download Python, GTK+, PyCairo, PyGObject, and PyGTk from the following addresses:
	
		http://www.python.org/ftp/python/2.6.5/python-2.6.5.msi
		http://downloads.sourceforge.net/gtk-win/gtk2-runtime-2.16.6-2010-05-12-ash.exe?download
		http://ftp.gnome.org/pub/GNOME/binaries/win32/pycairo/1.8/pycairo-1.8.6.win32-py2.6.exe
		http://ftp.gnome.org/pub/GNOME/binaries/win32/pygobject/2.20/pygobject-2.20.0.win32-py2.6.exe
		http://ftp.gnome.org/pub/GNOME/binaries/win32/pygtk/2.16/pygtk-2.16.0+glade.win32-py2.6.exe

	Install Python by double-clicking python.2.6.5.msi and following the onscreen instructions
	
	Install GTK+ by double-clicking gtk2-runtime-2.16.6-2010-05-12-ash.exe and following the onscreen instructions
	
		NOTE: Be sure to check if you already have a GTK+ 2.10 runtime installed, this may cause conflicts with others applications using the GTK+ runtime, like GIMP.
		See http://faq.pygtk.org/index.py?req=show&file=faq21.001.htp for more details
	
	Install PyCairo by double clicking pycairo-1.8.6.win32-py2.6.exe and following the onscreen instructions
	
	Install PyGObject by double-clicking pygobject-2.20.0.win32-py2.6.exe and following the onscreen instructions
	
	Install PyGTK by double-clicking pygtk-2.16.0+glade.win32-py2.6.exe and following the onscreen instructions
	
	To run Frappe, double-click the python script (Frappe-0.9.0.py).
	
	If the program doesn't run, the script is probably not in your path.  Trying copying the script to the desktop and double-clicking it.
	
	To run a python script from a location outside of your path, try adding python to your path variable.
	
		In Windows 2000 and XP, do the following:
		
			Right-click My Computer > click Properties > click Advanced tab > click Environment Variables > highlight Path, click Edit
			Add the following to the end of the Variable Value:
			
				;C:\Python26
	
			Click OK

		In Windows Vista and 7, do the following:
		
			Click Start > click Run > in the Run box, type:
			
				accounts
				
			Click Enter > click Change My Environment Variable > highlight Path > click Edit > add the following to the end of the Variable Value:
			
				;C:\Python26
			
			Click OK





U S A G E

	To use the program, enter the size of the success pool and click the Enter button.
	
	To export the results to a text file, click the Export button.
	
	To exit the program, simply click either the OK button or the Cancel button.





L I C E N S E

Copyright 2010 Meadow Hill Software.  Some rights reserved.

This work is licensed under a Creative Commons Attribution-Share Alike 3.0 United States License.
	
