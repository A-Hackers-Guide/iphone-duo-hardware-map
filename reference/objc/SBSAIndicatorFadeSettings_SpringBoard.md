# `SBSAIndicatorFadeSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 13 instance variables, 13 properties, 27 instance methods, 1 class methods

## Instance variables

```
d _staggerMilestoneThreshold;
d _staggerTimerBackstop;
d _completionTimerBackstop;
d _blurRadius;
@"SBFFluidBehaviorSettings" _containerBoundsBehaviorSettings;
@"SBFFluidBehaviorSettings" _containerBlurRadiusBehaviorSettings;
@"SBFFluidBehaviorSettings" _containerCenterBehaviorSettings;
@"SBFFluidBehaviorSettings" _indicatorElementAlphaBehaviorSettings;
@"SBFFluidBehaviorSettings" _indicatorElementBlurProgressBehaviorSettings;
@"SBFFluidBehaviorSettings" _indicatorElementTransformBehaviorSettings;
@"SBFFluidBehaviorSettings" _fixedIndicatorAlphaBehaviorSettings;
@"SBFFluidBehaviorSettings" _fixedIndicatorBlurProgressBehaviorSettings;
@"SBFFluidBehaviorSettings" _fixedIndicatorTransformBehaviorSettings;
```

## Properties

```
@property (Td,N,V_staggerMilestoneThreshold) staggerMilestoneThreshold;
@property (Td,N,V_staggerTimerBackstop) staggerTimerBackstop;
@property (Td,N,V_completionTimerBackstop) completionTimerBackstop;
@property (Td,N,V_blurRadius) blurRadius;
@property (T@"SBFFluidBehaviorSettings",&,N,V_containerBoundsBehaviorSettings) containerBoundsBehaviorSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_containerBlurRadiusBehaviorSettings) containerBlurRadiusBehaviorSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_containerCenterBehaviorSettings) containerCenterBehaviorSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_indicatorElementAlphaBehaviorSettings) indicatorElementAlphaBehaviorSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_indicatorElementBlurProgressBehaviorSettings) indicatorElementBlurProgressBehaviorSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_indicatorElementTransformBehaviorSettings) indicatorElementTransformBehaviorSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_fixedIndicatorAlphaBehaviorSettings) fixedIndicatorAlphaBehaviorSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_fixedIndicatorBlurProgressBehaviorSettings) fixedIndicatorBlurProgressBehaviorSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_fixedIndicatorTransformBehaviorSettings) fixedIndicatorTransformBehaviorSettings;
```

## Class methods

```
+[SBSAIndicatorFadeSettings settingsControllerModule];
```

## Instance methods

```
-[SBSAIndicatorFadeSettings setDefaultValues];
-[SBSAIndicatorFadeSettings blurRadius];
-[SBSAIndicatorFadeSettings setBlurRadius:];
-[SBSAIndicatorFadeSettings containerBoundsBehaviorSettings];
-[SBSAIndicatorFadeSettings containerCenterBehaviorSettings];
-[SBSAIndicatorFadeSettings completionTimerBackstop];
-[SBSAIndicatorFadeSettings containerBlurRadiusBehaviorSettings];
-[SBSAIndicatorFadeSettings fixedIndicatorAlphaBehaviorSettings];
-[SBSAIndicatorFadeSettings fixedIndicatorBlurProgressBehaviorSettings];
-[SBSAIndicatorFadeSettings fixedIndicatorTransformBehaviorSettings];
-[SBSAIndicatorFadeSettings indicatorElementAlphaBehaviorSettings];
-[SBSAIndicatorFadeSettings indicatorElementBlurProgressBehaviorSettings];
-[SBSAIndicatorFadeSettings indicatorElementTransformBehaviorSettings];
-[SBSAIndicatorFadeSettings setCompletionTimerBackstop:];
-[SBSAIndicatorFadeSettings setContainerBlurRadiusBehaviorSettings:];
-[SBSAIndicatorFadeSettings setContainerBoundsBehaviorSettings:];
-[SBSAIndicatorFadeSettings setContainerCenterBehaviorSettings:];
-[SBSAIndicatorFadeSettings setFixedIndicatorAlphaBehaviorSettings:];
-[SBSAIndicatorFadeSettings setFixedIndicatorBlurProgressBehaviorSettings:];
-[SBSAIndicatorFadeSettings setFixedIndicatorTransformBehaviorSettings:];
-[SBSAIndicatorFadeSettings setIndicatorElementAlphaBehaviorSettings:];
-[SBSAIndicatorFadeSettings setIndicatorElementBlurProgressBehaviorSettings:];
-[SBSAIndicatorFadeSettings setIndicatorElementTransformBehaviorSettings:];
-[SBSAIndicatorFadeSettings setStaggerMilestoneThreshold:];
-[SBSAIndicatorFadeSettings setStaggerTimerBackstop:];
-[SBSAIndicatorFadeSettings staggerMilestoneThreshold];
-[SBSAIndicatorFadeSettings staggerTimerBackstop];
```
