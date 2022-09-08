import setuptools

make_package=setuptools.setup(
    name="metal_rust_detection",
    version="0.1",
    author=["rohan"],
    description=("a simple rust detection technique using opencv tool which detects paricular rust from an image"),
    license="MIT",
   packages = setuptools.find_packages(where="src"), python_requires='>=3.6',
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    
    )
    