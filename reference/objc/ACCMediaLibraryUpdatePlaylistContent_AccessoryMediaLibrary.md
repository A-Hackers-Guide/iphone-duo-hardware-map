# `ACCMediaLibraryUpdatePlaylistContent`

- Image: [`/System/Library/PrivateFrameworks/AccessoryMediaLibrary.framework/AccessoryMediaLibrary`](../userland/System__Library__PrivateFrameworks__AccessoryMediaLibrary.framework__AccessoryMediaLibrary.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 26 instance methods, 0 class methods

## Instance variables

```
i _contentStyle;
@"NSString" _mediaLibraryUID;
@"NSString" _revision;
Q _persistentID;
@"NSMutableArray" _contentList;
```

## Properties

```
@property (T@"NSMutableArray",&,V_contentList) contentList;
@property (T@"NSString",&,V_mediaLibraryUID) mediaLibraryUID;
@property (T@"NSString",&,V_revision) revision;
@property (TQ,V_persistentID) persistentID;
@property (Ti,V_contentStyle) contentStyle;
```

## Instance methods

```
-[ACCMediaLibraryUpdatePlaylistContent contentStyle];
-[ACCMediaLibraryUpdatePlaylistContent persistentID];
-[ACCMediaLibraryUpdatePlaylistContent addContentItem:];
-[ACCMediaLibraryUpdatePlaylistContent setContentStyle:];
-[ACCMediaLibraryUpdatePlaylistContent revision];
-[ACCMediaLibraryUpdatePlaylistContent debugDescription];
-[ACCMediaLibraryUpdatePlaylistContent description];
-[ACCMediaLibraryUpdatePlaylistContent setRevision:];
-[ACCMediaLibraryUpdatePlaylistContent setPersistentID:];
-[ACCMediaLibraryUpdatePlaylistContent contentList];
-[ACCMediaLibraryUpdatePlaylistContent copyDict];
-[ACCMediaLibraryUpdatePlaylistContent copyContentList];
-[ACCMediaLibraryUpdatePlaylistContent mediaLibraryUID];
-[ACCMediaLibraryUpdatePlaylistContent setContentList:];
-[ACCMediaLibraryUpdatePlaylistContent addContentPersistentID:];
-[ACCMediaLibraryUpdatePlaylistContent contentListCount];
-[ACCMediaLibraryUpdatePlaylistContent copyContentDictList];
-[ACCMediaLibraryUpdatePlaylistContent getContentItemAtIndex:];
-[ACCMediaLibraryUpdatePlaylistContent initWithMediaLibrary:persistentID:revision:];
-[ACCMediaLibraryUpdatePlaylistContent initWithMediaLibrary:revision:dict:];
-[ACCMediaLibraryUpdatePlaylistContent iterateContentItems:];
-[ACCMediaLibraryUpdatePlaylistContent iterateContentPersistentIDs:];
-[ACCMediaLibraryUpdatePlaylistContent replaceContentItem:atIndex:];
-[ACCMediaLibraryUpdatePlaylistContent replaceContentList:];
-[ACCMediaLibraryUpdatePlaylistContent replaceContentPersistentID:atIndex:];
-[ACCMediaLibraryUpdatePlaylistContent setMediaLibraryUID:];
```
