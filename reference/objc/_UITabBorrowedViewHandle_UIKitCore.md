# `_UITabBorrowedViewHandle`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 8 properties, 17 instance methods, 0 class methods

## Instance variables

```
B _usesDefaultBarGlass;
B _allowsIntermediateSizes;
B _hidesBackground;
@"UIBarButtonItem" _barButtonItem;
@"UIView" _overrideView;
@"_UIBorrowedViewHandle" _handle;
```

## Properties

```
@property (T@"UIView",&,N,V_overrideView) overrideView;
@property (T@"_UIBorrowedViewHandle",&,N,V_handle) handle;
@property (TB,N,V_usesDefaultBarGlass) usesDefaultBarGlass;
@property (TB,N,V_allowsIntermediateSizes) allowsIntermediateSizes;
@property (TB,N,V_hidesBackground) hidesBackground;
@property (T@"UIView",R,N) hostedView;
@property (T@"UIView",R,N) borrowedView;
@property (T@"UIBarButtonItem",W,N,V_barButtonItem) barButtonItem;
```

## Instance methods

```
-[_UITabBorrowedViewHandle setHidesBackground:];
-[_UITabBorrowedViewHandle barButtonItem];
-[_UITabBorrowedViewHandle hostedView];
-[_UITabBorrowedViewHandle handle];
-[_UITabBorrowedViewHandle setHandle:];
-[_UITabBorrowedViewHandle hidesBackground];
-[_UITabBorrowedViewHandle isEqual:];
-[_UITabBorrowedViewHandle allowsIntermediateSizes];
-[_UITabBorrowedViewHandle borrowedView];
-[_UITabBorrowedViewHandle initWithHandle:overrideView:];
-[_UITabBorrowedViewHandle overrideView];
-[_UITabBorrowedViewHandle returnView];
-[_UITabBorrowedViewHandle setAllowsIntermediateSizes:];
-[_UITabBorrowedViewHandle setBarButtonItem:];
-[_UITabBorrowedViewHandle setOverrideView:];
-[_UITabBorrowedViewHandle setUsesDefaultBarGlass:];
-[_UITabBorrowedViewHandle usesDefaultBarGlass];
```
