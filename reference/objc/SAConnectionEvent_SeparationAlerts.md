# `SAConnectionEvent`

- Image: [`/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`](../userland/System__Library__PrivateFrameworks__SeparationAlerts.framework__SeparationAlerts.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OSLogCoding`, `TAEventProtocol`
- 3 instance variables, 7 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSUUID" _identifier;
q _state;
@"NSDate" _date;
```

## Properties

```
@property (T@"NSUUID",R,C,N,V_identifier) identifier;
@property (Tq,R,N,V_state) state;
@property (T@"NSDate",R,C,N,V_date) date;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SAConnectionEvent supportsSecureCoding];
```

## Instance methods

```
-[SAConnectionEvent identifier];
-[SAConnectionEvent date];
-[SAConnectionEvent getDate];
-[SAConnectionEvent descriptionDictionary];
-[SAConnectionEvent encodeWithCoder:];
-[SAConnectionEvent description];
-[SAConnectionEvent initWithCoder:];
-[SAConnectionEvent copyWithZone:];
-[SAConnectionEvent isEqual:];
-[SAConnectionEvent encodeWithOSLogCoder:options:maxLength:];
-[SAConnectionEvent state];
-[SAConnectionEvent initWithDeviceUUID:state:date:];
```
