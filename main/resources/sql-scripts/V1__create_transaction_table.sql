CREATE TABLE IF NOT EXISTS generate_transaction_id (

	`id` bigint(10) unsigned NOT NULL auto_increment,
	`sequence_name` char(12) NOT NULL default '',
	PRIMARY KEY (`id`),
	UNIQUE KEY transaction_id_sequence_name (`sequence_name`)

)