import cv2
import numpy as np


class NodePreprocessor():
    """
    docstring for NodePreprocessor

    """

    def __init__(self, steps_per_mm=None, sensor_positions=None):

        # dimensions and parameters

        self.steps_per_mm = steps_per_mm or 2
        self.sensor_positions = sensor_positions or [
            [-4.6, 0], [-2.3, 0], [0, 0], [2.3, 0], [4.6, 0], [0, 2.3]]
        self.number_of_sensors = len(self.sensor_positions)

        self.image_size_mm = [120, 120]
        self.pixel_per_steps = 1
        self.image_name = 'node-_.png'
        self.number_of_nodes = 5
        self.node_line_angles = [[0, 90, 180, 270], [
            0, 180, 270], [0, 270], [180, 270], [270]]
        self.line_thickness_mm = 30
        self.r,self.c=self.node_images.shape
        self.cordinate_convert_matrix=np.array([[1,0,int(self.c/2)],[0,-1,int(self.r/2)]])
    def draw_rect(self,image,angle):
    	r,c=image.shape
    	pt1=[r]
    	cv2.rectangle(image,)

    def to_image_cordinates(self,x,y):
    	return (tuple(np.dot(self.cordinate_convert_matrix,np.array([x,y,1]))))
    def get_images(self):
        self.sensor_image = np.zeros(((np.max(self.sensor_positions, axis=0)-(np.min(self.sensor_positions, axis=0))*self.steps_per_mm*self.pixel_per_steps,
                                      (np.max(self.sensor_positions, axis=1)-(np.min(self.sensor_positions, axis=1))*self.steps_per_mm*self.pixel_per_steps))

        self.node_images=[np.zeros((self.image_size_mm*self.steps_per_mm*self.pixel_per_steps+1, self.image_size_mm *
                                   self.steps_per_mm*self.pixel_per_steps+1)) for i in range(number_of_nodes)]
        for i in self.number_of_nodes:
        	try:
        		self.node_images[i]=cv2.imread('ImageData/'+self.image_name.replace(str(i)),cv2.IMREAD_GRAYSCALE)
        	except:
        		temp=np.zeros((self.image_size_mm*self.steps_per_mm*self.pixel_per_steps+1, self.image_size_mm *
                                   self.steps_per_mm*self.pixel_per_steps+1))

        		self.node_images[i]=

