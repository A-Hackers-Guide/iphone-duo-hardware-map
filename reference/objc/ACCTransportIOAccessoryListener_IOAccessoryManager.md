# `ACCTransportIOAccessoryListener`

- Image: [`/System/Library/CoreAccessories/PlugIns/Transports/IOAccessoryManager.transport/IOAccessoryManager`](../userland/System__Library__CoreAccessories__PlugIns__Transports__IOAccessoryManager.transport__IOAccessoryManager.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 20 instance variables, 1 properties, 30 instance methods, 0 class methods

## Instance variables

```
^{IONotificationPort=} _ioAccessoryManagerClassNotify;
I _ioAccessoryManagerClassIteratorArrived;
I _ioAccessoryManagerClassIteratorTerminated;
^{IONotificationPort=} _ioAccessoryPortClassNotify;
I _ioAccessoryPortClassIteratorArrived;
I _ioAccessoryPortClassIteratorTerminated;
^{IONotificationPort=} _ioAccessoryAuthCPClassNotify;
I _ioAccessoryAuthCPClassIteratorArrived;
I _ioAccessoryAuthCPClassIteratorTerminated;
^{IONotificationPort=} _ioAccessoryEAClassNotify;
I _ioAccessoryEAClassIteratorArrived;
I _ioAccessoryEAClassIteratorTerminated;
^{IONotificationPort=} _ioAccessoryOOBPairingClassNotify;
I _ioAccessoryOOBPairingClassIteratorArrived;
I _ioAccessoryOOBPairingClassIteratorTerminated;
^{IONotificationPort=} _ioAccessoryConfigStreamClassNotify;
I _ioAccessoryConfigStreamClassIteratorArrived;
I _ioAccessoryConfigStreamClassIteratorTerminated;
@"NSObject<OS_dispatch_queue>" _ioAccessoryListenerQueue;
@"<ACCTransportIOAccessoryListenerProtocol>" _delegate;
```

## Properties

```
@property (T@"<ACCTransportIOAccessoryListenerProtocol>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[ACCTransportIOAccessoryListener initWithDelegate:];
-[ACCTransportIOAccessoryListener dealloc];
-[ACCTransportIOAccessoryListener setDelegate:];
-[ACCTransportIOAccessoryListener delegate];
-[ACCTransportIOAccessoryListener startListening];
-[ACCTransportIOAccessoryListener stopListening];
-[ACCTransportIOAccessoryListener _ioAccessoryOOBPairingAttached:];
-[ACCTransportIOAccessoryListener _ioAccessoryAuthCPAttached:];
-[ACCTransportIOAccessoryListener _ioAccessoryAuthCPTerminated:];
-[ACCTransportIOAccessoryListener _ioAccessoryConfigStreamAttached:];
-[ACCTransportIOAccessoryListener _ioAccessoryConfigStreamTerminated:];
-[ACCTransportIOAccessoryListener _ioAccessoryEAAttached:];
-[ACCTransportIOAccessoryListener _ioAccessoryEATerminated:];
-[ACCTransportIOAccessoryListener _ioAccessoryManagerAttached:];
-[ACCTransportIOAccessoryListener _ioAccessoryManagerTerminated:];
-[ACCTransportIOAccessoryListener _ioAccessoryOOBPairingTerminated:];
-[ACCTransportIOAccessoryListener _ioAccessoryPortAttached:];
-[ACCTransportIOAccessoryListener _ioAccessoryPortTerminated:];
-[ACCTransportIOAccessoryListener _startListeningForIOAccessoryAuthCPClass];
-[ACCTransportIOAccessoryListener _startListeningForIOAccessoryConfigStreamClass];
-[ACCTransportIOAccessoryListener _startListeningForIOAccessoryEAClass];
-[ACCTransportIOAccessoryListener _startListeningForIOAccessoryManagerClass];
-[ACCTransportIOAccessoryListener _startListeningForIOAccessoryOOBPairingClass];
-[ACCTransportIOAccessoryListener _startListeningForIOAccessoryPortClass];
-[ACCTransportIOAccessoryListener _stopListeningForIOAccessoryAuthCPClass];
-[ACCTransportIOAccessoryListener _stopListeningForIOAccessoryConfigStreamClass];
-[ACCTransportIOAccessoryListener _stopListeningForIOAccessoryEAClass];
-[ACCTransportIOAccessoryListener _stopListeningForIOAccessoryManagerClass];
-[ACCTransportIOAccessoryListener _stopListeningForIOAccessoryOOBPairingClass];
-[ACCTransportIOAccessoryListener _stopListeningForIOAccessoryPortClass];
```
