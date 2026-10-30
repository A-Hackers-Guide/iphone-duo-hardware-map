# `_UIStickerRepresentation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 4 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSData" _data;
@"NSString" _type;
@"NSString" _role;
{CGSize="width"d"height"d} _size;
```

## Properties

```
@property (T@"NSData",&,N,V_data) data;
@property (T@"NSString",&,N,V_type) type;
@property (T{CGSize=dd},N,V_size) size;
@property (T@"NSString",&,N,V_role) role;
```

## Class methods

```
+[_UIStickerRepresentation supportsSecureCoding];
```

## Instance methods

```
-[_UIStickerRepresentation data];
-[_UIStickerRepresentation size];
-[_UIStickerRepresentation setType:];
-[_UIStickerRepresentation type];
-[_UIStickerRepresentation setData:];
-[_UIStickerRepresentation encodeWithCoder:];
-[_UIStickerRepresentation role];
-[_UIStickerRepresentation setRole:];
-[_UIStickerRepresentation initWithCoder:];
-[_UIStickerRepresentation setSize:];
-[_UIStickerRepresentation createPNGDataFromHEICData];
-[_UIStickerRepresentation initWithData:type:size:role:];
```
