# `ACCMediaLibraryUpdatePlaylist`

- Image: [`/System/Library/PrivateFrameworks/AccessoryMediaLibrary.framework/AccessoryMediaLibrary`](../userland/System__Library__PrivateFrameworks__AccessoryMediaLibrary.framework__AccessoryMediaLibrary.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 13 properties, 31 instance methods, 0 class methods

## Instance variables

```
B _folder;
B _geniusMix;
B _radioStation;
B _smartPlaylist;
S _radioStationOrdering;
i _contentStyle;
Q _validMask;
@"NSString" _mediaLibraryUID;
@"NSString" _revision;
Q _persistentID;
@"NSString" _name;
Q _parentPersistentID;
@"ACCMediaLibraryUpdatePlaylistContent" _content;
```

## Properties

```
@property (T@"NSString",&,V_mediaLibraryUID) mediaLibraryUID;
@property (T@"NSString",&,V_revision) revision;
@property (TQ,V_persistentID) persistentID;
@property (TQ,R,V_validMask) validMask;
@property (T@"NSString",&,V_name) name;
@property (TQ,V_parentPersistentID) parentPersistentID;
@property (TB,V_folder) folder;
@property (TB,V_geniusMix) geniusMix;
@property (TB,V_radioStation) radioStation;
@property (TB,V_smartPlaylist) smartPlaylist;
@property (TS,V_radioStationOrdering) radioStationOrdering;
@property (Ti,V_contentStyle) contentStyle;
@property (T@"ACCMediaLibraryUpdatePlaylistContent",&,V_content) content;
```

## Instance methods

```
-[ACCMediaLibraryUpdatePlaylist contentStyle];
-[ACCMediaLibraryUpdatePlaylist persistentID];
-[ACCMediaLibraryUpdatePlaylist setContentStyle:];
-[ACCMediaLibraryUpdatePlaylist revision];
-[ACCMediaLibraryUpdatePlaylist setContent:];
-[ACCMediaLibraryUpdatePlaylist debugDescription];
-[ACCMediaLibraryUpdatePlaylist validMask];
-[ACCMediaLibraryUpdatePlaylist content];
-[ACCMediaLibraryUpdatePlaylist folder];
-[ACCMediaLibraryUpdatePlaylist description];
-[ACCMediaLibraryUpdatePlaylist setName:];
-[ACCMediaLibraryUpdatePlaylist name];
-[ACCMediaLibraryUpdatePlaylist setFolder:];
-[ACCMediaLibraryUpdatePlaylist setRevision:];
-[ACCMediaLibraryUpdatePlaylist setPersistentID:];
-[ACCMediaLibraryUpdatePlaylist radioStation];
-[ACCMediaLibraryUpdatePlaylist setRadioStation:];
-[ACCMediaLibraryUpdatePlaylist geniusMix];
-[ACCMediaLibraryUpdatePlaylist copyDict];
-[ACCMediaLibraryUpdatePlaylist mediaLibraryUID];
-[ACCMediaLibraryUpdatePlaylist fillStruct:];
-[ACCMediaLibraryUpdatePlaylist initWithMediaLibrary:dict:];
-[ACCMediaLibraryUpdatePlaylist initWithMediaLibrary:persistentID:revision:];
-[ACCMediaLibraryUpdatePlaylist parentPersistentID];
-[ACCMediaLibraryUpdatePlaylist radioStationOrdering];
-[ACCMediaLibraryUpdatePlaylist setGeniusMix:];
-[ACCMediaLibraryUpdatePlaylist setMediaLibraryUID:];
-[ACCMediaLibraryUpdatePlaylist setParentPersistentID:];
-[ACCMediaLibraryUpdatePlaylist setRadioStationOrdering:];
-[ACCMediaLibraryUpdatePlaylist setSmartPlaylist:];
-[ACCMediaLibraryUpdatePlaylist smartPlaylist];
```
