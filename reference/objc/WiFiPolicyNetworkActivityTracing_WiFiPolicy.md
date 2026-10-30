# `WiFiPolicyNetworkActivityTracing`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMutableDictionary" _activities;
@"NSMutableSet" _connections;
```

## Class methods

```
+[WiFiPolicyNetworkActivityTracing sharedNetworkActivityTracing];
```

## Instance methods

```
-[WiFiPolicyNetworkActivityTracing init];
-[WiFiPolicyNetworkActivityTracing _networkActivityStart:activate:];
-[WiFiPolicyNetworkActivityTracing _networkActivityActivate:];
-[WiFiPolicyNetworkActivityTracing _networkActivityAddNWConnection:toActivityWithLabel:];
-[WiFiPolicyNetworkActivityTracing _networkActivityRemoveNWConnection:fromActivityWithLabel:completion:];
-[WiFiPolicyNetworkActivityTracing _networkActivityStop:withReason:withClientMetric:withClientDict:andError:];
-[WiFiPolicyNetworkActivityTracing _networkActivityTracingCancel];
-[WiFiPolicyNetworkActivityTracing currentNetworkActivityTokenWithCompletion:];
-[WiFiPolicyNetworkActivityTracing hasActivitiesRunning];
-[WiFiPolicyNetworkActivityTracing networkActivityActivate:];
-[WiFiPolicyNetworkActivityTracing networkActivityAddNWConnection:toActivityWithLabel:];
-[WiFiPolicyNetworkActivityTracing networkActivityRemoveNWConnection:fromActivityWithLabel:completion:];
-[WiFiPolicyNetworkActivityTracing networkActivityStart:activate:];
-[WiFiPolicyNetworkActivityTracing networkActivityStop:withReason:withClientMetric:withClientDict:andError:];
-[WiFiPolicyNetworkActivityTracing networkActivityTracingCompleteConnectionsActivities];
```
