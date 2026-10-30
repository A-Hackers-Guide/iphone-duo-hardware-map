# `SBBlurItemContainerSwitcherEventResponse`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifierEventResponse`
- 4 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
B _shouldBlur;
@"SBAppLayout" _appLayout;
@"SBBlurItemContainerParameters" _blurParameters;
q _animationUpdateMode;
```

## Properties

```
@property (T@"SBAppLayout",R,N,V_appLayout) appLayout;
@property (TB,R,N,V_shouldBlur) shouldBlur;
@property (T@"SBBlurItemContainerParameters",R,N,V_blurParameters) blurParameters;
@property (Tq,R,N,V_animationUpdateMode) animationUpdateMode;
```

## Instance methods

```
-[SBBlurItemContainerSwitcherEventResponse initWithAppLayout:shouldBlur:blurParameters:animationUpdateMode:];
-[SBBlurItemContainerSwitcherEventResponse appLayout];
-[SBBlurItemContainerSwitcherEventResponse shouldBlur];
-[SBBlurItemContainerSwitcherEventResponse blurParameters];
-[SBBlurItemContainerSwitcherEventResponse initWithAppLayout:shouldBlur:animationUpdateMode:];
-[SBBlurItemContainerSwitcherEventResponse animationUpdateMode];
-[SBBlurItemContainerSwitcherEventResponse type];
-[SBBlurItemContainerSwitcherEventResponse description];
```
