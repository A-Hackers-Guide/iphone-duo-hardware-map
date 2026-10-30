# `BWZoomCommandHandler`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 35 instance variables, 11 properties, 32 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _zoomLock;
f _appliedZoomFactor;
f _lastRequestedZoomFactor;
B _zoomFactorServiced;
@"BWZoomDelayBuffer" _zoomDelayBuffer;
B _clientCanCompensateForDelay;
@"<BWZoomCompletionDelegate>" _zoomCompletionDelegate;
@"<BWZoomCompletionDelegate>" _zoomCompletionDelegateForStereoAudio;
[2{?="value"q"timescale"i"flags"I"epoch"q}] _lastFramePTSes;
i _lastFrameCaptureID;
q _timeForLastRequestedZoomFactor;
{?="value"q"timescale"i"flags"I"epoch"q} _rampStartTime;
f _rampAcceleration;
f _rampStartFactor;
f _rampStartVelocity;
f _rampTargetFactor;
f _rampTargetVelocity;
i _rampCommandID;
B _rampActive;
i _rampType;
i _rampTuning;
d _rampDuration;
f _rampSnapFraction;
f _rampCurrentVelocity;
f _rampZoomFactorOfInterest;
@"NSArray" _fudgedZoomRanges;
f _maxZoomFactorToApplyFudge;
f _minZoomFactorToApplyFudge;
f _maxFudgedZoomFactor;
f _minFudgedZoomFactor;
f _springRampTension;
f _springRampFriction;
f _earlySwitchOverScaleFactorForZoomIn;
f _allowableMinimumDigitalZoomFactorDuringZoomOut;
i _springRampStartFrameDelayAt30fps;
```

## Properties

```
@property (Tf) requestedZoomFactor;
@property (Tf,R) requestedZoomFactorWithoutFudge;
@property (Tf,R) appliedZoomFactor;
@property (Tf,R) appliedZoomFactorWithoutFudge;
@property (Tf,R) rampTargetZoomFactor;
@property (Tf,R) earlySwitchOverScaleFactorForZoomIn;
@property (Tf,R) allowableMinimumDigitalZoomFactorDuringZoomOut;
@property (Ti,R) rampTuning;
@property (Tf,R) rampZoomFactorOfInterest;
@property (T@"<BWZoomCompletionDelegate>",N,V_zoomCompletionDelegate) zoomCompletionDelegate;
@property (T@"<BWZoomCompletionDelegate>",N,V_zoomCompletionDelegateForStereoAudio) zoomCompletionDelegateForStereoAudio;
```

## Class methods

```
+[BWZoomCommandHandler initialize];
```

## Instance methods

```
-[BWZoomCommandHandler rampTargetZoomFactor];
-[BWZoomCommandHandler zoomCompletionDelegateForStereoAudio];
-[BWZoomCommandHandler setFudgedZoomRanges:];
-[BWZoomCommandHandler init];
-[BWZoomCommandHandler setRequestedZoomFactor:];
-[BWZoomCommandHandler appliedZoomFactorWithoutFudge];
-[BWZoomCommandHandler dealloc];
-[BWZoomCommandHandler timeForLastRequestedZoomFactor];
-[BWZoomCommandHandler reset];
-[BWZoomCommandHandler resetZoomFactorOfInterest];
-[BWZoomCommandHandler requestedZoomFactor];
-[BWZoomCommandHandler updateRampTargetZoomFactor:];
-[BWZoomCommandHandler earlySwitchOverScaleFactorForZoomIn];
-[BWZoomCommandHandler removeFudgeFromZoomFactor:];
-[BWZoomCommandHandler appliedZoomFactor];
-[BWZoomCommandHandler setZoomCompletionDelegate:];
-[BWZoomCommandHandler predictRampZoomFactorAfterNumberOfFrames:settingZoomFactorOfInterest:];
-[BWZoomCommandHandler setZoomFactor:continueExistingRamp:];
-[BWZoomCommandHandler setZoomCompletionDelegateForStereoAudio:];
-[BWZoomCommandHandler updateISPZoomDelay:];
-[BWZoomCommandHandler applyFudgeToZoomFactor:];
-[BWZoomCommandHandler updateZoomModelAndAppliedZoomFactorForNextFrameWithPTS:captureID:delayedISPAppliedZoomFactor:];
-[BWZoomCommandHandler rampZoomFactorOfInterest];
-[BWZoomCommandHandler updateZoomModelForNextFrameWithPTS:captureID:];
-[BWZoomCommandHandler setTypicalISPZoomDelay:maxISPZoomDelay:clientCanCompensateForDelay:];
-[BWZoomCommandHandler rampToVideoZoomFactor:withRampType:rate:duration:snapToTargetZoomFactorWithinRampFraction:rampTuning:earlySwitchOverScaleFactorForZoomIn:allowableMinimumDigitalZoomFactorDuringZoomOut:commandID:];
-[BWZoomCommandHandler requestedZoomFactorWithoutFudge];
-[BWZoomCommandHandler rampTuning];
-[BWZoomCommandHandler rampToVideoZoomFactor:usingSpringWithTension:friction:snapFraction:rampTuning:earlySwitchOverScaleFactorForZoomIn:allowableMinimumDigitalZoomFactorDuringZoomOut:rampStartFrameDelayAt30fps:commandID:];
-[BWZoomCommandHandler updateAppliedZoomFactorForDelayedISPAppliedZoomFactor:];
-[BWZoomCommandHandler allowableMinimumDigitalZoomFactorDuringZoomOut];
-[BWZoomCommandHandler zoomCompletionDelegate];
```
