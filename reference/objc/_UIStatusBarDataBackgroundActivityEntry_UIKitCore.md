# `_UIStatusBarDataBackgroundActivityEntry`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIStatusBarDataEntry`
- 3 instance variables, 3 properties, 12 instance methods, 1 class methods

## Instance variables

```
q _type;
d _displayStartDate;
@"NSString" _detailString;
```

## Properties

```
@property (Tq,N,V_type) type;
@property (Td,N,V_displayStartDate) displayStartDate;
@property (T@"NSString",C,N,V_detailString) detailString;
```

## Class methods

```
+[_UIStatusBarDataBackgroundActivityEntry supportsSecureCoding];
```

## Instance methods

```
-[_UIStatusBarDataBackgroundActivityEntry detailString];
-[_UIStatusBarDataBackgroundActivityEntry _ui_descriptionBuilder];
-[_UIStatusBarDataBackgroundActivityEntry setType:];
-[_UIStatusBarDataBackgroundActivityEntry type];
-[_UIStatusBarDataBackgroundActivityEntry encodeWithCoder:];
-[_UIStatusBarDataBackgroundActivityEntry hash];
-[_UIStatusBarDataBackgroundActivityEntry initWithCoder:];
-[_UIStatusBarDataBackgroundActivityEntry displayStartDate];
-[_UIStatusBarDataBackgroundActivityEntry copyWithZone:];
-[_UIStatusBarDataBackgroundActivityEntry isEqual:];
-[_UIStatusBarDataBackgroundActivityEntry setDetailString:];
-[_UIStatusBarDataBackgroundActivityEntry setDisplayStartDate:];
```
