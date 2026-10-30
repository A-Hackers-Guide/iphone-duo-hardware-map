# `CMMetMinute`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 2 instance variables, 2 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSDate" fStartDate;
@"NSNumber" fAverageIntensity;
```

## Properties

```
@property (T@"NSDate",R,N) startDate;
@property (T@"NSNumber",R,N) averageIntensity;
```

## Class methods

```
+[CMMetMinute supportsSecureCoding];
```

## Instance methods

```
-[CMMetMinute startDate];
-[CMMetMinute dealloc];
-[CMMetMinute encodeWithCoder:];
-[CMMetMinute description];
-[CMMetMinute initWithCoder:];
-[CMMetMinute copyWithZone:];
-[CMMetMinute initWithSample:];
-[CMMetMinute averageIntensity];
-[CMMetMinute initWithStartDate:averageIntensity:];
```
