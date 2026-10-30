# `_UIUpdateHIDInput`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIUpdateHIDAbstractInput`
- 2 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
{_UIUpdateInputInternal="_state"{_UIUpdateInputState="mode"i"earliestModelTime"q"latestModelTime"q}"_flags"I"_alignments"[2{_UIUpdateInputAlignmentShift="shiftDuration"q}]"_set"^{_UIUpdateInputSet}"_setEntry"{?="le_next"^{_UIUpdateInputInternal}"le_prev"^^{_UIUpdateInputInternal}}"_readyForModelTimeCallback"^?"_context"^v"_name"*} _input;
@"NSMutableArray" _events;
```

## Instance methods

```
-[_UIUpdateHIDInput removeEvent:];
-[_UIUpdateHIDInput addEvent:];
-[_UIUpdateHIDInput stopEventForModelTime:alignment:];
```
