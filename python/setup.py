from setuptools import setup, find_packages

setup(
    name='terminalchatrobot',
    version='0.1.0',
    keywords=('terminal', 'chat', 'robot'),
    description='It is a terminal robot which can chat with you.',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    license='MIT License',
    install_requires=['requests'],

    entry_points={
        'console_scripts': [
            'terminalchatrobot = terminalchatrobot.terminalchatrobot:main'
        ]
    },

    author='xingbofeng',
    author_email='503908971@qq.com',

    packages=find_packages(),
    platforms='any',
)
