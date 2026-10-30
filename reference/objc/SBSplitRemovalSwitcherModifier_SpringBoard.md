# `SBSplitRemovalSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransitionSwitcherModifier`
- 8 instance variables, 0 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _fromAppLayout;
@"SBAppLayout" _toAppLayout;
q _layoutRoleToKeep;
q _layoutRoleToRemove;
q _animationStyle;
@"SBAppLayout" _remainingAppLayout;
@"SBAppLayout" _removedAppLayout;
q _animationPhase;
```

## Instance methods

```
-[SBSplitRemovalSwitcherModifier cornerRadiiForIndex:];
-[SBSplitRemovalSwitcherModifier animationAttributesForLayoutElement:];
-[SBSplitRemovalSwitcherModifier adjustedAppLayoutsForAppLayouts:];
-[SBSplitRemovalSwitcherModifier topMostLayoutElements];
-[SBSplitRemovalSwitcherModifier transitionWillUpdate];
-[SBSplitRemovalSwitcherModifier isWallpaperRequiredForSwitcher];
-[SBSplitRemovalSwitcherModifier visibleAppLayouts];
-[SBSplitRemovalSwitcherModifier isContentStatusBarVisibleForIndex:];
-[SBSplitRemovalSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBSplitRemovalSwitcherModifier handleTimerEvent:];
-[SBSplitRemovalSwitcherModifier scaleForLayoutRole:inAppLayout:];
-[SBSplitRemovalSwitcherModifier frameForLayoutRole:inAppLayout:withBounds:];
-[SBSplitRemovalSwitcherModifier wallpaperStyle];
-[SBSplitRemovalSwitcherModifier frameForIndex:];
-[SBSplitRemovalSwitcherModifier transitionWillBegin];
-[SBSplitRemovalSwitcherModifier asyncRenderingAttributesForAppLayout:];
-[SBSplitRemovalSwitcherModifier isLayoutRoleMatchMovedToScene:inAppLayout:];
-[SBSplitRemovalSwitcherModifier isLayoutRoleBlurred:inAppLayout:];
-[SBSplitRemovalSwitcherModifier handleSceneReadyEvent:];
-[SBSplitRemovalSwitcherModifier initWithTransitionID:fromAppLayout:toAppLayout:layoutRoleToRemove:animationStyle:];
```
