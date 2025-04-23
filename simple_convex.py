import cvxpy as cp
import numpy as np
import logging
import os

# Setup logging ke folder .logfile
log_dir = ".logfile"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(log_dir, "least_squares.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Program started")

# Data: matrix A dan vector b
np.random.seed(42)
A = np.random.randn(5, 3)
b = np.random.randn(5)

logging.info(f"A =\n{A}")
logging.info(f"b = {b}")

# Variabel optimasi
x = cp.Variable(3)

# Fungsi objektif: minimize ||Ax - b||^2
objective = cp.Minimize(cp.sum_squares(A @ x - b))

# Tanpa constraint
problem = cp.Problem(objective)

# Selesaikan
result = problem.solve()

# Output hasil
print("Hasil x optimal:")
print(x.value)

logging.info(f"x optimal = {x.value}")
logging.info(f"nilai minimum = {result}")
