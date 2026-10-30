# `CAFAppLink`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 4 instance variables, 4 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"NSString" _identifier;
@"NSString" _title;
@"NSString" _contentURLAction;
@"CAFSymbolImageWithColor" _symbolNameAndColor;
```

## Properties

```
@property (T@"NSString",&,N,V_identifier) identifier;
@property (T@"NSString",&,N,V_title) title;
@property (T@"NSString",&,N,V_contentURLAction) contentURLAction;
@property (T@"CAFSymbolImageWithColor",&,N,V_symbolNameAndColor) symbolNameAndColor;
```

## Class methods

```
+[CAFAppLink supportsSecureCoding];
```

## Instance methods

```
-[CAFAppLink identifier];
-[CAFAppLink setIdentifier:];
-[CAFAppLink title];
-[CAFAppLink encodeWithCoder:];
-[CAFAppLink hash];
-[CAFAppLink description];
-[CAFAppLink initWithCoder:];
-[CAFAppLink setTitle:];
-[CAFAppLink copyWithZone:];
-[CAFAppLink isEqual:];
-[CAFAppLink contentURLAction];
-[CAFAppLink symbolNameAndColor];
-[CAFAppLink initWithIdentifier:title:contentURLAction:symbolNameAndColor:];
-[CAFAppLink isEqualToAppLink:];
-[CAFAppLink setContentURLAction:];
-[CAFAppLink setSymbolNameAndColor:];
```
