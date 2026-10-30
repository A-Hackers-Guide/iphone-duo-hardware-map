# `CAMMutableVideoCaptureRequest`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMVideoCaptureRequest`
- Protocols: `CAMMutableCaptureRequestPersistence`, `CAMMutableCaptureRequestLocation`, `CAMMutableCaptureRequestPower`, `CAMMutableCaptureRequestOrigin`, `CAMMutableCaptureRequestEncodingBehavior`, `CAMMutableCaptureRequestLibrarySelection`
- 0 instance variables, 45 properties, 43 instance methods, 0 class methods

## Properties

```
@property (TB,D,N,GisTimelapse) timelapse;
@property (TB,D,N) shouldGenerateVideoPreviewImage;
@property (Td,D,N) maximumRecordedDuration;
@property (Tq,D,N) maximumRecordedFileSize;
@property (Tq,D,N) remainingDiskUsageThreshold;
@property (T@"<CAMVideoCaptureRequestDelegate>",W,D,N) delegate;
@property (Tq,D,N) captureOrientation;
@property (TB,D,N,GisCaptureMirrored) captureMirrored;
@property (Tq,D,N) captureDevice;
@property (Tq,D,N) captureMode;
@property (Tq,D,N) captureVideoConfiguration;
@property (Tq,D,N) pressType;
@property (Tq,D,N) torchMode;
@property (TB,D,N) wantsWhiteBalanceLocked;
@property (TS,D,N) sessionIdentifier;
@property (T@"CAMAnalyticsCaptureEvent",&,D,N) analyticsEvent;
@property (TQ,D,N) audioConfiguration;
@property (TB,D,N) trueVideoEnabled;
@property (TB,D,N) constituentDeviceSwitchingEnabled;
@property (TB,D,N,GisFrontRearSimultaneousVideoEnabled) frontRearSimultaneousVideoEnabled;
@property (TB,D,N,GisFrontRearSimultaneousVideoMirrored) frontRearSimultaneousVideoMirrored;
@property (TB,D,N) shouldUseProVideoStorage;
@property (Td,D,N) userInitiationTimestamp;
@property (Tq,N) persistenceOptions;
@property (TQ,N) deferredPersistenceOptions;
@property (Tq,N) temporaryPersistenceOptions;
@property (T@"NSURL",C,N) localDestinationURL;
@property (T@"NSString",C,N) persistenceUUID;
@property (TB,N) shouldExtractDiagnosticsFromMetadata;
@property (TB,N) shouldPersistDiagnosticsToSidecar;
@property (TB,N) shouldDelayRemotePersistence;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"CLLocation",&,N) location;
@property (T@"CLHeading",&,N) heading;
@property (TI,N) assertionIdentifier;
@property (Tq,N) origin;
@property (Tq,N) videoEncodingBehavior;
@property (Tq,N) photoEncodingBehavior;
@property (Tq,N) rawFileFormatBehavior;
@property (T@"NSArray",C,N) contactIDsInProximity;
@property (Tq,N) sharedLibraryMode;
@property (T@"NSDictionary",C,N) sharedLibraryDiagnostics;
```

## Instance methods

```
-[CAMMutableVideoCaptureRequest setCaptureDevice:];
-[CAMMutableVideoCaptureRequest isCaptureMirrored];
-[CAMMutableVideoCaptureRequest setDeferredPersistenceOptions:];
-[CAMMutableVideoCaptureRequest setHeading:];
-[CAMMutableVideoCaptureRequest setContactIDsInProximity:];
-[CAMMutableVideoCaptureRequest mutableCopyWithZone:];
-[CAMMutableVideoCaptureRequest setCaptureOrientation:];
-[CAMMutableVideoCaptureRequest setPersistenceUUID:];
-[CAMMutableVideoCaptureRequest setCaptureVideoConfiguration:];
-[CAMMutableVideoCaptureRequest setVideoEncodingBehavior:];
-[CAMMutableVideoCaptureRequest setAnalyticsEvent:];
-[CAMMutableVideoCaptureRequest setFrontRearSimultaneousVideoEnabled:];
-[CAMMutableVideoCaptureRequest setTemporaryPersistenceOptions:];
-[CAMMutableVideoCaptureRequest setCaptureMirrored:];
-[CAMMutableVideoCaptureRequest setSharedLibraryDiagnostics:];
-[CAMMutableVideoCaptureRequest setTimelapse:];
-[CAMMutableVideoCaptureRequest setShouldDelayRemotePersistence:];
-[CAMMutableVideoCaptureRequest setTrueVideoEnabled:];
-[CAMMutableVideoCaptureRequest setSessionIdentifier:];
-[CAMMutableVideoCaptureRequest setLocalDestinationURL:];
-[CAMMutableVideoCaptureRequest setPersistenceOptions:];
-[CAMMutableVideoCaptureRequest setMaximumRecordedDuration:];
-[CAMMutableVideoCaptureRequest setTorchMode:];
-[CAMMutableVideoCaptureRequest setConstituentDeviceSwitchingEnabled:];
-[CAMMutableVideoCaptureRequest setShouldPersistDiagnosticsToSidecar:];
-[CAMMutableVideoCaptureRequest setUserInitiationTimestamp:];
-[CAMMutableVideoCaptureRequest setPressType:];
-[CAMMutableVideoCaptureRequest setRemainingDiskUsageThreshold:];
-[CAMMutableVideoCaptureRequest setSharedLibraryMode:];
-[CAMMutableVideoCaptureRequest analyticsEvent];
-[CAMMutableVideoCaptureRequest setCaptureMode:];
-[CAMMutableVideoCaptureRequest setAudioConfiguration:];
-[CAMMutableVideoCaptureRequest setDelegate:];
-[CAMMutableVideoCaptureRequest setShouldExtractDiagnosticsFromMetadata:];
-[CAMMutableVideoCaptureRequest setShouldGenerateVideoPreviewImage:];
-[CAMMutableVideoCaptureRequest setAssertionIdentifier:];
-[CAMMutableVideoCaptureRequest setOrigin:];
-[CAMMutableVideoCaptureRequest setLocation:];
-[CAMMutableVideoCaptureRequest setMaximumRecordedFileSize:];
-[CAMMutableVideoCaptureRequest setShouldUseProVideoStorage:];
-[CAMMutableVideoCaptureRequest copyWithZone:];
-[CAMMutableVideoCaptureRequest setWantsWhiteBalanceLocked:];
-[CAMMutableVideoCaptureRequest setFrontRearSimultaneousVideoMirrored:];
```
