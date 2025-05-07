from setuptools import setup, find_packages

setup(
    name="telegram_bot",
    version="0.1",
    packages=find_packages(),
    install_requires=["py-hanspell"],
    entry_points={
        'console_scripts': [
            'telegram_bot = telegram_bot.main:main',  # 여기에서 수정
        ]
    },
    author="lihuiruo101",
    description="봇",
    python_requires='>=3.7',
)
