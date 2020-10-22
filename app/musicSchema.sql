create table Artist (
    id	            integer primary key autoincrement,
    artistName      varchar(64) not null,
    bio             varchar(200) not null
);

create table Album (
	id		        integer primary key autoincrement,
    albumName       varchar(64) not null,
    albumArtist     varchar(64) not null,
    foreign key (albumArtist) references Artist(artistName)
);

create table Song (
	id	          integer primary key autoincrement,
	songName      varchar(64) not null,
	songArtist    varchar(64) not null,
	songAlbum     varchar(64) not null,
	foreign key (songArtist) references Artist(artistName),
	foreign key (songAlbum) references Album(albumName)
);

