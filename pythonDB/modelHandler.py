import csv
import uuid
from models import Drawings
from index import db
from sqlalchemy import *



def addNewModel(data, name):
    csvfile = 'models/' + str(uuid.uuid4()) + '.csv'
    with open(csvfile, 'wb') as file:
        filewriter = csv.writer(file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['x', 'y', 'z', 'color', 'radius'])
        for item in data:
            filewriter.writerow(item)
    drawing = Drawings(
        name=name,
        fileName=csvfile
    )
    db.session.add(drawing)
    db.session.commit()

def getAllModels():
    drawings = Drawings.query.all()
    arr = []
    for drawing in drawings:
        arr.append(drawing.name)
    return arr

def getModel(name):
    fileName = Drawings.query.filter_by(name=name).first()
    if not fileName:
        return False
    return fileName.fileName
