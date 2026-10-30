# `UIKeyboardKeyplaneTransition`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 8 properties, 25 instance methods, 0 class methods

## Instance variables

```
d _currentProgress;
d _liftOffProgress;
d _finishProgress;
d _finishDuration;
d _finalTransitionStartTime;
@"CADisplayLink" _displayLink;
@"UIKBTree" _keyboard;
@"UIKBTree" _start;
@"UIKBTree" _end;
@"UIView" _startView;
@"UIView" _endView;
@? _completionBlock;
@"<UIKeyboardKeyplaneTransitionDelegate>" _transitionDelegate;
B _initiallyAtEnd;
@"NSMutableArray" _transitionViews;
@"UIKBKeyViewAnimator" _keyViewAnimator;
```

## Properties

```
@property (T@"UIKBTree",&,N,V_keyboard) keyboard;
@property (T@?,C,V_completionBlock) completionBlock;
@property (T@"<UIKeyboardKeyplaneTransitionDelegate>",W,N,V_transitionDelegate) transitionDelegate;
@property (TB,N,V_initiallyAtEnd) initiallyAtEnd;
@property (Td,R,N) nonInteractiveDuration;
@property (T@"UIKBKeyViewAnimator",&,N,V_keyViewAnimator) keyViewAnimator;
@property (Td,R,N) startHeight;
@property (Td,R,N) endHeight;
```

## Instance methods

```
-[UIKeyboardKeyplaneTransition updateWithProgress:];
-[UIKeyboardKeyplaneTransition keyboard];
-[UIKeyboardKeyplaneTransition setCompletionBlock:];
-[UIKeyboardKeyplaneTransition completionBlock];
-[UIKeyboardKeyplaneTransition keyViewAnimator];
-[UIKeyboardKeyplaneTransition dealloc];
-[UIKeyboardKeyplaneTransition removeAllAnimations];
-[UIKeyboardKeyplaneTransition setKeyViewAnimator:];
-[UIKeyboardKeyplaneTransition addTransitionView:startFrame:endFrame:];
-[UIKeyboardKeyplaneTransition canDisplayTransitionFromKeyplane:toKeyplane:];
-[UIKeyboardKeyplaneTransition cancelNonInteractiveAnimation];
-[UIKeyboardKeyplaneTransition commitTransitionRebuild];
-[UIKeyboardKeyplaneTransition endHeight];
-[UIKeyboardKeyplaneTransition finalizeTransition];
-[UIKeyboardKeyplaneTransition finishWithProgress:completionBlock:];
-[UIKeyboardKeyplaneTransition initiallyAtEnd];
-[UIKeyboardKeyplaneTransition nonInteractiveDuration];
-[UIKeyboardKeyplaneTransition rebuildWithStartKeyplane:startView:endKeyplane:endView:];
-[UIKeyboardKeyplaneTransition runNonInteractivelyWithCompletion:];
-[UIKeyboardKeyplaneTransition setInitiallyAtEnd:];
-[UIKeyboardKeyplaneTransition setKeyboard:];
-[UIKeyboardKeyplaneTransition setTransitionDelegate:];
-[UIKeyboardKeyplaneTransition startHeight];
-[UIKeyboardKeyplaneTransition transitionDelegate];
-[UIKeyboardKeyplaneTransition transitionToFinalState:];
```
