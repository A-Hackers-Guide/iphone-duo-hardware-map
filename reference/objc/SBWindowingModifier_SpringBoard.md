# `SBWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifierBase`
- Protocols: `SBSwitcherMultitaskingQueryProviding`, `SBChainableModifierDelegate`
- 11 instance variables, 9 properties, 135 instance methods, 0 class methods

## Instance variables

```
B _isUpdating;
B _hasBegun;
B _hasCompleted;
Q _activityIndex;
@"NSMutableArray" _currentResponses;
@"SBSwitcherModifierEvent" _currentEvent;
@"SBTransitionSwitcherModifierEvent" _transition;
@"SBGestureSwitcherModifierEvent" _gesture;
B _isScrolling;
@"NSMutableDictionary" _viewModels;
B _switcherModifierInteroperabilityEnabled;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,N,V_switcherModifierInteroperabilityEnabled) switcherModifierInteroperabilityEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBWindowingModifier scaleForIndex:];
-[SBWindowingModifier anchorPointForIndex:];
-[SBWindowingModifier titleOpacityForIndex:];
-[SBWindowingModifier supportsSplit];
-[SBWindowingModifier wallpaperGradientAttributesForItem:];
-[SBWindowingModifier handleEvent:];
-[SBWindowingModifier stateModel];
-[SBWindowingModifier maskedCornersForIndex:];
-[SBWindowingModifier activities];
-[SBWindowingModifier transitioningToAppLayout];
-[SBWindowingModifier cornerRadiiForIndex:];
-[SBWindowingModifier adjustedSpaceAccessoryViewAnchorPoint:forAppLayout:];
-[SBWindowingModifier animationAttributesForLayoutElement:];
-[SBWindowingModifier setState:];
-[SBWindowingModifier adjustedSpaceAccessoryViewFrame:forAppLayout:];
-[SBWindowingModifier appLayoutOnStage];
-[SBWindowingModifier personalityDebugColorStyleForAppLayout:];
-[SBWindowingModifier topMostLayoutElements];
-[SBWindowingModifier titleAndIconOpacityForIndex:];
-[SBWindowingModifier willUpdate];
-[SBWindowingModifier dimmingAlphaForLayoutRole:inAppLayout:];
-[SBWindowingModifier transitionDidUpdate:];
-[SBWindowingModifier adjustedSpaceAccessoryViewScale:forAppLayout:];
-[SBWindowingModifier update];
-[SBWindowingModifier visibleAppLayouts];
-[SBWindowingModifier layoutViewModelsIfNeeded];
-[SBWindowingModifier init];
-[SBWindowingModifier perspectiveAngleForIndex:];
-[SBWindowingModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBWindowingModifier isScrolling];
-[SBWindowingModifier didUpdate];
-[SBWindowingModifier shadowOpacityForLayoutRole:atIndex:];
-[SBWindowingModifier headerStyleForIndex:];
-[SBWindowingModifier adjustedSpaceAccessoryViewPerspectiveAngle:forAppLayout:];
-[SBWindowingModifier frameForIndex:];
-[SBWindowingModifier containerBorderForLayoutRole:inAppLayout:];
-[SBWindowingModifier complete];
-[SBWindowingModifier transitioningFromAppLayout];
-[SBWindowingModifier transitionWillBegin:];
-[SBWindowingModifier borderForItem:];
-[SBWindowingModifier shadowForItem:];
-[SBWindowingModifier visibleItems];
-[SBWindowingModifier cornersForItem:];
-[SBWindowingModifier wallpaperGradientAttributesForLayoutRole:inAppLayout:];
-[SBWindowingModifier spaceAccessoryViewModelForItem:];
-[SBWindowingModifier headerTrailingIconOpacityBehaviorForIndex:];
-[SBWindowingModifier animationAttributesForItem:];
-[SBWindowingModifier opacityForItem:];
-[SBWindowingModifier personalityDebugColorStyleForItem:];
-[SBWindowingModifier dimmingAlphaForItem:];
-[SBWindowingModifier perspectiveAngleForItem:];
-[SBWindowingModifier shadowStyleForLayoutRole:inAppLayout:];
-[SBWindowingModifier timerFired:];
-[SBWindowingModifier topMostItems];
-[SBWindowingModifier iconOpacityForIndex:];
-[SBWindowingModifier footerViewIconAlignmentForAppLayout:];
-[SBWindowingModifier supportsHomeAffordanceForItem:];
-[SBWindowingModifier isHomeAffordanceSupportedForAppLayout:];
-[SBWindowingModifier frameForItem:];
-[SBWindowingModifier titleStyleForItem:];
-[SBWindowingModifier _forwardingTargetForUpdate];
-[SBWindowingModifier didScroll:];
-[SBWindowingModifier displayCornerRadius];
-[SBWindowingModifier willBegin];
-[SBWindowingModifier didComplete];
-[SBWindowingModifier transitionPhase];
-[SBWindowingModifier removeResponse:];
-[SBWindowingModifier stripDidChange:];
-[SBWindowingModifier appendResponse:];
-[SBWindowingModifier transitioningToEnvironmentState];
-[SBWindowingModifier _evaluateInteroperability];
-[SBWindowingModifier _handleContinuousFoldEvent:];
-[SBWindowingModifier _handleGestureEvent:];
-[SBWindowingModifier _handleTransitionEvent:];
-[SBWindowingModifier _setSwitcherModifierInteroperabilityEnabled:force:];
-[SBWindowingModifier addChildModifier:atLevel:key:];
-[SBWindowingModifier appLayoutHeaderTapped:];
-[SBWindowingModifier appLayoutTapped:];
-[SBWindowingModifier appLayoutsToCacheSnapshotsInDeckRegionModel:visibleSpaceRange:numberOfSnapshotsToCache:biasForward:];
-[SBWindowingModifier appLayoutsToCacheSnapshotsWithVisibleRange:numberOfSnapshotsToCache:biasForward:];
-[SBWindowingModifier appLayoutsToCacheSnapshotsWithVisibleSpaceRange:numberOfSnapshotsToCache:biasForward:];
-[SBWindowingModifier appendResponses:];
-[SBWindowingModifier assistantPresentationChanged:];
-[SBWindowingModifier continuousFoldDidBegin:];
-[SBWindowingModifier continuousFoldDidEnd:];
-[SBWindowingModifier continuousFoldDidSwap:];
-[SBWindowingModifier continuousFoldWillSwap:];
-[SBWindowingModifier currentResponses];
-[SBWindowingModifier defaultAppLayoutsToCacheSnapshots];
-[SBWindowingModifier defaultFrameForLeafAppLayout:inSwitcherScreenRegion:];
-[SBWindowingModifier didEdgeProtectSlideOverTongue:];
-[SBWindowingModifier didHideMorphToPIPAppLayout:];
-[SBWindowingModifier distanceToLeadingEdgeOfLeadingCardFromTrailingEdgeOfScreenWithVisibleIndexToStartSearch:numberOfRows:padding:layoutDirection:];
-[SBWindowingModifier flexibleAutoLayoutSpaceForAppLayout:];
-[SBWindowingModifier gestureDidComplete:];
-[SBWindowingModifier gestureDidUpdate:];
-[SBWindowingModifier gestureWillBegin:];
-[SBWindowingModifier highlightDidChange:];
-[SBWindowingModifier homeGestureSettingsChanged:];
-[SBWindowingModifier itemInserted:];
-[SBWindowingModifier itemRemoved:];
-[SBWindowingModifier itemSwipedToKill:];
-[SBWindowingModifier prependResponse:];
-[SBWindowingModifier reduceMotionChanged:];
-[SBWindowingModifier regionContentsDidChange:];
-[SBWindowingModifier regionContentsWillChange:];
-[SBWindowingModifier removeChildModifier:];
-[SBWindowingModifier resizeProgressChanged:];
-[SBWindowingModifier setSwitcherModifierInteroperabilityEnabled:];
-[SBWindowingModifier setViewModel:forItem:];
-[SBWindowingModifier shouldInterruptForActivity:];
-[SBWindowingModifier shouldZoomToSystemApertureForEvent:activeLayout:];
-[SBWindowingModifier splitViewHandleTapped:];
-[SBWindowingModifier stripWillChange:];
-[SBWindowingModifier switcherInterfaceOrientationChanged:];
-[SBWindowingModifier switcherInterfaceOrientedDisplayCornerRadii];
-[SBWindowingModifier switcherModifierInteroperabilityEnabled];
-[SBWindowingModifier switcherSettingsChanged:];
-[SBWindowingModifier switcherShortcutActionPerformed:];
-[SBWindowingModifier tappedOutsideToDismiss:];
-[SBWindowingModifier topMostItemsByAddingAppLayoutAndAccessories:toTopMostItems:orderFront:];
-[SBWindowingModifier transitionDidComplete:];
-[SBWindowingModifier transitionWillPrepare:];
-[SBWindowingModifier transitioningFromAppsRegionModel];
-[SBWindowingModifier transitioningFromDeckRegionModel];
-[SBWindowingModifier transitioningFromEnvironmentMode];
-[SBWindowingModifier transitioningFromEnvironmentState];
-[SBWindowingModifier transitioningToAppsRegionModel];
-[SBWindowingModifier transitioningToDeckRegionModel];
-[SBWindowingModifier transitioningToEnvironmentMode];
-[SBWindowingModifier userDidInteractWithApp:];
-[SBWindowingModifier viewModelForItem:];
-[SBWindowingModifier viewModelItems];
-[SBWindowingModifier visibleSpaceRangeForActiveAppLayout:];
-[SBWindowingModifier windowingConfiguration];
```
