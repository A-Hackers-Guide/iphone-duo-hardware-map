# `_UIStatusBarLockItemPadlockView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `CAAnimationDelegate`
- 4 instance variables, 8 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"UIImageView" _bodyView;
@"UIImageView" _shackleView;
@? _completionBlock;
@"UIStatusBarLockItemView" _owner;
```

## Properties

```
@property (T@"UIImageView",&,N,V_bodyView) bodyView;
@property (T@"UIImageView",&,N,V_shackleView) shackleView;
@property (T@?,C,N,V_completionBlock) completionBlock;
@property (T@"UIStatusBarLockItemView",W,N,V_owner) owner;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIStatusBarLockItemPadlockView owner];
-[_UIStatusBarLockItemPadlockView setCompletionBlock:];
-[_UIStatusBarLockItemPadlockView completionBlock];
-[_UIStatusBarLockItemPadlockView animationDidStop:finished:];
-[_UIStatusBarLockItemPadlockView reset];
-[_UIStatusBarLockItemPadlockView setOwner:];
-[_UIStatusBarLockItemPadlockView bodyView];
-[_UIStatusBarLockItemPadlockView sizeThatFits:];
-[_UIStatusBarLockItemPadlockView setBodyView:];
-[_UIStatusBarLockItemPadlockView setShackleView:];
-[_UIStatusBarLockItemPadlockView animateUnlockCompletionBlock:];
-[_UIStatusBarLockItemPadlockView initWithFrame:owner:];
-[_UIStatusBarLockItemPadlockView jiggleCompletionBlock:];
-[_UIStatusBarLockItemPadlockView shackleView];
```
