# `MSCMSAttribute`

- Image: [`/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity`](../userland/System__Library__PrivateFrameworks__MessageSecurity.framework__MessageSecurity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MSCMSAttributeCoder`
- 4 instance variables, 4 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"MSOID" _attributeType;
@"NSArray" _attributeValues;
@"NSData" _attributeDERData;
^{Attribute={heim_oid=Q^I}{Attribute_value=I^{heim_base_data}}} _encodedAttribute;
```

## Properties

```
@property (T@"NSData",&,V_attributeDERData) attributeDERData;
@property (T^{Attribute={heim_oid=Q^I}{Attribute_value=I^{heim_base_data}}},V_encodedAttribute) encodedAttribute;
@property (T@"MSOID",R,&,V_attributeType) attributeType;
@property (T@"NSArray",R,&,V_attributeValues) attributeValues;
```

## Class methods

```
+[MSCMSAttribute decodeAttribute:error:];
```

## Instance methods

```
-[MSCMSAttribute attributeType];
-[MSCMSAttribute dealloc];
-[MSCMSAttribute attributeValues];
-[MSCMSAttribute initWithAttribute:error:];
-[MSCMSAttribute attributeDERData];
-[MSCMSAttribute encodeAttributeWithError:];
-[MSCMSAttribute encodedAttribute];
-[MSCMSAttribute generateAttributeStruct];
-[MSCMSAttribute initWithAttributeStruct:error:];
-[MSCMSAttribute initWithAttributeType:values:];
-[MSCMSAttribute initWithDER:];
-[MSCMSAttribute setAttributeDERData:];
-[MSCMSAttribute setEncodedAttribute:];
```
