from orator.seeds import Seeder
from app.Tag import Tag


class TagTableSeeder(Seeder):

    def run(self):
        tags = ['All', 'Architecture', 'Authentication', 'Jinja', 'Cache', 'Configuration',
                'Database', 'ORM', 'Orator', 'Forms', 'Installation', 'Jobs', 'Mail', 'Packages',
                'Queues', 'Requests', 'Security', 'Session', 'Testing', 'Validation', 'Views']
        
        for tag in tags:
            Tag.first_or_create(name=tag)
