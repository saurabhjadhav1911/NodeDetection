import cv2
import numpy as np


class NodePreprocessor():
    """
    docstring for NodePreprocessor

    """

    def __init__(self, steps_per_mm=None, sensor_positions=None):

        # dimensions and parameters

        self.steps_per_mm = steps_per_mm or 2
        self.sensor_positions = sensor_positions or np.array([
            [-46, 0], [-23, 0], [0, 0], [23, 0], [46, 0], [0, 23]])
        self.number_of_sensors = len(self.sensor_positions)

        self.image_size_mm = [120, 120]
        self.pixel_per_steps = 1
        self.image_name = 'node-_.png'
        self.number_of_nodes = 5
        self.node_line_angles = [[0, 90, 180, 270], [
            0, 180, 270], [0, 270], [180, 270], [270]]
        self.line_thickness_mm = 30

        self.node_images=np.zeros((self.number_of_nodes,self.image_size_mm[0]*self.steps_per_mm*self.pixel_per_steps+1, self.image_size_mm[1] *
                                   self.steps_per_mm*self.pixel_per_steps+1),dtype=object)
        self.r,self.c=self.node_images[0].shape
        self.cordinate_convert_matrix=np.array([[1,0,int(self.c/2)],[0,-1,int(self.r/2)]])
        self.get_images()

    def draw_rect(self,image,angle):
        r,c=image.shape
        d=sqrt(r**2+c**2)

        pt1=self.to_image_cordinates(0,0)
        pt1=self.to_image_cordinates(min(c/2,d*np.cos(angle*np.pi/180)),min(c/2,d*np.sin(angle*np.pi/180)))
        cv2.line(image,pt1,pt2,255,self.line_thickness_mm*self.steps_per_mm*self.pixel_per_steps/2)
        cv2.rectangle(image,)

    def to_image_cordinates(self,x,y):
        return (tuple(np.dot(self.cordinate_convert_matrix,np.array([x,y,1]))))

    def get_images(self):
        print(self.sensor_positions[:,0],self.sensor_positions[:,0])
        self.sensor_image = np.zeros(((np.max(self.sensor_positions[:,1])-np.min(self.sensor_positions[:,1]))*self.steps_per_mm*self.pixel_per_steps,
                                      (np.max(self.sensor_positions[:,0])-np.min(self.sensor_positions[:,0]))*self.steps_per_mm*self.pixel_per_steps),dtype=np.uint8)

        
        for i in range(self.number_of_nodes):

            try:
                self.node_images[i]=cv2.imread('ImageData/'+self.image_name.replace(str(i)),cv2.IMREAD_GRAYSCALE)
            except:
                temp=np.zeros((self.image_size_mm*self.steps_per_mm*self.pixel_per_steps+1, self.image_size_mm *
                                   self.steps_per_mm*self.pixel_per_steps+1),dtype=np.uint8)
                for angle in self.node_line_angles[i]:
                    self.draw_rect(temp,angle)
                self.node_images[i]=temp
    def show_images(self):
        for image in self.node_images:
            cv2.imshow('window',image)
            cv2.waitKey(0)
def main():
    NP=NodePreprocessor()
    NP.show_images()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    main()