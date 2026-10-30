# `UIPasteControlConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 7 instance variables, 7 properties, 17 instance methods, 1 class methods

## Instance variables

```
B __shouldLayoutSynchronously;
Q _displayMode;
q _cornerStyle;
d _cornerRadius;
Q _imagePlacement;
@"UIColor" _baseForegroundColor;
@"UIColor" _baseBackgroundColor;
```

## Properties

```
@property (TB,N,V__shouldLayoutSynchronously) _shouldLayoutSynchronously;
@property (TQ,N,V_displayMode) displayMode;
@property (Tq,N,V_cornerStyle) cornerStyle;
@property (Td,N,V_cornerRadius) cornerRadius;
@property (TQ,N,V_imagePlacement) imagePlacement;
@property (T@"UIColor",&,N,V_baseForegroundColor) baseForegroundColor;
@property (T@"UIColor",&,N,V_baseBackgroundColor) baseBackgroundColor;
```

## Class methods

```
+[UIPasteControlConfiguration supportsSecureCoding];
```

## Instance methods

```
-[UIPasteControlConfiguration cornerStyle];
-[UIPasteControlConfiguration setDisplayMode:];
-[UIPasteControlConfiguration init];
-[UIPasteControlConfiguration setCornerStyle:];
-[UIPasteControlConfiguration displayMode];
-[UIPasteControlConfiguration setCornerRadius:];
-[UIPasteControlConfiguration cornerRadius];
-[UIPasteControlConfiguration encodeWithCoder:];
-[UIPasteControlConfiguration initWithCoder:];
-[UIPasteControlConfiguration _shouldLayoutSynchronously];
-[UIPasteControlConfiguration baseBackgroundColor];
-[UIPasteControlConfiguration baseForegroundColor];
-[UIPasteControlConfiguration imagePlacement];
-[UIPasteControlConfiguration setBaseBackgroundColor:];
-[UIPasteControlConfiguration setBaseForegroundColor:];
-[UIPasteControlConfiguration setImagePlacement:];
-[UIPasteControlConfiguration set_shouldLayoutSynchronously:];
```
