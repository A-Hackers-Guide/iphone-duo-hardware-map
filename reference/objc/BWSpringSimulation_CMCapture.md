# `BWSpringSimulation`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 7 properties, 14 instance methods, 1 class methods

## Instance variables

```
d _tension;
d _friction;
d _convergedSpeed;
d _inputValue;
d _outputValue;
d _velocity;
d _previousForce;
B _completed;
i _updateCount;
```

## Properties

```
@property (Td,N,V_inputValue) input;
@property (Td,N,V_tension) tension;
@property (Td,N,V_friction) friction;
@property (Td,R,N,V_outputValue) output;
@property (Td,R,N,V_velocity) velocity;
@property (TB,R,N,GisCompleted,V_completed) completed;
@property (Ti,R,N,V_updateCount) updateCount;
```

## Class methods

```
+[BWSpringSimulation initialize];
```

## Instance methods

```
-[BWSpringSimulation setFriction:];
-[BWSpringSimulation tension];
-[BWSpringSimulation friction];
-[BWSpringSimulation input];
-[BWSpringSimulation setTension:];
-[BWSpringSimulation update];
-[BWSpringSimulation init];
-[BWSpringSimulation setInput:];
-[BWSpringSimulation isCompleted];
-[BWSpringSimulation velocity];
-[BWSpringSimulation updateCount];
-[BWSpringSimulation output];
-[BWSpringSimulation resetWithInput:initialOutput:initialVelocity:];
-[BWSpringSimulation resetWithInput:initialOutput:initialVelocity:convergedSpeed:];
```
