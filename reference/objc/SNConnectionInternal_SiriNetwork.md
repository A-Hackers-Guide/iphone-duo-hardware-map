# `SNConnectionInternal`

- Image: [`/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork`](../userland/System__Library__PrivateFrameworks__SiriNetwork.framework__SiriNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 1 properties, 16 instance methods, 0 class methods

## Instance variables

```
? delegate;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 connectionConfiguration;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 connectionQueue;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 activeConnectionGroup;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 activeBackgroundConnection;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 activeRoute;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 pendingBackgroundConnections;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 pendingRoutes;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 comatoseBackgroundConnections;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 comatoseRoutes;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 scheduledRoutes;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 isCanceled;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 isCanceledInternal;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 connectionMethodUsedHistory;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 networkManager;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 networkAnalytics;
```

## Properties

```
@property (T@"<SNConnectionDelegateInternal>",N,W,Vdelegate) delegate;
```

## Instance methods

```
-[SNConnectionInternal init];
-[SNConnectionInternal dealloc];
-[SNConnectionInternal startAndReturnError:];
-[SNConnectionInternal setDelegate:];
-[SNConnectionInternal delegate];
-[SNConnectionInternal probeConnection];
-[SNConnectionInternal setSendPings:];
-[SNConnectionInternal barrierWith:];
-[SNConnectionInternal cancelSynchronously:isOnConnectionQueue:with:];
-[SNConnectionInternal getSNConnectionAnalysisInfo:];
-[SNConnectionInternal getSNConnectionMetrics:with:];
-[SNConnectionInternal initWithConnectionInfo:connectionQueue:];
-[SNConnectionInternal initWithConnectionInfo:connectionQueue:networkManager:networkAnalytics:];
-[SNConnectionInternal sendCommand:with:];
-[SNConnectionInternal sendCommands:with:];
-[SNConnectionInternal sendData:with:];
```
