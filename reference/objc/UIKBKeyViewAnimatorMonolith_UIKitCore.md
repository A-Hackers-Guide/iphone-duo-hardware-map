# `UIKBKeyViewAnimatorMonolith`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKBKeyViewAnimator`
- Protocols: `_UIFloatingContentViewDelegate`
- 2 instance variables, 4 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _selectedKeyTimestamps;
@"NSMutableDictionary" _transitionCompletions;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIKBKeyViewAnimatorMonolith animateFloatingKeyView:toControlState:];
-[UIKBKeyViewAnimatorMonolith keyViewClassForKey:renderTraits:screenTraits:];
-[UIKBKeyViewAnimatorMonolith init];
-[UIKBKeyViewAnimatorMonolith addTransitionCompletion:forKeyName:];
-[UIKBKeyViewAnimatorMonolith reset];
-[UIKBKeyViewAnimatorMonolith shouldAssertCurrentKeyState:];
-[UIKBKeyViewAnimatorMonolith controlStateForKeyState:];
-[UIKBKeyViewAnimatorMonolith shouldTransitionKeyView:fromState:toState:];
-[UIKBKeyViewAnimatorMonolith transitionFloatingKeyView:toState:completion:];
-[UIKBKeyViewAnimatorMonolith floatingContentView:isTransitioningFromState:toState:];
-[UIKBKeyViewAnimatorMonolith _transitionFromState:toState:];
-[UIKBKeyViewAnimatorMonolith shouldPurgeKeyViews];
-[UIKBKeyViewAnimatorMonolith transitionKeyView:fromState:toState:completion:];
-[UIKBKeyViewAnimatorMonolith transitionOutKeyView:fromState:toState:completion:];
-[UIKBKeyViewAnimatorMonolith floatingContentView:didFinishTransitioningToState:];
```
