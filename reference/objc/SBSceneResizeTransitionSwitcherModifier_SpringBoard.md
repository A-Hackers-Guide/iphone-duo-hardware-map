# `SBSceneResizeTransitionSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransitionSwitcherModifier`
- 6 instance variables, 1 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _fromAppLayout;
@"SBAppLayout" _toAppLayout;
@"SBAppLayout" _discardedAppLayout;
q _discardedLayoutRole;
d _minimumCardWithForDismissal;
@"SBAppLayout" _selectedAppLayout;
```

## Properties

```
@property (T@"SBAppLayout",&,N,V_selectedAppLayout) selectedAppLayout;
```

## Instance methods

```
-[SBSceneResizeTransitionSwitcherModifier shouldUseAnchorPointToPinLayoutRolesToSpace:];
-[SBSceneResizeTransitionSwitcherModifier appLayoutsToEnsureExistForMainTransitionEvent:];
-[SBSceneResizeTransitionSwitcherModifier cornerRadiiForIndex:];
-[SBSceneResizeTransitionSwitcherModifier animationAttributesForLayoutElement:];
-[SBSceneResizeTransitionSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBSceneResizeTransitionSwitcherModifier frameForLayoutRole:inAppLayout:withBounds:];
-[SBSceneResizeTransitionSwitcherModifier frameForIndex:];
-[SBSceneResizeTransitionSwitcherModifier selectedAppLayout];
-[SBSceneResizeTransitionSwitcherModifier asyncRenderingAttributesForAppLayout:];
-[SBSceneResizeTransitionSwitcherModifier isLayoutRoleMatchMovedToScene:inAppLayout:];
-[SBSceneResizeTransitionSwitcherModifier isLayoutRoleBlurred:inAppLayout:];
-[SBSceneResizeTransitionSwitcherModifier handleSceneReadyEvent:];
-[SBSceneResizeTransitionSwitcherModifier initWithTransitionID:fromAppLayout:toAppLayout:minimumCardWithForDismissal:];
-[SBSceneResizeTransitionSwitcherModifier setSelectedAppLayout:];
```
