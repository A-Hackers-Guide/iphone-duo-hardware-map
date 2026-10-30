# `_UINavigationBarGestureHandler`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegatePrivate`
- 4 instance variables, 7 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"UISwipeGestureRecognizer" _popSwipeGestureRecognizer;
@"UINavigationBar" _navigationBar;
@"<_UINavigationBarGestureHandlerDelegate>" _delegate;
q _idiom;
```

## Properties

```
@property (T@"UINavigationBar",R,W,N,V_navigationBar) navigationBar;
@property (T@"<_UINavigationBarGestureHandlerDelegate>",W,N,V_delegate) delegate;
@property (Tq,N,V_idiom) idiom;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UINavigationBarGestureHandler navigationBar];
-[_UINavigationBarGestureHandler setIdiom:];
-[_UINavigationBarGestureHandler setDelegate:];
-[_UINavigationBarGestureHandler delegate];
-[_UINavigationBarGestureHandler _gestureRecognizerShouldBegin:];
-[_UINavigationBarGestureHandler initWithNavigationBar:];
-[_UINavigationBarGestureHandler idiom];
-[_UINavigationBarGestureHandler _handlePopSwipe:];
```
