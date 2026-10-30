# `WiFiPolicyNetworkActivity`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 0 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_nw_activity>" _activity;
q _state;
q _parentLabel;
@"NSObject<OS_nw_activity>" _parentActivity;
@"NSMutableSet" _connections;
B _hasStarted;
@"NSObject<OS_dispatch_source>" _activityTimer;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Instance methods

```
-[WiFiPolicyNetworkActivity nwActivity];
-[WiFiPolicyNetworkActivity setHasStarted:];
-[WiFiPolicyNetworkActivity initWithLabel:parent:];
-[WiFiPolicyNetworkActivity _networkActivityAbort];
-[WiFiPolicyNetworkActivity _cancelActivityTimer];
-[WiFiPolicyNetworkActivity hasStarted];
-[WiFiPolicyNetworkActivity _startActivityTimer];
-[WiFiPolicyNetworkActivity activate];
-[WiFiPolicyNetworkActivity addConnection:];
-[WiFiPolicyNetworkActivity _startMaxActivityLifetime];
-[WiFiPolicyNetworkActivity stopWithCompletionReason:withClientMetric:withClientDict:andError:];
-[WiFiPolicyNetworkActivity _networkActivityState:];
-[WiFiPolicyNetworkActivity description];
-[WiFiPolicyNetworkActivity parentLabel];
-[WiFiPolicyNetworkActivity removeConnection:];
-[WiFiPolicyNetworkActivity nwActivityToken];
-[WiFiPolicyNetworkActivity _networkActivityRestart];
-[WiFiPolicyNetworkActivity getState];
-[WiFiPolicyNetworkActivity setQueue:];
```
