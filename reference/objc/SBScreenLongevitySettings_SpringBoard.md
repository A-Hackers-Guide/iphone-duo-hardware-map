# `SBScreenLongevitySettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 14 instance variables, 14 properties, 29 instance methods, 1 class methods

## Instance variables

```
B _ignoreAutoLockSetToNever;
B _overrideEnablement;
B _enablement;
B _noisyLogging;
B _noOpButLogOnEnablementUpdate;
B _userPreferencesEnablement;
d _dimInterval;
d _waitInterval;
d _minimalFaceDetectionInterval;
d _undimFaceDetectionInterval;
d _touchAttentionLostTimeout;
d _dimmingAnimationLength;
d _undimmingAnimationLength;
d _faceDetectionScoreThreshold;
```

## Properties

```
@property (TB,N,V_ignoreAutoLockSetToNever) ignoreAutoLockSetToNever;
@property (TB,N,V_overrideEnablement) overrideEnablement;
@property (TB,N,V_enablement) enablement;
@property (Td,N,V_dimInterval) dimInterval;
@property (Td,N,V_waitInterval) waitInterval;
@property (Td,N,V_minimalFaceDetectionInterval) minimalFaceDetectionInterval;
@property (Td,N,V_undimFaceDetectionInterval) undimFaceDetectionInterval;
@property (Td,N,V_touchAttentionLostTimeout) touchAttentionLostTimeout;
@property (Td,N,V_dimmingAnimationLength) dimmingAnimationLength;
@property (Td,N,V_undimmingAnimationLength) undimmingAnimationLength;
@property (Td,N,V_faceDetectionScoreThreshold) faceDetectionScoreThreshold;
@property (TB,N,V_noisyLogging) noisyLogging;
@property (TB,N,V_noOpButLogOnEnablementUpdate) noOpButLogOnEnablementUpdate;
@property (TB,N,V_userPreferencesEnablement) userPreferencesEnablement;
```

## Class methods

```
+[SBScreenLongevitySettings settingsControllerModule];
```

## Instance methods

```
-[SBScreenLongevitySettings setEnablement:];
-[SBScreenLongevitySettings setDefaultValues];
-[SBScreenLongevitySettings enablement];
-[SBScreenLongevitySettings setDimInterval:];
-[SBScreenLongevitySettings setFaceDetectionScoreThreshold:];
-[SBScreenLongevitySettings dimInterval];
-[SBScreenLongevitySettings dimmingAnimationLength];
-[SBScreenLongevitySettings faceDetectionScoreThreshold];
-[SBScreenLongevitySettings ignoreAutoLockSetToNever];
-[SBScreenLongevitySettings minimalFaceDetectionInterval];
-[SBScreenLongevitySettings noOpButLogOnEnablementUpdate];
-[SBScreenLongevitySettings noisyLogging];
-[SBScreenLongevitySettings overrideEnablement];
-[SBScreenLongevitySettings setDimmingAnimationLength:];
-[SBScreenLongevitySettings setIgnoreAutoLockSetToNever:];
-[SBScreenLongevitySettings setMinimalFaceDetectionInterval:];
-[SBScreenLongevitySettings setNoOpButLogOnEnablementUpdate:];
-[SBScreenLongevitySettings setNoisyLogging:];
-[SBScreenLongevitySettings setOverrideEnablement:];
-[SBScreenLongevitySettings setTouchAttentionLostTimeout:];
-[SBScreenLongevitySettings setUndimFaceDetectionInterval:];
-[SBScreenLongevitySettings setUndimmingAnimationLength:];
-[SBScreenLongevitySettings setUserPreferencesEnablement:];
-[SBScreenLongevitySettings setWaitInterval:];
-[SBScreenLongevitySettings touchAttentionLostTimeout];
-[SBScreenLongevitySettings undimFaceDetectionInterval];
-[SBScreenLongevitySettings undimmingAnimationLength];
-[SBScreenLongevitySettings userPreferencesEnablement];
-[SBScreenLongevitySettings waitInterval];
```
