# `_UIHyperpoint`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIHyperregion_Internal`, `_UIHyperregion`, `NSSecureCoding`, `NSCopying`
- 2 instance variables, 6 properties, 14 instance methods, 2 class methods

## Instance variables

```
^d __value;
Q __dimensions;
```

## Properties

```
@property (Tr^d,R,N) _value;
@property (TQ,R,N,V__dimensions) _dimensions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIHyperpoint supportsSecureCoding];
+[_UIHyperpoint keyPathsForValuesAffectingSelf];
```

## Instance methods

```
-[_UIHyperpoint _value];
-[_UIHyperpoint initWithDimensions:];
-[_UIHyperpoint dealloc];
-[_UIHyperpoint _mutateValue:];
-[_UIHyperpoint _copyValue:];
-[_UIHyperpoint initWithValue:dimensions:];
-[_UIHyperpoint initWithValue:objCType:];
-[_UIHyperpoint encodeWithCoder:];
-[_UIHyperpoint description];
-[_UIHyperpoint initWithCoder:];
-[_UIHyperpoint _dimensions];
-[_UIHyperpoint copyWithZone:];
-[_UIHyperpoint isEqual:];
-[_UIHyperpoint _closestPoint:toPoint:];
```
