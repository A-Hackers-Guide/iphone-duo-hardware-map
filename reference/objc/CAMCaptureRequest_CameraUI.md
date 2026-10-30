# `CAMCaptureRequest`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `CAMDistinctPersistenceCopying`
- 28 instance variables, 35 properties, 36 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _contactIDsInProximity;
q _sharedLibraryMode;
@"NSDictionary" _sharedLibraryDiagnostics;
q _videoEncodingBehavior;
q _photoEncodingBehavior;
q _rawFileFormatBehavior;
q _origin;
I _assertionIdentifier;
B _capturedFromPhotoBooth;
@"CLLocation" _location;
@"CLHeading" _heading;
q _persistenceOptions;
Q _deferredPersistenceOptions;
q _temporaryPersistenceOptions;
@"NSURL" _localDestinationURL;
@"NSString" _persistenceUUID;
B _shouldExtractDiagnosticsFromMetadata;
B _shouldPersistDiagnosticsToSidecar;
B _shouldDelayRemotePersistence;
S _sessionIdentifier;
q _captureDevice;
q _captureMode;
q _captureOrientation;
B _captureMirrored;
q _pressType;
@"CAMAnalyticsCaptureEvent" _analyticsEvent;
Q _audioConfiguration;
q _type;
```

## Properties

```
@property (T@"NSArray",R,C,N,V_contactIDsInProximity) contactIDsInProximity;
@property (Tq,R,N,V_sharedLibraryMode) sharedLibraryMode;
@property (T@"NSDictionary",R,C,N,V_sharedLibraryDiagnostics) sharedLibraryDiagnostics;
@property (Tq,R,N,V_videoEncodingBehavior) videoEncodingBehavior;
@property (Tq,R,N,V_photoEncodingBehavior) photoEncodingBehavior;
@property (Tq,R,N,V_rawFileFormatBehavior) rawFileFormatBehavior;
@property (Tq,R,N,V_origin) origin;
@property (TI,R,N,V_assertionIdentifier) assertionIdentifier;
@property (TB,R,N,V_capturedFromPhotoBooth) capturedFromPhotoBooth;
@property (T@"CLLocation",R,N,V_location) location;
@property (T@"CLHeading",R,N,V_heading) heading;
@property (Tq,R,N,V_persistenceOptions) persistenceOptions;
@property (TQ,R,N,V_deferredPersistenceOptions) deferredPersistenceOptions;
@property (Tq,R,N,V_temporaryPersistenceOptions) temporaryPersistenceOptions;
@property (T@"NSURL",R,C,N,V_localDestinationURL) localDestinationURL;
@property (T@"NSString",R,C,N,V_persistenceUUID) persistenceUUID;
@property (TB,R,N) shouldPersistToIncomingDirectory;
@property (TB,R,N) shouldProtectPersistence;
@property (TB,R,N) shouldProtectPersistenceForVideo;
@property (TB,R,N,V_shouldExtractDiagnosticsFromMetadata) shouldExtractDiagnosticsFromMetadata;
@property (TB,R,N,V_shouldPersistDiagnosticsToSidecar) shouldPersistDiagnosticsToSidecar;
@property (TB,R,N,V_shouldDelayRemotePersistence) shouldDelayRemotePersistence;
@property (Tq,R,N,V_type) type;
@property (Tq,R,N,V_captureOrientation) captureOrientation;
@property (TB,R,N,GisCaptureMirrored,V_captureMirrored) captureMirrored;
@property (Tq,R,N,V_captureDevice) captureDevice;
@property (Tq,R,N) captureDevicePosition;
@property (Tq,R,N,V_captureMode) captureMode;
@property (Tq,R,N,V_pressType) pressType;
@property (TS,R,N,V_sessionIdentifier) sessionIdentifier;
@property (TQ,R,N,V_audioConfiguration) audioConfiguration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAMCaptureRequest shouldPersistToIncomingDirectoryWithPersistenceOptions:temporaryPersistenceOptions:];
```

## Instance methods

```
-[CAMCaptureRequest shouldProtectPersistenceForVideo];
-[CAMCaptureRequest photoEncodingBehavior];
-[CAMCaptureRequest sessionIdentifier];
-[CAMCaptureRequest isCaptureMirrored];
-[CAMCaptureRequest persistenceUUID];
-[CAMCaptureRequest origin];
-[CAMCaptureRequest sharedLibraryMode];
-[CAMCaptureRequest init];
-[CAMCaptureRequest captureDevice];
-[CAMCaptureRequest assertionIdentifier];
-[CAMCaptureRequest location];
-[CAMCaptureRequest initWithType:];
-[CAMCaptureRequest rawFileFormatBehavior];
-[CAMCaptureRequest initWithRequest:distinctPersistence:];
-[CAMCaptureRequest heading];
-[CAMCaptureRequest captureDevicePosition];
-[CAMCaptureRequest type];
-[CAMCaptureRequest captureMode];
-[CAMCaptureRequest audioConfiguration];
-[CAMCaptureRequest shouldDelayRemotePersistence];
-[CAMCaptureRequest copyWithZone:];
-[CAMCaptureRequest localDestinationURL];
-[CAMCaptureRequest captureOrientation];
-[CAMCaptureRequest pressType];
-[CAMCaptureRequest contactIDsInProximity];
-[CAMCaptureRequest sharedLibraryDiagnostics];
-[CAMCaptureRequest capturedFromPhotoBooth];
-[CAMCaptureRequest deferredPersistenceOptions];
-[CAMCaptureRequest distinctPersistenceCopy];
-[CAMCaptureRequest persistenceOptions];
-[CAMCaptureRequest shouldExtractDiagnosticsFromMetadata];
-[CAMCaptureRequest shouldPersistDiagnosticsToSidecar];
-[CAMCaptureRequest shouldPersistToIncomingDirectory];
-[CAMCaptureRequest shouldProtectPersistence];
-[CAMCaptureRequest temporaryPersistenceOptions];
-[CAMCaptureRequest videoEncodingBehavior];
```
