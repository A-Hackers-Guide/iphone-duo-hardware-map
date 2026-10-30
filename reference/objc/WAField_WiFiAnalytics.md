# `WAField`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 5 instance variables, 14 properties, 53 instance methods, 1 class methods

## Instance variables

```
@ _value;
@"NSString" _typeInfoForRepeatableSubmessage;
B _isRepeatable;
q _type;
@"NSString" _key;
```

## Properties

```
@property (Tq,N,V_type) type;
@property (TB,N,V_isRepeatable) isRepeatable;
@property (T@"NSString",&,N,V_key) key;
@property (T@"NSMutableArray",&,D,N) repeatableValues;
@property (Td,D,N) doubleValue;
@property (Tf,D,N) floatValue;
@property (Ti,D,N) int32Value;
@property (Tq,D,N) int64Value;
@property (TI,D,N) uint32Value;
@property (TQ,D,N) uint64Value;
@property (TB,D,N) boolValue;
@property (T@"NSString",&,D,N) stringValue;
@property (T@"NSData",&,D,N) bytesValue;
@property (T@"WAMessageAWD",&,D,N) subMessageValue;
```

## Class methods

```
+[WAField supportsSecureCoding];
```

## Instance methods

```
-[WAField stringValue];
-[WAField floatValue];
-[WAField int64Value];
-[WAField boolValue];
-[WAField _throwIncorrectRepeatableStateExceptionAsFieldShouldBeRepeatable:isGet:forType:];
-[WAField addRepeatableSubMessageValue:];
-[WAField setDoubleValue:];
-[WAField doubleValue];
-[WAField bytesValue];
-[WAField setStringValue:];
-[WAField init];
-[WAField addRepeatableInt32Value:];
-[WAField setFloatValue:];
-[WAField _throwIncorrecTypeExceptionForType:isGet:];
-[WAField setIsRepeatable:];
-[WAField setUint32Value:];
-[WAField int32Value];
-[WAField setInt64Value:];
-[WAField addRepeatableUInt64Value:];
-[WAField setKey:];
-[WAField initWithType:isRepeatable:andKey:andTypeInfoForRepeatableSubmessage:];
-[WAField addRepeatableBoolValue:];
-[WAField _addRepeatableValue:];
-[WAField addRepeatableUInt32Value:];
-[WAField setUint64Value:];
-[WAField uint64Value];
-[WAField _typeAsString:];
-[WAField addRepeatableString:];
-[WAField setBoolValue:];
-[WAField setType:];
-[WAField uint32Value];
-[WAField type];
-[WAField addRepeatableInt64Value:];
-[WAField addRepeatableDoubleValue:];
-[WAField setSubMessageValue:];
-[WAField encodeWithCoder:];
-[WAField setBytesValue:];
-[WAField setInt32Value:];
-[WAField addRepeatableFloatValue:];
-[WAField _ownTypeAsString];
-[WAField initWithType:isRepeatable:key:repeatableValues:doubleValue:floatValue:int32Value:int64Value:uint32Val:uint64Value:boolValue:stringValue:bytesValue:subMessageValue:andTypeInfoForRepeatableSubmessage:];
-[WAField description];
-[WAField subMessageValue];
-[WAField isNumerical];
-[WAField typeInformationForRepeatableSubmessage];
-[WAField initWithCoder:];
-[WAField repeatableValues];
-[WAField addRepeatableBytes:];
-[WAField copyWithZone:];
-[WAField setRepeatableValues:];
-[WAField setTypeInformationForRepeatableSubmessage:];
-[WAField isRepeatable];
-[WAField key];
```
