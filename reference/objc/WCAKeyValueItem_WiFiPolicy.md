# `WCAKeyValueItem`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 13 properties, 18 instance methods, 1 class methods

## Instance variables

```
@ _value;
@"NSString" _key;
```

## Properties

```
@property (T@"NSString",R,C,N,V_key) key;
@property (T@"NSDictionary",R,N) dictionaryValue;
@property (T@"NSArray",R,N) arrayValue;
@property (Td,R,N) doubleValue;
@property (Tf,R,N) floatValue;
@property (Ti,R,N) int32Value;
@property (Tq,R,N) int64Value;
@property (TI,R,N) uint32Value;
@property (TQ,R,N) uint64Value;
@property (TB,R,N) boolValue;
@property (T@"NSString",R,N) stringValue;
@property (T@"NSData",R,N) bytesValue;
@property (T@"NSError",R,C,N) error;
```

## Class methods

```
+[WCAKeyValueItem supportsSecureCoding];
```

## Instance methods

```
-[WCAKeyValueItem stringValue];
-[WCAKeyValueItem floatValue];
-[WCAKeyValueItem int64Value];
-[WCAKeyValueItem boolValue];
-[WCAKeyValueItem dictionaryValue];
-[WCAKeyValueItem doubleValue];
-[WCAKeyValueItem bytesValue];
-[WCAKeyValueItem int32Value];
-[WCAKeyValueItem error];
-[WCAKeyValueItem uint64Value];
-[WCAKeyValueItem uint32Value];
-[WCAKeyValueItem encodeWithCoder:];
-[WCAKeyValueItem description];
-[WCAKeyValueItem initWithCoder:];
-[WCAKeyValueItem arrayValue];
-[WCAKeyValueItem key];
-[WCAKeyValueItem initWithKey:value:];
-[WCAKeyValueItem initWithKey:error:];
```
