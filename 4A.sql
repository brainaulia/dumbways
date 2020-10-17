-- Insert data ke tabel Genre
INSERT INTO Genre (name)
VALUES
('POP'),
('Rock'),
('Jazz'),
('Blues'),
('Dangdut');

-- Insert data ke tabel Singers
INSERT INTO Singers (name)
VALUES
('Noah'),
('Payung Teduh'),
('Via Vallen'),
('Raissa'),
('Tulus');

-- Insert data ke tabel Music
INSERT INTO Music(title,durasi,id_genre,id_singer,deskripsi)
VALUES
('Separuh Aku','3.21',1,1,'Lagu Indonesia'),
('Akad','3.15',1,2,'Lagu Indonesia'),
('Sayang','3.40',5,3,'Lagu Indonesia'),
('Firasat','3.33',1,4,'Lagu Indonesia'),
('Gajah','3.52',1,5,'Lagu Indonesia');


-- Tampilkan Semua Music
SELECT * FROM Music;



-- tampilkan music per genre beserta singers, field ditampilkan title music, 
-- durasi music, name genre, name singer, image music, deskripsi music

SELECT Music.title,Music.durasi,Genre.name as Genre,Singers.name as Singer,Music.deskripsi FROM Music
JOIN Genre on Genre.id = Music.id_genre
JOIN Singers on Singers.id = Music.id_singer
ORDER BY Singer,Genre;


 -- tampilan detail music berdasarkan id
 SELECT * FROM Music ORDER BY id ASC;
