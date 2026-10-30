# `CAMExternalStorage`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAMStorageContainer`
- 7 instance variables, 13 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"<CAMPurgeableStorageContainerDelegate>" _delegate;
@"CAMCaptureGraphConfiguration" _graphConfiguration;
@"NSUUID" _uniqueIdentifier;
@"NSString" _displayName;
@"NSSet" _notRecommendedForCaptureReasons;
@"AVExternalStorageDevice" __underlyingStorageDevice;
@"NSURL" __baseURL;
```

## Properties

```
@property (T@"AVExternalStorageDevice",R,N,V__underlyingStorageDevice) _underlyingStorageDevice;
@property (T@"NSURL",R,N,V__baseURL) _baseURL;
@property (TB,R,N) connected;
@property (T@"NSUUID",R,N,V_uniqueIdentifier) uniqueIdentifier;
@property (T@"NSString",R,N,V_displayName) displayName;
@property (T@"NSSet",R,N,V_notRecommendedForCaptureReasons) notRecommendedForCaptureReasons;
@property (Tq,R,N) totalFreeBytes;
@property (T@"CAMCaptureGraphConfiguration",&,N,V_graphConfiguration) graphConfiguration;
@property (T@"<CAMPurgeableStorageContainerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMExternalStorage connected];
-[CAMExternalStorage hasDiskSpaceToAllowCaptureWithConfiguration:allowPurging:verbose:];
-[CAMExternalStorage displayName];
-[CAMExternalStorage hasDiskSpaceToAllowCaptureWithConfiguration:allowPurging:completion:];
-[CAMExternalStorage minimumDiskUsageThresholdInBytesForGraphConfiguration:];
-[CAMExternalStorage graphConfiguration];
-[CAMExternalStorage uniqueIdentifier];
-[CAMExternalStorage hasDiskSpaceToAllowCaptureWithConfiguration:allowPurging:];
-[CAMExternalStorage setDelegate:];
-[CAMExternalStorage totalFreeBytes];
-[CAMExternalStorage availableRecordingTimeInSecondsForGraphConfiguration:];
-[CAMExternalStorage setGraphConfiguration:];
-[CAMExternalStorage delegate];
-[CAMExternalStorage description];
-[CAMExternalStorage isEqual:];
-[CAMExternalStorage _baseURL];
-[CAMExternalStorage notRecommendedForCaptureReasons];
-[CAMExternalStorage _underlyingStorageDevice];
-[CAMExternalStorage generateDestinationURLWithExtension:];
-[CAMExternalStorage initWithNoDevice];
-[CAMExternalStorage initWithStorageDevice:];
```
