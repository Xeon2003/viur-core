import setuptools

setuptools.setup(
    name='viur-core',
    version='3.0.0-16',
    author="Mausbrand Informationssysteme GmbH",
    author_email="team@viur.dev",
    description="DESCR",
    packages = [f'viur.{mod}' for mod in setuptools.find_packages('.')],
    package_dir={"viur":"."},
    url="https://github.com/viur-framework/viur-core",
    install_requires = [
    "safeeval==0.0.5",
    "google-cloud-datastore==2.1.0",
    "google-cloud-logging==2.2.0",
    "google-cloud-storage==1.35.1",
    "google-cloud-tasks==2.1.0",
    "google-auth==1.24.0",
    "google-cloud-kms==2.2.0",
    "google-cloud-iam==2.1.0",

    "jinja2==2.11.3",
    "webob==1.8.6",
    "pillow==8.1.0",
    "urlfetch==1.2.2",
    "gunicorn==20.0.4"
    ],
    classifiers=[
     "Programming Language :: Python :: 3",
     "License :: OSI Approved :: MIT License",
     "Operating System :: OS Independent",
    ],
 )