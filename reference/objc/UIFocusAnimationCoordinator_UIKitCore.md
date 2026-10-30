# `UIFocusAnimationCoordinator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 18 properties, 35 instance methods, 3 class methods

## Instance variables

```
B _locked;
@"_UIFocusAnimationConfiguration" _focusingConfiguration;
@"_UIFocusAnimationConfiguration" _unfocusingConfiguration;
@"NSMutableArray" _focusingAnimations;
@"NSMutableArray" _legacyFocusingAnimations;
@"NSMutableArray" _unfocusingAnimations;
@"NSMutableArray" _legacyUnfocusingAnimations;
@"NSMutableArray" _focusingCompletions;
@"NSMutableArray" _unfocusingCompletions;
@"UIFocusUpdateContext" _focusUpdateContext;
q _activeFocusAnimation;
```

## Properties

```
@property (T@"_UIFocusAnimationConfiguration",&,N,V_focusingConfiguration) focusingConfiguration;
@property (T@"_UIFocusAnimationConfiguration",&,N,V_unfocusingConfiguration) unfocusingConfiguration;
@property (T@"NSMutableArray",R,N,V_focusingAnimations) focusingAnimations;
@property (T@"NSMutableArray",R,N,V_legacyFocusingAnimations) legacyFocusingAnimations;
@property (T@"NSMutableArray",R,N,V_unfocusingAnimations) unfocusingAnimations;
@property (T@"NSMutableArray",R,N,V_legacyUnfocusingAnimations) legacyUnfocusingAnimations;
@property (T@"NSMutableArray",R,N,V_focusingCompletions) focusingCompletions;
@property (T@"NSMutableArray",R,N,V_unfocusingCompletions) unfocusingCompletions;
@property (T@"UIFocusUpdateContext",R,N,G_focusUpdateContext,V_focusUpdateContext) focusUpdateContext;
@property (T@"_UIFocusAnimationConfiguration",R,C,N,G_activeConfiguration) activeConfiguration;
@property (TB,R,N,G_isLocked,V_locked) locked;
@property (Td,R,N,G_unfocusingRepositionAnimationDuration) unfocusingRepositionAnimationDuration;
@property (Tq,R,N,V_activeFocusAnimation) activeFocusAnimation;
@property (TQ,R,N,G_animationOptions) animationOptions;
@property (Td,R,N,G_animationDelay) animationDelay;
@property (Td,R,N,G_activeAnimationDuration) activeAnimationDuration;
@property (Td,R,N,G_focusingAnimationDuration) focusingAnimationDuration;
@property (Td,R,N,G_unfocusingAnimationDuration) unfocusingAnimationDuration;
```

## Class methods

```
+[UIFocusAnimationCoordinator _focusAnimationCoordinatorForAnimationType:withConfiguration:inContext:];
+[UIFocusAnimationCoordinator _focusingAnimationCoordinatorWithConfiguration:inContext:];
+[UIFocusAnimationCoordinator _unfocusingAnimationCoordinatorWithConfiguration:inContext:];
```

## Instance methods

```
-[UIFocusAnimationCoordinator _setConfiguration:forFocusAnimation:];
-[UIFocusAnimationCoordinator _animationDelay];
-[UIFocusAnimationCoordinator _unfocusingAnimationDuration];
-[UIFocusAnimationCoordinator _consumeBlocks:withAnimationContext:];
-[UIFocusAnimationCoordinator _activeAnimationDuration];
-[UIFocusAnimationCoordinator init];
-[UIFocusAnimationCoordinator addCoordinatedAnimations:completion:];
-[UIFocusAnimationCoordinator _configurationForFocusAnimation:];
-[UIFocusAnimationCoordinator _isLocked];
-[UIFocusAnimationCoordinator addCoordinatedAnimationsForAnimation:animations:completion:];
-[UIFocusAnimationCoordinator unfocusingConfiguration];
-[UIFocusAnimationCoordinator activeFocusAnimation];
-[UIFocusAnimationCoordinator focusingAnimations];
-[UIFocusAnimationCoordinator _consumeBlocks:];
-[UIFocusAnimationCoordinator _focusingAnimationDuration];
-[UIFocusAnimationCoordinator focusingConfiguration];
-[UIFocusAnimationCoordinator _cancelFocusAnimation:];
-[UIFocusAnimationCoordinator _animationOptions];
-[UIFocusAnimationCoordinator setFocusingConfiguration:];
-[UIFocusAnimationCoordinator _initWithFocusUpdateContext:];
-[UIFocusAnimationCoordinator legacyUnfocusingAnimations];
-[UIFocusAnimationCoordinator unfocusingCompletions];
-[UIFocusAnimationCoordinator _unfocusingRepositionAnimationDuration];
-[UIFocusAnimationCoordinator setUnfocusingConfiguration:];
-[UIFocusAnimationCoordinator _focusUpdateContext];
-[UIFocusAnimationCoordinator _animateFocusAnimation:];
-[UIFocusAnimationCoordinator focusingCompletions];
-[UIFocusAnimationCoordinator addCoordinatedUnfocusingAnimations:completion:];
-[UIFocusAnimationCoordinator addCoordinatedFocusingAnimations:completion:];
-[UIFocusAnimationCoordinator unfocusingAnimations];
-[UIFocusAnimationCoordinator _activeConfiguration];
-[UIFocusAnimationCoordinator _animate];
-[UIFocusAnimationCoordinator _configureWithFocusUpdateContext:];
-[UIFocusAnimationCoordinator legacyFocusingAnimations];
-[UIFocusAnimationCoordinator _prepareForFocusAnimation:];
```
