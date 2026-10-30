# `SASafeLocation`

- Image: [`/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`](../userland/System__Library__PrivateFrameworks__SeparationAlerts.framework__SeparationAlerts.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OSLogCoding`, `TAEventProtocol`
- 7 instance variables, 11 properties, 18 instance methods, 1 class methods

## Instance variables

```
@"NSUUID" _identifier;
d _latitude;
d _longitude;
d _radius;
Q _referenceFrame;
@"NSString" _name;
@"NSDate" _date;
```

## Properties

```
@property (T@"NSUUID",R,C,N,V_identifier) identifier;
@property (Td,R,N,V_latitude) latitude;
@property (Td,R,N,V_longitude) longitude;
@property (Td,R,N,V_radius) radius;
@property (TQ,R,N,V_referenceFrame) referenceFrame;
@property (T@"NSString",R,C,N,V_name) name;
@property (T@"NSDate",R,C,N,V_date) date;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SASafeLocation supportsSecureCoding];
```

## Instance methods

```
-[SASafeLocation identifier];
-[SASafeLocation latitude];
-[SASafeLocation longitude];
-[SASafeLocation referenceFrame];
-[SASafeLocation date];
-[SASafeLocation getDate];
-[SASafeLocation radius];
-[SASafeLocation descriptionDictionary];
-[SASafeLocation encodeWithCoder:];
-[SASafeLocation hash];
-[SASafeLocation description];
-[SASafeLocation initWithCoder:];
-[SASafeLocation copyWithZone:];
-[SASafeLocation isEqual:];
-[SASafeLocation name];
-[SASafeLocation encodeWithOSLogCoder:options:maxLength:];
-[SASafeLocation initWithLocationUUID:latitude:longitude:radius:referenceFrame:name:date:];
-[SASafeLocation isReallyEqual:];
```
