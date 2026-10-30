# `_TtC31VisualIntelligenceCameraSupport26StreamingSessionController`

- Image: [`/System/Library/PrivateFrameworks/VisualIntelligenceCameraSupport.framework/VisualIntelligenceCameraSupport`](../userland/System__Library__PrivateFrameworks__VisualIntelligenceCameraSupport.framework__VisualIntelligenceCameraSupport.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_TtCs12_SwiftObject`
- 29 instance variables, 0 properties, 0 instance methods, 0 class methods

## Instance variables

```
VisualIntelligenceCameraSupport.CameraSourceRunState _runState;
VisualIntelligenceCameraSupport.StreamPausedReason _streamPausedReason;
VisualIntelligenceCameraSupport.PauseRequest ? _latestPauseRequest;
__C.CVBuffer ? _displayFrame;
VisualIntelligenceCameraSupport.CameraCaptureEffectsMedia ? _captureEffectsMedia;
__C.CGRect ? _externalActivationFrameInContentView;
VisualIntelligenceCameraSupport.SaliencyStreamingSession _session;
_$sSi _sessionGeneration;
VisualIntelligenceCore.PresentationGeometry _presentationGeometry;
VisualIntelligenceCore.Angle ? _deferredUIRotation;
_$sScTyyt Swift.Never ? _displayFrameTask;
_$sScTyyt Swift.Never ? _captureEffectsMediaTask;
_$sSayScCyyt Swift.Never _runStateWaiters;
_$sSayScCyyt Swift.Never _captureEffectsMediaWaiters;
VisualIntelligenceCameraSupport.StreamingSessionController.Configuration _configuration;
VisualIntelligenceServices.EntryPoint entryPoint;
VisualIntelligenceCore.TrackManagerSupporting ? _trackManagerSupporting;
Synchronization.Mutex __C.CMTime latestFrameTimestamp;
Synchronization.Mutex VisualIntelligenceCameraSupport.StreamingSessionController.RunStateTracking runStateTracking;
Synchronization.Mutex _$syScT -> Swift.UInt32 Swift.Never ? shutterSoundPrewarm;
Synchronization.Mutex _$syScTyyt Swift.Never ? pendingEvictAll;
Synchronization.Mutex VisualIntelligenceCameraSupport.StreamingSessionController.FrameDeliveryState frameDeliveryState;
_$syycSg _onDisplayFrameArrived;
_$syycSg _onCaptureEffectsMediaArrived;
_$syyYbScMYccSg _onMissedPauseDetected;
VisualIntelligenceCameraSupport.MissedPauseContext ? _latestMissedPauseContext;
os.Logger logger;
VisualIntelligenceServices.VICoreAnalyticsSink ? analyticsSink;
Observation.ObservationRegistrar _$observationRegistrar;
```
