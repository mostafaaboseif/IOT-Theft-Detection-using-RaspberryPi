# IOT-Theft-Detection-using-RaspberryPi

The project consists of one multithreaded server and 2 clients that communicate using sockets. 
The server assigns each client to a separate thread. 
One client is connected to a camera used as a motion detector (takes 2 pictures and compares them pixel by pixel to check for change), 
and the other is connected to an external ADC using SPI that interfaces with a light sensor. 
Once the thief enters the room, the light sensor is triggered, it sends a tweet that a thief is detected in the house. 
Once the camera detect the thief in motion, it takes his picture and sends it to the server which forwards it into a face recognition module (implemented using convolution neural networks); 
if it doesn’t match one of the users, it adds the picture to the MySQL database of a web server we designed and sends a tweet contaning his picture.
