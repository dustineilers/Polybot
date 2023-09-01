import setup from setuptools

setup(
    name='polybot',
    version='1.0',
    description='a translation discord bot',
    author='dustin eilers',
    author_email='eilersd23@gmail.com',
    install_requires=[
        'async-timeout==4.0.3',
        'colorama==0.4.6',
        'deepl==1.15.0',
        'discord==2.3.2',
        'discord.py==2.3.2',
        'emoji==2.8.0',
        'python-dotenv==1.0.0'
    ]
)