# `_UIViewControllerKeyboardAnimationStyle`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIInputViewAnimationStyleDirectional`
- 5 instance variables, 5 properties, 20 instance methods, 1 class methods

## Instance variables

```
B _disableAlongsideView;
B _allowCustomTransition;
@"_UIViewControllerTransitionContext" _context;
@"_UIViewControllerKeyboardAnimationStyleInfo" _info;
q _keyboardAnimationType;
```

## Properties

```
@property (T@"_UIViewControllerKeyboardAnimationStyleInfo",R,N,V_info) info;
@property (TB,N,V_allowCustomTransition) allowCustomTransition;
@property (Tq,N,V_keyboardAnimationType) keyboardAnimationType;
@property (T@"_UIViewControllerTransitionContext",&,N,V_context) context;
@property (TB,N,V_disableAlongsideView) disableAlongsideView;
```

## Class methods

```
+[_UIViewControllerKeyboardAnimationStyle animationStyleWithContext:useCustomTransition:];
```

## Instance methods

```
-[_UIViewControllerKeyboardAnimationStyle initWithContext:];
-[_UIViewControllerKeyboardAnimationStyle setDisableAlongsideView:];
-[_UIViewControllerKeyboardAnimationStyle info];
-[_UIViewControllerKeyboardAnimationStyle canTakeSnapshot];
-[_UIViewControllerKeyboardAnimationStyle canDismissWithScrollView];
-[_UIViewControllerKeyboardAnimationStyle animationType];
-[_UIViewControllerKeyboardAnimationStyle launchAnimation:afterStarted:completion:forHost:fromCurrentPosition:];
-[_UIViewControllerKeyboardAnimationStyle controllerForStartPlacement:endPlacement:];
-[_UIViewControllerKeyboardAnimationStyle setAnimationType:];
-[_UIViewControllerKeyboardAnimationStyle setKeyboardAnimationType:];
-[_UIViewControllerKeyboardAnimationStyle _launchAnimation:afterStarted:completion:forHost:fromCurrentPosition:];
-[_UIViewControllerKeyboardAnimationStyle disableAlongsideView];
-[_UIViewControllerKeyboardAnimationStyle setContext:];
-[_UIViewControllerKeyboardAnimationStyle setAllowCustomTransition:];
-[_UIViewControllerKeyboardAnimationStyle isAnimationCompleted];
-[_UIViewControllerKeyboardAnimationStyle keyboardAnimationType];
-[_UIViewControllerKeyboardAnimationStyle copyWithZone:];
-[_UIViewControllerKeyboardAnimationStyle context];
-[_UIViewControllerKeyboardAnimationStyle isEqual:];
-[_UIViewControllerKeyboardAnimationStyle allowCustomTransition];
```
