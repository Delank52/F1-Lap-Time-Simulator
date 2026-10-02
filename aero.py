'''
Aero file, will be used to store the basic aerodynamic force model.
(Aerodynamic drag equation: F = 1/2 * rho * v^2 * C * A) (Cd for drag and Cl for downforce)
Where: rho = air density, v = velocity, C = drag coefficient, A = frontal area

    Assumptions:
        - Speed is relative the air.
        - Downforce is positive in the downward direction. Drag is positive in the direction of motion.
        - Coefficients are constant for the chosen setup.

This file calculates the aerodynamic forces acting on the car.
'''

def calc_downforce(speed_mps: float, air_density: float, reference_area: float, downforce_coefficient: float) -> float:

    if speed_mps < 0:
        raise ValueError("Speed must be non-negative.")
    if reference_area <= 0:
        raise ValueError("Reference area must be positive.")

    dynamic_pressure = 0.5*air_density*speed_mps**2  # Calculates dynamic pressure (N/m^2)
    
    downforce = dynamic_pressure*downforce_coefficient*reference_area  # Calculates downforce (N)
    
    return downforce


def calc_drag(speed_mps: float, air_density: float, reference_area: float, drag_coefficient: float) -> float:

    if speed_mps < 0 or air_density < 0 or drag_coefficient < 0:
        raise ValueError("Speed, air density, and drag coefficient must be non-negative.")
    if reference_area <= 0:
        raise ValueError("Reference area must be positive.")

    dynamic_pressure = 0.5*air_density*speed_mps**2  # Calculates dynamic pressure (N/m^2)
    
    drag = dynamic_pressure*drag_coefficient*reference_area  # Calculates drag (N)
    
    return drag



