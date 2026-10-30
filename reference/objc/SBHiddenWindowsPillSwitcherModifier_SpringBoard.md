# `SBHiddenWindowsPillSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifier`
- 4 instance variables, 2 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _toAppLayout;
@"SBAppLayout" _iconAppLayout;
@"SBSwitcherHiddenWindowsPill" _hiddenWindowsPill;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _iconFrame;
```

## Properties

```
@property (T@"SBSwitcherHiddenWindowsPill",R,N,V_hiddenWindowsPill) hiddenWindowsPill;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_iconFrame) iconFrame;
```

## Instance methods

```
-[SBHiddenWindowsPillSwitcherModifier contentAlphaForHiddenWindowsPill:];
-[SBHiddenWindowsPillSwitcherModifier backgroundForHiddenWindowsPill:];
-[SBHiddenWindowsPillSwitcherModifier handleTransitionEvent:];
-[SBHiddenWindowsPillSwitcherModifier anchorPointForHiddenWindowsPill:];
-[SBHiddenWindowsPillSwitcherModifier pillOffsetForHiddenWindowsPill:];
-[SBHiddenWindowsPillSwitcherModifier pillScaleForHiddenWindowsPill:];
-[SBHiddenWindowsPillSwitcherModifier iconFrame];
-[SBHiddenWindowsPillSwitcherModifier contentScaleForHiddenWindowsPill:];
-[SBHiddenWindowsPillSwitcherModifier centerForHiddenWindowsPill:];
-[SBHiddenWindowsPillSwitcherModifier contentBlurRadiusForHiddenWindowsPill:];
-[SBHiddenWindowsPillSwitcherModifier hiddenWindowsPillModeForHiddenWindowsPill:];
-[SBHiddenWindowsPillSwitcherModifier alphaForHiddenWindowsPill:];
-[SBHiddenWindowsPillSwitcherModifier transformForHiddenWindowsPill:];
-[SBHiddenWindowsPillSwitcherModifier _willDockBeVisibleAtEndOfTransition];
-[SBHiddenWindowsPillSwitcherModifier anchorPointXForIconMidX:pillFullWidth:containerViewBounds:screenMargin:];
-[SBHiddenWindowsPillSwitcherModifier hiddenWindowsPill];
-[SBHiddenWindowsPillSwitcherModifier initWithHiddenWindowsPill:];
```
