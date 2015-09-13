from setuptools import setup

setup(
    name='navinur',
    version='0.1',
    install_requires=[
        'django >= 1.8',
        'pyproj',
        'gunicorn',
        'psycopg2',
        # 'mapnik >= 2.0',
        'dj-static >= 0.0.6',
    ]
)