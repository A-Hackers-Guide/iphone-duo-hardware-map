# `CMPedometerEvent`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 2 instance variables, 2 properties, 8 instance methods, 2 class methods

## Instance variables

```
@"NSDate" fDate;
q fType;
```

## Properties

```
@property (T@"NSDate",R,N,VfDate) date;
@property (Tq,R,N,VfType) type;
```

## Class methods

```
+[CMPedometerEvent supportsSecureCoding];
+[CMPedometerEvent eventStringFromType:];
```

## Instance methods

```
-[CMPedometerEvent dealloc];
-[CMPedometerEvent date];
-[CMPedometerEvent type];
-[CMPedometerEvent encodeWithCoder:];
-[CMPedometerEvent description];
-[CMPedometerEvent initWithCoder:];
-[CMPedometerEvent copyWithZone:];
-[CMPedometerEvent initWithEventDate:type:];
```
