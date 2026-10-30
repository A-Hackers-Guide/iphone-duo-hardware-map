# `SBDisplayPortObserver`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 7 properties, 22 instance methods, 0 class methods

## Instance variables

```
B _matchingNotificationsStarted;
I _ioServiceAddedIterator;
@"<SBDisplayPortObserverDelegate>" _delegate;
@"NSObject<OS_dispatch_queue>" _queue;
^{IONotificationPort=} _ioNotificationPort;
@"NSMutableDictionary" _transportNotifiers;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T^{IONotificationPort=},N,SsetIONotificationPort:,V_ioNotificationPort) ioNotificationPort;
@property (TI,N,V_ioServiceAddedIterator) ioServiceAddedIterator;
@property (TB,N,V_matchingNotificationsStarted) matchingNotificationsStarted;
@property (T@"NSMutableDictionary",&,N,V_transportNotifiers) transportNotifiers;
@property (T@"<SBDisplayPortObserverDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N,GisDisplayPortConnected) displayPortConnected;
```

## Instance methods

```
-[SBDisplayPortObserver init];
-[SBDisplayPortObserver dealloc];
-[SBDisplayPortObserver queue];
-[SBDisplayPortObserver setDelegate:];
-[SBDisplayPortObserver delegate];
-[SBDisplayPortObserver _notifyDelegate];
-[SBDisplayPortObserver setQueue:];
-[SBDisplayPortObserver _addTransportNotificationForService:andRegistryEntryID:];
-[SBDisplayPortObserver _handleNotificationForService:messageType:messageArgument:];
-[SBDisplayPortObserver _handleServiceAdded:];
-[SBDisplayPortObserver _removeTransportNotificationForRegistryEntryID:];
-[SBDisplayPortObserver ioNotificationPort];
-[SBDisplayPortObserver ioServiceAddedIterator];
-[SBDisplayPortObserver isDisplayPortConnected];
-[SBDisplayPortObserver matchingNotificationsStarted];
-[SBDisplayPortObserver setIONotificationPort:];
-[SBDisplayPortObserver setIoServiceAddedIterator:];
-[SBDisplayPortObserver setMatchingNotificationsStarted:];
-[SBDisplayPortObserver setTransportNotifiers:];
-[SBDisplayPortObserver startMatchingNotifications];
-[SBDisplayPortObserver stopMatchingNotifications];
-[SBDisplayPortObserver transportNotifiers];
```
