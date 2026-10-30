# `SBInsertionSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifier`
- 4 instance variables, 1 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _appLayout;
B _isSimulatingPreInsertionState;
{CGPoint="x"d"y"d} _contentOffsetBeforeInsertion;
Q _phase;
```

## Properties

```
@property (TQ,R,N,V_phase) phase;
```

## Instance methods

```
-[SBInsertionSwitcherModifier clipsToUnobscuredMarginAtIndex:];
-[SBInsertionSwitcherModifier animationAttributesForLayoutElement:];
-[SBInsertionSwitcherModifier initWithAppLayout:];
-[SBInsertionSwitcherModifier phase];
-[SBInsertionSwitcherModifier visibleAppLayouts];
-[SBInsertionSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBInsertionSwitcherModifier scrollViewContentOffset];
-[SBInsertionSwitcherModifier _performBlockBySimulatingPreInsertionState:];
-[SBInsertionSwitcherModifier handleInsertionEvent:];
```
