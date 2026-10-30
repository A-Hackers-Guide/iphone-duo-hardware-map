# `SBDelayedPressInfo`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
B _longClick;
q _type;
q _phase;
d _timestamp;
```

## Properties

```
@property (Tq,N,V_type) type;
@property (Tq,N,V_phase) phase;
@property (Td,N,V_timestamp) timestamp;
@property (TB,N,GisLongClick,V_longClick) longClick;
```

## Instance methods

```
-[SBDelayedPressInfo setTimestamp:];
-[SBDelayedPressInfo phase];
-[SBDelayedPressInfo isLongClick];
-[SBDelayedPressInfo timestamp];
-[SBDelayedPressInfo setType:];
-[SBDelayedPressInfo type];
-[SBDelayedPressInfo setPhase:];
-[SBDelayedPressInfo setLongClick:];
```
