# `ULHomeSlamTimer`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 6 instance methods, 0 class methods

## Instance variables

```
d _timeoutSeconds;
@"NSDate" _startTime;
```

## Properties

```
@property (Td,N,V_timeoutSeconds) timeoutSeconds;
@property (T@"NSDate",&,N,V_startTime) startTime;
```

## Instance methods

```
-[ULHomeSlamTimer startTime];
-[ULHomeSlamTimer setStartTime:];
-[ULHomeSlamTimer timeoutSeconds];
-[ULHomeSlamTimer setTimeoutSeconds:];
-[ULHomeSlamTimer checkTimeoutAtDate:];
-[ULHomeSlamTimer initWithTimeout:andStartTime:];
```
