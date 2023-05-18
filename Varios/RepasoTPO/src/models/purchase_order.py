
class PurchaseOrder:

    def __init__(self, purchase_date, ISBN, user_id, full_address) -> None:
        self.purchase_date = purchase_date
        self.ISBN = ISBN
        self.user_id = user_id
        self.full_address = full_address
