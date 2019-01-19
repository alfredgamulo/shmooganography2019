Stéganô
=======

#### A Python Steganography module.


Installation
------------

Refers to the INSTALL file.


Use Stéganô as a library in your Python program
-----------------------------------------------

If you want to use Stéganô in your Python program you just have to import the appropriate steganography technique. For example:


    from stegano import slsb
    secret = slsb.hide("./pictures/Lenna.png", "Bonjour tout le monde")
    secret.save("./Lenna-secret.png")


Use Stéganô as a program
------------------------

In addition you can use Stéganô as a program.

Example:

    ~/stegano/$ sudo python setup.py install
    ~/$ slsb --hide -i ../examples/pictures/Lenna.png -o Lena1.png -m "MessageBo"


Examples
--------

There are some examples in the foler *examples*.


Turorial
--------

You will find a complete tutorial_ and some general informations about steganography_ and Stéganô.

.. _tutorial: http://projects.cedricbonhomme.org/projects/stegano/wiki/
.. _steganography: http://wiki.cedricbonhomme.org/security:steganography
