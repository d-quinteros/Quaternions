import numpy as np

class Quaternion:
    """
    A class representing an quaternion.
 
    Attributes:
        w (float): a scalar that stores the rotation around the axis (x,y,z) in radians, counterclockwise.
        x (float): the x component of the axis of roation.
        y (float): the y component of the axis of roation.
        z (float): the z component of the axis of roation.
    """
    def __init__(self, w, x, y, z):
        """
        Initializes a Quaternion object.
 
        Parameters:
            w (float): a scalar that stores the rotation around the axis (x,y,z) in radians, counterclockwise.
            x (float): the x-component of the axis of roation.
            y (float): the y-component of the axis of roation.
            z (float): the z-component of the axis of roation.
        """
        self.quat = np.array([w, x, y, z], dtype=np.float64)

    @property
    def w(self):
        """
        Returns the scalar (real) part (w) of the quaternion.

        Returns:
            w (float): The scalar (real) part of the quaternion.
        """
        return self.quat[0]

    @property
    def x(self):
        """
        Returns the first element (x-component) of the quaternion's vector part.

        Returns:
            x (float): The x-component of the quaternion's vector part.
        """
        return self.quat[1]

    @property
    def y(self):
        """
        Returns the second element (y-component) of the quaternion's vector part.

        Returns:
            y (float): The y-component of the quaternion's vector part.
        """
        return self.quat[2]

    @property
    def z(self):
        """
        Returns the third element (z-component) of the quaternion's vector part.

        Returns:
            z (float): The z-component of the quaternion's vector part.
        """
        return self.quat[3]

    def normalize(self):
        """
        Normalizes the quaternion to unit length.
        """
        norm = np.linalg.norm(self.quat)
        if norm != 0:
            self.quat /= norm

    def conjugate(self):
        """
        Returns the conjugate of the quaternion.

        Returns:
            Quaternion: Result of the conjugation operation.
        """
        return Quaternion(self.w, -self.x, -self.y, -self.z)

    def __mul__(self, other):
        """
        Implements multiplication (*) operation for Quaternions.

        Performs quaternion multiplication with another quaternion or scalar value.

        Args:
            other (Quaternion or int or float): The object to multiply with.

        Returns:
            Quaternion: Result of the multiplication operation.
        """
        if isinstance(other, Quaternion):
            w = self.w * other.w - self.x * other.x - self.y * other.y - self.z * other.z
            x = self.w * other.x + self.x * other.w + self.y * other.z - self.z * other.y
            y = self.w * other.y - self.x * other.z + self.y * other.w + self.z * other.x
            z = self.w * other.z + self.x * other.y - self.y * other.x + self.z * other.w
            return Quaternion(w, x, y, z)
        elif isinstance(other, (int, float)):
            return Quaternion(self.w * other, self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError("Multiplication not supported with given type.")

    def rotate_point(self, point):
        """
        Rotate a 3D point using quaternion rotation.

        Args:
            point (list): 3D coordinate [x, y, z] to be rotated.

        Returns:
            roated_p (Quaternion): Rotated 3D coordinate as a quaternion. The coordinates of the rotated point are in the x, y, and z components
        """
        if len(point) != 3:
            raise ValueError("Point must be a 3D coordinate (x, y, z).")
        p_quat = Quaternion(0, point[0], point[1], point[2])
        rotated_p = self * p_quat * self.conjugate()
        return rotated_p