# `SBSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifierBase`
- 4 instance variables, 0 properties, 88 instance methods, 1 class methods

## Instance variables

```
B _verifyModifierStackCoherencyCheckAfterHandlingEvent;
Q _windowing_cachedIndex;
Q _windowing_cachedAppLayoutsGenerationCount;
@"SBAppLayout" _windowing_cachedAppLayout;
```

## Class methods

```
+[SBSwitcherModifier newEventResponse];
```

## Instance methods

```
-[SBSwitcherModifier handleGestureEvent:];
-[SBSwitcherModifier wallpaperGradientAttributesForItem:];
-[SBSwitcherModifier handleHomeGestureSettingsChangedEvent:];
-[SBSwitcherModifier handleAssistantIslandEvent:];
-[SBSwitcherModifier _handleEvent:];
-[SBSwitcherModifier handleContinuousExposeStripEdgeProtectTongueEvent:];
-[SBSwitcherModifier handleTransitionEvent:];
-[SBSwitcherModifier handleMoveDisplayItemFromOtherDisplayEvent:];
-[SBSwitcherModifier init];
-[SBSwitcherModifier displayName];
-[SBSwitcherModifier handleTimerEvent:];
-[SBSwitcherModifier handleSwitcherSettingsChangedEvent:];
-[SBSwitcherModifier borderForItem:];
-[SBSwitcherModifier shadowForItem:];
-[SBSwitcherModifier visibleItems];
-[SBSwitcherModifier cornersForItem:];
-[SBSwitcherModifier handleResizeProgressEvent:];
-[SBSwitcherModifier loggingCategory];
-[SBSwitcherModifier handleRepositionProgressEvent:];
-[SBSwitcherModifier handleTapOutsideToDismissEvent:];
-[SBSwitcherModifier handleRemovalEvent:];
-[SBSwitcherModifier handleTapAppLayoutEvent:];
-[SBSwitcherModifier handleDidEdgeProtectResizeGrabberEvent:];
-[SBSwitcherModifier handleSlideOverEdgeProtectTongueEvent:];
-[SBSwitcherModifier handleContinuousExposeIdentifiersChangedEvent:];
-[SBSwitcherModifier spaceAccessoryViewModelForItem:];
-[SBSwitcherModifier handleSwitcherShortcutActionEvent:];
-[SBSwitcherModifier animationAttributesForItem:];
-[SBSwitcherModifier opacityForItem:];
-[SBSwitcherModifier handleScrollEvent:];
-[SBSwitcherModifier personalityDebugColorStyleForItem:];
-[SBSwitcherModifier dimmingAlphaForItem:];
-[SBSwitcherModifier perspectiveAngleForItem:];
-[SBSwitcherModifier handleAssistantPresentationChangedEvent:];
-[SBSwitcherModifier topMostItems];
-[SBSwitcherModifier supportsHomeAffordanceForItem:];
-[SBSwitcherModifier frameForItem:];
-[SBSwitcherModifier titleStyleForItem:];
-[SBSwitcherModifier displayCornerRadius];
-[SBSwitcherModifier handleUpdateWindowingModeEvent:];
-[SBSwitcherModifier handleReduceMotionChangedEvent:];
-[SBSwitcherModifier appLayoutContainsFullScreenDisplayItem:];
-[SBSwitcherModifier appLayoutsToCacheSnapshotsWithVisibleRange:numberOfSnapshotsToCache:biasForward:];
-[SBSwitcherModifier assistantIsEffectivelyPresentedAndWantsDeemphasizedBackdrop];
-[SBSwitcherModifier autoLayoutItemIntersectsHomeAffordanceArea:];
-[SBSwitcherModifier defaultAppLayoutsToCacheSnapshots];
-[SBSwitcherModifier defaultFrameForLeafAppLayout:inSwitcherScreenRegion:];
-[SBSwitcherModifier defaultMultitaskingLayoutAttributesForDisplayItem:layoutAttributes:layoutGrid:];
-[SBSwitcherModifier displayItemsChangingSizeFromAppLayout:toAppLayout:fromDisplayItemLayoutAttributesMap:toDisplayItemLayoutAttributesMap:];
-[SBSwitcherModifier distanceToLeadingEdgeOfLeadingCardFromTrailingEdgeOfScreenWithVisibleIndexToStartSearch:numberOfRows:padding:layoutDirection:];
-[SBSwitcherModifier dummyAppLayoutWithBundleIdentifier:sceneIdentifier:];
-[SBSwitcherModifier flexibleAutoLayoutSpaceForAppLayout:];
-[SBSwitcherModifier flexibleAutoLayoutSpaceForAppLayout:calculatedUsingNewLayoutAttributesMap:itemsNeedingPositionSnapping:itemsNeedingSizeSnapping:];
-[SBSwitcherModifier handleAnimatablePropertyChangedEvent:];
-[SBSwitcherModifier handleAppInteractionEvent:];
-[SBSwitcherModifier handleBlurProgressEvent:];
-[SBSwitcherModifier handleContinuousFoldEvent:];
-[SBSwitcherModifier handleHardwareButtonDropletAnimationEvent:];
-[SBSwitcherModifier handleHideMorphToPIPAppLayoutEvent:];
-[SBSwitcherModifier handleHighlightEvent:];
-[SBSwitcherModifier handleHomeGrabberSettingsChangedEvent:];
-[SBSwitcherModifier handleHoverEvent:];
-[SBSwitcherModifier handleInitialSetupEvent:];
-[SBSwitcherModifier handleInsertionEvent:];
-[SBSwitcherModifier handleKeyboardInputEvent:];
-[SBSwitcherModifier handleMedusaSettingsChangedEvent:];
-[SBSwitcherModifier handlePointerCrossedDisplayBoundaryEvent:];
-[SBSwitcherModifier handlePrepareForSceneUpdateEvent:];
-[SBSwitcherModifier handleSceneReadyEvent:];
-[SBSwitcherModifier handleShelfFocusedDisplayItemsChangedEvent:];
-[SBSwitcherModifier handleSwipeHiddenWindowsPill:];
-[SBSwitcherModifier handleSwipeToKillEvent:];
-[SBSwitcherModifier handleTapAppLayoutHeaderEvent:];
-[SBSwitcherModifier handleTapHiddenWindowsPill:];
-[SBSwitcherModifier handleTapSlideOverTongueEvent:];
-[SBSwitcherModifier handleTransientUIIndirectPannedToDismissSwitcherModifierEvent:];
-[SBSwitcherModifier handleTransientUITapToDismissSwitcherModifierEvent:];
-[SBSwitcherModifier handleUpdateFocusedAppLayoutEvent:];
-[SBSwitcherModifier indexOfFirstFloatingAppFromAppLayouts:];
-[SBSwitcherModifier indexOfFirstMainAppLayoutFromAppLayouts:];
-[SBSwitcherModifier performWithTemporarilyInsertedAppLayout:atIndex:block:];
-[SBSwitcherModifier scaledFrameForIndex:];
-[SBSwitcherModifier scaledFrameForLayoutRole:inAppLayout:atIndex:];
-[SBSwitcherModifier shouldZoomToSystemApertureForEvent:activeLayout:];
-[SBSwitcherModifier stackDescription];
-[SBSwitcherModifier stackDescriptionWithPrefix:];
-[SBSwitcherModifier topMostLayoutElementsByAddingAppLayoutAndAccessories:toTopMostLayoutElements:orderFront:];
-[SBSwitcherModifier windowingConfiguration];
```
