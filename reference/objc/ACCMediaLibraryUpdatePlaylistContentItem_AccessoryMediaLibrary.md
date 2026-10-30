# `ACCMediaLibraryUpdatePlaylistContentItem`

- Image: [`/System/Library/PrivateFrameworks/AccessoryMediaLibrary.framework/AccessoryMediaLibrary`](../userland/System__Library__PrivateFrameworks__AccessoryMediaLibrary.framework__AccessoryMediaLibrary.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 25 instance methods, 0 class methods

## Instance variables

```
Q _validMask;
@"NSString" _mediaLibraryUID;
Q _playlistPersistentID;
Q _persistentID;
@"NSString" _title;
@"NSString" _albumTitle;
@"NSString" _artist;
@"NSString" _albumArtist;
@"NSString" _genre;
@"NSString" _composer;
```

## Properties

```
@property (T@"NSString",&,V_mediaLibraryUID) mediaLibraryUID;
@property (TQ,V_playlistPersistentID) playlistPersistentID;
@property (TQ,R,V_validMask) validMask;
@property (TQ,V_persistentID) persistentID;
@property (T@"NSString",&,V_title) title;
@property (T@"NSString",&,V_albumTitle) albumTitle;
@property (T@"NSString",&,V_artist) artist;
@property (T@"NSString",&,V_albumArtist) albumArtist;
@property (T@"NSString",&,V_genre) genre;
@property (T@"NSString",&,V_composer) composer;
```

## Instance methods

```
-[ACCMediaLibraryUpdatePlaylistContentItem setGenre:];
-[ACCMediaLibraryUpdatePlaylistContentItem albumArtist];
-[ACCMediaLibraryUpdatePlaylistContentItem persistentID];
-[ACCMediaLibraryUpdatePlaylistContentItem debugDescription];
-[ACCMediaLibraryUpdatePlaylistContentItem validMask];
-[ACCMediaLibraryUpdatePlaylistContentItem artist];
-[ACCMediaLibraryUpdatePlaylistContentItem composer];
-[ACCMediaLibraryUpdatePlaylistContentItem genre];
-[ACCMediaLibraryUpdatePlaylistContentItem title];
-[ACCMediaLibraryUpdatePlaylistContentItem setComposer:];
-[ACCMediaLibraryUpdatePlaylistContentItem description];
-[ACCMediaLibraryUpdatePlaylistContentItem setTitle:];
-[ACCMediaLibraryUpdatePlaylistContentItem setArtist:];
-[ACCMediaLibraryUpdatePlaylistContentItem setAlbumArtist:];
-[ACCMediaLibraryUpdatePlaylistContentItem setPersistentID:];
-[ACCMediaLibraryUpdatePlaylistContentItem albumTitle];
-[ACCMediaLibraryUpdatePlaylistContentItem playlistPersistentID];
-[ACCMediaLibraryUpdatePlaylistContentItem setPlaylistPersistentID:];
-[ACCMediaLibraryUpdatePlaylistContentItem setAlbumTitle:];
-[ACCMediaLibraryUpdatePlaylistContentItem mediaLibraryUID];
-[ACCMediaLibraryUpdatePlaylistContentItem copyNSRepresentation:];
-[ACCMediaLibraryUpdatePlaylistContentItem fillStruct:];
-[ACCMediaLibraryUpdatePlaylistContentItem initWithMediaLibrary:persistentID:playlistPersistentID:];
-[ACCMediaLibraryUpdatePlaylistContentItem initWithMediaLibrary:playlistPersistentID:dict:];
-[ACCMediaLibraryUpdatePlaylistContentItem setMediaLibraryUID:];
```
