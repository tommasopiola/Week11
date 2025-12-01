from database import DAO

results = DAO.read_objects()
print(results)
print(len(results))