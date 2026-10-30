# `CMMotionTimeRange`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CMLogItem`
- 2 instance variables, 2 properties, 8 instance methods, 3 class methods

## Instance variables

```
@"NSDate" fStartDate;
@"NSDate" fEndDate;
```

## Properties

```
@property (T@"NSDate",R,N) startDate;
@property (T@"NSDate",R,N) endDate;
```

## Class methods

```
+[CMMotionTimeRange supportsSecureCoding];
+[CMMotionTimeRange CLMotionTimeRangeFromCMMotionTimeRange:];
+[CMMotionTimeRange CMMotionTimeRangeFromCLMotionTimeRange:];
```

## Instance methods

```
-[CMMotionTimeRange startDate];
-[CMMotionTimeRange dealloc];
-[CMMotionTimeRange endDate];
-[CMMotionTimeRange initWithStartDate:endDate:];
-[CMMotionTimeRange encodeWithCoder:];
-[CMMotionTimeRange description];
-[CMMotionTimeRange initWithCoder:];
-[CMMotionTimeRange copyWithZone:];
```
