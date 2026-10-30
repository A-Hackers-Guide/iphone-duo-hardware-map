# `ACCMediaLibraryUpdateItem`

- Image: [`/System/Library/PrivateFrameworks/AccessoryMediaLibrary.framework/AccessoryMediaLibrary`](../userland/System__Library__PrivateFrameworks__AccessoryMediaLibrary.framework__AccessoryMediaLibrary.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 25 instance variables, 25 properties, 55 instance methods, 0 class methods

## Instance variables

```
B _partOfCompilation;
B _local;
S _albumTrackNumber;
S _albumTrackCount;
S _albumDiscNumber;
S _albumDiscCount;
S _chapterCount;
i _type;
i _rating;
I _duration;
Q _validMask;
@"NSString" _mediaLibraryUID;
@"NSString" _revision;
Q _persistentID;
@"NSString" _title;
Q _albumPersistentID;
@"NSString" _albumTitle;
Q _artistPersistentID;
@"NSString" _artist;
Q _albumArtistPersistentID;
@"NSString" _albumArtist;
Q _genrePersistentID;
@"NSString" _genre;
Q _composerPersistentID;
@"NSString" _composer;
```

## Properties

```
@property (T@"NSString",&,V_mediaLibraryUID) mediaLibraryUID;
@property (T@"NSString",&,V_revision) revision;
@property (TQ,V_persistentID) persistentID;
@property (TQ,R,V_validMask) validMask;
@property (T@"NSString",&,V_title) title;
@property (Ti,V_type) type;
@property (Ti,V_rating) rating;
@property (TI,V_duration) duration;
@property (TQ,V_albumPersistentID) albumPersistentID;
@property (T@"NSString",&,V_albumTitle) albumTitle;
@property (TS,V_albumTrackNumber) albumTrackNumber;
@property (TS,V_albumTrackCount) albumTrackCount;
@property (TS,V_albumDiscNumber) albumDiscNumber;
@property (TS,V_albumDiscCount) albumDiscCount;
@property (TQ,V_artistPersistentID) artistPersistentID;
@property (T@"NSString",&,V_artist) artist;
@property (TQ,V_albumArtistPersistentID) albumArtistPersistentID;
@property (T@"NSString",&,V_albumArtist) albumArtist;
@property (TQ,V_genrePersistentID) genrePersistentID;
@property (T@"NSString",&,V_genre) genre;
@property (TQ,V_composerPersistentID) composerPersistentID;
@property (T@"NSString",&,V_composer) composer;
@property (TB,V_partOfCompilation) partOfCompilation;
@property (TB,V_local) local;
@property (TS,V_chapterCount) chapterCount;
```

## Instance methods

```
-[ACCMediaLibraryUpdateItem local];
-[ACCMediaLibraryUpdateItem setGenre:];
-[ACCMediaLibraryUpdateItem albumArtistPersistentID];
-[ACCMediaLibraryUpdateItem albumArtist];
-[ACCMediaLibraryUpdateItem genrePersistentID];
-[ACCMediaLibraryUpdateItem persistentID];
-[ACCMediaLibraryUpdateItem albumPersistentID];
-[ACCMediaLibraryUpdateItem rating];
-[ACCMediaLibraryUpdateItem setRating:];
-[ACCMediaLibraryUpdateItem revision];
-[ACCMediaLibraryUpdateItem setLocal:];
-[ACCMediaLibraryUpdateItem setChapterCount:];
-[ACCMediaLibraryUpdateItem debugDescription];
-[ACCMediaLibraryUpdateItem validMask];
-[ACCMediaLibraryUpdateItem composerPersistentID];
-[ACCMediaLibraryUpdateItem albumTrackCount];
-[ACCMediaLibraryUpdateItem artist];
-[ACCMediaLibraryUpdateItem composer];
-[ACCMediaLibraryUpdateItem genre];
-[ACCMediaLibraryUpdateItem artistPersistentID];
-[ACCMediaLibraryUpdateItem duration];
-[ACCMediaLibraryUpdateItem setType:];
-[ACCMediaLibraryUpdateItem type];
-[ACCMediaLibraryUpdateItem title];
-[ACCMediaLibraryUpdateItem setComposer:];
-[ACCMediaLibraryUpdateItem description];
-[ACCMediaLibraryUpdateItem setTitle:];
-[ACCMediaLibraryUpdateItem setDuration:];
-[ACCMediaLibraryUpdateItem albumTrackNumber];
-[ACCMediaLibraryUpdateItem chapterCount];
-[ACCMediaLibraryUpdateItem setArtist:];
-[ACCMediaLibraryUpdateItem setAlbumArtist:];
-[ACCMediaLibraryUpdateItem setAlbumPersistentID:];
-[ACCMediaLibraryUpdateItem setRevision:];
-[ACCMediaLibraryUpdateItem setPersistentID:];
-[ACCMediaLibraryUpdateItem albumTitle];
-[ACCMediaLibraryUpdateItem setAlbumTitle:];
-[ACCMediaLibraryUpdateItem copyDict];
-[ACCMediaLibraryUpdateItem albumDiscNumber];
-[ACCMediaLibraryUpdateItem mediaLibraryUID];
-[ACCMediaLibraryUpdateItem albumDiscCount];
-[ACCMediaLibraryUpdateItem fillStruct:];
-[ACCMediaLibraryUpdateItem initWithMediaLibrary:dict:];
-[ACCMediaLibraryUpdateItem initWithMediaLibrary:persistentID:revision:];
-[ACCMediaLibraryUpdateItem partOfCompilation];
-[ACCMediaLibraryUpdateItem setAlbumArtistPersistentID:];
-[ACCMediaLibraryUpdateItem setAlbumDiscCount:];
-[ACCMediaLibraryUpdateItem setAlbumDiscNumber:];
-[ACCMediaLibraryUpdateItem setAlbumTrackCount:];
-[ACCMediaLibraryUpdateItem setAlbumTrackNumber:];
-[ACCMediaLibraryUpdateItem setArtistPersistentID:];
-[ACCMediaLibraryUpdateItem setComposerPersistentID:];
-[ACCMediaLibraryUpdateItem setGenrePersistentID:];
-[ACCMediaLibraryUpdateItem setMediaLibraryUID:];
-[ACCMediaLibraryUpdateItem setPartOfCompilation:];
```
