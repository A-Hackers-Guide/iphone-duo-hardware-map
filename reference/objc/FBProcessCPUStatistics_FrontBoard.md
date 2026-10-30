# `FBProcessCPUStatistics`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"RBSProcessHandle" _handle;
{FBProcessTimes="beginUserCPUElapsedTime"d"beginSystemCPUElapsedTime"d"beginIdleCPUElapsedTime"d"beginApplicationCPUElapsedTime"d} _times;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
```

## Properties

```
@property (Td,R,N) totalElapsedTime;
@property (Td,R,N) totalElapsedUserTime;
@property (Td,R,N) totalElapsedSystemTime;
@property (Td,R,N) totalElapsedIdleTime;
```

## Instance methods

```
-[FBProcessCPUStatistics _hostwideUserElapsedCPUTime:systemElapsedCPUTime:idleElapsedCPUTime:];
-[FBProcessCPUStatistics _lock_getApplicationCPUTimesForUser:system:idle:];
-[FBProcessCPUStatistics initWithProcessHandle:];
-[FBProcessCPUStatistics totalElapsedUserTime];
-[FBProcessCPUStatistics reset];
-[FBProcessCPUStatistics totalElapsedTime];
-[FBProcessCPUStatistics totalElapsedIdleTime];
-[FBProcessCPUStatistics totalElapsedSystemTime];
-[FBProcessCPUStatistics descriptionForCrashReport];
```
