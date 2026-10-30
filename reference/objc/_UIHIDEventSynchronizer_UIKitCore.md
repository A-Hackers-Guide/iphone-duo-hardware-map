# `_UIHIDEventSynchronizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
Q _strategy;
q _state;
@? _outputEventsHandler;
@? _completionHandler;
@"NSObject<OS_dispatch_queue>" _queue;
{CGPoint="x"d"y"d} _initialPosition;
d _timestampOfInitialInputEvent;
@"_UIHIDPath" _outputPath;
@"_UIHIDPathCollection" _outputPathCollection;
@"_UIHIDPathSynchronizationFilter" _pathFilter;
q _endingDeliveryPhase;
@"_UIDisplayLinkOnDispatchQueue" _displayLink;
i _offsetToNextCoalescableEventIndex;
```

## Instance methods

```
-[_UIHIDEventSynchronizer dealloc];
-[_UIHIDEventSynchronizer _renderEvents:];
```
