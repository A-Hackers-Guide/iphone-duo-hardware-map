# `UICellAccessoryPopUpMenu`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UICellAccessory`
- 2 instance variables, 3 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"UIMenu" _menu;
@? _selectedElementDidChangeHandler;
```

## Properties

```
@property (T@"UIMenu",R,N) _internalMenu;
@property (T@"UIMenu",R,C,N,V_menu) menu;
@property (T@?,C,N,V_selectedElementDidChangeHandler) selectedElementDidChangeHandler;
```

## Class methods

```
+[UICellAccessoryPopUpMenu supportsSecureCoding];
```

## Instance methods

```
-[UICellAccessoryPopUpMenu menu];
-[UICellAccessoryPopUpMenu _systemType];
-[UICellAccessoryPopUpMenu _systemTypePlacementForHeader:];
-[UICellAccessoryPopUpMenu setSelectedElementDidChangeHandler:];
-[UICellAccessoryPopUpMenu _canDirectlyUpdateExistingAccessoryViewFrom:];
-[UICellAccessoryPopUpMenu encodeWithCoder:];
-[UICellAccessoryPopUpMenu hash];
-[UICellAccessoryPopUpMenu initWithCoder:];
-[UICellAccessoryPopUpMenu copyWithZone:];
-[UICellAccessoryPopUpMenu isEqual:];
-[UICellAccessoryPopUpMenu _identifier];
-[UICellAccessoryPopUpMenu selectedElementDidChangeHandler];
-[UICellAccessoryPopUpMenu _internalMenu];
-[UICellAccessoryPopUpMenu initWithMenu:];
```
