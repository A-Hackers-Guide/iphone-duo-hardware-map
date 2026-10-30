# `WAMessageAWD`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 6 instance variables, 6 properties, 21 instance methods, 1 class methods

## Instance variables

```
B _isRootMessage;
@"NSMutableDictionary" _mutableFields;
@"NSString" _key;
@"NSString" _originalClassName;
@"NSString" _uuid;
Q _metricID;
```

## Properties

```
@property (T@"NSMutableDictionary",R,N,V_mutableFields) mutableFields;
@property (T@"NSString",R,N,V_key) key;
@property (TB,R,N,V_isRootMessage) isRootMessage;
@property (T@"NSString",R,N,V_originalClassName) originalClassName;
@property (T@"NSString",R,N,V_uuid) uuid;
@property (TQ,R,N,V_metricID) metricID;
```

## Class methods

```
+[WAMessageAWD supportsSecureCoding];
```

## Instance methods

```
-[WAMessageAWD uuid];
-[WAMessageAWD init];
-[WAMessageAWD setUuid:];
-[WAMessageAWD initWithKey:andFields:isRootMessage:originalClassName:uuid:];
-[WAMessageAWD setIsRootMessage:];
-[WAMessageAWD setKey:];
-[WAMessageAWD metricID];
-[WAMessageAWD setMetricID:];
-[WAMessageAWD setMutableFields:];
-[WAMessageAWD encodeWithCoder:];
-[WAMessageAWD addField:];
-[WAMessageAWD fieldForKey:];
-[WAMessageAWD description];
-[WAMessageAWD initWithCoder:];
-[WAMessageAWD setOriginalClassName:];
-[WAMessageAWD copyWithZone:];
-[WAMessageAWD isEqual:];
-[WAMessageAWD originalClassName];
-[WAMessageAWD isRootMessage];
-[WAMessageAWD key];
-[WAMessageAWD mutableFields];
```
