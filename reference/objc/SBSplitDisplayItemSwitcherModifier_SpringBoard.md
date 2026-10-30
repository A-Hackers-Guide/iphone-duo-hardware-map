# `SBSplitDisplayItemSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifier`
- 6 instance variables, 6 properties, 23 instance methods, 0 class methods

## Instance variables

```
B _completesWhenGesturePossible;
B _hasInvalidatedAppLayoutsForInsertion;
B _hasInvalidatedAppLayoutsForRemoval;
@"SBDisplayItem" _displayItem;
@"SBSwitcherModifier" _wrappingModifier;
@"SBAppLayout" _overrideAndPromoteChildAppLayout;
```

## Properties

```
@property (TB,N,V_hasInvalidatedAppLayoutsForInsertion) hasInvalidatedAppLayoutsForInsertion;
@property (TB,N,V_hasInvalidatedAppLayoutsForRemoval) hasInvalidatedAppLayoutsForRemoval;
@property (T@"SBAppLayout",&,N,V_overrideAndPromoteChildAppLayout) overrideAndPromoteChildAppLayout;
@property (T@"SBDisplayItem",R,N,V_displayItem) displayItem;
@property (T@"SBSwitcherModifier",R,N,V_wrappingModifier) wrappingModifier;
@property (TB,N,V_completesWhenGesturePossible) completesWhenGesturePossible;
```

## Instance methods

```
-[SBSplitDisplayItemSwitcherModifier handleGestureEvent:];
-[SBSplitDisplayItemSwitcherModifier appLayoutsToEnsureExistForMainTransitionEvent:];
-[SBSplitDisplayItemSwitcherModifier handleEvent:];
-[SBSplitDisplayItemSwitcherModifier adjustedAppLayoutsForAppLayouts:];
-[SBSplitDisplayItemSwitcherModifier topMostLayoutElements];
-[SBSplitDisplayItemSwitcherModifier frameForLayoutRole:inAppLayout:withBounds:];
-[SBSplitDisplayItemSwitcherModifier frameForIndex:];
-[SBSplitDisplayItemSwitcherModifier completesWhenChildrenComplete];
-[SBSplitDisplayItemSwitcherModifier displayItem];
-[SBSplitDisplayItemSwitcherModifier preferredAppLayoutToReuseAccessoryForAppLayout:fromAppLayouts:];
-[SBSplitDisplayItemSwitcherModifier initWithDisplayItem:];
-[SBSplitDisplayItemSwitcherModifier _performOverrideAndPromoteChildAppLayoutToParent:withBlock:];
-[SBSplitDisplayItemSwitcherModifier appLayoutContainingAppLayout:];
-[SBSplitDisplayItemSwitcherModifier completesWhenGesturePossible];
-[SBSplitDisplayItemSwitcherModifier hasInvalidatedAppLayoutsForInsertion];
-[SBSplitDisplayItemSwitcherModifier hasInvalidatedAppLayoutsForRemoval];
-[SBSplitDisplayItemSwitcherModifier initWithDisplayItem:wrappingModifier:];
-[SBSplitDisplayItemSwitcherModifier overrideAndPromoteChildAppLayout];
-[SBSplitDisplayItemSwitcherModifier setCompletesWhenGesturePossible:];
-[SBSplitDisplayItemSwitcherModifier setHasInvalidatedAppLayoutsForInsertion:];
-[SBSplitDisplayItemSwitcherModifier setHasInvalidatedAppLayoutsForRemoval:];
-[SBSplitDisplayItemSwitcherModifier setOverrideAndPromoteChildAppLayout:];
-[SBSplitDisplayItemSwitcherModifier wrappingModifier];
```
