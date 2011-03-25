CREATE TABLE forum_mysqlftsindex (
	id int NOT NULL AUTO_INCREMENT,
	node_id int NOT NULL UNIQUE,
	title varchar(300) NOT NULL,
	body longtext NOT NULL,
	tagnames varchar(125) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (node_id) REFERENCES forum_node (id)   ON UPDATE CASCADE ON DELETE CASCADE,
	FULLTEXT (title, body, tagnames)
) ENGINE=`MyISAM`;

CREATE TRIGGER fts_on_insert AFTER INSERT ON forum_node
  FOR EACH ROW
  BEGIN
    INSERT INTO forum_mysqlftsindex (node_id, title, body, tagnames) VALUES (NEW.id, NEW.title, NEW.body, NEW.tagnames);
  END;

CREATE TRIGGER fts_on_update AFTER UPDATE ON forum_node
  FOR EACH ROW
  BEGIN
    UPDATE forum_mysqlftsindex SET title = NEW.title, body = NEW.body, tagnames = NEW.tagnames WHERE node_id = NEW.id;
  END;

INSERT INTO forum_mysqlftsindex (node_id, title, body, tagnames) SELECT id, title, body, tagnames FROM forum_node;