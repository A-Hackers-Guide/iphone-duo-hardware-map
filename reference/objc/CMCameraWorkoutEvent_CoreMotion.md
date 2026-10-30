# `CMCameraWorkoutEvent`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
i _eventType;
d _localMachtime;
d _globalMachtime;
q _workoutType;
```

## Properties

```
@property (Td,N,V_localMachtime) localMachtime;
@property (Td,N,V_globalMachtime) globalMachtime;
@property (Ti,N,V_eventType) eventType;
@property (Tq,N,V_workoutType) workoutType;
```

## Instance methods

```
-[CMCameraWorkoutEvent eventType];
-[CMCameraWorkoutEvent setEventType:];
-[CMCameraWorkoutEvent setWorkoutType:];
-[CMCameraWorkoutEvent workoutType];
-[CMCameraWorkoutEvent globalMachtime];
-[CMCameraWorkoutEvent localMachtime];
-[CMCameraWorkoutEvent setGlobalMachtime:];
-[CMCameraWorkoutEvent setLocalMachtime:];
```
