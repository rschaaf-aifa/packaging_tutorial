import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-rschaaf-aifa",
    version="0.0.1",
    author="Reinhold Schaaf",
    author_email="rschaaf@astro.uni-bonn.de",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url = "https://github.com/rschaaf-aifa/packaging_tutorial",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)","
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
