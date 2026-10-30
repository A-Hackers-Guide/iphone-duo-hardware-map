# `SBHomePeekWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 4 instance variables, 2 properties, 38 instance methods, 0 class methods

## Instance variables

```
B _hasUpdatedForcePeekingEdge;
B _forcePeekingTrailingEdge;
@"SBAppLayout" _peekingAppLayout;
q _configuration;
```

## Properties

```
@property (T@"SBAppLayout",R,N,V_peekingAppLayout) peekingAppLayout;
@property (Tq,R,N,V_configuration) configuration;
```

## Instance methods

```
-[SBHomePeekWindowingModifier isSwitcherWindowUserInteractionEnabled];
-[SBHomePeekWindowingModifier shouldUseAnchorPointToPinLayoutRolesToSpace:];
-[SBHomePeekWindowingModifier appLayoutsToEnsureExistForMainTransitionEvent:];
-[SBHomePeekWindowingModifier isHomeScreenContentRequired];
-[SBHomePeekWindowingModifier peekingAppLayout];
-[SBHomePeekWindowingModifier transactionCompletionOptions];
-[SBHomePeekWindowingModifier adjustedAppLayoutsForAppLayouts:];
-[SBHomePeekWindowingModifier isSwitcherWindowVisible];
-[SBHomePeekWindowingModifier transitionDidUpdate:];
-[SBHomePeekWindowingModifier layoutViewModelsIfNeeded];
-[SBHomePeekWindowingModifier perspectiveAngleForLayoutRole:inAppLayout:withPerspectiveAngle:];
-[SBHomePeekWindowingModifier shouldAllowContentViewTouchesForLayoutRole:inAppLayout:];
-[SBHomePeekWindowingModifier scaleForLayoutRole:inAppLayout:];
-[SBHomePeekWindowingModifier frameForLayoutRole:inAppLayout:withBounds:];
-[SBHomePeekWindowingModifier switcherHitTestsAsOpaque];
-[SBHomePeekWindowingModifier destinationAppLayoutForDismissingCurrentMode];
-[SBHomePeekWindowingModifier keyboardSuppressionMode];
-[SBHomePeekWindowingModifier transitionWillBegin:];
-[SBHomePeekWindowingModifier shadowForItem:];
-[SBHomePeekWindowingModifier visibleItems];
-[SBHomePeekWindowingModifier cornersForItem:];
-[SBHomePeekWindowingModifier configuration];
-[SBHomePeekWindowingModifier isLayoutRoleSelectable:inAppLayout:];
-[SBHomePeekWindowingModifier opacityForItem:];
-[SBHomePeekWindowingModifier topMostItems];
-[SBHomePeekWindowingModifier frameForItem:];
-[SBHomePeekWindowingModifier titleStyleForItem:];
-[SBHomePeekWindowingModifier willBegin];
-[SBHomePeekWindowingModifier _configureAndAddDismissalTransitionRequest:];
-[SBHomePeekWindowingModifier _frameForContinuousExposePeekingDisplayItem:inAppLayout:bounds:];
-[SBHomePeekWindowingModifier _updateForcePeekingEdgeIfNeeded];
-[SBHomePeekWindowingModifier _numberOfPeekingItemsAboveDisplayItem:inAppLayout:bounds:];
-[SBHomePeekWindowingModifier _numberOfPeekingItemsAboveDisplayItem:peekingOnEdge:autoLayoutSpace:zOrderedItems:bounds:];
-[SBHomePeekWindowingModifier _peekEdgeForDisplayItem:withZOrderedItems:autoLayoutSpace:bounds:];
-[SBHomePeekWindowingModifier _perspectiveAngleForPeekingEdge:];
-[SBHomePeekWindowingModifier appLayoutTapped:];
-[SBHomePeekWindowingModifier initWithPeekingAppLayout:configuration:];
-[SBHomePeekWindowingModifier tappedOutsideToDismiss:];
```
