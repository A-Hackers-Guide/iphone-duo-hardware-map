# `SATransparencyEvent`

- Image: [`/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`](../userland/System__Library__PrivateFrameworks__SeparationAlerts.framework__SeparationAlerts.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OSLogCoding`, `TAEventProtocol`
- 1 instance variables, 5 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSDate" _date;
```

## Properties

```
@property (T@"NSDate",R,C,N,V_date) date;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SATransparencyEvent supportsSecureCoding];
```

## Instance methods

```
-[SATransparencyEvent initWithDate:];
-[SATransparencyEvent date];
-[SATransparencyEvent getDate];
-[SATransparencyEvent descriptionDictionary];
-[SATransparencyEvent encodeWithCoder:];
-[SATransparencyEvent hash];
-[SATransparencyEvent description];
-[SATransparencyEvent initWithCoder:];
-[SATransparencyEvent copyWithZone:];
-[SATransparencyEvent isEqual:];
-[SATransparencyEvent encodeWithOSLogCoder:options:maxLength:];
```
