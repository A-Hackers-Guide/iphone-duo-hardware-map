# `/System/Library/PrivateFrameworks/CompanionCamera.framework/CompanionCamera`

iOS 27.2 dyld shared cache image. Version `2024.200.4.0.0`. **[DSC]**

## Linked libraries (11)

- `/System/Library/PrivateFrameworks/DockKitCore.framework/DockKitCore`
- `/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`
- `/System/Library/Frameworks/UIKit.framework/UIKit`
- `/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics`
- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics`
- `/System/Library/Frameworks/AVFoundation.framework/AVFoundation`
- `/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 6 classes, 5 protocols, 234 methods, 12 properties

### Class pages

Every class and protocol, with its methods: [`CCCameraConnection`](../objc/CCCameraConnection_CompanionCamera.md), [`CCCameraConnectionInternal`](../objc/CCCameraConnectionInternal_CompanionCamera.md), [`CCCameraConnectionProtocol`](../objc/CCCameraConnectionProtocol_CompanionCamera.protocol.md), [`CCCameraConnectionReliabilityMonitor`](../objc/CCCameraConnectionReliabilityMonitor_CompanionCamera.md), [`CCCameraServerProtocol`](../objc/CCCameraServerProtocol_CompanionCamera.protocol.md), [`FigCameraViewfinderDelegate`](../objc/FigCameraViewfinderDelegate_CompanionCamera.protocol.md), [`FigCameraViewfinderSessionDelegate`](../objc/FigCameraViewfinderSessionDelegate_CompanionCamera.protocol.md), [`NSObject`](../objc/NSObject_CompanionCamera.protocol.md), [`ViewfinderErrorReport`](../objc/ViewfinderErrorReport_CompanionCamera.md), [`ViewfinderErrorReporter`](../objc/ViewfinderErrorReporter_CompanionCamera.md), [`ViewfinderReliability`](../objc/ViewfinderReliability_CompanionCamera.md)

### Classes

`CCCameraConnection`, `CCCameraConnectionInternal`, `CCCameraConnectionReliabilityMonitor`, `ViewfinderErrorReport`, `ViewfinderErrorReporter`, `ViewfinderReliability`

### Protocols

`CCCameraConnectionProtocol`, `CCCameraServerProtocol`, `FigCameraViewfinderDelegate`, `FigCameraViewfinderSessionDelegate`, `NSObject`

### Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<CCCameraConnectionDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"CCCameraConnection",W,N,V_parent) parent;
@property (Tq,R,N,V_code) code;
@property (Ti,R,N,V_status) status;
```

## Strings (163)

```
-[CCCameraConnection didPauseCaptureTimerWithPauseTime:]
-[CCCameraConnection countdownCanceled]
-[CCCameraConnection xpc_pauseCaptureWithReply:]
On
CC_RapidDisconnection
CC_Leaked
CloseCameraMessageReceived
FigCameraViewfinderStarted
-[CCCameraConnection didStopCapture]
-[CCCameraConnection willStartPersonalPhotographerCapture]
-[CCCameraConnection xpc_stopPersonalPhotographerSessionWithReply:]
Panorama
Cinematic
SpatialPhoto
AvailableAndNotSuggested
EnabledAndNotSuggested
com.apple.companion.camera.device-disconnected
-[CCCameraConnection takePhotoWithCountdown:]
(unknown: %i)
com.apple.NanoCamera
ViewfinderReliability
DaemonXPCConnectionInvalidation
-[CCCameraConnection _checkin]
not-included
\xf0Q
SpatialVideo
Active
-[CCCameraConnection dealloc]
OnOff
-[CCCameraConnection _connect]
-[CCCameraConnection cameraViewfinderSessionPreviewStreamDidOpen:]
NC_FigNeroStartErr
FigCameraViewfinderCreation
v16@?0@\"NSError\"8
-[CCCameraConnection personalPhotographerModeDidChange:]
DeviceTooHot
FigCameraViewfinderSessionPreviewStreamDidClose
-[CCCameraConnection _disconnect]
Unsupported
EnabledWideDualLowLightAvailable
-[CCCameraConnection xpc_suspend]
LensOccluded
preview
com.apple.companion.camera.device-connected
-[CCCameraConnection personalPhotographerSupportDidChange:]
-[CCCameraConnection cameraViewfinderSession:didCapturePhotoWithStatus:thumbnailData:timestamp:]
Unknown
Front
FigCameraViewfinderSessionOpenPreviewStream
-[CCCameraConnection xpc_endBurstCaptureWithReply:]
-[CCCameraConnection cameraViewfinder:viewfinderSessionDidEnd:]
Timelapse
NC_FigNeroStopErr
-[CCCameraConnection burstCaptureDidStop]
-[CCCameraConnection willStartCapturing]
Photo
AutoOnOff
PeakPowerExceeded
OpenCameraMessageReceived
CameraPreviewIDSSocketCreationFailed
PortraitUpsideDown
LandscapeRight
Off
-[CCCameraConnection init]
-[CCCameraConnection cameraViewfinder:viewfinderSessionDidBegin:]
Square
NC_FigNeroDisconnectionRetryAttempt
CC_SessionPreviewStreamDidClose
-[CCCameraConnection personalPhotographerStatusDidChange:]
CC_UnpexpectedInstanceCount
code=%@ status=%d
-[CCCameraConnection xpc_startPersonalPhotographerSessionWithReply:]
AvailableAndSuggested
EnabledAndSuggested
com.apple.companion.camera
-[CCCameraConnection xpc_beginBurstCaptureWithReply:]
{CGPoint=dd}
AutoOff
BackgroundTooFar
%@: %lu\n
TooMuchLight
status
v12@?0i8
Portrait
Auto
CameraAppLaunchFailed
-[CCCameraConnection _handleInterruption]
-[CCCameraConnection xpc_startCaptureWithMode:reply:]
Video
NotEnoughLightWideDualLowLightAvailable
i
-[CCCameraConnection didStartCaptureTimer]
-[CCCameraConnection _handleInvalidation]
SubjectTooFar
DaemonXPCConnectionReceived
q
FigCameraViewfinderSessionDidEnd
-[CCCameraConnection burstCaptureWillStart]
VisualIntelligence
NotSupported
/Library/Caches/com.apple.xbs/A4666B86-B326-4270-BD15-A26D8A288A6B/TemporaryDirectory.PeO2Rh/Sources/NanoCamera/CompanionCamera/CCCameraConnection.m
-[CCCameraConnection didStopPersonalPhotographerCapture]
-[CCCameraConnection xpc_setCaptureMode:reply:]
-[CCCameraConnection _openPreview]
Disabled
app
ViewfinderReliability_CheckRepeatedEvents
FigCameraViewfinderSessionDidBegin
v8@?0
-[CCCameraConnection personalPhotographerSessionTimerStateDidChange:]
Enabled
ViewfinderErrorReporter
CameraAppLaunchhSucceeded
-[CCCameraConnection didResumeCaptureTimerWithNewStartTime:]
-[CCCameraConnection xpc_ensureSwitchedToOneOfSupportedCaptureModes:reply:]
-[CCCameraConnection xpc_stopCaptureWithReply:]
-[CCCameraConnection xpc_setPreviewEndpoint:]
-[CCCameraConnection isPreviewConnected]
LandscapeLeft
Slomo
NotEnoughLight
-[CCCameraConnection xpc_setCaptureDevice:reply:]
-[CCCameraConnection xpc_resumeCaptureWithReply:]
Back
SubjectTooClose
control
com.apple.NanoCamera.viewfinderError
@\"NSDictionary\"8@?0
code
-[CCCameraConnection _closePreview]
None
ViewfinderReliability_CheckUnexpectedEvents
CameraAppLaunch
DaemonXPCConnectionInterruption
FigCameraViewfinderSessionPreviewStreamDidOpen
interruption
%@
Forcing mode to %@
Passed invalid focusPoint parameter %@
Opening preview stream, destination: %@, session:%@
Count of events:\n%@
Repeated event: %@
Resumed xpc connection %@
Connection interrupted %lu times
Reset events.
Unexpected event: %@
Device disconnected
invalidation
Preview desired state: %d, current state: %d
Closing preview stream, session:%@
[lifecycle] Skipping sessionDidEnd (mismatch) stored=%@ eventSession=%@
[lifecycle] Skipping streamDidOpen (mismatch) stored=%@ eventSession=%@
[lifecycle] Skipping streamDidCloseWithStatus (mismatch) stored=%@ eventSession=%@
Reporting error %@
%s (%s:%d)
_xpc is %@
captureDevice: %lu
captureMode: %lu
Focus Point: {%.4f, %.4f}
supportedCaptureDevices:%@ captureDevice:%@ supportedCaptureModes:%@ captureMode:%@ capturing:%d captureStartDate:%@ capturingPaused:%d capturePauseDate:%@ orientation:%@ toggleCameraDeviceSupport:%d zoomSupport:%d zoomAmount:%f zoomMagnifi
previewStreamDidCloseWithStatus: %d
Connection interruption limit reached
Device connected
```
