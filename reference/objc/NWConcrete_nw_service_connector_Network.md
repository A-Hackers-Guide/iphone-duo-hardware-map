# `NWConcrete_nw_service_connector`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_service_connector`
- 23 instance variables, 4 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_nw_listener>" listener;
I state;
@"NSObject<OS_nw_parameters>" clientParameters;
@"NSObject<OS_dispatch_queue>" serviceConnectorQueue;
Q uniqueID;
S localPortHBO;
C retryCounterForAddressInUse;
^v retryAddrInUseTimer;
@? serviceAvailableBlock;
@"NSObject<OS_nw_array>" pendingUnverifiedIncomingRequests;
@"NSObject<OS_nw_dictionary>" pendingIncomingRequests;
@"NSObject<OS_nw_dictionary>" activeConnections;
@"NSObject<OS_nw_dictionary>" activeOutgoingRequests;
@"NSObject<OS_xpc_object>" remotePubKeys;
@"NSObject<OS_nw_array>" activeBrowsers;
@"NSObject<OS_nw_dictionary>" activeListeners;
@"NSObject<OS_nw_array>" activeConnectionGroups;
@"NSObject<OS_nw_endpoint>" endpoint;
^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v} localPrivKey;
[32C] localPubKey;
b1 useLargeUUIDForTesting;
b1 failConnectionAfterVerificationFailsForTesting;
b1 failConnectionAfterVerificationPassesForTesting;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[NWConcrete_nw_service_connector init];
-[NWConcrete_nw_service_connector dealloc];
-[NWConcrete_nw_service_connector description];
```
