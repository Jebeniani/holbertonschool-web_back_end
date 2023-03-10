-- creating a table users with specified requirements
CREATE TRIGGER decrement AFTER INSERT ON orders
FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE NAME = NEW.item_id;
