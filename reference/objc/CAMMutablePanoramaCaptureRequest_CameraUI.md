# `CAMMutablePanoramaCaptureRequest`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMPanoramaCaptureRequest`
- Protocols: `CAMMutableCaptureRequestPersistence`, `CAMMutableCaptureRequestLocation`, `CAMMutableCaptureRequestPower`, `CAMMutableCaptureRequestOrigin`, `CAMMutableCaptureRequestEncodingBehavior`, `CAMMutableCaptureRequestLibrarySelection`
- 0 instance variables, 29 properties, 26 instance methods, 0 class methods

## Properties

```
@property (T@"<CAMPanoramaCaptureRequestDelegate>",W,D,N) delegate;
@property (Tq,D,N) captureOrientation;
@property (Tq,D,N) captureDevice;
@property (Tq,D,N) captureMode;
@property (Tq,D,N) pressType;
@property (TS,D,N) sessionIdentifier;
@property (T@"CAMAnalyticsCaptureEvent",&,D,N) analyticsEvent;
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
-[CAMMutablePanoramaCaptureRequest setPhotoEncodingBehavior:];
-[CAMMutablePanoramaCaptureRequest setCaptureDevice:];
-[CAMMutablePanoramaCaptureRequest setDeferredPersistenceOptions:];
-[CAMMutablePanoramaCaptureRequest setHeading:];
-[CAMMutablePanoramaCaptureRequest setContactIDsInProximity:];
-[CAMMutablePanoramaCaptureRequest mutableCopyWithZone:];
-[CAMMutablePanoramaCaptureRequest setCaptureOrientation:];
-[CAMMutablePanoramaCaptureRequest setPersistenceUUID:];
-[CAMMutablePanoramaCaptureRequest setAnalyticsEvent:];
-[CAMMutablePanoramaCaptureRequest setTemporaryPersistenceOptions:];
-[CAMMutablePanoramaCaptureRequest setSharedLibraryDiagnostics:];
-[CAMMutablePanoramaCaptureRequest setShouldDelayRemotePersistence:];
-[CAMMutablePanoramaCaptureRequest setSessionIdentifier:];
-[CAMMutablePanoramaCaptureRequest setLocalDestinationURL:];
-[CAMMutablePanoramaCaptureRequest setPersistenceOptions:];
-[CAMMutablePanoramaCaptureRequest setShouldPersistDiagnosticsToSidecar:];
-[CAMMutablePanoramaCaptureRequest setPressType:];
-[CAMMutablePanoramaCaptureRequest setSharedLibraryMode:];
-[CAMMutablePanoramaCaptureRequest analyticsEvent];
-[CAMMutablePanoramaCaptureRequest setCaptureMode:];
-[CAMMutablePanoramaCaptureRequest setDelegate:];
-[CAMMutablePanoramaCaptureRequest setShouldExtractDiagnosticsFromMetadata:];
-[CAMMutablePanoramaCaptureRequest setAssertionIdentifier:];
-[CAMMutablePanoramaCaptureRequest setOrigin:];
-[CAMMutablePanoramaCaptureRequest setLocation:];
-[CAMMutablePanoramaCaptureRequest copyWithZone:];
```
