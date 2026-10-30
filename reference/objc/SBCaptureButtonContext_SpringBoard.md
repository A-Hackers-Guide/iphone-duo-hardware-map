# `SBCaptureButtonContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBDictionaryRepresentable`
- 30 instance variables, 34 properties, 77 instance methods, 4 class methods

## Instance variables

```
B _inGameMode;
B _uiLocked;
B _inCameraPose;
B _cameraPrewarmed;
B _suppressedOnButtonDown;
B _prewarmLockoutActive;
B _inAmbientPresentationMode;
B _connectedToWirelessCharger;
B _voiceOverScreenCurtainActive;
B _wantsClickAgain;
Q _machAbsoluteTimestamp;
Q _event;
Q _gesture;
Q _inGameModeStreakCount;
q _backlightState;
d _timeSinceLastViewUnobstructed;
d _timeSinceLastStationary;
d _timeSinceLastNonStationary;
d _timeSinceLastStationarySquelch;
d _lowLatencyTimeSinceLastStationary;
d _lowLatencyTimeSinceLastNonStationary;
@"SBDeviceMotionVector" _gravity;
@"SBDeviceMotionVector" _rotationRate;
q _deviceOrientation;
@"SBCaptureButtonPolicy" _policy;
q _suppressionState;
@"NSString" _captureAppBundleID;
@"NSString" _foregroundAppBundleID;
d _pressDuration;
d _timeSinceLastClickAgainCoaching;
```

## Properties

```
@property (TQ,N,V_machAbsoluteTimestamp) machAbsoluteTimestamp;
@property (TQ,N,V_event) event;
@property (TQ,N,V_gesture) gesture;
@property (TB,N,V_inGameMode) inGameMode;
@property (TQ,N,V_inGameModeStreakCount) inGameModeStreakCount;
@property (Tq,N,V_backlightState) backlightState;
@property (Td,N,V_timeSinceLastViewUnobstructed) timeSinceLastViewUnobstructed;
@property (TB,N,V_uiLocked) uiLocked;
@property (Td,N,V_timeSinceLastStationary) timeSinceLastStationary;
@property (Td,N,V_timeSinceLastNonStationary) timeSinceLastNonStationary;
@property (Td,N,V_timeSinceLastStationarySquelch) timeSinceLastStationarySquelch;
@property (Td,N,V_lowLatencyTimeSinceLastStationary) lowLatencyTimeSinceLastStationary;
@property (Td,N,V_lowLatencyTimeSinceLastNonStationary) lowLatencyTimeSinceLastNonStationary;
@property (TB,N,V_inCameraPose) inCameraPose;
@property (T@"SBDeviceMotionVector",&,N,V_gravity) gravity;
@property (T@"SBDeviceMotionVector",&,N,V_rotationRate) rotationRate;
@property (Tq,N,V_deviceOrientation) deviceOrientation;
@property (T@"SBCaptureButtonPolicy",&,N,V_policy) policy;
@property (TB,N,V_cameraPrewarmed) cameraPrewarmed;
@property (TB,N,V_suppressedOnButtonDown) suppressedOnButtonDown;
@property (Tq,N,V_suppressionState) suppressionState;
@property (TB,N,GisPrewarmLockoutActive,V_prewarmLockoutActive) prewarmLockoutActive;
@property (T@"NSString",C,N,V_captureAppBundleID) captureAppBundleID;
@property (T@"NSString",C,N,V_foregroundAppBundleID) foregroundAppBundleID;
@property (Td,N,V_pressDuration) pressDuration;
@property (TB,N,GisInAmbientPresentationMode,V_inAmbientPresentationMode) inAmbientPresentationMode;
@property (TB,N,GisConnectedToWirelessCharger,V_connectedToWirelessCharger) connectedToWirelessCharger;
@property (TB,N,GisVoiceOverScreenCurtainActive,V_voiceOverScreenCurtainActive) voiceOverScreenCurtainActive;
@property (TB,N,V_wantsClickAgain) wantsClickAgain;
@property (Td,N,V_timeSinceLastClickAgainCoaching) timeSinceLastClickAgainCoaching;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBCaptureButtonContext defaultContext];
+[SBCaptureButtonContext defaultPolicy];
+[SBCaptureButtonContext defaultGravity];
+[SBCaptureButtonContext defaultRotationRate];
```

## Instance methods

```
-[SBCaptureButtonContext setEvent:];
-[SBCaptureButtonContext isSuppressed];
-[SBCaptureButtonContext setDeviceOrientation:];
-[SBCaptureButtonContext setBacklightState:];
-[SBCaptureButtonContext deviceOrientation];
-[SBCaptureButtonContext isScreenOn];
-[SBCaptureButtonContext setPressDuration:];
-[SBCaptureButtonContext setGesture:];
-[SBCaptureButtonContext initWithDictionary:];
-[SBCaptureButtonContext succinctDescriptionBuilder];
-[SBCaptureButtonContext uiLocked];
-[SBCaptureButtonContext event];
-[SBCaptureButtonContext pressDuration];
-[SBCaptureButtonContext foregroundAppBundleID];
-[SBCaptureButtonContext descriptionWithMultilinePrefix:];
-[SBCaptureButtonContext succinctDescription];
-[SBCaptureButtonContext backlightState];
-[SBCaptureButtonContext gravity];
-[SBCaptureButtonContext hash];
-[SBCaptureButtonContext description];
-[SBCaptureButtonContext gesture];
-[SBCaptureButtonContext setGravity:];
-[SBCaptureButtonContext isEqual:];
-[SBCaptureButtonContext setPolicy:];
-[SBCaptureButtonContext setUiLocked:];
-[SBCaptureButtonContext descriptionBuilderWithMultilinePrefix:];
-[SBCaptureButtonContext dictionaryRepresentation];
-[SBCaptureButtonContext policy];
-[SBCaptureButtonContext rotationRate];
-[SBCaptureButtonContext setRotationRate:];
-[SBCaptureButtonContext suppressionState];
-[SBCaptureButtonContext isWithinDirectLaunchGracePeriod];
-[SBCaptureButtonContext cameraPrewarmed];
-[SBCaptureButtonContext computedContext];
-[SBCaptureButtonContext shouldSuspendLaunchOnButtonDown];
-[SBCaptureButtonContext stationaryState];
-[SBCaptureButtonContext timeSinceLastClickAgainCoaching];
-[SBCaptureButtonContext wantsClickAgain];
-[SBCaptureButtonContext captureAppBundleID];
-[SBCaptureButtonContext inCameraPose];
-[SBCaptureButtonContext inGameMode];
-[SBCaptureButtonContext inGameModeStreakCount];
-[SBCaptureButtonContext initWithEvent:gesture:machAbsoluteTimestamp:consoleModeActive:consoleModeActiveStreakCount:backlightState:timeSinceLastViewUnobstructed:uiLocked:timeSinceLastStationary:timeSinceLastNonStationary:timeSinceLastStationarySquelch:lowLatencyTimeSinceLastStationary:lowLatencyTimeSinceLastNonStationary:inCameraPose:gravity:rotationRate:deviceOrientation:policy:cameraPrewarmed:suppressedOnButtonDown:suppressionState:prewarmLockoutActive:captureAppBundleID:pressDuration:foregroundAppBundleID:inAmbientPresentationMode:connectedToWirelessCharger:voiceOverScreenCurtainActive:wantsClickAgain:timeSinceLastClickAgainCoaching:];
-[SBCaptureButtonContext isConnectedToWirelessCharger];
-[SBCaptureButtonContext isInAmbientPresentationMode];
-[SBCaptureButtonContext isPrewarmLockoutActive];
-[SBCaptureButtonContext isVoiceOverScreenCurtainActive];
-[SBCaptureButtonContext isWithinClickAgainTimeout];
-[SBCaptureButtonContext lowLatencyTimeSinceLastNonStationary];
-[SBCaptureButtonContext lowLatencyTimeSinceLastStationary];
-[SBCaptureButtonContext machAbsoluteTimestamp];
-[SBCaptureButtonContext setCameraPrewarmed:];
-[SBCaptureButtonContext setCaptureAppBundleID:];
-[SBCaptureButtonContext setConnectedToWirelessCharger:];
-[SBCaptureButtonContext setForegroundAppBundleID:];
-[SBCaptureButtonContext setInAmbientPresentationMode:];
-[SBCaptureButtonContext setInCameraPose:];
-[SBCaptureButtonContext setInGameMode:];
-[SBCaptureButtonContext setInGameModeStreakCount:];
-[SBCaptureButtonContext setLowLatencyTimeSinceLastNonStationary:];
-[SBCaptureButtonContext setLowLatencyTimeSinceLastStationary:];
-[SBCaptureButtonContext setMachAbsoluteTimestamp:];
-[SBCaptureButtonContext setPrewarmLockoutActive:];
-[SBCaptureButtonContext setSuppressedOnButtonDown:];
-[SBCaptureButtonContext setSuppressionState:];
-[SBCaptureButtonContext setTimeSinceLastClickAgainCoaching:];
-[SBCaptureButtonContext setTimeSinceLastNonStationary:];
-[SBCaptureButtonContext setTimeSinceLastStationary:];
-[SBCaptureButtonContext setTimeSinceLastStationarySquelch:];
-[SBCaptureButtonContext setTimeSinceLastViewUnobstructed:];
-[SBCaptureButtonContext setVoiceOverScreenCurtainActive:];
-[SBCaptureButtonContext setWantsClickAgain:];
-[SBCaptureButtonContext suppressedOnButtonDown];
-[SBCaptureButtonContext timeSinceLastNonStationary];
-[SBCaptureButtonContext timeSinceLastStationary];
-[SBCaptureButtonContext timeSinceLastStationarySquelch];
-[SBCaptureButtonContext timeSinceLastViewUnobstructed];
```
