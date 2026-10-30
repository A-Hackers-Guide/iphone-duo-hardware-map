# `SBSAPreferences`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSABlockMutating`, `SBSAInterfaceElementAnimationDescribing`, `BSXPCAutoCoding`, `SBSAPreferencesRepresenting`, `NSCopying`, `SBSADictionaryDescribable`
- 26 instance variables, 35 properties, 75 instance methods, 3 class methods

## Instance variables

```
B _finalizedForApplication;
B _blobEnabled;
B _collisionImminent;
@"NSArray" _containerViewDescriptions;
@"SBSAContainerViewDescription" _indicatorContainerViewDescription;
@"SBSAIndicatorElementDescription" _indicatorElementDescription;
@"NSArray" _blankingRegionContainerViewDescriptions;
@"NSArray" _blankingRegionElementDescriptions;
@"NSArray" _effectPackageViewDescriptions;
@"SBSAViewDescription" _containerParentViewDescription;
@"NSArray" _elementDescriptions;
@"SBSAElementLayoutTransition" _elementLayoutTransition;
@"SBSAElementLayoutTransition" _lastChangingElementLayoutTransition;
@"SBSABackgroundBlurDescription" _backgroundBlurDescription;
@"SBSAStatusBarAvoidanceDescription" _statusBarAvoidanceDescription;
@"SBSAMaintainedPreferences" _maintainedPreferences;
@"SBSAViewDescription" _fixedSensorMatchMoveSourceViewDescription;
@"SBSAExcursionViewDescription" _acceptanceBounceExcursionViewDescription;
d _blobRadius;
@"NSArray" _gestureDescriptions;
@"NSArray" _timerDescriptions;
@"NSArray" _actions;
@"NSMutableDictionary" _interfaceElementPropertiesToBehaviorSettings;
@"NSMutableDictionary" _interfaceElementPropertiesToMilestones;
{SBSystemApertureContainerRenderingConfiguration="renderingStyle"q"cloningStyle"q"alwaysRenderInSnapshots"B} _curtainRenderingConfiguration;
{SBSystemApertureContainerRenderingConfiguration="renderingStyle"q"cloningStyle"q"alwaysRenderInSnapshots"B} _highLevelCurtainRenderingConfiguration;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSArray",C,N,S_setGestureDescriptions:,V_gestureDescriptions) gestureDescriptions;
@property (T@"NSArray",C,N,S_setTimerDescriptions:,V_timerDescriptions) timerDescriptions;
@property (T@"NSArray",C,N,S_setActions:,V_actions) actions;
@property (T@"SBSAContainerViewDescription",C,N,S_setIndicatorContainerViewDescription:,V_indicatorContainerViewDescription) indicatorContainerViewDescription;
@property (T@"SBSAIndicatorElementDescription",C,N,S_setIndicatorElementDescription:,V_indicatorElementDescription) indicatorElementDescription;
@property (T@"NSArray",C,N,S_setBlankingRegionContainerViewDescriptions:,V_blankingRegionContainerViewDescriptions) blankingRegionContainerViewDescriptions;
@property (T@"NSArray",C,N,S_setBlankingRegionElementDescriptions:,V_blankingRegionElementDescriptions) blankingRegionElementDescriptions;
@property (T@"NSArray",C,N,S_setEffectPackageViewDescriptions:,V_effectPackageViewDescriptions) effectPackageViewDescriptions;
@property (T@"SBSAViewDescription",C,N,S_setContainerParentViewDescription:,V_containerParentViewDescription) containerParentViewDescription;
@property (T@"NSArray",C,N,S_setContainerViewDescriptions:,V_containerViewDescriptions) containerViewDescriptions;
@property (T@"NSArray",C,N,S_setElementDescriptions:,V_elementDescriptions) elementDescriptions;
@property (T@"SBSAElementLayoutTransition",C,N,S_setElementLayoutTransition:,V_elementLayoutTransition) elementLayoutTransition;
@property (T@"SBSAElementLayoutTransition",C,N,S_setLastChangingElementLayoutTransition:,V_lastChangingElementLayoutTransition) lastChangingElementLayoutTransition;
@property (T@"SBSABackgroundBlurDescription",C,N,S_setBackgroundBlurDescription:,V_backgroundBlurDescription) backgroundBlurDescription;
@property (T@"SBSAStatusBarAvoidanceDescription",C,N,S_setStatusBarAvoidanceDescription:,V_statusBarAvoidanceDescription) statusBarAvoidanceDescription;
@property (T@"SBSAMaintainedPreferences",C,N,S_setMaintainedPreferences:,V_maintainedPreferences) maintainedPreferences;
@property (T{SBSystemApertureContainerRenderingConfiguration=qqB},N,S_setCurtainRenderingConfiguration:,V_curtainRenderingConfiguration) curtainRenderingConfiguration;
@property (T{SBSystemApertureContainerRenderingConfiguration=qqB},N,S_setHighLevelCurtainRenderingConfiguration:,V_highLevelCurtainRenderingConfiguration) highLevelCurtainRenderingConfiguration;
@property (T@"SBSAViewDescription",C,N,S_setFixedSensorMatchMoveSourceViewDescription:,V_fixedSensorMatchMoveSourceViewDescription) fixedSensorMatchMoveSourceViewDescription;
@property (T@"SBSAExcursionViewDescription",C,N,S_setAcceptanceBounceExcursionViewDescription:,V_acceptanceBounceExcursionViewDescription) acceptanceBounceExcursionViewDescription;
@property (TB,N,GisBlobEnabled,S_setBlobEnabled:,V_blobEnabled) blobEnabled;
@property (Td,N,S_setBlobRadius:,V_blobRadius) blobRadius;
@property (TB,N,GisCollisionImminent,S_setCollisionImminent:,V_collisionImminent) collisionImminent;
@property (T@"NSMutableDictionary",&,N,G_interfaceElementPropertiesToBehaviorSettings,S_setInterfaceElementPropertiesToBehaviorSettings:,V_interfaceElementPropertiesToBehaviorSettings) interfaceElementPropertiesToBehaviorSettings;
@property (T@"NSMutableDictionary",&,N,G_interfaceElementPropertiesToMilestones,S_setInterfaceElementPropertiesToMilestones:,V_interfaceElementPropertiesToMilestones) interfaceElementPropertiesToMilestones;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSArray",R,C,N) propertiesWithAnimatedTransitionDescriptions;
@property (T@"BSOrderedDictionary",R,C,N) dictionaryDescription;
```

## Class methods

```
+[SBSAPreferences initialize];
+[SBSAPreferences instanceWithBlock:];
+[SBSAPreferences mutatorClass];
```

## Instance methods

```
-[SBSAPreferences effectPackageViewDescriptions];
-[SBSAPreferences propertiesWithAnimatedTransitionDescriptions];
-[SBSAPreferences containerViewDescriptions];
-[SBSAPreferences statusBarAvoidanceDescription];
-[SBSAPreferences curtainRenderingConfiguration];
-[SBSAPreferences maintainedPreferences];
-[SBSAPreferences actions];
-[SBSAPreferences gestureDescriptions];
-[SBSAPreferences isBlobEnabled];
-[SBSAPreferences effectiveMilestoneProvidingAnimatedTransitionDescriptionForProperty:];
-[SBSAPreferences timerDescriptions];
-[SBSAPreferences lastChangingElementLayoutTransition];
-[SBSAPreferences backgroundBlurDescription];
-[SBSAPreferences dictionaryDescription];
-[SBSAPreferences encodeWithCoder:];
-[SBSAPreferences blobRadius];
-[SBSAPreferences hash];
-[SBSAPreferences elementLayoutTransition];
-[SBSAPreferences elementDescriptions];
-[SBSAPreferences containerParentViewDescription];
-[SBSAPreferences description];
-[SBSAPreferences fixedSensorMatchMoveSourceViewDescription];
-[SBSAPreferences blankingRegionContainerViewDescriptions];
-[SBSAPreferences blankingRegionElementDescriptions];
-[SBSAPreferences copyWithZone:];
-[SBSAPreferences animatedTransitionDescriptionForProperty:];
-[SBSAPreferences isEqual:];
-[SBSAPreferences isCollisionImminent];
-[SBSAPreferences highLevelCurtainRenderingConfiguration];
-[SBSAPreferences effectiveAnimatedTransitionDescriptionForProperty:];
-[SBSAPreferences indicatorElementDescription];
-[SBSAPreferences acceptanceBounceExcursionViewDescription];
-[SBSAPreferences copyWithBlock:];
-[SBSAPreferences indicatorContainerViewDescription];
-[SBSAPreferences _setActions:];
-[SBSAPreferences membersForCoder];
-[SBSAPreferences _setBlobRadius:];
-[SBSAPreferences _doesUnanimatedTransitionDescriptionExistForProperty:];
-[SBSAPreferences _effectiveTransitionDescriptionForPropertyForProperty:addingMilestonesAndCreatingUniqueDescriptionIfIndirect:];
-[SBSAPreferences _interfaceElementPropertiesToBehaviorSettings];
-[SBSAPreferences _interfaceElementPropertiesToMilestones];
-[SBSAPreferences _setAcceptanceBounceExcursionViewDescription:];
-[SBSAPreferences _setBackgroundBlurDescription:];
-[SBSAPreferences _setBlankingRegionContainerViewDescriptions:];
-[SBSAPreferences _setBlankingRegionElementDescriptions:];
-[SBSAPreferences _setBlobEnabled:];
-[SBSAPreferences _setCollisionImminent:];
-[SBSAPreferences _setContainerParentViewDescription:];
-[SBSAPreferences _setContainerViewDescriptions:];
-[SBSAPreferences _setCurtainRenderingConfiguration:];
-[SBSAPreferences _setEffectPackageViewDescriptions:];
-[SBSAPreferences _setElementDescriptions:];
-[SBSAPreferences _setElementLayoutTransition:];
-[SBSAPreferences _setFixedSensorMatchMoveSourceViewDescription:];
-[SBSAPreferences _setGestureDescriptions:];
-[SBSAPreferences _setHighLevelCurtainRenderingConfiguration:];
-[SBSAPreferences _setIndicatorContainerViewDescription:];
-[SBSAPreferences _setIndicatorElementDescription:];
-[SBSAPreferences _setInterfaceElementPropertiesToBehaviorSettings:];
-[SBSAPreferences _setInterfaceElementPropertiesToMilestones:];
-[SBSAPreferences _setLastChangingElementLayoutTransition:];
-[SBSAPreferences _setMaintainedPreferences:];
-[SBSAPreferences _setStatusBarAvoidanceDescription:];
-[SBSAPreferences _setTimerDescriptions:];
-[SBSAPreferences blankingContainerViewDescriptionForElementIdentity:];
-[SBSAPreferences blankingRegionAppearanceStateContextForElementIdentity:];
-[SBSAPreferences blankingRegionAppearanceStateContextForRegionIdentifier:];
-[SBSAPreferences copyByAddingActions:];
-[SBSAPreferences copyByUpdatingBackgroundBlurDescription:];
-[SBSAPreferences copyByUpdatingContainerViewDescriptions:];
-[SBSAPreferences copyByUpdatingElementDescriptions:];
-[SBSAPreferences copyByUpdatingMaintainedPreferences:];
-[SBSAPreferences copyByUpdatingStatusBarAvoidanceDescription:];
-[SBSAPreferences copyWithCancellationOfGestureOfClass:context:];
-[SBSAPreferences finalizePreferencesForApplication:];
```
