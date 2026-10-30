# `_UICellAccessoryConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 6 properties, 15 instance methods, 1 class methods

## Instance variables

```
B _usesDefaultLayoutWidth;
@"UIColor" _tintColor;
@"UIColor" _backgroundColor;
```

## Properties

```
@property (TB,R,N,G_isSystemType) isSystemType;
@property (Tq,R,N,G_systemType) systemType;
@property (T@"NSString",R,N,G_identifier) identifier;
@property (T@"UIColor",&,N,G_backgroundColor,S_setBackgroundColor:,V_backgroundColor) backgroundColor;
@property (TB,N,V_usesDefaultLayoutWidth) usesDefaultLayoutWidth;
@property (T@"UIColor",&,N,V_tintColor) tintColor;
```

## Class methods

```
+[_UICellAccessoryConfiguration supportsSecureCoding];
```

## Instance methods

```
-[_UICellAccessoryConfiguration _systemType];
-[_UICellAccessoryConfiguration _backgroundColor];
-[_UICellAccessoryConfiguration init];
-[_UICellAccessoryConfiguration setTintColor:];
-[_UICellAccessoryConfiguration encodeWithCoder:];
-[_UICellAccessoryConfiguration hash];
-[_UICellAccessoryConfiguration tintColor];
-[_UICellAccessoryConfiguration initWithCoder:];
-[_UICellAccessoryConfiguration copyWithZone:];
-[_UICellAccessoryConfiguration isEqual:];
-[_UICellAccessoryConfiguration _identifier];
-[_UICellAccessoryConfiguration _isSystemType];
-[_UICellAccessoryConfiguration _setBackgroundColor:];
-[_UICellAccessoryConfiguration setUsesDefaultLayoutWidth:];
-[_UICellAccessoryConfiguration usesDefaultLayoutWidth];
```
