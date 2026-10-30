# `_UIUpdateHIDDigitizerInput`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIUpdateHIDAbstractInput`
- 9 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
{_UIUpdateInputInternal="_state"{_UIUpdateInputState="mode"i"earliestModelTime"q"latestModelTime"q}"_flags"I"_alignments"[2{_UIUpdateInputAlignmentShift="shiftDuration"q}]"_set"^{_UIUpdateInputSet}"_setEntry"{?="le_next"^{_UIUpdateInputInternal}"le_prev"^^{_UIUpdateInputInternal}}"_readyForModelTimeCallback"^?"_context"^v"_name"*} _input;
^{_UIUpdateInputTimingProfile=qqQBqqBQQ^{_UIUpdateInputReadyProfile}^{_UIUpdateInputReadyProfile}} _profile;
@"NSMutableArray" _events;
@"NSMutableSet" _touches;
q _eventModelTimeDifferenceMin;
q _eventModelTimeDifferenceMax;
q _nextEventReceiveDeadlineTimeDifference;
q _eventPhaseTime;
B _nextEventExpected;
```

## Instance methods

```
-[_UIUpdateHIDDigitizerInput removeEvent:];
-[_UIUpdateHIDDigitizerInput addEvent:];
-[_UIUpdateHIDDigitizerInput dealloc];
-[_UIUpdateHIDDigitizerInput stopEventForModelTime:alignment:];
```
