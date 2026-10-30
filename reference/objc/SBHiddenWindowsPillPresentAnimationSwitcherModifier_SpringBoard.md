# `SBHiddenWindowsPillPresentAnimationSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifier`
- 5 instance variables, 2 properties, 20 instance methods, 0 class methods

## Instance variables

```
Q _phase;
@"SBAppLayout" _iconAppLayout;
Q _generationCount;
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
-[SBHiddenWindowsPillPresentAnimationSwitcherModifier dockWindowLevelPriority];
-[SBHiddenWindowsPillPresentAnimationSwitcherModifier dockWindowLevel];
-[SBHiddenWindowsPillPresentAnimationSwitcherModifier bounceIconScaleForHiddenWindowsPill:];
-[SBHiddenWindowsPillPresentAnimationSwitcherModifier animationAttributesForLayoutElement:];
-[SBHiddenWindowsPillPresentAnimationSwitcherModifier hiddenWindowsPills];
-[SBHiddenWindowsPillPresentAnimationSwitcherModifier wantsDockWindowLevelAssertion];
-[SBHiddenWindowsPillPresentAnimationSwitcherModifier handleTransitionEvent:];
-[SBHiddenWindowsPillPresentAnimationSwitcherModifier anchorPointForHiddenWindowsPill:];
-[SBHiddenWindowsPillPresentAnimationSwitcherModifier handleTimerEvent:];
-[SBHiddenWindowsPillPresentAnimationSwitcherModifier switcherHitTestsAsOpaque];
-[SBHiddenWindowsPillPresentAnimationSwitcherModifier pillScaleForHiddenWindowsPill:];
-[SBHiddenWindowsPillPresentAnimationSwitcherModifier iconFrame];
-[SBHiddenWindowsPillPresentAnimationSwitcherModifier centerForHiddenWindowsPill:];
-[SBHiddenWindowsPillPresentAnimationSwitcherModifier bounceIconCenterForHiddenWindowsPill:];
-[SBHiddenWindowsPillPresentAnimationSwitcherModifier shouldBounceIconPresentForHiddenWindowsPill:];
-[SBHiddenWindowsPillPresentAnimationSwitcherModifier hiddenWindowsPillModeForHiddenWindowsPill:];
-[SBHiddenWindowsPillPresentAnimationSwitcherModifier alphaForHiddenWindowsPill:];
-[SBHiddenWindowsPillPresentAnimationSwitcherModifier transformForHiddenWindowsPill:];
-[SBHiddenWindowsPillPresentAnimationSwitcherModifier hiddenWindowsPill];
-[SBHiddenWindowsPillPresentAnimationSwitcherModifier initWithHiddenWindowsPill:];
```
