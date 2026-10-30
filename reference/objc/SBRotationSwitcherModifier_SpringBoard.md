# `SBRotationSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransitionSwitcherModifier`
- 4 instance variables, 4 properties, 15 instance methods, 0 class methods

## Instance variables

```
B _shouldNotUseAnchorPointToPinLayoutRolesToSpace;
@"SBAppLayout" _appLayout;
q _fromInterfaceOrientation;
q _toInterfaceOrientation;
```

## Properties

```
@property (T@"SBAppLayout",R,N,V_appLayout) appLayout;
@property (Tq,R,N,V_fromInterfaceOrientation) fromInterfaceOrientation;
@property (Tq,R,N,V_toInterfaceOrientation) toInterfaceOrientation;
@property (TB,N,V_shouldNotUseAnchorPointToPinLayoutRolesToSpace) shouldNotUseAnchorPointToPinLayoutRolesToSpace;
```

## Instance methods

```
-[SBRotationSwitcherModifier rotationAngleForIndex:];
-[SBRotationSwitcherModifier shouldUseAnchorPointToPinLayoutRolesToSpace:];
-[SBRotationSwitcherModifier animationAttributesForLayoutElement:];
-[SBRotationSwitcherModifier toInterfaceOrientation];
-[SBRotationSwitcherModifier appLayout];
-[SBRotationSwitcherModifier transitionWillBegin];
-[SBRotationSwitcherModifier keyboardSuppressionMode];
-[SBRotationSwitcherModifier fromInterfaceOrientation];
-[SBRotationSwitcherModifier shouldPerformRotationAnimationForOrientationChange];
-[SBRotationSwitcherModifier appLayoutsToResignActive];
-[SBRotationSwitcherModifier asyncRenderingAttributesForAppLayout:];
-[SBRotationSwitcherModifier initWithTransitionID:appLayout:fromInterfaceOrientation:toInterfaceOrientation:];
-[SBRotationSwitcherModifier requireStripContentsInViewHierarchy];
-[SBRotationSwitcherModifier setShouldNotUseAnchorPointToPinLayoutRolesToSpace:];
-[SBRotationSwitcherModifier shouldNotUseAnchorPointToPinLayoutRolesToSpace];
```
