from database.DB_connect import DBConnect
from model.connessione import Connessione
from model.state import State


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllYears():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """
                    SELECT distinct SUBSTRING(datetime, 1, 4) as year
                    FROM sighting s 
                    where `datetime` > '1909-03-15 23:59:59.999'
                    and `datetime` < '2015-01-01 00:00:00.000'
                    order by `datetime` asc
                """

        cursor.execute(query)

        for row in cursor:
            result.append(row["year"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllForme():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """
                    SELECT DISTINCT s.shape
                    from sighting s 
                    where shape != ""
                    order by shape asc
                """

        cursor.execute(query)

        for row in cursor:
            result.append(row["shape"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllStates():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """
                    SELECT *
                    from state s
                """

        cursor.execute(query)

        for row in cursor:
            result.append(State(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllNeighbours(idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """
                    SELECT *
                    from neighbor n 
                    where state1 < state2
                    order by state1 asc
                """

        cursor.execute(query)

        for row in cursor:
            result.append((idMap[row["state1"]], idMap[row["state2"]]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllPeso(idMap, forma, anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """
                    SELECT tb1.stateId as s1, tb2.stateId as s2, sum(tb1.N + tb2.N) as N
                    FROM (
                    SELECT UPPER(state) as stateId, count(*) as N
                    FROM sighting s 
                    WHERE shape = %s
                    and SUBSTRING(datetime, 1, 4) = %s
                    group by state
                    ) as tb1,
                    (SELECT UPPER(state) as stateId, count(*) as N
                    FROM sighting s 
                    WHERE shape = %s
                    and SUBSTRING(datetime, 1, 4) = %s
                    group by state) as tb2
                    where tb1.stateId < tb2.stateId
                    group by tb1.stateId , tb2.stateId
                """

        cursor.execute(query, (forma, anno, forma, anno))

        for row in cursor:
            result.append(Connessione(**row))

        cursor.close()
        conn.close()
        return result
