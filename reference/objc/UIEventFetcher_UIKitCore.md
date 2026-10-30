# `UIEventFetcher`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 0 properties, 1 instance methods, 0 class methods

## Instance variables

```
@"<UIEventFetcherSink>" _eventFetcherSink;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _filteredHIDEventsLock;
@"NSMutableArray" _filteredHIDEvents;
@"NSMutableArray" _eventFilters;
@"NSMutableDictionary" _latestMoveDragEventsBySessionID;
@? _receiveBlock;
@? _gameControllerEventFilterGenerator;
@? _passiveObservationFilterGenerator;
@? _watchSystemAppFilter;
B _pendingDragMoveEventsResend;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMutableDictionary" _latestHoverEventsByContextID;
@"_UIHIDEventSynchronizer" _synchronizer;
```

## Instance methods

```
-[UIEventFetcher _receiveHIDEvent:];
```
