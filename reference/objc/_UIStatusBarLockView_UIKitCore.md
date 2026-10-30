# `_UIStatusBarLockView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `CAAnimationDelegate`, `_UIStatusBarDisplayable`
- 3 instance variables, 12 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"_UIStatusBarImageView" _bodyView;
@"_UIStatusBarImageView" _shackleView;
@? _completionBlock;
```

## Properties

```
@property (T@"_UIStatusBarImageView",&,N,V_bodyView) bodyView;
@property (T@"_UIStatusBarImageView",&,N,V_shackleView) shackleView;
@property (T@?,C,N,V_completionBlock) completionBlock;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,?,R,N) wantsCrossfade;
@property (TB,?,R,N) prefersBaselineAlignment;
@property (TB,?,R,N) prefersCenterVerticalAlignment;
@property (Tq,?,R,N) overriddenVerticalAlignment;
@property (T@"UIAccessibilityHUDItem",?,R,N) accessibilityHUDRepresentation;
```

## Instance methods

```
-[_UIStatusBarLockView prefersBaselineAlignment];
-[_UIStatusBarLockView applyStyleAttributes:];
-[_UIStatusBarLockView intrinsicContentSize];
-[_UIStatusBarLockView setCompletionBlock:];
-[_UIStatusBarLockView completionBlock];
-[_UIStatusBarLockView animationDidStop:finished:];
-[_UIStatusBarLockView bodyView];
-[_UIStatusBarLockView initWithFrame:];
-[_UIStatusBarLockView setBodyView:];
-[_UIStatusBarLockView setShackleView:];
-[_UIStatusBarLockView animateUnlockWithCompletionBlock:];
-[_UIStatusBarLockView jiggleWithCompletionBlock:];
-[_UIStatusBarLockView resetLock];
-[_UIStatusBarLockView shackleView];
```
