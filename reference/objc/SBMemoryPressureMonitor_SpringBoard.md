# `SBMemoryPressureMonitor`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 1 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"SBMiscellaneousDefaults" _miscellaneousDefaults;
@"NSObject<OS_dispatch_source>" _memoryPressureSource;
I _memoryPressureStatus;
```

## Properties

```
@property (TB,R,N) isUnderMemoryPressure;
```

## Instance methods

```
-[SBMemoryPressureMonitor _handleMemoryPressureChanged];
-[SBMemoryPressureMonitor _setMemoryPressureStatus:];
-[SBMemoryPressureMonitor initWithMiscellaneousDefaults:];
-[SBMemoryPressureMonitor initWithMiscellaneousDefaults:observesMemoryPressure:];
-[SBMemoryPressureMonitor isUnderMemoryPressure];
```
