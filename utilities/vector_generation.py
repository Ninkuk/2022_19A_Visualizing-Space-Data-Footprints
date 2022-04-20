import math as m 
import spiceypy as spice

mapId = 64361
polyId = 64360

def get_mapcam_vectors(desired_grid_size=10):
    """This function returns the vector grid that represents the field of view of the map camera. 
    The grid_size determines the accuracy (max will be at 1024).


    Args:
        grid_size (int): Range 10-1024

    Returns:
        list: The fov vectors for the mapcam(length = grid_size ^ 2)
    """

    fov_params_map = spice.getfov(-mapId, 4) # extracting fov parameters from ik kernel

    range_x = range(0, desired_grid_size + 1, 1)
    range_y = range(0, desired_grid_size + 1, 1)

    displacement_vector_map = fov_params_map[4][2] - fov_params_map[4][0] # This represents the displacement from top left to bottom right boundary vector.

    projection_vectors_map = [] # vector list to be returned

    for xi in range_x:
        for yi in range_y:
            x_vec = fov_params_map[4][0][0] + displacement_vector_map[0] * xi / desired_grid_size # 'steps' along x axis
            y_vec = fov_params_map[4][0][1] + displacement_vector_map[1] * yi / desired_grid_size # 'steps' along y axis
            z_vec = fov_params_map[4][0][2]
            projection_vectors_map.append([x_vec,y_vec,z_vec])
    
    return projection_vectors_map

def get_polycam_vectors(desired_grid_size=10):
    """This function returns the vector grid that represents the field of view of the poly camera. 
    The grid_size determines the accuracy (max will be at 1024).


    Args:
        grid_size (int): Range 10-1024

    Returns:
        list: The fov vectors for the polycam(length = grid_size ^ 2)
    """
    
    fov_params_poly = spice.getfov(-polyId, 4) # extracting fov parameters from ik kernel

    range_x = range(0, desired_grid_size + 1, 1)
    range_y = range(0, desired_grid_size + 1, 1)

    displacement_vector_poly = fov_params_poly[4][2]- fov_params_poly[4][0]  # This represents the displacement from top left to bottom right boundary vector.

    projection_vectors_poly = [] # vector list to be returned

    for xi in range_x:
        for yi in range_y:
            x_vec = fov_params_poly[4][0][0] + displacement_vector_poly[0] * xi / desired_grid_size # 'steps' along x axis
            y_vec = fov_params_poly[4][0][1] + displacement_vector_poly[1] * yi / desired_grid_size # 'steps' along y axis
            z_vec = fov_params_poly[4][0][2]
            projection_vectors_poly.append([x_vec,y_vec,z_vec])


def get_rectangular_boundary(projection_vectors, desired_grid_size=10):
  range_x = range(0, desired_grid_size + 1, 1)
  range_y = range(0, desired_grid_size + 1, 1)

  rectangular_boundary_vectors = []

  count = 0

  for xi in range_x:
    for yi in range_y:
      if xi == desired_grid_size or xi == 0 or yi == desired_grid_size or yi == 0:
       rectangular_boundary_vectors.append(projection_vectors[count])
      count = count + 1

  return rectangular_boundary_vectors
