# `SBContinuousExposeWindowDropSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransitionSwitcherModifier`
- 5 instance variables, 3 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"SBDisplayItem" _minimizingItem;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _initialFrameOfMinimizingItem;
@"SBDisplayItem" _selectedDisplayItem;
@"SBAppLayout" _toAppLayout;
{CGPoint="x"d"y"d} _liftOffVelocity;
```

## Properties

```
@property (T@"SBDisplayItem",R,N,V_selectedDisplayItem) selectedDisplayItem;
@property (T@"SBAppLayout",R,N,V_toAppLayout) toAppLayout;
@property (T{CGPoint=dd},R,N,V_liftOffVelocity) liftOffVelocity;
```

## Instance methods

```
-[SBContinuousExposeWindowDropSwitcherModifier shouldUseAnchorPointToPinLayoutRolesToSpace:];
-[SBContinuousExposeWindowDropSwitcherModifier didMoveToParentModifier:];
-[SBContinuousExposeWindowDropSwitcherModifier animationAttributesForLayoutElement:];
-[SBContinuousExposeWindowDropSwitcherModifier handleTransitionEvent:];
-[SBContinuousExposeWindowDropSwitcherModifier fadeInDelayForSplitViewHandles];
-[SBContinuousExposeWindowDropSwitcherModifier transitionDidEnd];
-[SBContinuousExposeWindowDropSwitcherModifier frameForLayoutRole:inAppLayout:withBounds:];
-[SBContinuousExposeWindowDropSwitcherModifier fullyPresentedFrameForAppLayout:frame:];
-[SBContinuousExposeWindowDropSwitcherModifier asyncRenderingDisabled];
-[SBContinuousExposeWindowDropSwitcherModifier _appLayoutContainingDisplayItem:];
-[SBContinuousExposeWindowDropSwitcherModifier toAppLayout];
-[SBContinuousExposeWindowDropSwitcherModifier isLayoutRoleMatchMovedToScene:inAppLayout:];
-[SBContinuousExposeWindowDropSwitcherModifier maskedCornersForLayoutRole:inAppLayout:withMaskedCorners:];
-[SBContinuousExposeWindowDropSwitcherModifier liftOffVelocity];
-[SBContinuousExposeWindowDropSwitcherModifier _isLayoutRolePartOfWindowDragInteraction:inAppLayout:];
-[SBContinuousExposeWindowDropSwitcherModifier handleSceneReadyEvent:];
-[SBContinuousExposeWindowDropSwitcherModifier initWithTransitionID:selectedDisplayItem:toAppLayout:initialAppLayout:liftOffVelocity:];
-[SBContinuousExposeWindowDropSwitcherModifier selectedDisplayItem];
```
