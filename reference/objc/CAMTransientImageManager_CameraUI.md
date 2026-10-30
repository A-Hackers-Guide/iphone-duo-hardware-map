# `CAMTransientImageManager`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PUTransientImageManager`
- 2 instance variables, 7 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" __pairedVideosByPairedUUID;
@"NSMutableDictionary" __activeRequestsByPairedUUID;
```

## Properties

```
@property (T@"NSMutableDictionary",R,N,V__pairedVideosByPairedUUID) _pairedVideosByPairedUUID;
@property (T@"NSMutableDictionary",R,N,V__activeRequestsByPairedUUID) _activeRequestsByPairedUUID;
@property (TB,R,N,GisEmpty) empty;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMTransientImageManager init];
-[CAMTransientImageManager isEmpty];
-[CAMTransientImageManager requestPairedVideoURLForUUID:resultHandler:];
-[CAMTransientImageManager _activeRequestsByPairedUUID];
-[CAMTransientImageManager _handleRequestTimeout:];
-[CAMTransientImageManager _pairedVideosByPairedUUID];
-[CAMTransientImageManager existingPairedVideoForUUID:];
-[CAMTransientImageManager existingPairedVideoUUIDs];
-[CAMTransientImageManager insertPairedVideoWithConvertible:filterType:];
-[CAMTransientImageManager removePairedVideoForUUID:];
```
