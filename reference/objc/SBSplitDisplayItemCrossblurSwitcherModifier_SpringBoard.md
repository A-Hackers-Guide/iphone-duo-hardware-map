# `SBSplitDisplayItemCrossblurSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifier`
- 4 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"SBSplitDisplayItemSwitcherModifier" _toSplitDisplayItemModifier;
@"SBAppLayout" _fromAppLayout;
@"SBAppLayout" _toAppLayout;
q _layoutRole;
```

## Properties

```
@property (T@"SBAppLayout",R,N,V_fromAppLayout) fromAppLayout;
@property (T@"SBAppLayout",R,N,V_toAppLayout) toAppLayout;
@property (Tq,R,N,V_layoutRole) layoutRole;
```

## Instance methods

```
-[SBSplitDisplayItemCrossblurSwitcherModifier handleEvent:];
-[SBSplitDisplayItemCrossblurSwitcherModifier layoutRole];
-[SBSplitDisplayItemCrossblurSwitcherModifier visibleHomeAffordanceLayoutElements];
-[SBSplitDisplayItemCrossblurSwitcherModifier topMostLayoutElements];
-[SBSplitDisplayItemCrossblurSwitcherModifier containerLeafAppLayoutForShelf:];
-[SBSplitDisplayItemCrossblurSwitcherModifier fromAppLayout];
-[SBSplitDisplayItemCrossblurSwitcherModifier homeAffordanceLayoutElementToPortalIntoShelf:];
-[SBSplitDisplayItemCrossblurSwitcherModifier toAppLayout];
-[SBSplitDisplayItemCrossblurSwitcherModifier _previousHomeAffordanceAppLayout];
-[SBSplitDisplayItemCrossblurSwitcherModifier appLayoutContainingAppLayout:];
-[SBSplitDisplayItemCrossblurSwitcherModifier initWithTransitionID:fromAppLayout:toAppLayout:layoutRole:];
```
