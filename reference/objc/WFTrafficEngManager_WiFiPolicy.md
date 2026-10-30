# `WFTrafficEngManager`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 1 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _traffic_engr_queue;
@"RPCompanionLinkClient" _discoveryClient;
B _configured;
@"<WFTrafficEngDelegate>" _trafficEngDelegate;
```

## Properties

```
@property (T@"<WFTrafficEngDelegate>",N,V_trafficEngDelegate) trafficEngDelegate;
```

## Instance methods

```
-[WFTrafficEngManager cleanup];
-[WFTrafficEngManager dealloc];
-[WFTrafficEngManager __activateDiscovery];
-[WFTrafficEngManager __collectCriticalAppInfo];
-[WFTrafficEngManager __configureRapportDiscoveryClient];
-[WFTrafficEngManager __configureRapportSessionClient:];
-[WFTrafficEngManager __invalidateDiscovery];
-[WFTrafficEngManager __invalidateSession];
-[WFTrafficEngManager __registerCallbacksAndActivate];
-[WFTrafficEngManager __registerRequestHandler];
-[WFTrafficEngManager __requestCriticalAppInfo:completionBlock:];
-[WFTrafficEngManager __sendEventToPeers];
-[WFTrafficEngManager __sendKeepAliveEvent:dictionary:];
-[WFTrafficEngManager __sendPeriodicEvent:];
-[WFTrafficEngManager __tearDownRapportDataSession];
-[WFTrafficEngManager initWithTrafficEngDelegate:];
-[WFTrafficEngManager setTrafficEngDelegate:];
-[WFTrafficEngManager trafficEngDelegate];
```
