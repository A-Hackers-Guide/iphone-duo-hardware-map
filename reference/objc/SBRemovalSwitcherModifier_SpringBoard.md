# `SBRemovalSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifier`
- 10 instance variables, 0 properties, 18 instance methods, 0 class methods

## Instance variables

```
q _layoutRole;
@"SBAppLayout" _appLayout;
q _reason;
@"SBSwitcherModifier" _multitaskingModifier;
B _hasResizedEnoughToUnblur;
Q _indexToScrollToAfterRemoval;
Q _indexOfAppLayoutPriorToRemoval;
@"NSSet" _visibleAppLayoutsPriorToRemoval;
@"SBAppLayout" _resultingAppLayoutIfAny;
Q _phase;
```

## Instance methods

```
-[SBRemovalSwitcherModifier shouldScaleContentToFillBoundsAtIndex:];
-[SBRemovalSwitcherModifier shouldUseAnchorPointToPinLayoutRolesToSpace:];
-[SBRemovalSwitcherModifier clipsToUnobscuredMarginAtIndex:];
-[SBRemovalSwitcherModifier animationAttributesForLayoutElement:];
-[SBRemovalSwitcherModifier topMostLayoutElements];
-[SBRemovalSwitcherModifier visibleAppLayouts];
-[SBRemovalSwitcherModifier shouldAccessoryDrawShadowForAppLayout:];
-[SBRemovalSwitcherModifier handleResizeProgressEvent:];
-[SBRemovalSwitcherModifier handleRemovalEvent:];
-[SBRemovalSwitcherModifier blurViewIconScaleForIndex:];
-[SBRemovalSwitcherModifier resizeProgressNotificationsForLayoutRole:inAppLayout:];
-[SBRemovalSwitcherModifier asyncRenderingAttributesForAppLayout:];
-[SBRemovalSwitcherModifier isLayoutRoleBlurred:inAppLayout:];
-[SBRemovalSwitcherModifier _performBlockWhileSimulatingPostRemovalAppLayoutState:];
-[SBRemovalSwitcherModifier _remainingAppLayoutForRemovingLayoutRole:inAppLayout:];
-[SBRemovalSwitcherModifier handleInsertionEvent:];
-[SBRemovalSwitcherModifier handleSceneReadyEvent:];
-[SBRemovalSwitcherModifier initWithLayoutRole:inAppLayout:reason:];
```
