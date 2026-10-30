# `CAFBatchUpdateItem`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 4 instance variables, 4 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSNumber" _pluginID;
@"NSNumber" _priority;
@"NSNumber" _instanceID;
@ _value;
```

## Properties

```
@property (T@"NSNumber",R,N,V_pluginID) pluginID;
@property (T@"NSNumber",R,N,V_priority) priority;
@property (T@"NSNumber",R,N,V_instanceID) instanceID;
@property (T@,R,N,V_value) value;
```

## Class methods

```
+[CAFBatchUpdateItem supportsSecureCoding];
```

## Instance methods

```
-[CAFBatchUpdateItem priority];
-[CAFBatchUpdateItem value];
-[CAFBatchUpdateItem encodeWithCoder:];
-[CAFBatchUpdateItem instanceID];
-[CAFBatchUpdateItem description];
-[CAFBatchUpdateItem initWithCoder:];
-[CAFBatchUpdateItem copyWithZone:];
-[CAFBatchUpdateItem initWithService:characteristicType:value:];
-[CAFBatchUpdateItem pluginID];
```
