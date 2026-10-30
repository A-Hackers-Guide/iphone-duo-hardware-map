# `BKHIDEventDeliveryManagerServer`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`](../userland/System__Library__PrivateFrameworks__BackBoardHIDEventFoundation.framework__BackBoardHIDEventFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKSHIDEventDeliveryManagerServerInterface`, `BKHIDDomainServiceDelegate`, `BKHIDDomainIncomingServiceConnectionHandler`, `_BKHIDIncomingServiceConnectionHandler`
- 4 instance variables, 6 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"BKHIDDomainServiceServer" _server;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"<BKHIDEventDeliveryManagerServerRuleChangeAuthority>" _ruleChangeAuthority;
@"<BKHIDEventDeliveryManagerIncomingServiceConnectionHandler>" _incomingServiceConnectionHandler;
```

## Properties

```
@property (T@"<BKHIDEventDeliveryManagerIncomingServiceConnectionHandler>",R,N) incomingConnectionHandler;
@property (T@"<BKHIDEventDeliveryManagerServerRuleChangeAuthority>",R,N) ruleChangeAuthority;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKHIDEventDeliveryManagerServer authenticationMessage:matchesDeferringNamespacePredicate:];
-[BKHIDEventDeliveryManagerServer connectionDidTerminate:];
-[BKHIDEventDeliveryManagerServer activate];
-[BKHIDEventDeliveryManagerServer connectionDescriptionForDeferringRuleIdentity:];
-[BKHIDEventDeliveryManagerServer deliveryChainsDescription];
-[BKHIDEventDeliveryManagerServer deliveryGraphDescription];
-[BKHIDEventDeliveryManagerServer resolutionDescriptionForEventDescriptor:senderDescriptor:];
-[BKHIDEventDeliveryManagerServer resolutionDescriptionForKeyCommand:senderDescriptor:];
-[BKHIDEventDeliveryManagerServer submitRuleChanges:];
-[BKHIDEventDeliveryManagerServer acceptIncomingServiceConnection:serviceQueue:clientCalloutContextualizer:];
-[BKHIDEventDeliveryManagerServer handleIncomingServiceConnection:];
-[BKHIDEventDeliveryManagerServer incomingConnectionHandler];
-[BKHIDEventDeliveryManagerServer initWithDeliveryManagerProvider:ruleChangeAuthority:];
-[BKHIDEventDeliveryManagerServer initWithIncomingServiceConnectionHandler:ruleChangeAuthority:];
-[BKHIDEventDeliveryManagerServer rejectIncomingServiceConnection:];
-[BKHIDEventDeliveryManagerServer ruleChangeAuthority];
```
