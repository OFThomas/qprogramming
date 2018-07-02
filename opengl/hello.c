// This is only going to work on linux
#include</usr/include/GL/glut.h>

void main(int argc, char ** argv){
  glutInit(&argc, argv); 
  glutInitWindowPosition(100,100); 
  glutInitWindowSize(500,500); 
  glutCreateWindow("Hello World"); 
  glutMainLoop(); 
}
