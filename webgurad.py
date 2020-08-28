# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

"""
This example shows how to make simple web authentication.

To run the example:
    $ python webguard.py

When you visit http://127.0.0.1:8889/, the page will ask for an username &
password. See the code in main() to get the correct username & password!
"""

import sys

from zope.interface import implementer

from twisted.python import log
from twisted.internet import reactor
from twisted.web import server, resource, guard
from twisted.web.static import File
from twisted.cred.portal import IRealm, Portal
from twisted.cred.checkers import InMemoryUsernamePasswordDatabaseDontUse


# webpage child class
class WebRoot(resource.Resource):
    pass
    
    # def getChild(self, name, request):
    #     if name == '':
    #         return self
    #     # elif name == 'foo':
    #     return resource.Resource.getChild(self, name, request)
    #     # else:
    #     #     return File(name)

    # def render_GET(self, request):
    #     return "Hello, world! I am located at %r." % (request.path,)


web_root = WebRoot()

fileDirRoot = File('/var/www/twisted_web1')
fileDir = File('/var/www/user/public_html')
fileDir1 = File('/var/www/user1/public_html')
# todo: Check why site.domain// got double //
web_root.putChild('',fileDirRoot) # Site root
web_root.putChild('user', fileDir)
web_root.putChild('user1', fileDir1)


@implementer(IRealm)
class SimpleRealm(object):
    """
    A realm which gives out L{GuardedResource} instances for authenticated
    users.
    """

    def requestAvatar(self, avatarId, mind, *interfaces):
        root = resource.IResource
        if root in interfaces:
            return resource.IResource, web_root, lambda: None
        raise NotImplementedError()


def main():
    # log
    log.startLogging(sys.stdout)

    checkers = [InMemoryUsernamePasswordDatabaseDontUse(joe='blow')]

    portal = Portal(SimpleRealm(), checkers)

    credFactory = [guard.DigestCredentialFactory('md5', 'example.com')]

    wrapper = guard.HTTPAuthSessionWrapper(portal, credFactory)

    factory = server.Site(resource=wrapper)

    reactor.listenTCP(8889, factory)

    reactor.run()


if __name__ == '__main__':
    main()
