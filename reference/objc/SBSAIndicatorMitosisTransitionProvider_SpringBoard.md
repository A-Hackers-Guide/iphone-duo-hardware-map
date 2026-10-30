# `SBSAIndicatorMitosisTransitionProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSABasePreferencesProvider`
- 7 instance variables, 2 properties, 18 instance methods, 1 class methods

## Instance variables

```
Q _activePhase;
@"SBSAInterfaceElementPropertyIdentity" _pendingPhaseTransitionPropertyIdentity;
@"NSUUID" _pendingPhaseTransitionTimerIdentity;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _initialSensorAwareContainerFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _initialSensorAwareContentFrame;
B _reversed;
Q _type;
```

## Properties

```
@property (TQ,N,V_type) type;
@property (TB,R,N,GisReversed,V_reversed) reversed;
```

## Class methods

```
+[SBSAIndicatorMitosisTransitionProvider initialize];
```

## Instance methods

```
-[SBSAIndicatorMitosisTransitionProvider isReversed];
-[SBSAIndicatorMitosisTransitionProvider debugDescription];
-[SBSAIndicatorMitosisTransitionProvider setType:];
-[SBSAIndicatorMitosisTransitionProvider type];
-[SBSAIndicatorMitosisTransitionProvider membersForCoder];
-[SBSAIndicatorMitosisTransitionProvider _wantsIndicatorUnderAssociatedContainerWithPreferences:context:];
-[SBSAIndicatorMitosisTransitionProvider _advancePhaseWithContext:];
-[SBSAIndicatorMitosisTransitionProvider _associatedContainerViewDescriptionFromPreferences:context:outIndex:];
-[SBSAIndicatorMitosisTransitionProvider _milestoneDidReachExpectedMilestone:property:context:];
-[SBSAIndicatorMitosisTransitionProvider _mitosisPhaseSettingsForPhase:];
-[SBSAIndicatorMitosisTransitionProvider _mitosisSettings];
-[SBSAIndicatorMitosisTransitionProvider _positionIndicatorUnderAssociatedContainerWithPreferences:context:];
-[SBSAIndicatorMitosisTransitionProvider _updateMaintainedPreferencesForActivePhaseWithContext:];
-[SBSAIndicatorMitosisTransitionProvider _updatedPreferencesFromPreferences:context:relevantPropertyIdentity:];
-[SBSAIndicatorMitosisTransitionProvider _updatedPreferencesWithPhaseSettings:preferences:context:];
-[SBSAIndicatorMitosisTransitionProvider initWithType:reversed:];
-[SBSAIndicatorMitosisTransitionProvider milestoneForPhase:];
-[SBSAIndicatorMitosisTransitionProvider preferencesFromContext:];
```
