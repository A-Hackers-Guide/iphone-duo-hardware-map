# `SBContinuousExposeAppToAppModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransitionSwitcherModifier`
- 24 instance variables, 14 properties, 44 instance methods, 0 class methods

## Instance variables

```
@"NSSet" _displayItemsChangingSize;
@"NSSet" _displayItemsChangingPosition;
@"NSMutableSet" _pendingDisplayItemSceneUpdates;
@"NSSet" _appLayoutsNeedingHiding;
@"SBDisplayItem" _fromTopMostDisplayItem;
@"SBDisplayItem" _toTopMostDisplayItem;
B _ignoreTapsDuringMorphTransition;
@"NSString" _uniqueAnimationIdentifier;
B _stripWasInitiallyPresented;
B _isFromPeek;
B _continuousExposeConfigurationChangeTransition;
B _commandTabTransition;
B _launchingFromDockTransition;
B _morphFromInAppViewTransition;
B _launchingFromSpotlightTransition;
B _isTopAffordanceMenuTransition;
B _shouldOrderToAppLayoutFront;
@"SBAppLayout" _fromAppLayout;
q _fromInterfaceOrientation;
@"SBAppLayout" _toAppLayout;
q _toInterfaceOrientation;
@"NSDictionary" _fromDisplayItemLayoutAttributesMap;
@"NSDictionary" _toDisplayItemLayoutAttributesMap;
@"SBAppLayout" _ignoredAppLayout;
```

## Properties

```
@property (T@"SBAppLayout",R,N,V_fromAppLayout) fromAppLayout;
@property (Tq,R,N,V_fromInterfaceOrientation) fromInterfaceOrientation;
@property (T@"SBAppLayout",R,N,V_toAppLayout) toAppLayout;
@property (Tq,R,N,V_toInterfaceOrientation) toInterfaceOrientation;
@property (T@"NSDictionary",R,C,N,V_fromDisplayItemLayoutAttributesMap) fromDisplayItemLayoutAttributesMap;
@property (T@"NSDictionary",R,C,N,V_toDisplayItemLayoutAttributesMap) toDisplayItemLayoutAttributesMap;
@property (TB,N,GisContinuousExposeConfigurationChangeTransition,V_continuousExposeConfigurationChangeTransition) continuousExposeConfigurationChangeTransition;
@property (TB,N,GisCommandTabTransition,V_commandTabTransition) commandTabTransition;
@property (TB,N,GisLaunchingFromDockTransition,V_launchingFromDockTransition) launchingFromDockTransition;
@property (TB,N,GisMorphFromInAppViewTransition,V_morphFromInAppViewTransition) morphFromInAppViewTransition;
@property (TB,N,GisLaunchingFromSpotlightTransition,V_launchingFromSpotlightTransition) launchingFromSpotlightTransition;
@property (TB,N,V_isTopAffordanceMenuTransition) isTopAffordanceMenuTransition;
@property (T@"SBAppLayout",&,N,V_ignoredAppLayout) ignoredAppLayout;
@property (TB,N,V_shouldOrderToAppLayoutFront) shouldOrderToAppLayoutFront;
```

## Instance methods

```
-[SBContinuousExposeAppToAppModifier appLayoutsToEnsureExistForMainTransitionEvent:];
-[SBContinuousExposeAppToAppModifier setLaunchingFromDockTransition:];
-[SBContinuousExposeAppToAppModifier didMoveToParentModifier:];
-[SBContinuousExposeAppToAppModifier animationAttributesForLayoutElement:];
-[SBContinuousExposeAppToAppModifier _layoutSettings];
-[SBContinuousExposeAppToAppModifier topMostLayoutElements];
-[SBContinuousExposeAppToAppModifier fromDisplayItemLayoutAttributesMap];
-[SBContinuousExposeAppToAppModifier toInterfaceOrientation];
-[SBContinuousExposeAppToAppModifier fadeInDelayForSplitViewHandles];
-[SBContinuousExposeAppToAppModifier perspectiveAngleForIndex:];
-[SBContinuousExposeAppToAppModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBContinuousExposeAppToAppModifier transitionDidEnd];
-[SBContinuousExposeAppToAppModifier handleTimerEvent:];
-[SBContinuousExposeAppToAppModifier transitionWillBegin];
-[SBContinuousExposeAppToAppModifier fromAppLayout];
-[SBContinuousExposeAppToAppModifier blurDelayForLayoutRole:inAppLayout:];
-[SBContinuousExposeAppToAppModifier fromInterfaceOrientation];
-[SBContinuousExposeAppToAppModifier ignoredAppLayout];
-[SBContinuousExposeAppToAppModifier setCommandTabTransition:];
-[SBContinuousExposeAppToAppModifier handleTapAppLayoutEvent:];
-[SBContinuousExposeAppToAppModifier asyncRenderingDisabled];
-[SBContinuousExposeAppToAppModifier isLaunchingFromDockTransition];
-[SBContinuousExposeAppToAppModifier toDisplayItemLayoutAttributesMap];
-[SBContinuousExposeAppToAppModifier isCommandTabTransition];
-[SBContinuousExposeAppToAppModifier toAppLayout];
-[SBContinuousExposeAppToAppModifier isLayoutRoleMatchMovedToScene:inAppLayout:];
-[SBContinuousExposeAppToAppModifier maskedCornersForLayoutRole:inAppLayout:withMaskedCorners:];
-[SBContinuousExposeAppToAppModifier setIgnoredAppLayout:];
-[SBContinuousExposeAppToAppModifier isLayoutRoleBlurred:inAppLayout:];
-[SBContinuousExposeAppToAppModifier setShouldOrderToAppLayoutFront:];
-[SBContinuousExposeAppToAppModifier _ignoreTapsDuringMorphTransitionReason];
-[SBContinuousExposeAppToAppModifier _shouldIgnoreTapsUntilDelay:];
-[SBContinuousExposeAppToAppModifier _topMostDisplayItemInDisplayItemLayoutAttributesMap:];
-[SBContinuousExposeAppToAppModifier handleSceneReadyEvent:];
-[SBContinuousExposeAppToAppModifier initWithTransitionID:fromAppLayout:fromInterfaceOrientation:toAppLayout:toInterfaceOrientation:fromDisplayItemLayoutAttributesMap:toDisplayItemLayoutAttributesMap:];
-[SBContinuousExposeAppToAppModifier isContinuousExposeConfigurationChangeTransition];
-[SBContinuousExposeAppToAppModifier isLaunchingFromSpotlightTransition];
-[SBContinuousExposeAppToAppModifier isMorphFromInAppViewTransition];
-[SBContinuousExposeAppToAppModifier isTopAffordanceMenuTransition];
-[SBContinuousExposeAppToAppModifier setContinuousExposeConfigurationChangeTransition:];
-[SBContinuousExposeAppToAppModifier setIsTopAffordanceMenuTransition:];
-[SBContinuousExposeAppToAppModifier setLaunchingFromSpotlightTransition:];
-[SBContinuousExposeAppToAppModifier setMorphFromInAppViewTransition:];
-[SBContinuousExposeAppToAppModifier shouldOrderToAppLayoutFront];
```
