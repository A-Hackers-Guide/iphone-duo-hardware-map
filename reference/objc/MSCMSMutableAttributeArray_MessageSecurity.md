# `MSCMSMutableAttributeArray`

- Image: [`/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity`](../userland/System__Library__PrivateFrameworks__MessageSecurity.framework__MessageSecurity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSMutableArray`
- 3 instance variables, 3 properties, 20 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _attributes;
@"NSMutableArray" _genericAttributes;
@"NSData" _encodedAttributeSet;
```

## Properties

```
@property (T@"NSMutableArray",&,V_attributes) attributes;
@property (T@"NSMutableArray",&,V_genericAttributes) genericAttributes;
@property (T@"NSData",&,V_encodedAttributeSet) encodedAttributeSet;
```

## Class methods

```
+[MSCMSMutableAttributeArray createAttributeArrayFromAttributeSetRaw:error:];
```

## Instance methods

```
-[MSCMSMutableAttributeArray removeLastObject];
-[MSCMSMutableAttributeArray replaceObjectAtIndex:withObject:];
-[MSCMSMutableAttributeArray setEncodedAttributeSet:];
-[MSCMSMutableAttributeArray addObject:];
-[MSCMSMutableAttributeArray setAttributes:];
-[MSCMSMutableAttributeArray count];
-[MSCMSMutableAttributeArray reset];
-[MSCMSMutableAttributeArray insertObject:atIndex:];
-[MSCMSMutableAttributeArray encodedAttributeSet];
-[MSCMSMutableAttributeArray setGenericAttributes:];
-[MSCMSMutableAttributeArray removeObjectAtIndex:];
-[MSCMSMutableAttributeArray removeAttributes:];
-[MSCMSMutableAttributeArray initWithCapacity:];
-[MSCMSMutableAttributeArray genericAttributes];
-[MSCMSMutableAttributeArray encodeAttributesWithError:];
-[MSCMSMutableAttributeArray attributes];
-[MSCMSMutableAttributeArray objectAtIndex:];
-[MSCMSMutableAttributeArray encodeImplicitAttributesWithError:];
-[MSCMSMutableAttributeArray calculateAttributesWithDigest:error:];
-[MSCMSMutableAttributeArray getAttributesWithType:];
```
