# `_UIDebuggingOverlayDetail`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 5 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSString" _title;
@"NSString" _detail;
q _accessoryType;
```

## Properties

```
@property (T@"NSString",&,N,V_title) title;
@property (T@"NSString",&,N,V_detail) detail;
@property (Tq,N,V_accessoryType) accessoryType;
@property (T@"UIView",R,N) view;
@property (T@"UIViewController",R,N) viewController;
```

## Class methods

```
+[_UIDebuggingOverlayDetail detailWithTitle:detail:];
```

## Instance methods

```
-[_UIDebuggingOverlayDetail detail];
-[_UIDebuggingOverlayDetail viewController];
-[_UIDebuggingOverlayDetail view];
-[_UIDebuggingOverlayDetail title];
-[_UIDebuggingOverlayDetail setTitle:];
-[_UIDebuggingOverlayDetail setDetail:];
-[_UIDebuggingOverlayDetail _updateForInspectedView:];
-[_UIDebuggingOverlayDetail accessoryType];
-[_UIDebuggingOverlayDetail setAccessoryType:];
```
