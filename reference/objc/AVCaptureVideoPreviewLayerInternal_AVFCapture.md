# `AVCaptureVideoPreviewLayerInternal`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 52 instance variables, 0 properties, 0 instance methods, 0 class methods

## Instance variables

```
@"NSString" sinkID;
@"AVCaptureSession" session;
@"AVCaptureConnection" connection;
^{OpaqueFigCaptureSession=} figCaptureSession;
@"NSObject<OS_dispatch_queue>" figCaptureSessionSyncQueue;
@"CALayer" sublayer;
{CGSize="width"d"height"d} sensorSize;
@"NSString" sensorToPreviewVTScalingMode;
I imageQueueSlot;
{CGSize="width"d"height"d} previewSize;
d previewRotationDegrees;
@"NSString" gravity;
B disableActions;
@"AVWeakReference" weakReference;
B isPreviewing;
q orientation;
B automaticallyAdjustsMirroring;
B mirrored;
B isPresentationLayer;
B visible;
B isPaused;
B chromaNoiseReductionEnabled;
i changeSeed;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} captureDeviceTransform;
d rollAdjustment;
B depthDataDeliverySupported;
B depthDataDeliveryEnabled;
B filterRenderingEnabled;
B unoptimizedFilterRenderingEnabled;
@"NSArray" videoPreviewFilters;
B semanticStyleRenderingSupported;
B semanticStyleRenderingEnabled;
@"AVSemanticStyle" semanticStyle;
d oddScreenWidth;
d oddScreenScale;
B portraitAutoSuggestEnabled;
B portraitAutoSuggestSupported;
B zoomPictureInPictureOverlaySupported;
B zoomPictureInPictureOverlayEnabled;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} zoomPictureInPictureOverlayRect;
B deferredStartEnabled;
i didStartPreviewingWithImageQueueNilCount;
B requestedPreferredDynamicRangeHigh;
B clientLaunchTelemetryEnabled;
B undimOnNextFirstPreviewFrame;
@"NSObject<OS_dispatch_source>" previewMonitorTimer;
@"NSObject<OS_dispatch_queue>" previewMonitorTimerQueue;
d previewMonitorTimerStartTime;
B previewMonitorDidDisplayFirstPreviewFrame;
B previewMonitorStoppedBySession;
B previewMonitorClientWantsPreviewDisplayedBySession;
B previewMonitorClientShowingViewfinder;
```
