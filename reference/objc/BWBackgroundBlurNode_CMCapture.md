# `BWBackgroundBlurNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- Protocols: `FigCaptureDisplayLayoutObserver`, `BWPortraitEffectPropertiesDelegate`
- 55 instance variables, 14 properties, 38 instance methods, 1 class methods

## Instance variables

```
^{opaqueCMFormatDescription=} _outputFormatDescription;
@"BWLimitedGMErrorLogger" _limitedGMErrorLogger;
@"PTEffect" _ptEffect;
@"PTEffect" _reconfiguredPTEffect;
@"<MTLCommandQueue>" _metalCommandQueue;
@"NSObject<OS_dispatch_queue>" _ptEffectReleaseQueue;
@"BWNodeInput" _videoInput;
@"BWNodeOutput" _videoOutput;
@"BWNodeInput" _stillImageInput;
@"BWNodeOutput" _stillImageOutput;
B _stillImageCaptureEnabled;
^{OpaqueVTPixelTransferSession=} _stillImagePixelTransferSession;
[2{?="sampleBuffer"^{opaqueCMSampleBuffer}"pts"{?="value"q"timescale"i"flags"I"epoch"q}}] _stillCaptureQueue;
I _stillCaptureEnqueueIndex;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _bufferServicingLock;
i _deviceType;
@"NSString" _clientApplicationID;
i _continuityCameraClientDeviceClass;
@"BWStats" _backgroundBlurProcessingTimeStats;
i _numberOfFramesThatCouldNotBeBlurred;
i _maxThermalSystemPressureLevel;
B _previousEffectBypassed;
@"NSObject<OS_dispatch_queue>" _asyncInitQueue;
@"NSObject<OS_dispatch_queue>" _asyncProcessingQueue;
i _maxLossyCompressionLevel;
B _isHighQualityEffectSupported;
B _fastSwitchEnabled;
B _effectBypassed;
Q _activeBlurEffect;
Q _availablePTEffects;
B _upstreamDeviceOrientationCorrectionEnabled;
@"BWDeviceOrientationMonitor" _deviceOrientationMonitor;
q _activeDisplayRegion;
q _activeInterfaceOrientation;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _activeDisplayRegionLock;
B _registeredAsDisplayLayoutObserver;
@"PTEffectRenderRequest" _ptEffectRenderRequest;
f _backgroundBlurAperture;
f _studioLightingIntensity;
B _gesturesEnabled;
B _suppressedGesturesEnabled;
^{__CVBuffer=} _backgroundReplacementPixelBuffer;
@"NSMutableArray" _pendingPTEffectReactions;
q _reactionCounterAPI;
I _reactionCounterAll;
{?="value"q"timescale"i"flags"I"epoch"q} _lastRenderPTS;
@"NSMutableDictionary" _lastActiveReactions;
B _activeReactionsDirty;
@? _reactionsInProgressObserver;
@? _suppressedGestureObserver;
{?="value"q"timescale"i"flags"I"epoch"q} _framerateThrottleNextPTS;
@"BWRingLightController" _ringLightController;
@"<BWBackgroundBlurNodeRingLightScreenNitsEstimationEnabledChangedDelegate>" _ringLightScreenNitsEstimationEnabledChangedDelegate;
@"BWDeviceThermalMonitor" _thermalMonitor;
q _effectQuality;
```

## Properties

```
@property (Tq,N,V_effectQuality) effectQuality;
@property (T@"BWNodeInput",R,N,V_videoInput) videoInput;
@property (T@"BWNodeOutput",R,N,V_videoOutput) videoOutput;
@property (T@"BWNodeInput",R,N,V_stillImageInput) stillImageInput;
@property (T@"BWNodeOutput",R,N,V_stillImageOutput) stillImageOutput;
@property (T@"NSString",C,N,V_clientApplicationID) clientApplicationID;
@property (Ti,N,V_continuityCameraClientDeviceClass) continuityCameraClientDeviceClass;
@property (TB,N,V_effectBypassed) effectBypassed;
@property (TQ,N) activeBlurEffect;
@property (TB,N) ringLightEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWBackgroundBlurNode initialize];
```

## Instance methods

```
-[BWBackgroundBlurNode setContinuityCameraClientDeviceClass:];
-[BWBackgroundBlurNode prepareForCurrentConfigurationToBecomeLive];
-[BWBackgroundBlurNode reactionCount];
-[BWBackgroundBlurNode effectQuality];
-[BWBackgroundBlurNode renderSampleBuffer:forInput:];
-[BWBackgroundBlurNode didChangeStudioLightingIntensity:];
-[BWBackgroundBlurNode layoutMonitor:didUpdateLayout:];
-[BWBackgroundBlurNode setSuppressedGestureHandler:];
-[BWBackgroundBlurNode dealloc];
-[BWBackgroundBlurNode setReactionsInProgressChangedHandler:];
-[BWBackgroundBlurNode setEffectQuality:];
-[BWBackgroundBlurNode setRingLightEnabled:];
-[BWBackgroundBlurNode setClientApplicationID:];
-[BWBackgroundBlurNode continuityCameraClientDeviceClass];
-[BWBackgroundBlurNode didChangeBackgroundBlurAperture:];
-[BWBackgroundBlurNode didChangeSuppressedGesturesEnabled:];
-[BWBackgroundBlurNode videoOutput];
-[BWBackgroundBlurNode didChangeGesturesEnabled:];
-[BWBackgroundBlurNode didReachEndOfDataForConfigurationID:input:];
-[BWBackgroundBlurNode ringLightEnabled];
-[BWBackgroundBlurNode performReactionEffect:];
-[BWBackgroundBlurNode nodeSubType];
-[BWBackgroundBlurNode lowPowerModeChanged:];
-[BWBackgroundBlurNode didSelectFormat:forInput:];
-[BWBackgroundBlurNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWBackgroundBlurNode didChangeBackgroundReplacementPixelBuffer:];
-[BWBackgroundBlurNode stillImageOutput];
-[BWBackgroundBlurNode nodeType];
-[BWBackgroundBlurNode didChangePortraitEffectStudioLightQuality:];
-[BWBackgroundBlurNode clientApplicationID];
-[BWBackgroundBlurNode stillImageInput];
-[BWBackgroundBlurNode activeBlurEffect];
-[BWBackgroundBlurNode effectBypassed];
-[BWBackgroundBlurNode initWithStillImageCaptureEnabled:maxLossyCompressionLevel:fastSwitchEnabled:availableEffects:activeEffect:isHighQualitySupported:upstreamDeviceOrientationCorrectionEnabled:deviceType:captureDevice:];
-[BWBackgroundBlurNode setActiveBlurEffect:];
-[BWBackgroundBlurNode setEffectBypassed:];
-[BWBackgroundBlurNode setRingLightScreenNitsEstimationEnabledChangedDelegate:];
-[BWBackgroundBlurNode videoInput];
```
