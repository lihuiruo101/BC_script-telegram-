from setuptools import setup, find_packages

setup(
    name="telegram_bot",
    version="0.1",
    packages=find_packages(),
    install_requires=["py-hanspell"],
    entry_points={
        'console_scripts': [
            'spcheck = spcheck.__main__:main',
        ]
    },
    author="lihuiruo101",
    description="봇",
    python_requires='>=3.7',
)
