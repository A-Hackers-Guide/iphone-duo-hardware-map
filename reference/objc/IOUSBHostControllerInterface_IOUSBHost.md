# `IOUSBHostControllerInterface`

- Image: [`/System/Library/PrivateFrameworks/IOUSBHost.framework/IOUSBHost`](../userland/System__Library__PrivateFrameworks__IOUSBHost.framework__IOUSBHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 25 instance variables, 23 properties, 59 instance methods, 0 class methods

## Instance variables

```
@"NSData" _capabilitiesData;
[16@"IOUSBHostCIPortStateMachine"] _portStateMachine;
AB _destroyed;
B _interruptDeliveryPending;
I _ioConnect;
@"NSObject<OS_dispatch_queue>" _queue;
Q _interruptRateHz;
@"IOUSBHostCIControllerStateMachine" _controllerStateMachine;
r^{IOUSBHostCIMessage=IIQ} _capabilities;
@"NSUUID" _uuid;
Q _ioConnectAsyncPending;
^{IONotificationPort=} _notificationPortRef;
@? _commandHandler;
@? _doorbellHandler;
^? _interestHandler;
@"IOUSBHostInterestNotifier" _interestNotifier;
@"NSMutableData" _doorbells;
@"NSMutableData" _interrupts;
@"NSRecursiveLock" _interruptLock;
Q _interruptProducerIndex;
Q _interruptConsumerIndex;
@"NSObject<OS_dispatch_queue>" _interruptQueue;
Q _nextInterruptTime;
@"NSObject<OS_os_log>" _log;
{IOUSBHostCIMessage="control"I"data0"I"data1"Q} _command;
```

## Properties

```
@property (T@"IOUSBHostCIControllerStateMachine",&,N,V_controllerStateMachine) controllerStateMachine;
@property (Tr^{IOUSBHostCIMessage=IIQ},N,V_capabilities) capabilities;
@property (T@"NSUUID",&,N,V_uuid) uuid;
@property (TI,N,V_ioConnect) ioConnect;
@property (TQ,N,V_ioConnectAsyncPending) ioConnectAsyncPending;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T^{IONotificationPort=},N,V_notificationPortRef) notificationPortRef;
@property (T@?,C,N,V_commandHandler) commandHandler;
@property (T@?,C,N,V_doorbellHandler) doorbellHandler;
@property (T^?,N,V_interestHandler) interestHandler;
@property (T@"IOUSBHostInterestNotifier",&,N,V_interestNotifier) interestNotifier;
@property (T{IOUSBHostCIMessage=IIQ},V_command) command;
@property (T@"NSMutableData",&,N,V_doorbells) doorbells;
@property (T@"NSMutableData",&,N,V_interrupts) interrupts;
@property (T@"NSRecursiveLock",&,N,V_interruptLock) interruptLock;
@property (TQ,V_interruptProducerIndex) interruptProducerIndex;
@property (TQ,V_interruptConsumerIndex) interruptConsumerIndex;
@property (TB,V_interruptDeliveryPending) interruptDeliveryPending;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_interruptQueue) interruptQueue;
@property (TQ,V_nextInterruptTime) nextInterruptTime;
@property (TB,R,D) destroyed;
@property (T@"NSObject<OS_os_log>",&,N,V_log) log;
@property (TQ,N,V_interruptRateHz) interruptRateHz;
```

## Instance methods

```
-[IOUSBHostControllerInterface setLog:];
-[IOUSBHostControllerInterface commandHandler];
-[IOUSBHostControllerInterface uuid];
-[IOUSBHostControllerInterface destroy];
-[IOUSBHostControllerInterface dealloc];
-[IOUSBHostControllerInterface setUuid:];
-[IOUSBHostControllerInterface command];
-[IOUSBHostControllerInterface queue];
-[IOUSBHostControllerInterface capabilities];
-[IOUSBHostControllerInterface setCommandHandler:];
-[IOUSBHostControllerInterface log];
-[IOUSBHostControllerInterface setCapabilities:];
-[IOUSBHostControllerInterface setCommand:];
-[IOUSBHostControllerInterface setQueue:];
-[IOUSBHostControllerInterface destroyed];
-[IOUSBHostControllerInterface doorbellHandler];
-[IOUSBHostControllerInterface interestHandler];
-[IOUSBHostControllerInterface interruptRateHz];
-[IOUSBHostControllerInterface capabilitiesForPort:];
-[IOUSBHostControllerInterface commandAsyncCallbackWithResult:error:];
-[IOUSBHostControllerInterface controllerStateMachine];
-[IOUSBHostControllerInterface deliverInterrupts];
-[IOUSBHostControllerInterface descriptionForMessage:];
-[IOUSBHostControllerInterface doorbellAsyncCallbackWithResult:length:error:];
-[IOUSBHostControllerInterface doorbells];
-[IOUSBHostControllerInterface enqueueInterrupt:error:];
-[IOUSBHostControllerInterface enqueueInterrupt:expedite:error:];
-[IOUSBHostControllerInterface enqueueInterrupts:count:error:];
-[IOUSBHostControllerInterface enqueueInterrupts:count:expedite:error:];
-[IOUSBHostControllerInterface getPortStateMachineForCommand:error:];
-[IOUSBHostControllerInterface getPortStateMachineForPort:error:];
-[IOUSBHostControllerInterface initWithCapabilities:queue:interruptRateHz:error:commandHandler:doorbellHandler:interestHandler:];
-[IOUSBHostControllerInterface interestNotifier];
-[IOUSBHostControllerInterface interruptConsumerIndex];
-[IOUSBHostControllerInterface interruptDeliveryPending];
-[IOUSBHostControllerInterface interruptLock];
-[IOUSBHostControllerInterface interruptProducerIndex];
-[IOUSBHostControllerInterface interruptQueue];
-[IOUSBHostControllerInterface interrupts];
-[IOUSBHostControllerInterface ioConnect];
-[IOUSBHostControllerInterface ioConnectAsyncPending];
-[IOUSBHostControllerInterface nextInterruptTime];
-[IOUSBHostControllerInterface notificationPortRef];
-[IOUSBHostControllerInterface setControllerStateMachine:];
-[IOUSBHostControllerInterface setDoorbellHandler:];
-[IOUSBHostControllerInterface setDoorbells:];
-[IOUSBHostControllerInterface setInterestHandler:];
-[IOUSBHostControllerInterface setInterestNotifier:];
-[IOUSBHostControllerInterface setInterruptConsumerIndex:];
-[IOUSBHostControllerInterface setInterruptDeliveryPending:];
-[IOUSBHostControllerInterface setInterruptLock:];
-[IOUSBHostControllerInterface setInterruptProducerIndex:];
-[IOUSBHostControllerInterface setInterruptQueue:];
-[IOUSBHostControllerInterface setInterruptRateHz:];
-[IOUSBHostControllerInterface setInterrupts:];
-[IOUSBHostControllerInterface setIoConnect:];
-[IOUSBHostControllerInterface setIoConnectAsyncPending:];
-[IOUSBHostControllerInterface setNextInterruptTime:];
-[IOUSBHostControllerInterface setNotificationPortRef:];
```
