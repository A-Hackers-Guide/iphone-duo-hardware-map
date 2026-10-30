# `SBHomePeekToFullScreenTransitionModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 6 instance variables, 1 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _toAppLayout;
@"SBAppLayout" _fromAppLayout;
@"SBAppLayout" _slidingOffPeekingAppLayout;
@"SBHomePeekWindowingModifier" _fromHomePeekModifier;
B _toFullScreen;
@"SBSwitcherModifier" _transitionModifier;
```

## Properties

```
@property (T@"SBSwitcherModifier",R,N,V_transitionModifier) transitionModifier;
```

## Instance methods

```
-[SBHomePeekToFullScreenTransitionModifier shouldUseAnchorPointToPinLayoutRolesToSpace:];
-[SBHomePeekToFullScreenTransitionModifier appLayoutsToEnsureExistForMainTransitionEvent:];
-[SBHomePeekToFullScreenTransitionModifier perspectiveAngleForLayoutRole:inAppLayout:withPerspectiveAngle:];
-[SBHomePeekToFullScreenTransitionModifier fadeInDelayForSplitViewHandles];
-[SBHomePeekToFullScreenTransitionModifier scaleForLayoutRole:inAppLayout:];
-[SBHomePeekToFullScreenTransitionModifier frameForLayoutRole:inAppLayout:withBounds:];
-[SBHomePeekToFullScreenTransitionModifier transitionWillBegin:];
-[SBHomePeekToFullScreenTransitionModifier completesWhenChildrenComplete];
-[SBHomePeekToFullScreenTransitionModifier animationAttributesForItem:];
-[SBHomePeekToFullScreenTransitionModifier opacityForItem:];
-[SBHomePeekToFullScreenTransitionModifier topMostItems];
-[SBHomePeekToFullScreenTransitionModifier frameForItem:];
-[SBHomePeekToFullScreenTransitionModifier wantsSpaceAccessoryViewGenieForAppLayout:];
-[SBHomePeekToFullScreenTransitionModifier initWithTransitionModifier:slidingOffPeekingAppLayout:fromPeekingConfiguration:];
-[SBHomePeekToFullScreenTransitionModifier transitionModifier];
```
