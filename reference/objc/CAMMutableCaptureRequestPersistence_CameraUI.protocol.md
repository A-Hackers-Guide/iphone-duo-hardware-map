# `CAMMutableCaptureRequestPersistence` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 8 properties, 16 instance methods, 0 class methods

## Properties

```
@property (Tq,N) persistenceOptions;
@property (TQ,N) deferredPersistenceOptions;
@property (Tq,N) temporaryPersistenceOptions;
@property (T@"NSURL",C,N) localDestinationURL;
@property (T@"NSString",C,N) persistenceUUID;
@property (TB,N) shouldExtractDiagnosticsFromMetadata;
@property (TB,N) shouldPersistDiagnosticsToSidecar;
@property (TB,N) shouldDelayRemotePersistence;
```

## Instance methods

```
-[CAMMutableCaptureRequestPersistence persistenceUUID];
-[CAMMutableCaptureRequestPersistence setDeferredPersistenceOptions:];
-[CAMMutableCaptureRequestPersistence setPersistenceUUID:];
-[CAMMutableCaptureRequestPersistence setTemporaryPersistenceOptions:];
-[CAMMutableCaptureRequestPersistence setShouldDelayRemotePersistence:];
-[CAMMutableCaptureRequestPersistence setLocalDestinationURL:];
-[CAMMutableCaptureRequestPersistence setPersistenceOptions:];
-[CAMMutableCaptureRequestPersistence setShouldPersistDiagnosticsToSidecar:];
-[CAMMutableCaptureRequestPersistence setShouldExtractDiagnosticsFromMetadata:];
-[CAMMutableCaptureRequestPersistence shouldDelayRemotePersistence];
-[CAMMutableCaptureRequestPersistence localDestinationURL];
-[CAMMutableCaptureRequestPersistence deferredPersistenceOptions];
-[CAMMutableCaptureRequestPersistence persistenceOptions];
-[CAMMutableCaptureRequestPersistence shouldExtractDiagnosticsFromMetadata];
-[CAMMutableCaptureRequestPersistence shouldPersistDiagnosticsToSidecar];
-[CAMMutableCaptureRequestPersistence temporaryPersistenceOptions];
```
