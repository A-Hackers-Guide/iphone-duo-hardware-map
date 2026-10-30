# `_UIOHypogeanViewHandle`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 4 properties, 10 instance methods, 1 class methods

## Instance variables

```
I _contextId;
@"NSString" _uniqueIdentifier;
Q _renderId;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _bounds;
```

## Properties

```
@property (T@"NSString",C,N,V_uniqueIdentifier) uniqueIdentifier;
@property (TQ,N,V_renderId) renderId;
@property (TI,N,V_contextId) contextId;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_bounds) bounds;
```

## Class methods

```
+[_UIOHypogeanViewHandle supportsSecureCoding];
```

## Instance methods

```
-[_UIOHypogeanViewHandle contextId];
-[_UIOHypogeanViewHandle setContextId:];
-[_UIOHypogeanViewHandle setUniqueIdentifier:];
-[_UIOHypogeanViewHandle uniqueIdentifier];
-[_UIOHypogeanViewHandle setBounds:];
-[_UIOHypogeanViewHandle encodeWithCoder:];
-[_UIOHypogeanViewHandle bounds];
-[_UIOHypogeanViewHandle initWithCoder:];
-[_UIOHypogeanViewHandle renderId];
-[_UIOHypogeanViewHandle setRenderId:];
```
