# `CAMStorageContainer` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 3 properties, 10 instance methods, 0 class methods

## Properties

```
@property (Tq,R,N) totalFreeBytes;
@property (T@"CAMCaptureGraphConfiguration",&,N) graphConfiguration;
@property (T@"<CAMPurgeableStorageContainerDelegate>",W,N) delegate;
```

## Instance methods

```
-[CAMStorageContainer hasDiskSpaceToAllowCaptureWithConfiguration:allowPurging:verbose:];
-[CAMStorageContainer hasDiskSpaceToAllowCaptureWithConfiguration:allowPurging:completion:];
-[CAMStorageContainer minimumDiskUsageThresholdInBytesForGraphConfiguration:];
-[CAMStorageContainer graphConfiguration];
-[CAMStorageContainer hasDiskSpaceToAllowCaptureWithConfiguration:allowPurging:];
-[CAMStorageContainer setDelegate:];
-[CAMStorageContainer totalFreeBytes];
-[CAMStorageContainer availableRecordingTimeInSecondsForGraphConfiguration:];
-[CAMStorageContainer setGraphConfiguration:];
-[CAMStorageContainer delegate];
```
