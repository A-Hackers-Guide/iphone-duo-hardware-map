# `TUNicknamesMetadataCacheDataProvider`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `TUMetadataCacheDataProvider`
- Protocols: `IMNicknameListener`
- 1 instance variables, 5 properties, 7 instance methods, 2 class methods

## Instance variables

```
@"IMNicknameProvider" _nicknameProvider;
```

## Properties

```
@property (T@"IMNicknameProvider",R,N,V_nicknameProvider) nicknameProvider;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TUNicknamesMetadataCacheDataProvider sharedInstance];
+[TUNicknamesMetadataCacheDataProvider tuMetadataDestinationIDForHandleValue:];
```

## Instance methods

```
-[TUNicknamesMetadataCacheDataProvider init];
-[TUNicknamesMetadataCacheDataProvider nicknameStoreDidChange:];
-[TUNicknamesMetadataCacheDataProvider nicknameProvider];
-[TUNicknamesMetadataCacheDataProvider fetchNicknameForHandleValue:];
-[TUNicknamesMetadataCacheDataProvider formattedNicknameStringForHandleValue:];
-[TUNicknamesMetadataCacheDataProvider formattedNicknameStringForNickname:];
-[TUNicknamesMetadataCacheDataProvider updateCacheWithDestinationIDs:withGroup:];
```
