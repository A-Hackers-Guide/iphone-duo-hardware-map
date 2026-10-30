# `_UIKeyboardAnimatorAnimationStyle`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIInputViewAnimationStyle`
- 4 instance variables, 1 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"_UIKeyboardAnimator" _animator;
@"<UIInputViewAnimationHost>" _currentHost;
B _currentFromPosition;
q _keyboardAnimationType;
```

## Properties

```
@property (Tq,N,V_keyboardAnimationType) keyboardAnimationType;
```

## Class methods

```
+[_UIKeyboardAnimatorAnimationStyle animationStyleWithAnimator:];
```

## Instance methods

```
-[_UIKeyboardAnimatorAnimationStyle animationType];
-[_UIKeyboardAnimatorAnimationStyle launchAnimation:afterStarted:completion:forHost:fromCurrentPosition:];
-[_UIKeyboardAnimatorAnimationStyle controllerForStartPlacement:endPlacement:];
-[_UIKeyboardAnimatorAnimationStyle setAnimationType:];
-[_UIKeyboardAnimatorAnimationStyle setKeyboardAnimationType:];
-[_UIKeyboardAnimatorAnimationStyle keyboardAnimationType];
-[_UIKeyboardAnimatorAnimationStyle defaultLaunchAnimation:afterStarted:completion:];
```
