# `_UIBorrowedViewHandle`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 7 instance methods, 0 class methods

## Instance variables

```
B _valid;
@"UIView" _view;
@"_UILendableViewContainer" _lender;
```

## Properties

```
@property (TB,N,GisValid,V_valid) valid;
@property (T@"_UILendableViewContainer",W,N,V_lender) lender;
@property (T@"UIView",R,N,V_view) view;
```

## Instance methods

```
-[_UIBorrowedViewHandle setValid:];
-[_UIBorrowedViewHandle view];
-[_UIBorrowedViewHandle isValid];
-[_UIBorrowedViewHandle _initWithView:lender:];
-[_UIBorrowedViewHandle lender];
-[_UIBorrowedViewHandle returnView];
-[_UIBorrowedViewHandle setLender:];
```
