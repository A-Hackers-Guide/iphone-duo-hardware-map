# `CAMStorageController`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAMStorageContainer`
- 6 instance variables, 15 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"CAMCaptureGraphConfiguration" _graphConfiguration;
@"<CAMPurgeableStorageContainerDelegate>" _delegate;
@"CAMExternalStorage" _externalStorage;
@"CAMVirtualCaptureCardInternalStorage" _virtualCaptureCardInternalStorage;
@"CAMInternalStorage" __internalStorage;
@"<CAMStorageContainer>" __currentStorage;
```

## Properties

```
@property (T@"CAMInternalStorage",R,N,V__internalStorage) _internalStorage;
@property (TB,R,N) _isUsingInternalStorage;
@property (TB,R,N) _isUsingVirtualCaptureCardInternalStorage;
@property (TB,R,N) _isUsingExternalStorage;
@property (T@"<CAMStorageContainer>",&,N,S_setCurrentStorage:,V__currentStorage) _currentStorage;
@property (T@"<CAMPurgeableStorageContainerDelegate>",W,N,V_delegate) delegate;
@property (T@"<CAMPurgeableStorageContainer>",R,W,N) purgeableStorageContainer;
@property (T@"CAMExternalStorage",&,N,V_externalStorage) externalStorage;
@property (T@"CAMVirtualCaptureCardInternalStorage",R,N,V_virtualCaptureCardInternalStorage) virtualCaptureCardInternalStorage;
@property (Tq,R,N) totalFreeBytes;
@property (T@"CAMCaptureGraphConfiguration",&,N,V_graphConfiguration) graphConfiguration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMStorageController hasDiskSpaceToAllowCaptureWithConfiguration:allowPurging:verbose:];
-[CAMStorageController init];
-[CAMStorageController hasDiskSpaceToAllowCaptureWithConfiguration:allowPurging:completion:];
-[CAMStorageController minimumDiskUsageThresholdInBytesForGraphConfiguration:];
-[CAMStorageController graphConfiguration];
-[CAMStorageController hasDiskSpaceToAllowCaptureWithConfiguration:allowPurging:];
-[CAMStorageController setDelegate:];
-[CAMStorageController totalFreeBytes];
-[CAMStorageController setExternalStorage:];
-[CAMStorageController availableRecordingTimeInSecondsForGraphConfiguration:];
-[CAMStorageController setGraphConfiguration:];
-[CAMStorageController delegate];
-[CAMStorageController externalStorage];
-[CAMStorageController _currentStorage];
-[CAMStorageController _internalStorage];
-[CAMStorageController _isUsingExternalStorage];
-[CAMStorageController _isUsingInternalStorage];
-[CAMStorageController _isUsingVirtualCaptureCardInternalStorage];
-[CAMStorageController _resolveCurrentStorageForCurrentGraphConfiguration];
-[CAMStorageController _setCurrentStorage:];
-[CAMStorageController _updateGraphConfigurationOnCurrentStorage];
-[CAMStorageController _updateStorageDelegates];
-[CAMStorageController purgeableStorageContainer];
-[CAMStorageController virtualCaptureCardInternalStorage];
```
