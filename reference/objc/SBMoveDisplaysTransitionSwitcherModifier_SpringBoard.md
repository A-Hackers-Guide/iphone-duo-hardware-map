# `SBMoveDisplaysTransitionSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransitionSwitcherModifier`
- 3 instance variables, 3 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"SBTransitionSwitcherModifierMoveDisplaysContext" _moveDisplaysContext;
@"SBAppLayout" _fromAppLayout;
@"SBAppLayout" _remainingAppLayout;
```

## Properties

```
@property (T@"SBAppLayout",R,N,V_fromAppLayout) fromAppLayout;
@property (T@"SBAppLayout",R,N,V_remainingAppLayout) remainingAppLayout;
@property (T@"SBTransitionSwitcherModifierMoveDisplaysContext",R,N,V_moveDisplaysContext) moveDisplaysContext;
```

## Instance methods

```
-[SBMoveDisplaysTransitionSwitcherModifier scaleForIndex:];
-[SBMoveDisplaysTransitionSwitcherModifier anchorPointForIndex:];
-[SBMoveDisplaysTransitionSwitcherModifier adjustedAppLayoutsForAppLayouts:];
-[SBMoveDisplaysTransitionSwitcherModifier topMostLayoutElements];
-[SBMoveDisplaysTransitionSwitcherModifier isSwitcherWindowVisible];
-[SBMoveDisplaysTransitionSwitcherModifier transitionWillUpdate];
-[SBMoveDisplaysTransitionSwitcherModifier visibleAppLayouts];
-[SBMoveDisplaysTransitionSwitcherModifier perspectiveAngleForIndex:];
-[SBMoveDisplaysTransitionSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBMoveDisplaysTransitionSwitcherModifier transitionDidEnd];
-[SBMoveDisplaysTransitionSwitcherModifier scaleForLayoutRole:inAppLayout:];
-[SBMoveDisplaysTransitionSwitcherModifier frameForLayoutRole:inAppLayout:withBounds:];
-[SBMoveDisplaysTransitionSwitcherModifier frameForIndex:];
-[SBMoveDisplaysTransitionSwitcherModifier transitionWillBegin];
-[SBMoveDisplaysTransitionSwitcherModifier fromAppLayout];
-[SBMoveDisplaysTransitionSwitcherModifier isLayoutRoleMatchMovedToScene:inAppLayout:];
-[SBMoveDisplaysTransitionSwitcherModifier moveDisplaysContext];
-[SBMoveDisplaysTransitionSwitcherModifier isLayoutRoleBlurred:inAppLayout:];
-[SBMoveDisplaysTransitionSwitcherModifier _appLayoutsContainingMovingDisplayItems];
-[SBMoveDisplaysTransitionSwitcherModifier handleSceneReadyEvent:];
-[SBMoveDisplaysTransitionSwitcherModifier initWithTransitionEvent:];
-[SBMoveDisplaysTransitionSwitcherModifier remainingAppLayout];
```
