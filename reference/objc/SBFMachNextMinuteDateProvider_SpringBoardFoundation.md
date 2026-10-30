# `SBFMachNextMinuteDateProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFDateProviding`
- 6 instance variables, 5 properties, 6 instance methods, 0 class methods

## Instance variables

```
Q _nextToken;
B _hasMachTimer;
i _clockSetNotifyToken;
@"UIView" _referenceView;
@"NSMutableDictionary" _minuteHandlers;
{_SBFMachTimer="machPort"I"cfPort"^{__CFMachPort}"runloopSource"^{__CFRunLoopSource}"callback"^?"callbackContext"^v} _machTimer;
```

## Properties

```
@property (Td,?,N) additionalOffset;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFMachNextMinuteDateProvider dealloc];
-[SBFMachNextMinuteDateProvider date];
-[SBFMachNextMinuteDateProvider initWithReferenceView:];
-[SBFMachNextMinuteDateProvider observeMinuteUpdatesWithHandler:];
-[SBFMachNextMinuteDateProvider removeMinuteUpdateHandler:];
-[SBFMachNextMinuteDateProvider _onMachTimer];
```
