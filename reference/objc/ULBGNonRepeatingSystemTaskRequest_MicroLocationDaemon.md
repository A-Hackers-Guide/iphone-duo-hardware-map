# `ULBGNonRepeatingSystemTaskRequest`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULBGSystemTaskRequest`
- 2 instance variables, 2 properties, 6 instance methods, 0 class methods

## Instance variables

```
d _scheduleAfter;
d _trySchedulingBefore;
```

## Properties

```
@property (Td,N,V_scheduleAfter) scheduleAfter;
@property (Td,N,V_trySchedulingBefore) trySchedulingBefore;
```

## Instance methods

```
-[ULBGNonRepeatingSystemTaskRequest setTrySchedulingBefore:];
-[ULBGNonRepeatingSystemTaskRequest setScheduleAfter:];
-[ULBGNonRepeatingSystemTaskRequest trySchedulingBefore];
-[ULBGNonRepeatingSystemTaskRequest createRequestFromSelf];
-[ULBGNonRepeatingSystemTaskRequest scheduleAfter];
-[ULBGNonRepeatingSystemTaskRequest initWithIdentifier:scheduleAfter:trySchedulingBefore:];
```
