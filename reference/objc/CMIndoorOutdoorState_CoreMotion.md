# `CMIndoorOutdoorState`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 3 instance variables, 3 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSDate" fStartDate;
q fType;
q fConfidence;
```

## Properties

```
@property (T@"NSDate",R,N) startDate;
@property (Tq,R,N) type;
@property (Tq,R,N) confidence;
```

## Class methods

```
+[CMIndoorOutdoorState supportsSecureCoding];
```

## Instance methods

```
-[CMIndoorOutdoorState startDate];
-[CMIndoorOutdoorState dealloc];
-[CMIndoorOutdoorState type];
-[CMIndoorOutdoorState encodeWithCoder:];
-[CMIndoorOutdoorState description];
-[CMIndoorOutdoorState initWithCoder:];
-[CMIndoorOutdoorState copyWithZone:];
-[CMIndoorOutdoorState confidence];
-[CMIndoorOutdoorState initWithStartDate:type:confidence:];
```
