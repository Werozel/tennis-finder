import setuptools

setuptools.setup(
    name="tennis_finder",
    packages=setuptools.find_packages(),
    package_dir={"tennis_finder": "tennis_finder"},
    # package_data={
    #     'tennis_finder': ['package_data.dat'],
    # },
    include_package_data=True,
)