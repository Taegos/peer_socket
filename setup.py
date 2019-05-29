import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="peer_socket",
    version="0.0.1",
    author="Benjamin Fischer",
    author_email="benjamin.fischr@gmail.com",
    description="Peer socket",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Taegos/peer_socket",
    download_url="https://github.com/Taegos/peer_socket/archive/0.0.1.tar.gz",
    packages=setuptools.find_packages(),
    install_requires=["jsonpickle"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)