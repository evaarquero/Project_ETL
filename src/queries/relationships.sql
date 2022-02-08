ALTER TABLE `Spotify`.`rank_streamed_artists` 
ADD COLUMN `past_concerts_int_artist` INT(11) NOT NULL AFTER `last_update`,
ADD COLUMN `upcoming_concerts_int_artist` INT(11) NOT NULL AFTER `past_concerts_int_artist`,
ADD COLUMN `spotify_info_name` VARCHAR(50) NOT NULL AFTER `upcoming_concerts_int_artist`,
DROP PRIMARY KEY,
ADD PRIMARY KEY (`streaming_rank`, `past_concerts_int_artist`, `upcoming_concerts_int_artist`, `spotify_info_name`),
ADD INDEX `fk_rank_streamed_artists_past_concerts_idx` (`past_concerts_int_artist` ASC) VISIBLE,
ADD INDEX `fk_rank_streamed_artists_upcoming_concerts1_idx` (`upcoming_concerts_int_artist` ASC) VISIBLE,
ADD INDEX `fk_rank_streamed_artists_spotify_info1_idx` (`spotify_info_name` ASC) VISIBLE;

ALTER TABLE `Spotify`.`rank_streamed_artists` 
ADD CONSTRAINT `fk_rank_streamed_artists_past_concerts`
  FOREIGN KEY (`past_concerts_int_artist`)
  REFERENCES `Spotify`.`past_concerts` (`int_artist`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_rank_streamed_artists_upcoming_concerts1`
  FOREIGN KEY (`upcoming_concerts_int_artist`)
  REFERENCES `Spotify`.`upcoming_concerts` (`int_artist`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_rank_streamed_artists_spotify_info1`
  FOREIGN KEY (`spotify_info_name`)
  REFERENCES `Spotify`.`spotify_info` (`name`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION