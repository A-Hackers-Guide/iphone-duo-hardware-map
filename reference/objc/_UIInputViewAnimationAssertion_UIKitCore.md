# `_UIInputViewAnimationAssertion`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 10 instance methods, 1 class methods

## Instance variables

```
B _valid;
B _animated;
i _direction;
@"UIKeyboardSceneDelegate" _sceneDelegate;
@"UIInputViewAnimationStyle" _style;
```

## Properties

```
@property (TB,N,V_valid) valid;
@property (TB,N,V_animated) animated;
@property (T@"UIKeyboardSceneDelegate",W,N,V_sceneDelegate) sceneDelegate;
@property (T@"UIInputViewAnimationStyle",&,N,V_style) style;
@property (Ti,R,N,V_direction) direction;
```

## Class methods

```
+[_UIInputViewAnimationAssertion _assertionWithDirection:animated:sceneDelegate:];
```

## Instance methods

```
-[_UIInputViewAnimationAssertion valid];
-[_UIInputViewAnimationAssertion animated];
-[_UIInputViewAnimationAssertion setValid:];
-[_UIInputViewAnimationAssertion style];
-[_UIInputViewAnimationAssertion setAnimated:];
-[_UIInputViewAnimationAssertion setStyle:];
-[_UIInputViewAnimationAssertion direction];
-[_UIInputViewAnimationAssertion invalidate];
-[_UIInputViewAnimationAssertion setSceneDelegate:];
-[_UIInputViewAnimationAssertion sceneDelegate];
```
