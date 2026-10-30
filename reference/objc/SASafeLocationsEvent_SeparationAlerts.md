# `SASafeLocationsEvent`

- Image: [`/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`](../userland/System__Library__PrivateFrameworks__SeparationAlerts.framework__SeparationAlerts.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TAEventProtocol`
- 2 instance variables, 6 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _safeLocations;
@"NSDate" _date;
```

## Properties

```
@property (T@"NSDictionary",R,C,N,V_safeLocations) safeLocations;
@property (T@"NSDate",R,C,N,V_date) date;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SASafeLocationsEvent supportsSecureCoding];
```

## Instance methods

```
-[SASafeLocationsEvent date];
-[SASafeLocationsEvent getDate];
-[SASafeLocationsEvent descriptionDictionary];
-[SASafeLocationsEvent encodeWithCoder:];
-[SASafeLocationsEvent description];
-[SASafeLocationsEvent initWithCoder:];
-[SASafeLocationsEvent copyWithZone:];
-[SASafeLocationsEvent isEqual:];
-[SASafeLocationsEvent safeLocations];
-[SASafeLocationsEvent encodeWithOSLogCoder:options:maxLength:];
-[SASafeLocationsEvent initWithSafeLocations:date:];
```
