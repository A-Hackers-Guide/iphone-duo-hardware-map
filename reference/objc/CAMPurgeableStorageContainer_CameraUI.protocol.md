# `CAMPurgeableStorageContainer` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `CAMStorageContainer`
- 0 instance variables, 4 properties, 8 instance methods, 0 class methods

## Properties

```
@property (TB,R,N,GisPurging) purging;
@property (TB,R,N,GisCancelingPurge) cancelingPurge;
@property (TB,R,N,GhasPurgeableResources) hasPurgeableResources;
@property (T@"<CAMPurgeableStorageContainerDelegate>",W,N) delegate;
```

## Instance methods

```
-[CAMPurgeableStorageContainer cancelPurge];
-[CAMPurgeableStorageContainer hasPurgeableResources];
-[CAMPurgeableStorageContainer setDelegate:];
-[CAMPurgeableStorageContainer purgeFastPurgeableSpaceWithRequestType:];
-[CAMPurgeableStorageContainer isCancelingPurge];
-[CAMPurgeableStorageContainer delegate];
-[CAMPurgeableStorageContainer reportLowDiskEventWithIdentifier:];
-[CAMPurgeableStorageContainer isPurging];
```
