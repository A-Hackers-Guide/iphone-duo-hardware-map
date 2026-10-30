# `nw_listener_inbox`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSObject<nw_listener_inbox_delegate>" _delegate;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSString" _description;
@"NSObject<OS_nw_endpoint>" _local_endpoint;
@"NSObject<OS_nw_interface>" _interface;
@"NSObject<OS_nw_parameters>" _parameters;
i _level;
b1 _suspended;
B _multicast;
```

## Properties

```
@property (T@"NSObject<OS_nw_endpoint>",R,N,V_local_endpoint) local_endpoint;
@property (T@"NSObject<OS_nw_interface>",R,N,V_interface) interface;
@property (TB,N,V_multicast) multicast;
```

## Instance methods

```
-[nw_listener_inbox initWithDelegate:];
-[nw_listener_inbox isSuspended];
-[nw_listener_inbox suspend];
-[nw_listener_inbox start];
-[nw_listener_inbox interface];
-[nw_listener_inbox cancel];
-[nw_listener_inbox resume];
-[nw_listener_inbox local_endpoint];
-[nw_listener_inbox multicast];
-[nw_listener_inbox setMulticast:];
```
