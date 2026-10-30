# `SBSystemAnimationSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 10 instance variables, 10 properties, 21 instance methods, 1 class methods

## Instance variables

```
f _assistantAnimationDuration;
f _assistantDismissAnimationDurationOverApp;
f _assistantBottomEdgeDismissThreshold;
f _assistantBottomEdgeDismissVelocity;
f _spotlightNoninteractiveAnimationDuration;
@"SBFAnimationSettings" _slideoverDosidoAnimationSettings;
@"SBEntityRemovalAnimationSettings" _entityRemovalAnimationSettings;
@"SBFWakeAnimationSettings" _wakeAnimationSettings;
@"SBFFluidBehaviorSettings" _foldRegionAnimationSettings;
@"SBFFluidBehaviorSettings" _cameraExclusionRegionAnimationSettings;
```

## Properties

```
@property (Tf,N,V_assistantAnimationDuration) assistantAnimationDuration;
@property (Tf,N,V_assistantDismissAnimationDurationOverApp) assistantDismissAnimationDurationOverApp;
@property (Tf,N,V_assistantBottomEdgeDismissThreshold) assistantBottomEdgeDismissThreshold;
@property (Tf,N,V_assistantBottomEdgeDismissVelocity) assistantBottomEdgeDismissVelocity;
@property (Tf,N,V_spotlightNoninteractiveAnimationDuration) spotlightNoninteractiveAnimationDuration;
@property (T@"SBFAnimationSettings",&,N,V_slideoverDosidoAnimationSettings) slideoverDosidoAnimationSettings;
@property (T@"SBEntityRemovalAnimationSettings",&,N,V_entityRemovalAnimationSettings) entityRemovalAnimationSettings;
@property (T@"SBFWakeAnimationSettings",&,N,V_wakeAnimationSettings) wakeAnimationSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_foldRegionAnimationSettings) foldRegionAnimationSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_cameraExclusionRegionAnimationSettings) cameraExclusionRegionAnimationSettings;
```

## Class methods

```
+[SBSystemAnimationSettings settingsControllerModule];
```

## Instance methods

```
-[SBSystemAnimationSettings setDefaultValues];
-[SBSystemAnimationSettings setFoldRegionAnimationSettings:];
-[SBSystemAnimationSettings assistantAnimationDuration];
-[SBSystemAnimationSettings assistantBottomEdgeDismissThreshold];
-[SBSystemAnimationSettings assistantBottomEdgeDismissVelocity];
-[SBSystemAnimationSettings assistantDismissAnimationDurationOverApp];
-[SBSystemAnimationSettings cameraExclusionRegionAnimationSettings];
-[SBSystemAnimationSettings entityRemovalAnimationSettings];
-[SBSystemAnimationSettings foldRegionAnimationSettings];
-[SBSystemAnimationSettings setAssistantAnimationDuration:];
-[SBSystemAnimationSettings setAssistantBottomEdgeDismissThreshold:];
-[SBSystemAnimationSettings setAssistantBottomEdgeDismissVelocity:];
-[SBSystemAnimationSettings setAssistantDismissAnimationDurationOverApp:];
-[SBSystemAnimationSettings setCameraExclusionRegionAnimationSettings:];
-[SBSystemAnimationSettings setEntityRemovalAnimationSettings:];
-[SBSystemAnimationSettings setSlideoverDosidoAnimationSettings:];
-[SBSystemAnimationSettings setSpotlightNoninteractiveAnimationDuration:];
-[SBSystemAnimationSettings setWakeAnimationSettings:];
-[SBSystemAnimationSettings slideoverDosidoAnimationSettings];
-[SBSystemAnimationSettings spotlightNoninteractiveAnimationDuration];
-[SBSystemAnimationSettings wakeAnimationSettings];
```
