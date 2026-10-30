# `SBPIPSplitPIPSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 16 instance variables, 16 properties, 33 instance methods, 1 class methods

## Instance variables

```
B _allowSplitPIPEverywhere;
@"SBFFluidBehaviorSettings" _pipResizeSettings;
@"SBFFluidBehaviorSettings" _applicationResizeSettings;
@"SBFFluidBehaviorSettings" _stagingDropSettings;
@"SBFFluidBehaviorSettings" _stagingEnterResizeSettings;
@"SBFFluidBehaviorSettings" _stagingExitResizeSettings;
d _stagingDecelerationDipThreshold;
d _stagingDecelerationDipMinimumStraightness;
d _stagingHoldVelocity;
d _stagingHoldDuration;
d _stagingHoldResetVelocity;
d _stagingDecelerationRatio;
d _stagingMinimumPeakVelocity;
d _stagingPeakSpeedWindow;
d _keyboardMinimumHeightFraction;
d _keyboardCompactVideoScale;
```

## Properties

```
@property (T@"SBFFluidBehaviorSettings",&,N,V_pipResizeSettings) pipResizeSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_applicationResizeSettings) applicationResizeSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_stagingDropSettings) stagingDropSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_stagingEnterResizeSettings) stagingEnterResizeSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_stagingExitResizeSettings) stagingExitResizeSettings;
@property (Td,N,V_stagingDecelerationDipThreshold) stagingDecelerationDipThreshold;
@property (Td,N,V_stagingDecelerationDipMinimumStraightness) stagingDecelerationDipMinimumStraightness;
@property (Td,N,V_stagingHoldVelocity) stagingHoldVelocity;
@property (Td,N,V_stagingHoldDuration) stagingHoldDuration;
@property (Td,N,V_stagingHoldResetVelocity) stagingHoldResetVelocity;
@property (Td,N,V_stagingDecelerationRatio) stagingDecelerationRatio;
@property (Td,N,V_stagingMinimumPeakVelocity) stagingMinimumPeakVelocity;
@property (Td,N,V_stagingPeakSpeedWindow) stagingPeakSpeedWindow;
@property (TB,N,V_allowSplitPIPEverywhere) allowSplitPIPEverywhere;
@property (Td,N,V_keyboardMinimumHeightFraction) keyboardMinimumHeightFraction;
@property (Td,N,V_keyboardCompactVideoScale) keyboardCompactVideoScale;
```

## Class methods

```
+[SBPIPSplitPIPSettings settingsControllerModule];
```

## Instance methods

```
-[SBPIPSplitPIPSettings setDefaultValues];
-[SBPIPSplitPIPSettings stagingDecelerationDipThreshold];
-[SBPIPSplitPIPSettings allowSplitPIPEverywhere];
-[SBPIPSplitPIPSettings applicationResizeSettings];
-[SBPIPSplitPIPSettings keyboardCompactVideoScale];
-[SBPIPSplitPIPSettings keyboardMinimumHeightFraction];
-[SBPIPSplitPIPSettings pipResizeSettings];
-[SBPIPSplitPIPSettings setAllowSplitPIPEverywhere:];
-[SBPIPSplitPIPSettings setApplicationResizeSettings:];
-[SBPIPSplitPIPSettings setKeyboardCompactVideoScale:];
-[SBPIPSplitPIPSettings setKeyboardMinimumHeightFraction:];
-[SBPIPSplitPIPSettings setPipResizeSettings:];
-[SBPIPSplitPIPSettings setStagingDecelerationDipMinimumStraightness:];
-[SBPIPSplitPIPSettings setStagingDecelerationDipThreshold:];
-[SBPIPSplitPIPSettings setStagingDecelerationRatio:];
-[SBPIPSplitPIPSettings setStagingDropSettings:];
-[SBPIPSplitPIPSettings setStagingEnterResizeSettings:];
-[SBPIPSplitPIPSettings setStagingExitResizeSettings:];
-[SBPIPSplitPIPSettings setStagingHoldDuration:];
-[SBPIPSplitPIPSettings setStagingHoldResetVelocity:];
-[SBPIPSplitPIPSettings setStagingHoldVelocity:];
-[SBPIPSplitPIPSettings setStagingMinimumPeakVelocity:];
-[SBPIPSplitPIPSettings setStagingPeakSpeedWindow:];
-[SBPIPSplitPIPSettings stagingDecelerationDipMinimumStraightness];
-[SBPIPSplitPIPSettings stagingDecelerationRatio];
-[SBPIPSplitPIPSettings stagingDropSettings];
-[SBPIPSplitPIPSettings stagingEnterResizeSettings];
-[SBPIPSplitPIPSettings stagingExitResizeSettings];
-[SBPIPSplitPIPSettings stagingHoldDuration];
-[SBPIPSplitPIPSettings stagingHoldResetVelocity];
-[SBPIPSplitPIPSettings stagingHoldVelocity];
-[SBPIPSplitPIPSettings stagingMinimumPeakVelocity];
-[SBPIPSplitPIPSettings stagingPeakSpeedWindow];
```
