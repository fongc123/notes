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

```

