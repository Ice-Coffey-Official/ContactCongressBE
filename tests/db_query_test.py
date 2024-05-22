import contentGen
import createDB
from util import *

generator = contentGen.ContentGenerator()

def test_get_first():
    database = createDB.Database()
    joe = database.getFirst(name='joe biden')
    assert len(joe) == 1
    assert joe == [('Joe Biden', 'District of Columbia', 'Democrat', 'November 20, 1942', 'January 20, 2021', '1600 Pennsylvania Avenue NW, Washington, DC 20500', '(202) 456-1111', 'mailto:comments@whitehouse.gov', 'https://www.whitehouse.gov/administration/president-biden/', 'https://twitter.com/JoeBiden', 'whitehouse')]

    joe2 = database.getFirst(num = 2, name='joe biden')
    assert len(joe2) == 2
    assert joe2[1] == ('Joe Biden', 'District of Columbia', 'Democrat', 'November 20, 1942', 'January 20, 2021', '1600 Pennsylvania Avenue NW, Washington, DC 20500', '(202) 456-1111', 'mailto:comments@whitehouse.gov', 'https://www.whitehouse.gov/administration/president-biden/', 'https://twitter.com/JoeBiden', 'candidate')

def test_get_all():
    database = createDB.Database()
    joe = database.getAll(name='joe biden')
    assert len(joe) == 2
    assert joe[1] == ('Joe Biden', 'District of Columbia', 'Democrat', 'November 20, 1942', 'January 20, 2021', '1600 Pennsylvania Avenue NW, Washington, DC 20500', '(202) 456-1111', 'mailto:comments@whitehouse.gov', 'https://www.whitehouse.gov/administration/president-biden/', 'https://twitter.com/JoeBiden', 'candidate')