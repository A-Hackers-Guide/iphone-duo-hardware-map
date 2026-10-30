# `SBStashSlideOverItemIndirectGestureWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 9 instance variables, 0 properties, 26 instance methods, 0 class methods

## Instance variables

```
{SBDisplayItemSlideOverConfiguration="corner"q"yOffsetFromCorner"d"size"{CGSize="width"d"height"d}"isActive"B"isStashed"B"dodgesDock"B} _initialSlideOverConfiguration;
@"SBDisplayItem" _slideOverDisplayItem;
@"NSUUID" _gestureID;
{CGPoint="x"d"y"d} _translation;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _initialFrame;
@"SBAppLayout" _initialAppLayout;
B _wantsSlideOverTongue;
Q _slideOverTongueState;
Q _slideOverTongueDirection;
```

## Instance methods

```
-[SBStashSlideOverItemIndirectGestureWindowingModifier shouldUseAnchorPointToPinLayoutRolesToSpace:];
-[SBStashSlideOverItemIndirectGestureWindowingModifier adjustedAppLayoutsForAppLayouts:];
-[SBStashSlideOverItemIndirectGestureWindowingModifier isSwitcherWindowVisible];
-[SBStashSlideOverItemIndirectGestureWindowingModifier appLayoutsToCacheSnapshots];
-[SBStashSlideOverItemIndirectGestureWindowingModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBStashSlideOverItemIndirectGestureWindowingModifier frameForLayoutRole:inAppLayout:withBounds:];
-[SBStashSlideOverItemIndirectGestureWindowingModifier transitionWillBegin:];
-[SBStashSlideOverItemIndirectGestureWindowingModifier visibleItems];
-[SBStashSlideOverItemIndirectGestureWindowingModifier cornersForItem:];
-[SBStashSlideOverItemIndirectGestureWindowingModifier wantsSlideOverTongue];
-[SBStashSlideOverItemIndirectGestureWindowingModifier slideOverTongueDirection];
-[SBStashSlideOverItemIndirectGestureWindowingModifier animationAttributesForItem:];
-[SBStashSlideOverItemIndirectGestureWindowingModifier isLayoutRoleMatchMovedToScene:inAppLayout:];
-[SBStashSlideOverItemIndirectGestureWindowingModifier topMostItems];
-[SBStashSlideOverItemIndirectGestureWindowingModifier appLayoutToAttachSlideOverTongue];
-[SBStashSlideOverItemIndirectGestureWindowingModifier slideOverTongueState];
-[SBStashSlideOverItemIndirectGestureWindowingModifier frameForItem:];
-[SBStashSlideOverItemIndirectGestureWindowingModifier appLayoutsToCacheFullsizeSnapshots];
-[SBStashSlideOverItemIndirectGestureWindowingModifier willBegin];
-[SBStashSlideOverItemIndirectGestureWindowingModifier didComplete];
-[SBStashSlideOverItemIndirectGestureWindowingModifier _responseForGestureEnd:];
-[SBStashSlideOverItemIndirectGestureWindowingModifier _slideOverAppLayout];
-[SBStashSlideOverItemIndirectGestureWindowingModifier gestureDidComplete:];
-[SBStashSlideOverItemIndirectGestureWindowingModifier gestureDidUpdate:];
-[SBStashSlideOverItemIndirectGestureWindowingModifier gestureWillBegin:];
-[SBStashSlideOverItemIndirectGestureWindowingModifier transitionDidComplete:];
```
