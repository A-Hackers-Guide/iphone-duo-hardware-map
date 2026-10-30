# `BWRingLightController`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWRingLightDisplayBrightnessObserver`
- 15 instance variables, 8 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"CBClient" _cbClient;
@"CBDisplayClient" _displayClient;
@"CBDisplayBrightnessClient" _displayBrightnessClient;
B _displayBrightnessClientSupportsSDRNits;
@"NSObject<OS_dispatch_queue>" _notifyQueue;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _ringLightEnabledLock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _userBrightnessChangeLock;
B _receivedBrightnessCommitUpdate;
f _userChangeBrightnessInitialNits;
f _userChangeBrightnessFinalNits;
f _deviceMaxScreenNits;
{?="ringLightEnabled"B"ringLightMetadataFile"@"NSString""ringLightColor"f"ringLightWidth"f"ringLightAdjustWidth"B"ringLightRecommendedScreenNitsFloor"f"ringLightMode"q"ringLightOnboardingState"q"ringLightAdaptiveSettings"@"NSData"} _ringLightState;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _ringLightStateLock;
@"BWFigVideoCaptureDevice" _captureDevice;
@"FigWeakReference" _weakReferenceToSelf;
```

## Properties

```
@property (Tf,R,N,V_deviceMaxScreenNits) deviceMaxScreenNits;
@property (TB,N) ringLightEnabled;
@property (TB,R,N) screenNitsEstimationEnabled;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_notifyQueue) notifyQueue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWRingLightController initialize];
```

## Instance methods

```
-[BWRingLightController tearDown];
-[BWRingLightController dealloc];
-[BWRingLightController setRingLightEnabled:];
-[BWRingLightController notifyQueue];
-[BWRingLightController ringLightEnabled];
-[BWRingLightController brightnessCommitUpdate:];
-[BWRingLightController configureEffectDescriptor:];
-[BWRingLightController deviceMaxScreenNits];
-[BWRingLightController initWithDisplayID:captureDevice:];
-[BWRingLightController populateRenderRequest:metadataDictionary:];
-[BWRingLightController prepareRenderRequest:];
-[BWRingLightController processRenderRequestOutput:];
-[BWRingLightController screenNitsEstimationEnabled];
```
