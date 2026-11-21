from setuptools import setup

package_name = "rover_mission"

setup(
    name=package_name,
    version="0.1.0",
    packages=[package_name],
    data_files=[
        (
            "share/ament_index/resource_index/packages",
            ["resource/" + package_name],
        ),
        ("share/" + package_name, ["package.xml"]),
        ("share/" + package_name + "/config", ["config/waypoints_demo.yaml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Rover Team",
    maintainer_email="rover@example.com",
    description="Mission orchestration for the rover mini demo.",
    license="Proprietary",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "mission_node = rover_mission.mission_node:main",
        ],
    },
)
