# `CTStewieDataClient`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CTStewieStateMonitorDelegate`, `CTConnectionPairDelegate`
- 11 instance variables, 4 properties, 15 instance methods, 0 class methods

## Instance variables

```
B fStarted;
@"NSObject<OS_dispatch_queue>" fQueue;
q fRequestedServices;
q fConnectedServices;
@"<CTStewieDataClientDelegate>" fDelegate;
@"NSObject<OS_dispatch_queue>" fDelegateQueue;
@"CTConnectionPair" fConnectionPair;
q fConnectionPairState;
@"CTStewieState" fState;
@"CTStewieStateMonitor" fMonitor;
{map<std::string, dispatch::block<void (^)(CTStewieMessageAck *, NSDictionary *)>, std::less<std::string>, std::allocator<std::pair<const std::string, dispatch::block<void (^)(CTStewieMessageAck *, NSDictionary *)>>>>="__tree_"{__tree<std::__value_type<std::string, dispatch::block<void (^)(CTStewieMessageAck *, NSDictionary *)>>, std::__map_value_compare<std::string, std::pair<const std::string, dispatch::block<void (^)(CTStewieMessageAck *, NSDictionary *)>>, std::less<std::string>>, std::allocator<std::pair<const std::string, dispatch::block<void (^)(CTStewieMessageAck *, NSDictionary *)>>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} fOutgoingMessages;
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
-[CTStewieDataClient sendMessage:completion:];
-[CTStewieDataClient invokeSendCompletionForMsgId:ack:metadata:];
-[CTStewieDataClient sendMessageInternal:usingConnection:completion:];
-[CTStewieDataClient failAllPendingMessages];
-[CTStewieDataClient start];
-[CTStewieDataClient connectionPairStateChanged:];
-[CTStewieDataClient receivedData:fromConnectionId:];
-[CTStewieDataClient stateChanged:];
-[CTStewieDataClient dispatchOnDelegateQueue:];
-[CTStewieDataClient reEvaluate];
-[CTStewieDataClient discardConnectionPairIfRequired];
-[CTStewieDataClient getState];
-[CTStewieDataClient updateConnectedServices:];
-[CTStewieDataClient initWithServices:delegate:delegateQueue:];
-[CTStewieDataClient createConnectionPairIfRequired];
```
