# `_UIDatePickerCalendarTimeLabelStateMachineContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
Q _currentState;
@? _updateHandler;
B _isFirstResponder;
Q _lastDistinctState;
Q _previousState;
```

## Properties

```
@property (TQ,R,N,V_lastDistinctState) lastDistinctState;
@property (TQ,R,N,V_previousState) previousState;
@property (TQ,R,N,V_currentState) currentState;
@property (T^Q,R,N) currentStateRef;
@property (TB,N,V_isFirstResponder) isFirstResponder;
```

## Instance methods

```
-[_UIDatePickerCalendarTimeLabelStateMachineContext initWithUpdateHandler:];
-[_UIDatePickerCalendarTimeLabelStateMachineContext isFirstResponder];
-[_UIDatePickerCalendarTimeLabelStateMachineContext setIsFirstResponder:];
-[_UIDatePickerCalendarTimeLabelStateMachineContext previousState];
-[_UIDatePickerCalendarTimeLabelStateMachineContext currentState];
-[_UIDatePickerCalendarTimeLabelStateMachineContext currentStateRef];
-[_UIDatePickerCalendarTimeLabelStateMachineContext _updateFromState:];
-[_UIDatePickerCalendarTimeLabelStateMachineContext currentSateCanTransitionWithEvents:];
-[_UIDatePickerCalendarTimeLabelStateMachineContext lastDistinctState];
```
