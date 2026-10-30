# `CMCaptureLocalSessionController`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 26 instance variables, 4 properties, 39 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMutableDictionary" _streamsBySinkID;
@"NSMutableSet" _activeVideoCameraSinkIDs;
^{OpaqueFigCaptureSession=} _videoCameraCaptureSession;
@"NSNumber" _activeMaxFrameRate;
@"NSNumber" _activeMinFrameRate;
@"NSMutableSet" _activeVideoCameraOutputMetadataIdentifiers;
^{OpaqueFigCaptureSource=} _videoCameraCaptureSource;
@"FigCaptureSourceAttributes" _videoCameraCaptureSourceAttributes;
@"FigCaptureSessionConfiguration" _videoCameraCaptureSessionConfig;
@"NSArray" _videoCameraDeviceFormats;
@"FigCaptureSourceVideoFormat" _videoCameraActiveDeviceFormat;
B _videoCameraCaptureSessionRunning;
^{OpaqueFigCaptureSession=} _metadataCameraCaptureSession;
@"NSSet" _activeMetadataCameraMetadataIdentifiers;
@"NSDictionary" _activeMetadataCameraFaceTrackingAttributes;
^{OpaqueFigCaptureSource=} _metadataCameraCaptureSource;
@"FigCaptureSourceAttributes" _metadataCameraCaptureSourceAttributes;
@"FigCaptureSessionConfiguration" _metadataCameraCaptureSessionConfig;
@"FigCaptureSourceVideoFormat" _metadataDeviceFormat;
B _metadataCameraCaptureSessionRunning;
B _metadataCameraSinkIDActive;
AB _invalidated;
@ _availabilityChangedNotificationToken;
Q _frameTimeoutNotificationRegistrationCount;
B _registeredForSystemStateChangeNotification;
```

## Properties

```
@property (T@"NSNumber",&,N) activeMaxFrameRate;
@property (T@"NSNumber",&,N) activeMinFrameRate;
@property (T@"FigCaptureSourceAttributes",R,N) videoCameraSourceAttributes;
@property (T@"FigCaptureSourceAttributes",R,N) metadataCameraSourceAttributes;
```

## Class methods

```
+[CMCaptureLocalSessionController initialize];
```

## Instance methods

```
-[CMCaptureLocalSessionController initWithQueue:];
-[CMCaptureLocalSessionController observeValueForKeyPath:ofObject:change:context:];
-[CMCaptureLocalSessionController dealloc];
-[CMCaptureLocalSessionController invalidate];
-[CMCaptureLocalSessionController startSessionForStream:outError:];
-[CMCaptureLocalSessionController _bestVideoCameraActiveDeviceFormatForVideoConnectionConfiguration:];
-[CMCaptureLocalSessionController _configureVideoCameraStreamOutputFormat];
-[CMCaptureLocalSessionController _createCaptureSessions];
-[CMCaptureLocalSessionController _detectedObjectsSupportedForSinkID:];
-[CMCaptureLocalSessionController _determineMetadataCameraConfiguration];
-[CMCaptureLocalSessionController _determineVideoCameraOutputMetadataIdentifiers];
-[CMCaptureLocalSessionController _enableConnectionsForActiveVideoCameraSourcedSinkIDs];
-[CMCaptureLocalSessionController _newMetadataCameraFigCaptureSessionConfiguration];
-[CMCaptureLocalSessionController _newVideoCameraFigCaptureSessionConfiguration];
-[CMCaptureLocalSessionController _prepareForSessionRestartDueToUnrecoverableError];
-[CMCaptureLocalSessionController _resolveCaptureSourcePropertiesFromLocalVideoCameraSessionConfigurationValues];
-[CMCaptureLocalSessionController _resolveMetadataCameraFigCaptureSessionConfigurationValuesFromLocalSessionConfigurationValues];
-[CMCaptureLocalSessionController _resolveVideoCameraFigCaptureSessionConfigurationValuesFromLocalSessionConfigurationValues];
-[CMCaptureLocalSessionController _startSession:sessionRunningInOut:];
-[CMCaptureLocalSessionController _startSessionForMetadataCameraStream:outError:];
-[CMCaptureLocalSessionController _startSessionForVideoCameraStream:outError:];
-[CMCaptureLocalSessionController _stopSession:sessionRunningInOut:];
-[CMCaptureLocalSessionController _stopSessionForMetadataCameraStream:outError:];
-[CMCaptureLocalSessionController _stopSessionForVideoCameraStream:outError:];
-[CMCaptureLocalSessionController _updateFrameRate];
-[CMCaptureLocalSessionController _updateSessionConfigurationForMetadataCameraStream];
-[CMCaptureLocalSessionController _updateSessionConfigurationForVideoCameraStream];
-[CMCaptureLocalSessionController _updateVideoCameraActiveSinkIDsWhenStartingStream:];
-[CMCaptureLocalSessionController _updateVideoCameraActiveSinkIDsWhenStoppingStream:];
-[CMCaptureLocalSessionController activeMaxFrameRate];
-[CMCaptureLocalSessionController activeMinFrameRate];
-[CMCaptureLocalSessionController associateStream:withSink:];
-[CMCaptureLocalSessionController metadataCameraSourceAttributes];
-[CMCaptureLocalSessionController setActiveMaxFrameRate:];
-[CMCaptureLocalSessionController setActiveMinFrameRate:];
-[CMCaptureLocalSessionController setCaptureSourceProperty:withValue:];
-[CMCaptureLocalSessionController stopSessionForStream:outError:];
-[CMCaptureLocalSessionController updateSessionConfigurationForStream:];
-[CMCaptureLocalSessionController videoCameraSourceAttributes];
```
