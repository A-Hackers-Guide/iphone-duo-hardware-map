# `_UILendableViewContainer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
B _loaned;
@"UIView" _view;
@"<_UILendableViewContainerDelegate>" _delegate;
```

## Properties

```
@property (TB,R,N,GisLoaned,V_loaned) loaned;
@property (T@"UIView",R,N,V_view) view;
@property (T@"UIView",R,N) ownedView;
@property (T@"<_UILendableViewContainerDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[_UILendableViewContainer isLoaned];
-[_UILendableViewContainer initWithView:];
-[_UILendableViewContainer lend];
-[_UILendableViewContainer ownedView];
-[_UILendableViewContainer view];
-[_UILendableViewContainer setDelegate:];
-[_UILendableViewContainer delegate];
-[_UILendableViewContainer _returnView:];
-[_UILendableViewContainer description];
```
