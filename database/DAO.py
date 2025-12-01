from database.DB_connect import DBConnect
from model.object import Object
from model.connessione import Connessione

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def readConnessioni(objects_dict):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = ''' SELECT eo1.object_id AS o1, eo2.object_id AS o2, COUNT(*) AS peso
                    FROM exhibition eo1, exhibition eo2
                    WHERE eo1.id_exhibition = eo2.id_exhibition
                    AND eo2.id_exhibition < eo1.id_exhibition
                    GROUP BY eo1.id_exhibition, eo2.id_exhibition'''

        cursor.execute(query)

        for row in cursor:
            o1 = objects_dict[row['o1']]
            o2 = objects_dict[row['o2']]
            peso = row['peso']
            result.append(Connessione(o1, o2, peso))

        cursor.close()
        conn.close()
        return result