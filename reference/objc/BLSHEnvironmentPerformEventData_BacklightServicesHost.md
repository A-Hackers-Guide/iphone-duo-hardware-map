# `BLSHEnvironmentPerformEventData`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
q _stateMachineOldBacklightState;
q _eventPreviousBacklightState;
q _eventNewBacklightState;
Q _startedTime;
```

## Properties

```
@property (Tq,R,N,V_stateMachineOldBacklightState) stateMachineOldBacklightState;
@property (Tq,R,N,V_eventPreviousBacklightState) eventPreviousBacklightState;
@property (Tq,R,N,V_eventNewBacklightState) eventNewBacklightState;
@property (TQ,R,N,V_startedTime) startedTime;
```

## Instance methods

```
-[BLSHEnvironmentPerformEventData description];
-[BLSHEnvironmentPerformEventData isEqual:];
-[BLSHEnvironmentPerformEventData eventNewBacklightState];
-[BLSHEnvironmentPerformEventData eventPreviousBacklightState];
-[BLSHEnvironmentPerformEventData initWithStateMachineOldBacklightState:eventPreviousBacklightState:eventNewBacklightState:];
-[BLSHEnvironmentPerformEventData startedTime];
-[BLSHEnvironmentPerformEventData stateMachineOldBacklightState];
```
