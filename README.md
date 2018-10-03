***For easy P2pool install and auto setup of Core wallet config files including merged coins. Double click to run p2pool feature and custom web UI visit the following link:***


		https://github.com/farsider350/p2pool-oneclick/blob/dgb-scrypt-merged/README.md

		
For the experienced p2pool setup follow the guide bellow

P2pool installation with pypy -- Windows
--------------------------------------

		On Windows, pypy is only supported via the Windows Subsystem for Linux (WSL). P2pool on pypy on WSL is much faster than P2pool on
		CPython on native Windows. To install WSL, first follow the steps outlined here:

		https://msdn.microsoft.com/en-us/commandline/wsl/install_guide

		Once you've done that, run bash and follow the rest of the steps below.


P2pool installation with pypy -- Linux and Windows
-------------------------------------------------

Copy and paste the following commands one paragraph at a time into a bash shell in order to install p2pool on Windows or Linux.


		sudo apt-get update

		sudo apt-get install pypy pypy-dev pypy-setuptools gcc build-essential git

		wget https://bootstrap.pypa.io/ez_setup.py -O - | sudo pypy
		sudo rm setuptools-*.zip

		wget https://pypi.python.org/packages/source/z/zope.interface/zope.interface-4.1.3.tar.gz#md5=9ae3d24c0c7415deb249dd1a132f0f79
		tar zxf zope.interface-4.1.3.tar.gz
		cd zope.interface-4.1.3/
		sudo pypy setup.py install
		cd ..
		sudo rm -r zope.interface-4.1.3*

		wget https://pypi.python.org/packages/source/T/Twisted/Twisted-15.4.0.tar.bz2
		tar jxf Twisted-15.4.0.tar.bz2
		cd Twisted-15.4.0
		sudo pypy setup.py install
		cd ..
		sudo rm -r Twisted-15.4.0*

		git clone https://github.com/farsider350/p2pool-dgb-scrypt-350.git
		cd p2pool-dgb-scrypt-350
		cd digibyte_subsidy
		sudo pypy setup.py install
		cd ..
		cd litecoin_scrypt
		sudo pypy setup.py install    
    
	
digibyte.conf
	
		server=1
		rpcuser=user
		rpcpassword=anything long
		algo=scrypt
		listenonion=0
		listen=1
		daemon=1
		gen=0
		onlynet=IPv4
		rpcworkqueue=32
		rpcthreads=96
		rpcallowip=127.0.0.1
		rpcport=14024
		port=12026
		deprecatedrpc=accounts

Running P2Pool:
-------------------------
To use P2Pool, you must be running your own local myriadcoind. For standard configurations, using P2Pool should be as simple as:

		For Zen Server
		pypy run_p2pool.py --net digibyte
		
		If the Zen Server has no peers and throws an error, start up with 'digibyte2' and let others use 'digibyte' to connect to you.
		
		For Ilsawa's Server
		pypy run_p2pool.py --net digibyteils
	
To make your node accessible from the internet, open the following ports on your router (both the worker port and peer-2-peer port please!): Worker Port = 5025; Peer-2-Peer Port = 5024

Run for additional options:

		pypy run_p2pool.py --help

Donations towards further development:
-------------------------
BTC: 12nQSWig35Wue2AGjiGM5F2LUvSwq8uQqS
DGB: DG21rdLGRR2sMZDA1pXCrR93dKwjSz8yHo
