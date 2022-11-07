<span style = "color:lightblue">PyTorch</span> is a machine learning framework based on the Torch library. It can be used for machine learning applications, such as computer vision and natural language processing (NLP).

# Windows
PyTorch can be installed on Windows distributions. **It is recommended that the Windows system has an NVIDIA GPU in order to harness the full power of PyTorch's CUDA support**.

1. Navigate to the [PyTorch installation website](https://pytorch.org/get-started/locally/).
2. Determine the following specifications.
	1. PyTorch build: `1.12.1`
	2. OS: `Windows`
	3. Package Manager: Anaconda
	4. Compute Platform: CUDA `11.6` (NVIDIA GPUs)
3. Download the CUDA Toolkit with the **correct version**. Navigate to [this link](https://developer.nvidia.com/cuda-toolkit-archive) for an archive of CUDA versions.
4. Install the required packages into an environment as given by the PyTorch website: `conda install pytorch torchvision torchaudio cudatoolkit=11.6 -c pytorch -c conda-forge`

# Speed Demonstration
GPU acceleration works by heavy parallelization of computation. There are many cores in a GPU, but each core is not powerful. The code example below demonstrates the difference in computational speeds for increasingly parallel tasks.

```python
import torch
import time

ARR_SIZE = 4

print(torch.cuda.is_available()) # True

# specify the GPU device
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

for i in range(0, 5):
	# calculate size as power of 10
	n = 4 * (10 ** i)

	# calculate CPU time
	cpu_start = time.time()
	cpu_array = torch.ones(n, n)
	for _ in range(1000):
		cpu_array += cpu_array
	print("CPU Time ({}): {}".format(n, time.time() - cpu_start))

	# calculate GPU time
	gpu_start = time.time()
	gpu_array = torch.ones(n, n).to(device) # send to GPU
	for _ in range(1000):
		gpu_array += gpu_array
	print("GPU Time ({}): {}".format(n, time.time() - gpu_start))
```

The output of the above code block is shown below.

```text
CPU Time (4): 0.003499746322631836
GPU Time (4): 0.00500035285949707

CPU Time (40): 0.0015006065368652344
GPU Time (40): 0.004498958587646484

CPU Time (400): 0.006999492645263672
GPU Time (400): 0.005000591278076172

CPU Time (4000): 4.817999839782715
GPU Time (4000): 0.021498680114746094

CPU Time (40000): 485.8700020313263
GPU Time (40000): 4.476001501083374
```

Thus, parallel computations are faster on the GPU.

# Modular Programming
In PyTorch, neural networks, regardless of their complexity, are built by basic building blocks of modules. Some exemplar modules are shown below.

```python
import torch.nn as nn

# linear module
model = nn.Linear()

# a module of modules
model = nn.Sequential(...)
```

A model can be a singular module or can be comprised of multiple modules. With this, a **customized** model (e.g., flatten layer in [[Convolutional Neural Networks|CNNs]] to vectorize matrices) can be built regardless of whether a layer that achieves a certain function exists.