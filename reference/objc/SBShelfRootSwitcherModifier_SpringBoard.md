# `SBShelfRootSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBFluidSwitcherRootSwitcherModifier`
- Protocols: `SBShelfExpansionSwitcherModifierDelegate`
- 7 instance variables, 8 properties, 29 instance methods, 0 class methods

## Instance variables

```
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _portraitContainerBounds;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _landscapeContainerBounds;
B _isRoutingFrameForIndexToFloating;
Q _displayMode;
Q _appearanceState;
Q _animationStyle;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _targetFrame;
```

## Properties

```
@property (TQ,N,V_displayMode) displayMode;
@property (TQ,N,V_appearanceState) appearanceState;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_targetFrame) targetFrame;
@property (TQ,N,V_animationStyle) animationStyle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBShelfRootSwitcherModifier didMoveToParentModifier:];
-[SBShelfRootSwitcherModifier userScrollingModifierForScrollEvent:];
-[SBShelfRootSwitcherModifier multitaskingModifierForEvent:];
-[SBShelfRootSwitcherModifier containerViewBounds];
-[SBShelfRootSwitcherModifier setDisplayMode:];
-[SBShelfRootSwitcherModifier insertionModifierForInsertionEvent:];
-[SBShelfRootSwitcherModifier headerStyleForIndex:];
-[SBShelfRootSwitcherModifier frameForIndex:];
-[SBShelfRootSwitcherModifier displayMode];
-[SBShelfRootSwitcherModifier tintStyleForLayoutRole:inAppLayout:];
-[SBShelfRootSwitcherModifier animationStyle];
-[SBShelfRootSwitcherModifier keyboardSuppressionMode];
-[SBShelfRootSwitcherModifier removalModifierForRemovalEvent:];
-[SBShelfRootSwitcherModifier floorModifierForTransitionEvent:];
-[SBShelfRootSwitcherModifier setDelegate:];
-[SBShelfRootSwitcherModifier focusedAppModifierForUpdateFocusedAppLayoutEvent:];
-[SBShelfRootSwitcherModifier appLayoutsToResignActive];
-[SBShelfRootSwitcherModifier floorModifierForGestureEvent:];
-[SBShelfRootSwitcherModifier setAnimationStyle:];
-[SBShelfRootSwitcherModifier transitionModifierForMainTransitionEvent:];
-[SBShelfRootSwitcherModifier assistantIslandModifierForEvent:];
-[SBShelfRootSwitcherModifier swipeToKillModifierForSwipeToKillEvent:];
-[SBShelfRootSwitcherModifier setTargetFrame:];
-[SBShelfRootSwitcherModifier targetFrame];
-[SBShelfRootSwitcherModifier appearanceState];
-[SBShelfRootSwitcherModifier setAppearanceState:];
-[SBShelfRootSwitcherModifier floatingDockHeight];
-[SBShelfRootSwitcherModifier _rebuildContainerBounds];
-[SBShelfRootSwitcherModifier orderedVisibleAppLayoutsForShelfExpansionModifier:];
```
