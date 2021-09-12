from setuptools import setup, find_packages

# FUNÇÃO PARA NÃO TER QUE ESCREVER TODOS OS REQUISITOS NO: 'install_requires' E NO 'extra_require'

def read(filename): 
    return [
         # RETIRA O \n DE CADA REQUISITO 
        req.strip()
         for req
         # RETORNA TODOS OS REQUISITOS
         in open(filename).readlines() 
         
         ]

setup(
    name = 'eat_it_delivery',
    version = '0.1.0',
    description = 'Delivery Application',
    packages = find_packages(),
    include_package_date = True,
    install_requires = read('requirements.txt'),
    extra_require = {
        "dev": read("requirements-dev.txt")
    }
)