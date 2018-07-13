''' A ViewHelperProvider Service Provider '''
from masonite.provider import ServiceProvider

class ViewHelperProvider(ServiceProvider):

    wsgi = False

    def register(self):
        pass

    def boot(self, ViewClass):

        ViewClass.share({
            'show_if': self.show_if
        })
    
    def show_if(self, statement1, statement2, output):
        if statement1 == statement2:
            return output
        
        return ''
