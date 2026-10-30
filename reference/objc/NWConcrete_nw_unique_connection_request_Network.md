# `NWConcrete_nw_unique_connection_request`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_unique_connection_request`
- 26 instance variables, 4 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_nw_endpoint>" endpoint;
@"NSObject<OS_nw_parameters>" userParameters;
[436c] service;
Q sequenceNumber;
Q uniqueID;
[16C] uuid;
[64C] signature;
* incomingReqBytesToVerify;
I incomingReqBytesToVerifyLen;
@"NWConcrete_nw_connection" connection;
@"NSObject<OS_nw_path_evaluator>" pathEvaluator;
@"NSObject<OS_nw_path_evaluator>" pathEvaluatorForPolicyAbort;
@? requestCompletionBlock;
^v rejectTimer;
^v preexistingConnectionTimer;
b1 isIncoming;
b1 isPending;
b1 pendingRequestAccepted;
b1 isWaitingForListenerReady;
b1 isWaitingForActiveConnection;
b1 hasRequestedPubKey;
b1 hasBeenProcessed;
b1 isWaitingForPathUpdate;
b1 retryImmediately;
b1 hasRetriedOnce;
b1 usesASQUIC;
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
-[NWConcrete_nw_unique_connection_request init];
-[NWConcrete_nw_unique_connection_request dealloc];
-[NWConcrete_nw_unique_connection_request description];
```
