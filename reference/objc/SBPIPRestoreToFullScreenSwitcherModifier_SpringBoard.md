# `SBPIPRestoreToFullScreenSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransitionSwitcherModifier`
- 6 instance variables, 2 properties, 29 instance methods, 0 class methods

## Instance variables

```
q _toLayoutRole;
@"SBAppLayout" _fromAppLayout;
@"SBAppLayout" _toAppLayout;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _toAppLayoutBoundingBox;
B _shouldClippingTakeShadowIntoAccount;
B _shouldForceDefaultAnchorPointForTransition;
```

## Properties

```
@property (TB,N,V_shouldClippingTakeShadowIntoAccount) shouldClippingTakeShadowIntoAccount;
@property (TB,N,V_shouldForceDefaultAnchorPointForTransition) shouldForceDefaultAnchorPointForTransition;
```

## Instance methods

```
-[SBPIPRestoreToFullScreenSwitcherModifier scaleForIndex:];
-[SBPIPRestoreToFullScreenSwitcherModifier anchorPointForIndex:];
-[SBPIPRestoreToFullScreenSwitcherModifier clippingFrameForIndex:withBounds:];
-[SBPIPRestoreToFullScreenSwitcherModifier shouldUseAnchorPointToPinLayoutRolesToSpace:];
-[SBPIPRestoreToFullScreenSwitcherModifier clipsToBoundsAtIndex:];
-[SBPIPRestoreToFullScreenSwitcherModifier _isToAppLayout:];
-[SBPIPRestoreToFullScreenSwitcherModifier shouldForceDefaultAnchorPointForTransition];
-[SBPIPRestoreToFullScreenSwitcherModifier cornerRadiiForIndex:];
-[SBPIPRestoreToFullScreenSwitcherModifier adjustedSpaceAccessoryViewAnchorPoint:forAppLayout:];
-[SBPIPRestoreToFullScreenSwitcherModifier animationAttributesForLayoutElement:];
-[SBPIPRestoreToFullScreenSwitcherModifier setShouldForceDefaultAnchorPointForTransition:];
-[SBPIPRestoreToFullScreenSwitcherModifier clippingFrameForLayoutRole:inAppLayout:atIndex:withBounds:];
-[SBPIPRestoreToFullScreenSwitcherModifier adjustedSpaceAccessoryViewFrame:forAppLayout:];
-[SBPIPRestoreToFullScreenSwitcherModifier visibleHomeAffordanceLayoutElements];
-[SBPIPRestoreToFullScreenSwitcherModifier shouldPinLayoutRolesToSpace:];
-[SBPIPRestoreToFullScreenSwitcherModifier visibleAppLayouts];
-[SBPIPRestoreToFullScreenSwitcherModifier initWithTransitionID:transitionModifier:fromAppLayout:toAppLayout:toLayoutRole:];
-[SBPIPRestoreToFullScreenSwitcherModifier perspectiveAngleForIndex:];
-[SBPIPRestoreToFullScreenSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBPIPRestoreToFullScreenSwitcherModifier frameForIndex:];
-[SBPIPRestoreToFullScreenSwitcherModifier transitionWillBegin];
-[SBPIPRestoreToFullScreenSwitcherModifier _isToOrFromAppLayoutIndex:];
-[SBPIPRestoreToFullScreenSwitcherModifier _isToOrFromAppLayout:];
-[SBPIPRestoreToFullScreenSwitcherModifier completesWhenChildrenComplete];
-[SBPIPRestoreToFullScreenSwitcherModifier _isFromAppLayoutIndex:];
-[SBPIPRestoreToFullScreenSwitcherModifier shouldClippingTakeShadowIntoAccount];
-[SBPIPRestoreToFullScreenSwitcherModifier _insetFrameForDiffuseShadowRadius:];
-[SBPIPRestoreToFullScreenSwitcherModifier setShouldClippingTakeShadowIntoAccount:];
-[SBPIPRestoreToFullScreenSwitcherModifier _isToAppLayoutIndex:];
```
