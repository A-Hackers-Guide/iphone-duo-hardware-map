# `_UIViewControllerTransition`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 4 instance variables, 4 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"_UIViewControllerTransitionOptions" _options;
@"UIViewController" __associatedViewController;
@? __viewProvider;
@? __interactiveDismissShouldBeginHandler;
```

## Properties

```
@property (T@"UIViewController",W,N,V__associatedViewController) _associatedViewController;
@property (T@?,C,N,V__viewProvider) _viewProvider;
@property (T@"_UIViewControllerTransitionOptions",&,N,S_setOptions:,V_options) _options;
@property (T@?,C,N,V__interactiveDismissShouldBeginHandler) _interactiveDismissShouldBeginHandler;
```

## Class methods

```
+[_UIViewControllerTransition zoomWithSourceViewProvider:];
```

## Instance methods

```
-[_UIViewControllerTransition _options];
-[_UIViewControllerTransition _setOptions:];
-[_UIViewControllerTransition _viewProvider];
-[_UIViewControllerTransition _associatedViewController];
-[_UIViewControllerTransition set_viewProvider:];
-[_UIViewControllerTransition set_associatedViewController:];
-[_UIViewControllerTransition copyWithZone:];
-[_UIViewControllerTransition _apiTransition];
-[_UIViewControllerTransition _interactiveDismissShouldBeginHandler];
-[_UIViewControllerTransition set_interactiveDismissShouldBeginHandler:];
```
