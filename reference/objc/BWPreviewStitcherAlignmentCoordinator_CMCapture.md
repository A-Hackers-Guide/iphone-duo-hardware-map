# `BWPreviewStitcherAlignmentCoordinator`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 21 instance variables, 7 properties, 23 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _cameraInfo;
B _excludeStaticComponentFromAlignmentShiftsEnabled;
B _superWideSensorCenterOffsetEnabled;
f _perFrameAlignmentShiftSmoothingFactor;
B _applyCameraShift;
[2{CGPoint="x"d"y"d}] _perFrameAlignmentShifts;
[2[3{BWPreviewStitcherRegistrationShift="currentValue"{CGPoint="x"d"y"d}"targetValue"{CGPoint="x"d"y"d}"valueIsUpdated"B"lastRegistrationWasValid"B"registeredFrameCaptureID"i"rampX"@"BWRamp""rampY"@"BWRamp"}]] _registrationShifts;
i _numFramesToRamp;
i _frameCaptureID;
{?="value"q"timescale"i"flags"I"epoch"q} _currentPTS;
i _currentPairType;
f _narrowerCameraNondisruptiveSwitchingScaleFactor;
f _widerCameraNondisruptiveSwitchingScaleFactor;
[2i] _lastRegisteredFrameCaptureID;
i _lastRegisteredPairType;
{CGPoint="x"d"y"d} _lastRegisteredPerFrameAlignmentShift;
f _lastRegisteredWiderCameraNondisruptiveSwitchingScaleFactor;
[3{CGPoint="x"d"y"d}] _widerCameraRegionPresentationShifts;
{CGPoint="x"d"y"d} _nextNarrowerCameraPresentationShift;
B _registrationEnabled;
B _firstRegistrationCompleted;
```

## Properties

```
@property (TB,R,N,V_excludeStaticComponentFromAlignmentShiftsEnabled) excludeStaticComponentFromAlignmentShiftsEnabled;
@property (TB,R,N) registrationEnabled;
@property (TB,R,N,V_firstRegistrationCompleted) firstRegistrationCompleted;
@property (Tq,R,N) numberOfFramesSinceLastRegistration;
@property (TB,R,N) registrationIsReady;
@property (TB,R,N) centerRegistrationValid;
@property (T{CGPoint=dd},R,N,V_nextNarrowerCameraPresentationShift) nextNarrowerCameraPresentationShift;
```

## Class methods

```
+[BWPreviewStitcherAlignmentCoordinator initialize];
```

## Instance methods

```
-[BWPreviewStitcherAlignmentCoordinator setIsRegisteringForFrameCaptureID:];
-[BWPreviewStitcherAlignmentCoordinator centerWiderCameraPresentationShiftWithAppliedScale:offset:];
-[BWPreviewStitcherAlignmentCoordinator runRegistrationShiftRampsWithOverrideEdgesToCenterShift:];
-[BWPreviewStitcherAlignmentCoordinator initWithCameraInfoArray:excludeStaticComponentFromAlignmentShifts:];
-[BWPreviewStitcherAlignmentCoordinator leftWiderCameraPresentationShiftWithAppliedScale:offset:];
-[BWPreviewStitcherAlignmentCoordinator dealloc];
-[BWPreviewStitcherAlignmentCoordinator startRegistrationShiftRampsWithNumFrames:];
-[BWPreviewStitcherAlignmentCoordinator numberOfFramesSinceLastRegistration];
-[BWPreviewStitcherAlignmentCoordinator centerRegistrationValid];
-[BWPreviewStitcherAlignmentCoordinator nextNarrowerCameraPresentationShift];
-[BWPreviewStitcherAlignmentCoordinator registrationIsReady];
-[BWPreviewStitcherAlignmentCoordinator _perFrameAlignmentShiftForCurrentPair];
-[BWPreviewStitcherAlignmentCoordinator setTargetRegistrationShiftsWithApproximateCorrection:];
-[BWPreviewStitcherAlignmentCoordinator cancelRegistrationShiftRampsWithOverrideEdgesToCenterShift:rampEdgesToCenter:];
-[BWPreviewStitcherAlignmentCoordinator firstRegistrationCompleted];
-[BWPreviewStitcherAlignmentCoordinator _widerCameraPresentationShiftForRegion:withAppliedScale:offset:];
-[BWPreviewStitcherAlignmentCoordinator rightWiderCameraPresentationShiftWithAppliedScale:offset:];
-[BWPreviewStitcherAlignmentCoordinator registrationEnabled];
-[BWPreviewStitcherAlignmentCoordinator setTargetRegistrationShiftsWithRegistrationResult:];
-[BWPreviewStitcherAlignmentCoordinator updateWithFramePairInfo:perFrameAlignmentShift:];
-[BWPreviewStitcherAlignmentCoordinator _perFrameAlignmentShiftForPairType:];
-[BWPreviewStitcherAlignmentCoordinator excludeStaticComponentFromAlignmentShiftsEnabled];
-[BWPreviewStitcherAlignmentCoordinator targetCenterRegistrationShiftForCameraPairType:];
```
