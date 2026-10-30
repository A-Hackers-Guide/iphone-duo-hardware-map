# `SBHiddenWindowsPillRootSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifier`
- 9 instance variables, 2 properties, 21 instance methods, 0 class methods

## Instance variables

```
B _isPresented;
B _isPendingDismissal;
B _pillTapped;
B _isRotating;
@"SBAppLayout" _iconAppLayout;
@"SBAppLayout" _toAppLayout;
@"SBUnlockedEnvironmentState" _toUnlockedEnvironmentState;
B _alwaysMaterializes;
@"SBSwitcherHiddenWindowsPill" _hiddenWindowsPill;
```

## Properties

```
@property (T@"SBSwitcherHiddenWindowsPill",R,N,V_hiddenWindowsPill) hiddenWindowsPill;
@property (TB,R,N,V_alwaysMaterializes) alwaysMaterializes;
```

## Instance methods

```
-[SBHiddenWindowsPillRootSwitcherModifier handleGestureEvent:];
-[SBHiddenWindowsPillRootSwitcherModifier topMostLayoutElements];
-[SBHiddenWindowsPillRootSwitcherModifier hiddenWindowsPills];
-[SBHiddenWindowsPillRootSwitcherModifier handleTransitionEvent:];
-[SBHiddenWindowsPillRootSwitcherModifier wantsKeyboardInputEvents];
-[SBHiddenWindowsPillRootSwitcherModifier alphaForHiddenWindowsPill:];
-[SBHiddenWindowsPillRootSwitcherModifier _dismissalTransitionRequest];
-[SBHiddenWindowsPillRootSwitcherModifier _shouldDematerialize];
-[SBHiddenWindowsPillRootSwitcherModifier _shouldDismissForSwipeTranslation:velocity:];
-[SBHiddenWindowsPillRootSwitcherModifier _shouldMaterialize];
-[SBHiddenWindowsPillRootSwitcherModifier _shouldUseButterflyAnimation];
-[SBHiddenWindowsPillRootSwitcherModifier _willDockBeVisibleAtEndOfTransition];
-[SBHiddenWindowsPillRootSwitcherModifier alwaysMaterializes];
-[SBHiddenWindowsPillRootSwitcherModifier handleKeyboardInputEvent:];
-[SBHiddenWindowsPillRootSwitcherModifier handleSwipeHiddenWindowsPill:];
-[SBHiddenWindowsPillRootSwitcherModifier handleTapHiddenWindowsPill:];
-[SBHiddenWindowsPillRootSwitcherModifier handleTransientUIIndirectPannedToDismissSwitcherModifierEvent:];
-[SBHiddenWindowsPillRootSwitcherModifier handleTransientUITapToDismissSwitcherModifierEvent:];
-[SBHiddenWindowsPillRootSwitcherModifier hiddenWindowsPill];
-[SBHiddenWindowsPillRootSwitcherModifier initWithHiddenWindowsPill:alwaysMaterializes:];
-[SBHiddenWindowsPillRootSwitcherModifier removeChildModifier:];
```
