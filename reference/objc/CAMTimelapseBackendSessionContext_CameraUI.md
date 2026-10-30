# `CAMTimelapseBackendSessionContext`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSString" _timelapseUUID;
@"CAMTimelapseState" _state;
@"NSArray" _filesToDelete;
@"NSArray" _filesToWrite;
```

## Properties

```
@property (T@"NSString",R,N,V_timelapseUUID) timelapseUUID;
@property (T@"CAMTimelapseState",&,N,V_state) state;
@property (T@"NSArray",&,N,V_filesToDelete) filesToDelete;
@property (T@"NSArray",&,N,V_filesToWrite) filesToWrite;
```

## Instance methods

```
-[CAMTimelapseBackendSessionContext setState:];
-[CAMTimelapseBackendSessionContext init];
-[CAMTimelapseBackendSessionContext description];
-[CAMTimelapseBackendSessionContext state];
-[CAMTimelapseBackendSessionContext filesToDelete];
-[CAMTimelapseBackendSessionContext filesToWrite];
-[CAMTimelapseBackendSessionContext initWithTimelapseUUID:];
-[CAMTimelapseBackendSessionContext setFilesToDelete:];
-[CAMTimelapseBackendSessionContext setFilesToWrite:];
-[CAMTimelapseBackendSessionContext timelapseUUID];
```
