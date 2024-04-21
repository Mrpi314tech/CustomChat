from setuptools import setup, find_packages

setup(
    name='CustomChat',
    version='1.0.9',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4'
    ],
    # other metadata
    author='Mrpi314tech',
    author_email='123scoring@gmail.com',
    description="CustomChat: An AI-powered chatbot with easy customization. Powered by a simple but effective Python AI, it opens websites, executes commands, and delivers tailored responses. Enhance your projects with CustomChat's versatility and adaptability.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Mrpi314tech/CustomChat',
    classifiers=[
        'Programming Language :: Python :: 3',
        # other classifiers
    ],
)
