# `CTSIMToolkitItem`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 9 instance methods, 1 class methods

## Instance variables

```
B _selected;
@"NSString" _text;
```

## Properties

```
@property (T@"NSString",&,N,V_text) text;
@property (TB,N,V_selected) selected;
```

## Class methods

```
+[CTSIMToolkitItem supportsSecureCoding];
```

## Instance methods

```
-[CTSIMToolkitItem setSelected:];
-[CTSIMToolkitItem text];
-[CTSIMToolkitItem encodeWithCoder:];
-[CTSIMToolkitItem description];
-[CTSIMToolkitItem initWithCoder:];
-[CTSIMToolkitItem setText:];
-[CTSIMToolkitItem copyWithZone:];
-[CTSIMToolkitItem selected];
-[CTSIMToolkitItem initWithText:selected:];
```
