# `UICalendarViewDecoration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UICalendarViewDecorationProviding`
- 1 instance variables, 2 properties, 10 instance methods, 5 class methods

## Instance variables

```
@"_UICalendarViewDecorationItem" _decoration;
```

## Properties

```
@property (T@"UIView",&,N,S_setDecorationView:) _decorationView;
@property (T@"UIView",W,N,S_setParent:) _parent;
```

## Class methods

```
+[UICalendarViewDecoration decorationWithImage:color:size:];
+[UICalendarViewDecoration _referenceHeightForTraitCollection:];
+[UICalendarViewDecoration decorationWithColor:size:];
+[UICalendarViewDecoration decorationWithCustomViewProvider:];
+[UICalendarViewDecoration decorationWithImage:];
```

## Instance methods

```
-[UICalendarViewDecoration _parent];
-[UICalendarViewDecoration init];
-[UICalendarViewDecoration _setParent:];
-[UICalendarViewDecoration _decorationView];
-[UICalendarViewDecoration _decorationViewForReuseView:];
-[UICalendarViewDecoration _decorationViewReusableKey];
-[UICalendarViewDecoration _setDecorationView:];
-[UICalendarViewDecoration initWithCustomViewProvider:];
-[UICalendarViewDecoration initWithDecorationItem:];
-[UICalendarViewDecoration initWithImage:color:size:];
```
