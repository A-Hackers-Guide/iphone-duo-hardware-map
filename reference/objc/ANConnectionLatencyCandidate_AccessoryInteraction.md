# `ANConnectionLatencyCandidate`

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 3 instance methods, 1 class methods

## Instance variables

```
B _force;
q _latency;
```

## Properties

```
@property (Tq,R,N,V_latency) latency;
@property (TB,R,N,V_force) force;
```

## Class methods

```
+[ANConnectionLatencyCandidate candidateWithFirmwareUpdateMode:preparingForRanging:activeTask:isRoseInitialized:pendingTasks:isMaintenanceConnectCondition:isLeashSlotInUse:willSleep:];
```

## Instance methods

```
-[ANConnectionLatencyCandidate latency];
-[ANConnectionLatencyCandidate force];
-[ANConnectionLatencyCandidate initWithLatency:force:];
```
