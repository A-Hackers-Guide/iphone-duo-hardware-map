# `CAMVideoCaptureRequest`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMCaptureRequest`
- Protocols: `NSCopying`, `NSMutableCopying`
- 15 instance variables, 15 properties, 20 instance methods, 0 class methods

## Instance variables

```
B _timelapse;
B _shouldGenerateVideoPreviewImage;
d _maximumRecordedDuration;
q _maximumRecordedFileSize;
q _remainingDiskUsageThreshold;
@"<CAMVideoCaptureRequestDelegate>" _delegate;
q _captureVideoConfiguration;
q _torchMode;
B _wantsWhiteBalanceLocked;
d _userInitiationTimestamp;
B _trueVideoEnabled;
B _constituentDeviceSwitchingEnabled;
B _frontRearSimultaneousVideoEnabled;
B _frontRearSimultaneousVideoMirrored;
B _shouldUseProVideoStorage;
```

## Properties

```
@property (TB,R,N,GisTimelapse,V_timelapse) timelapse;
@property (TB,R,N,V_shouldGenerateVideoPreviewImage) shouldGenerateVideoPreviewImage;
@property (Td,R,N,V_maximumRecordedDuration) maximumRecordedDuration;
@property (Tq,R,N,V_maximumRecordedFileSize) maximumRecordedFileSize;
@property (Tq,R,N,V_remainingDiskUsageThreshold) remainingDiskUsageThreshold;
@property (T@"<CAMVideoCaptureRequestDelegate>",R,W,N,V_delegate) delegate;
@property (Tq,R,N,V_captureVideoConfiguration) captureVideoConfiguration;
@property (Tq,R,N,V_torchMode) torchMode;
@property (TB,R,N,V_wantsWhiteBalanceLocked) wantsWhiteBalanceLocked;
@property (TB,R,N,V_trueVideoEnabled) trueVideoEnabled;
@property (TB,R,N,V_constituentDeviceSwitchingEnabled) constituentDeviceSwitchingEnabled;
@property (TB,R,N,GisFrontRearSimultaneousVideoEnabled,V_frontRearSimultaneousVideoEnabled) frontRearSimultaneousVideoEnabled;
@property (TB,R,N,GisFrontRearSimultaneousVideoMirrored,V_frontRearSimultaneousVideoMirrored) frontRearSimultaneousVideoMirrored;
@property (TB,R,N,V_shouldUseProVideoStorage) shouldUseProVideoStorage;
@property (Td,R,N,V_userInitiationTimestamp) userInitiationTimestamp;
```

## Instance methods

```
-[CAMVideoCaptureRequest mutableCopyWithZone:];
-[CAMVideoCaptureRequest remainingDiskUsageThreshold];
-[CAMVideoCaptureRequest isFrontRearSimultaneousVideoMirrored];
-[CAMVideoCaptureRequest captureVideoConfiguration];
-[CAMVideoCaptureRequest maximumRecordedDuration];
-[CAMVideoCaptureRequest init];
-[CAMVideoCaptureRequest isFrontRearSimultaneousVideoEnabled];
-[CAMVideoCaptureRequest wantsWhiteBalanceLocked];
-[CAMVideoCaptureRequest trueVideoEnabled];
-[CAMVideoCaptureRequest isTimelapse];
-[CAMVideoCaptureRequest initWithRequest:distinctPersistence:];
-[CAMVideoCaptureRequest maximumRecordedFileSize];
-[CAMVideoCaptureRequest userInitiationTimestamp];
-[CAMVideoCaptureRequest shouldUseProVideoStorage];
-[CAMVideoCaptureRequest shouldGenerateVideoPreviewImage];
-[CAMVideoCaptureRequest torchMode];
-[CAMVideoCaptureRequest constituentDeviceSwitchingEnabled];
-[CAMVideoCaptureRequest delegate];
-[CAMVideoCaptureRequest description];
-[CAMVideoCaptureRequest copyWithZone:];
```
