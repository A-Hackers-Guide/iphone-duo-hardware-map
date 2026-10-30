# `WFBlackListNode`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 5 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _blacklistMetrics;
B _enterprisePolicy;
@"<WFBlacklistNetwork>" _networkDelegate;
@"NSMutableArray" _blacklistTriggers;
@"NSMutableArray" _blacklistedStatesCurrent;
@"NSMutableArray" _blacklistedStatesHistory;
```

## Properties

```
@property (T@"<WFBlacklistNetwork>",&,V_networkDelegate) networkDelegate;
@property (T@"NSMutableArray",&,V_blacklistTriggers) blacklistTriggers;
@property (T@"NSMutableArray",&,V_blacklistedStatesCurrent) blacklistedStatesCurrent;
@property (T@"NSMutableArray",&,V_blacklistedStatesHistory) blacklistedStatesHistory;
@property (TB,V_enterprisePolicy) enterprisePolicy;
```

## Instance methods

```
-[WFBlackListNode networkDelegate];
-[WFBlackListNode dealloc];
-[WFBlackListNode setNetworkDelegate:];
-[WFBlackListNode _copyCreateBlacklistedState:reason:reasonData:];
-[WFBlackListNode addBlacklistTrigger:reasonData:bssid:];
-[WFBlackListNode addBlacklistedState:reason:reasonData:];
-[WFBlackListNode addBlacklistedStateHistory:state:reason:reasonData:];
-[WFBlackListNode blacklistTriggers];
-[WFBlackListNode blacklistedStatesCurrent];
-[WFBlackListNode blacklistedStatesHistory];
-[WFBlackListNode containsNetwork:];
-[WFBlackListNode enterprisePolicy];
-[WFBlackListNode hasBlacklistedState:];
-[WFBlackListNode initWithBlacklistNetwork:];
-[WFBlackListNode networkPruned];
-[WFBlackListNode processBlacklistedStateMetric:unblacklisting:unblacklistingReason:];
-[WFBlackListNode setBlacklistTriggers:];
-[WFBlackListNode setBlacklistedStatesCurrent:];
-[WFBlackListNode setBlacklistedStatesHistory:];
-[WFBlackListNode setEnterprisePolicy:];
-[WFBlackListNode updateNetwork:];
```
