# `SBHiddenWindowsPillDismissAnimationSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifier`
- 11 instance variables, 1 properties, 18 instance methods, 0 class methods

## Instance variables

```
Q _pillAnimationPhase;
Q _iconBounceAnimationPhase;
Q _iconScaleAnimationPhase;
Q _pillGenerationCount;
Q _iconBounceGenerationCount;
Q _iconScaleGenerationCount;
@"SBAppLayout" _iconAppLayout;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _iconFrame;
Q _horizontalRange;
B _isFloatingDockFullyPresentedInitially;
@"SBSwitcherHiddenWindowsPill" _hiddenWindowsPill;
```

## Properties

```
@property (T@"SBSwitcherHiddenWindowsPill",R,N,V_hiddenWindowsPill) hiddenWindowsPill;
```

## Instance methods

```
-[SBHiddenWindowsPillDismissAnimationSwitcherModifier dockWindowLevelPriority];
-[SBHiddenWindowsPillDismissAnimationSwitcherModifier dockWindowLevel];
-[SBHiddenWindowsPillDismissAnimationSwitcherModifier bounceIconScaleForHiddenWindowsPill:];
-[SBHiddenWindowsPillDismissAnimationSwitcherModifier animationAttributesForLayoutElement:];
-[SBHiddenWindowsPillDismissAnimationSwitcherModifier wantsDockWindowLevelAssertion];
-[SBHiddenWindowsPillDismissAnimationSwitcherModifier handleTransitionEvent:];
-[SBHiddenWindowsPillDismissAnimationSwitcherModifier anchorPointForHiddenWindowsPill:];
-[SBHiddenWindowsPillDismissAnimationSwitcherModifier pillOffsetForHiddenWindowsPill:];
-[SBHiddenWindowsPillDismissAnimationSwitcherModifier handleTimerEvent:];
-[SBHiddenWindowsPillDismissAnimationSwitcherModifier switcherHitTestsAsOpaque];
-[SBHiddenWindowsPillDismissAnimationSwitcherModifier pillScaleForHiddenWindowsPill:];
-[SBHiddenWindowsPillDismissAnimationSwitcherModifier centerForHiddenWindowsPill:];
-[SBHiddenWindowsPillDismissAnimationSwitcherModifier bounceIconCenterForHiddenWindowsPill:];
-[SBHiddenWindowsPillDismissAnimationSwitcherModifier shouldBounceIconPresentForHiddenWindowsPill:];
-[SBHiddenWindowsPillDismissAnimationSwitcherModifier hiddenWindowsPillModeForHiddenWindowsPill:];
-[SBHiddenWindowsPillDismissAnimationSwitcherModifier transformForHiddenWindowsPill:];
-[SBHiddenWindowsPillDismissAnimationSwitcherModifier hiddenWindowsPill];
-[SBHiddenWindowsPillDismissAnimationSwitcherModifier initWithHiddenWindowsPill:];
```
