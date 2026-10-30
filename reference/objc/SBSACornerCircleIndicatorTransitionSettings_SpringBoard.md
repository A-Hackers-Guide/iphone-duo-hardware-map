# `SBSACornerCircleIndicatorTransitionSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 6 instance variables, 6 properties, 13 instance methods, 1 class methods

## Instance variables

```
d _fadeMilestoneThreshold;
d _fadeTimerBackstop;
d _collapseTimerBackstop;
@"SBFFluidBehaviorSettings" _dotAlphaBehaviorSettings;
@"SBFFluidBehaviorSettings" _cornerCircleAttachedContainerBoundsBehaviorSettings;
@"SBFFluidBehaviorSettings" _cornerCircleAttachedContainerCenterBehaviorSettings;
```

## Properties

```
@property (Td,N,V_fadeMilestoneThreshold) fadeMilestoneThreshold;
@property (Td,N,V_fadeTimerBackstop) fadeTimerBackstop;
@property (Td,N,V_collapseTimerBackstop) collapseTimerBackstop;
@property (T@"SBFFluidBehaviorSettings",&,N,V_dotAlphaBehaviorSettings) dotAlphaBehaviorSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_cornerCircleAttachedContainerBoundsBehaviorSettings) cornerCircleAttachedContainerBoundsBehaviorSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_cornerCircleAttachedContainerCenterBehaviorSettings) cornerCircleAttachedContainerCenterBehaviorSettings;
```

## Class methods

```
+[SBSACornerCircleIndicatorTransitionSettings settingsControllerModule];
```

## Instance methods

```
-[SBSACornerCircleIndicatorTransitionSettings setDefaultValues];
-[SBSACornerCircleIndicatorTransitionSettings collapseTimerBackstop];
-[SBSACornerCircleIndicatorTransitionSettings cornerCircleAttachedContainerBoundsBehaviorSettings];
-[SBSACornerCircleIndicatorTransitionSettings cornerCircleAttachedContainerCenterBehaviorSettings];
-[SBSACornerCircleIndicatorTransitionSettings dotAlphaBehaviorSettings];
-[SBSACornerCircleIndicatorTransitionSettings fadeMilestoneThreshold];
-[SBSACornerCircleIndicatorTransitionSettings fadeTimerBackstop];
-[SBSACornerCircleIndicatorTransitionSettings setCollapseTimerBackstop:];
-[SBSACornerCircleIndicatorTransitionSettings setCornerCircleAttachedContainerBoundsBehaviorSettings:];
-[SBSACornerCircleIndicatorTransitionSettings setCornerCircleAttachedContainerCenterBehaviorSettings:];
-[SBSACornerCircleIndicatorTransitionSettings setDotAlphaBehaviorSettings:];
-[SBSACornerCircleIndicatorTransitionSettings setFadeMilestoneThreshold:];
-[SBSACornerCircleIndicatorTransitionSettings setFadeTimerBackstop:];
```
