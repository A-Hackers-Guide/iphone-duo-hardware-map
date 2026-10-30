# `CAMNebulaKeepAliveController`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
B __didCreateKeepAliveDirectory;
i __nebuladKeepAliveFileDescriptor;
@"NSObject<OS_dispatch_queue>" __syncQueue;
@"NSMutableSet" __nebuladKeepAliveIdentifiers;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__syncQueue) _syncQueue;
@property (Ti,N,S_setNebuladKeepAliveFileDescriptor:,V__nebuladKeepAliveFileDescriptor) _nebuladKeepAliveFileDescriptor;
@property (T@"NSMutableSet",R,N,V__nebuladKeepAliveIdentifiers) _nebuladKeepAliveIdentifiers;
@property (TB,N,S_setDidCreateKeepAliveDirectory:,V__didCreateKeepAliveDirectory) _didCreateKeepAliveDirectory;
```

## Instance methods

```
-[CAMNebulaKeepAliveController _syncQueue];
-[CAMNebulaKeepAliveController init];
-[CAMNebulaKeepAliveController _nebuladKeepAliveFileDescriptor];
-[CAMNebulaKeepAliveController _didCreateKeepAliveDirectory];
-[CAMNebulaKeepAliveController _keepAliveFilePath];
-[CAMNebulaKeepAliveController _nebuladKeepAliveIdentifiers];
-[CAMNebulaKeepAliveController _setDidCreateKeepAliveDirectory:];
-[CAMNebulaKeepAliveController _setNebuladKeepAliveFileDescriptor:];
-[CAMNebulaKeepAliveController removeKeepAliveFileIfNotKeptForAnyIdentifiers];
-[CAMNebulaKeepAliveController startKeepAliveForIdentifier:];
-[CAMNebulaKeepAliveController stopKeepAliveForIdentifier:];
```
