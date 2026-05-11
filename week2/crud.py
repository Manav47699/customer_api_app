import logging
import models

logger = logging.getLogger(__name__)


#CREATE C
def create_customer(db, customer_data):
    logger.info("Adding new customer")
    db_obj = models.Customer(**customer_data.dict()) #unpacks the Pydantic schema dictionary into keyword arguments
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

#READ R
#skip (how many rows to skip), limit (how many rows to read at once). They are mainly used for PAGINATION
def get_customers(db, skip=0, limit=100):
    logger.info(f"Reading customers: skip={skip}, limit={limit}")
    return db.query(models.Customer).offset(skip).limit(limit).all()

# this function is the main FETCHING function.
def get_customer(db, id):
    logger.info(f"Reading customer #{id}")
    return db.query(models.Customer).get(id)

#UPDATE U
def update_customer(db, id, data):
    logger.info(f"Updating customer #{id}")
    db_obj = get_customer(db, id)
    if db_obj:
# this line loops through every key (k) and value (v) in the data dictionary and uses setattr to dynamically update each matching attribute on the database object.
        for k, v in data.dict().items(): setattr(db_obj, k, v)

        db.commit()
    return db_obj

#DELETE D
def delete_customer(db, id):
    logger.info(f"Deleting customer #{id}")
    db_obj = get_customer(db, id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
        return True
    return False