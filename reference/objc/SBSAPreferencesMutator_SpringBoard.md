# `SBSAPreferencesMutator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSAInterfaceElementAnimationDescribing`, `SBSAInterfaceElementAnimationCustomizing`
- 1 instance variables, 28 properties, 58 instance methods, 0 class methods

## Instance variables

```
@"SBSAPreferences" _preferences;
```

## Properties

```
@property (T@"SBSAPreferences",R,N,V_preferences) preferences;
@property (T@"NSArray",C,N) gestureDescriptions;
@property (T@"NSArray",C,N) timerDescriptions;
@property (T@"NSArray",C,N) actions;
@property (T@"SBSAContainerViewDescription",C,N) indicatorContainerViewDescription;
@property (T@"SBSAIndicatorElementDescription",C,N) indicatorElementDescription;
@property (T@"NSArray",C,N) blankingRegionContainerViewDescriptions;
@property (T@"NSArray",C,N) blankingRegionElementDescriptions;
@property (T@"NSArray",C,N) effectPackageViewDescriptions;
@property (T@"SBSAViewDescription",C,N) containerParentViewDescription;
@property (T@"NSArray",C,N) containerViewDescriptions;
@property (T@"NSArray",C,N) elementDescriptions;
@property (T@"SBSAElementLayoutTransition",C,N) elementLayoutTransition;
@property (T@"SBSAElementLayoutTransition",C,N) lastChangingElementLayoutTransition;
@property (T@"SBSABackgroundBlurDescription",C,N) backgroundBlurDescription;
@property (T@"SBSAStatusBarAvoidanceDescription",C,N) statusBarAvoidanceDescription;
@property (T@"SBSAMaintainedPreferences",C,N) maintainedPreferences;
@property (T{SBSystemApertureContainerRenderingConfiguration=qqB},N) curtainRenderingConfiguration;
@property (T{SBSystemApertureContainerRenderingConfiguration=qqB},N) highLevelCurtainRenderingConfiguration;
@property (T@"SBSAViewDescription",C,N) fixedSensorMatchMoveSourceViewDescription;
@property (T@"SBSAExcursionViewDescription",C,N) acceptanceBounceExcursionViewDescription;
@property (TB,N,GisBlobEnabled) blobEnabled;
@property (Td,N) blobRadius;
@property (TB,N,GisCollisionImminent) collisionImminent;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSAPreferencesMutator setIndicatorElementDescription:];
-[SBSAPreferencesMutator setContainerParentViewDescription:];
-[SBSAPreferencesMutator effectPackageViewDescriptions];
-[SBSAPreferencesMutator setBlankingRegionElementDescriptions:];
-[SBSAPreferencesMutator propertiesWithAnimatedTransitionDescriptions];
-[SBSAPreferencesMutator containerViewDescriptions];
-[SBSAPreferencesMutator setFixedSensorMatchMoveSourceViewDescription:];
-[SBSAPreferencesMutator setHighLevelCurtainRenderingConfiguration:];
-[SBSAPreferencesMutator setActions:];
-[SBSAPreferencesMutator setTimerDescriptions:];
-[SBSAPreferencesMutator preferences];
-[SBSAPreferencesMutator setBackgroundBlurDescription:];
-[SBSAPreferencesMutator statusBarAvoidanceDescription];
-[SBSAPreferencesMutator associateAnimatedTransitionDescriptionOfProperty:withProperty:withMilestones:];
-[SBSAPreferencesMutator curtainRenderingConfiguration];
-[SBSAPreferencesMutator setBlobEnabled:];
-[SBSAPreferencesMutator setAnimatedTransitionDescription:overridingExistingUnanimatedSettings:forProperty:withMilestones:];
-[SBSAPreferencesMutator maintainedPreferences];
-[SBSAPreferencesMutator setIndicatorContainerViewDescription:];
-[SBSAPreferencesMutator actions];
-[SBSAPreferencesMutator setCurtainRenderingConfiguration:];
-[SBSAPreferencesMutator setGestureDescriptions:];
-[SBSAPreferencesMutator gestureDescriptions];
-[SBSAPreferencesMutator setContainerViewDescriptions:];
-[SBSAPreferencesMutator isBlobEnabled];
-[SBSAPreferencesMutator setElementDescriptions:];
-[SBSAPreferencesMutator effectiveMilestoneProvidingAnimatedTransitionDescriptionForProperty:];
-[SBSAPreferencesMutator timerDescriptions];
-[SBSAPreferencesMutator lastChangingElementLayoutTransition];
-[SBSAPreferencesMutator initWithPreferences:];
-[SBSAPreferencesMutator backgroundBlurDescription];
-[SBSAPreferencesMutator addMilestones:forPropertyIdentity:];
-[SBSAPreferencesMutator setCollisionImminent:];
-[SBSAPreferencesMutator blobRadius];
-[SBSAPreferencesMutator elementLayoutTransition];
-[SBSAPreferencesMutator elementDescriptions];
-[SBSAPreferencesMutator containerParentViewDescription];
-[SBSAPreferencesMutator setBlobRadius:];
-[SBSAPreferencesMutator associateAnimatedTransitionDescriptionOfProperty:overridingExistingUnanimatedSettings:withProperty:withMilestones:];
-[SBSAPreferencesMutator description];
-[SBSAPreferencesMutator fixedSensorMatchMoveSourceViewDescription];
-[SBSAPreferencesMutator setMaintainedPreferences:];
-[SBSAPreferencesMutator setElementLayoutTransition:];
-[SBSAPreferencesMutator setStatusBarAvoidanceDescription:];
-[SBSAPreferencesMutator setBlankingRegionContainerViewDescriptions:];
-[SBSAPreferencesMutator blankingRegionContainerViewDescriptions];
-[SBSAPreferencesMutator blankingRegionElementDescriptions];
-[SBSAPreferencesMutator animatedTransitionDescriptionForProperty:];
-[SBSAPreferencesMutator setEffectPackageViewDescriptions:];
-[SBSAPreferencesMutator setLastChangingElementLayoutTransition:];
-[SBSAPreferencesMutator isCollisionImminent];
-[SBSAPreferencesMutator setAcceptanceBounceExcursionViewDescription:];
-[SBSAPreferencesMutator highLevelCurtainRenderingConfiguration];
-[SBSAPreferencesMutator effectiveAnimatedTransitionDescriptionForProperty:];
-[SBSAPreferencesMutator setAnimatedTransitionDescription:forProperty:withMilestones:];
-[SBSAPreferencesMutator indicatorElementDescription];
-[SBSAPreferencesMutator acceptanceBounceExcursionViewDescription];
-[SBSAPreferencesMutator indicatorContainerViewDescription];
```
