# `CLSubmersionStateMachine`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
d _maxDepth;
d _deepThreshold;
d _nearDepthLimitThreshold;
d _pastMaxDepthThreshold;
d _sensorErrorThreshold;
q _type;
```

## Properties

```
@property (Td,R,N,V_deepThreshold) deepThreshold;
@property (Td,R,N,V_nearDepthLimitThreshold) nearDepthLimitThreshold;
@property (Td,R,N,V_pastMaxDepthThreshold) pastMaxDepthThreshold;
@property (Td,R,N,V_sensorErrorThreshold) sensorErrorThreshold;
@property (Tq,N,V_type) type;
```

## Instance methods

```
-[CLSubmersionStateMachine initWithType:];
-[CLSubmersionStateMachine getType];
-[CLSubmersionStateMachine setType:];
-[CLSubmersionStateMachine type];
-[CLSubmersionStateMachine stateFromDepth:forceSubmersion:];
-[CLSubmersionStateMachine deepThreshold];
-[CLSubmersionStateMachine initializeThresholds];
-[CLSubmersionStateMachine nearDepthLimitThreshold];
-[CLSubmersionStateMachine pastMaxDepthThreshold];
-[CLSubmersionStateMachine sensorErrorThreshold];
```
