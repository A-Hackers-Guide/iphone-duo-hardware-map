# `SBHiddenWindowsPillMaterializeAnimationSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifier`
- 4 instance variables, 2 properties, 10 instance methods, 0 class methods

## Instance variables

```
Q _animationPhase;
Q _generationCount;
@"SBSwitcherHiddenWindowsPill" _hiddenWindowsPill;
Q _direction;
```

## Properties

```
@property (T@"SBSwitcherHiddenWindowsPill",R,N,V_hiddenWindowsPill) hiddenWindowsPill;
@property (TQ,R,N,V_direction) direction;
```

## Instance methods

```
-[SBHiddenWindowsPillMaterializeAnimationSwitcherModifier animationAttributesForLayoutElement:];
-[SBHiddenWindowsPillMaterializeAnimationSwitcherModifier contentAlphaForHiddenWindowsPill:];
-[SBHiddenWindowsPillMaterializeAnimationSwitcherModifier backgroundForHiddenWindowsPill:];
-[SBHiddenWindowsPillMaterializeAnimationSwitcherModifier handleTransitionEvent:];
-[SBHiddenWindowsPillMaterializeAnimationSwitcherModifier handleTimerEvent:];
-[SBHiddenWindowsPillMaterializeAnimationSwitcherModifier contentScaleForHiddenWindowsPill:];
-[SBHiddenWindowsPillMaterializeAnimationSwitcherModifier contentBlurRadiusForHiddenWindowsPill:];
-[SBHiddenWindowsPillMaterializeAnimationSwitcherModifier direction];
-[SBHiddenWindowsPillMaterializeAnimationSwitcherModifier hiddenWindowsPill];
-[SBHiddenWindowsPillMaterializeAnimationSwitcherModifier initWithHiddenWindowsPill:direction:];
```
