# `SBSAIndicatorMitosisPhaseSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 11 instance variables, 11 properties, 24 instance methods, 2 class methods

## Instance variables

```
d _blobRadius;
d _sensorShadowProgress;
@"PTSizeSettings" _scale;
@"PTSizeSettings" _contentScale;
@"PTPointSettings" _containerCenterOffset;
d _phaseEndMilestone;
q _phaseEndMilestoneTarget;
@"NSString" _phaseEndMilestoneTargetProperty;
@"SBSAIndicatorAssociatedContainerTransitionSettings" _associatedContainerBehaviorSettings;
@"SBSAIndicatorContainerElementTransitionSettings" _indicatorElementTransitionSettings;
@"NSString" _phaseName;
```

## Properties

```
@property (T@"NSString",&,N,V_phaseName) phaseName;
@property (Td,N,V_blobRadius) blobRadius;
@property (Td,N,V_sensorShadowProgress) sensorShadowProgress;
@property (T@"PTSizeSettings",&,N,V_scale) scale;
@property (T@"PTSizeSettings",&,N,V_contentScale) contentScale;
@property (T@"PTPointSettings",&,N,V_containerCenterOffset) containerCenterOffset;
@property (Td,N,V_phaseEndMilestone) phaseEndMilestone;
@property (Tq,N,V_phaseEndMilestoneTarget) phaseEndMilestoneTarget;
@property (T@"NSString",&,N,V_phaseEndMilestoneTargetProperty) phaseEndMilestoneTargetProperty;
@property (T@"SBSAIndicatorAssociatedContainerTransitionSettings",&,N,V_associatedContainerBehaviorSettings) associatedContainerBehaviorSettings;
@property (T@"SBSAIndicatorContainerElementTransitionSettings",&,N,V_indicatorElementTransitionSettings) indicatorElementTransitionSettings;
```

## Class methods

```
+[SBSAIndicatorMitosisPhaseSettings ignoresKey:];
+[SBSAIndicatorMitosisPhaseSettings settingsControllerModule];
```

## Instance methods

```
-[SBSAIndicatorMitosisPhaseSettings drillDownSummary];
-[SBSAIndicatorMitosisPhaseSettings setScale:];
-[SBSAIndicatorMitosisPhaseSettings scale];
-[SBSAIndicatorMitosisPhaseSettings setDefaultValues];
-[SBSAIndicatorMitosisPhaseSettings setContentScale:];
-[SBSAIndicatorMitosisPhaseSettings contentScale];
-[SBSAIndicatorMitosisPhaseSettings blobRadius];
-[SBSAIndicatorMitosisPhaseSettings setBlobRadius:];
-[SBSAIndicatorMitosisPhaseSettings phaseEndMilestoneTargetProperty];
-[SBSAIndicatorMitosisPhaseSettings associatedContainerBehaviorSettings];
-[SBSAIndicatorMitosisPhaseSettings containerCenterOffset];
-[SBSAIndicatorMitosisPhaseSettings indicatorElementTransitionSettings];
-[SBSAIndicatorMitosisPhaseSettings phaseEndMilestone];
-[SBSAIndicatorMitosisPhaseSettings phaseEndMilestoneTarget];
-[SBSAIndicatorMitosisPhaseSettings phaseName];
-[SBSAIndicatorMitosisPhaseSettings sensorShadowProgress];
-[SBSAIndicatorMitosisPhaseSettings setAssociatedContainerBehaviorSettings:];
-[SBSAIndicatorMitosisPhaseSettings setContainerCenterOffset:];
-[SBSAIndicatorMitosisPhaseSettings setIndicatorElementTransitionSettings:];
-[SBSAIndicatorMitosisPhaseSettings setPhaseEndMilestone:];
-[SBSAIndicatorMitosisPhaseSettings setPhaseEndMilestoneTarget:];
-[SBSAIndicatorMitosisPhaseSettings setPhaseEndMilestoneTargetProperty:];
-[SBSAIndicatorMitosisPhaseSettings setPhaseName:];
-[SBSAIndicatorMitosisPhaseSettings setSensorShadowProgress:];
```
