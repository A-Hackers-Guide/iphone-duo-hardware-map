# `_UIEditMenuHandoffContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"UIEditMenuConfiguration" _configuration;
@"UIMenu" _preparedMenu;
q _arrowDirection;
@"UIView" _sourceView;
```

## Properties

```
@property (T@"UIEditMenuConfiguration",R,N,V_configuration) configuration;
@property (T@"UIMenu",R,N,V_preparedMenu) preparedMenu;
@property (Tq,R,N,V_arrowDirection) arrowDirection;
@property (T@"UIView",R,N,V_sourceView) sourceView;
```

## Class methods

```
+[_UIEditMenuHandoffContext contextForConfiguration:preparedMenu:sourceView:arrowDirection:];
```

## Instance methods

```
-[_UIEditMenuHandoffContext configuration];
-[_UIEditMenuHandoffContext arrowDirection];
-[_UIEditMenuHandoffContext sourceView];
-[_UIEditMenuHandoffContext preparedMenu];
```
