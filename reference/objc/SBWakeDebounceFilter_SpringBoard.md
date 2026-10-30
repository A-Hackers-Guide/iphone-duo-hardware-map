# `SBWakeDebounceFilter`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 3 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _wakeEvents;
q _oldestWakeEventIndex;
Q _intervalActivationLimit;
@"NSNumber" _overrideTime;
d _filterInterval;
```

## Properties

```
@property (T@"NSNumber",C,N,G_overrideTime,S_setOverrideTime:,V_overrideTime) overrideTime;
@property (Td,N,V_filterInterval) filterInterval;
@property (TQ,N,V_intervalActivationLimit) intervalActivationLimit;
```

## Instance methods

```
-[SBWakeDebounceFilter filterInterval];
-[SBWakeDebounceFilter setFilterInterval:];
-[SBWakeDebounceFilter _overrideTime];
-[SBWakeDebounceFilter _setOverrideTime:];
-[SBWakeDebounceFilter intervalActivationLimit];
-[SBWakeDebounceFilter setIntervalActivationLimit:];
-[SBWakeDebounceFilter wakeEventOccurred];
```
