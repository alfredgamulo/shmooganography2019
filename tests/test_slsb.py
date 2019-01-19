#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Stéganô - Stéganô is a basic Python Steganography module.
# Copyright (C) 2010-2016  Cédric Bonhomme - https://www.cedricbonhomme.org
#
# For more information : https://github.com/cedricbonhomme/Stegano
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

__author__ = "Cedric Bonhomme"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2016/04/12 $"
__license__ = "GPLv3"

import os
import unittest

from stegano import slsb

class TestSLSB(unittest.TestCase):

    def test_hide_empty_message(self):
        """
        Test hiding the empty string.
        """
        secret = slsb.hide("./examples/pictures/Lenna.png", "")
        secret.save("./image.png")

        clear_message = slsb.reveal("./image.png")

        self.assertEqual("", clear_message)

    def test_hide_and_reveal(self):
        messages_to_hide = ["a", "foo", "Hello World!", ":Python:"]

        for message in messages_to_hide:
            secret = slsb.hide("./examples/pictures/Lenna.png", message)
            secret.save("./image.png")

            clear_message = slsb.reveal("./image.png")

            self.assertEqual(message, clear_message)

    def test_with_long_message(self):
        with open("./examples/lorem_ipsum.txt") as f:
            message = f.read()
        secret = slsb.hide("./examples/pictures/Lenna.png", message)
        secret.save("./image.png")

        clear_message = slsb.reveal("./image.png")
        self.assertEqual(message, clear_message)

    def test_with_too_long_message(self):
        with open("./examples/lorem_ipsum.txt") as f:
            message = f.read()
        message += message*2
        with self.assertRaises(Exception):
            slsb.hide("./examples/pictures/Lenna.png", message)

    def tearDown(self):
        try:
            os.unlink("./image.png")
        except:
            pass


if __name__ == '__main__':
    unittest.main()

  		 	  
  		   	
  		  	 
  		 		 
  		 	  
  		  		
  			  	
  		    
  		    
  		   	
  		 	  
  		   	
  		  	 
  		 		 
  		 	  
  		  		
  			  	
  		    
  		    
  		   	
  		 	  
  		   	
  		  	 
  		 		 
  		 	  
  		  		
  			  	
  		    
  		    
  		   	
  		 	  
  		   	
  		  	 
  		 		 
  		 	  
  		  		
  			  	
  		    
  		    
  		   	
  		 	  
  		   	
  		  	 
  		 		 
  		 	  
  		  		
  			  	
  		    
  		    
  		   	
  		 	  
  		   	
  		  	 
  		 		 
  		 	  
  		  		
  			  	
  		    
  		    
  		   	
  		 	  
  		   	
  		  	 
  		 		 
  		 	  
  		  		
  			  	
  		    
  		    
  		   	
  		 	  
  		   	
  		  	 
  		 		 
  		 	  
  		  		
  			  	
  		    
  		    
  		   	
  		 	  
  		   	
  		  	 
  		 		 
  		 	  
  		  		
  			  	
  		    
  		    
  		   	
  		 	  
  		   	
  		  	 
  		 		 
  		 	  
  		  		
  			  	
  		    
  		    
  		   	
  		 	  
  		   	
  		  	 
  		 		 
  		 	  
  		  		
  			  	
  		    
  		    
  		   	
  		 	  
  		   	
  		  	 
  		 		 
  		 	  
  		  		
  			  	
  		    
  		    
  		   	
  		 	  
  		   	
  		  	 
  		 		 
  		 	  
  		  		
  			  	
  		    
  		    
  		   	
  		 	  
  		   	
  		  	 
  		 		 
  		 	  
  		  		
  			  	
  		    
  		    
  		   	
  		 	  
  		   	
  		  	 
  		 		 
  		 	  
  		  		
  			  	
  		    
  		    
  		   	
  		 	  
  		   	
  		  	 
  		 		 
  		 	  
  		  		