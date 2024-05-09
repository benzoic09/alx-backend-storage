-- script that creates a trigger that decreases the 
-- quantity of an item after adding a new order.

CREATE TRIGGER decrease_quantity_after_order
AFTER INSERT ON orders
FOR EACH ROW
		UPDATE items
		SET quantity = quantity - NEW.quantity
		WHERE item_id = NEW.item_id;
