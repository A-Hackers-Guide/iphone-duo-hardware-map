# `UIViewAnimationBlockDelegate`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 3 properties, 10 instance methods, 2 class methods

## Instance variables

```
B _didBeginBlockAnimation;
B _allowUserInteraction;
B _isZeroDuration;
B _allowsUserInteractionToCutOffEndOfAnimation;
B _allowsHitTesting;
B _animationDidStopSent;
@? _start;
@? _completion;
@"NSMutableArray" _systemPostAnimationActions;
B __forcingImmediateCompletion;
@"UIViewAnimationState" _animationState;
```

## Properties

```
@property (TB,R,N,V_allowUserInteraction) _allowsUserInteraction;
@property (TB,N,S_setForcingImmediateCompletion:,V__forcingImmediateCompletion) _forcingImmediateCompletion;
@property (T@"UIViewAnimationState",W,N,V_animationState) _animationState;
```

## Class methods

```
+[UIViewAnimationBlockDelegate setAnimationBlockDelegateWithDuration:options:start:completion:];
+[UIViewAnimationBlockDelegate animationBlockDelegateWithDuration:options:start:completion:];
```

## Instance methods

```
-[UIViewAnimationBlockDelegate _animationState];
-[UIViewAnimationBlockDelegate _didEndBlockAnimation:finished:context:];
-[UIViewAnimationBlockDelegate _forcingImmediateCompletion];
-[UIViewAnimationBlockDelegate _allowsUserInteractionToCutOffEndOfAnimation];
-[UIViewAnimationBlockDelegate _allowsUserInteraction];
-[UIViewAnimationBlockDelegate _setForcingImmediateCompletion:];
-[UIViewAnimationBlockDelegate _sendDeferredCompletion:];
-[UIViewAnimationBlockDelegate _allowsHitTesting];
-[UIViewAnimationBlockDelegate _willBeginBlockAnimation:context:];
-[UIViewAnimationBlockDelegate set_animationState:];
```
