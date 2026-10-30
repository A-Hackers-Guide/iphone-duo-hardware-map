# `CWFNetworkDenyListItem`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 5 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _denyListMetrics;
B _enterprisePolicy;
@"CWFScanResult" _scanResultForNetworkDenyListItem;
@"NSMutableArray" _denyListTriggers;
@"NSMutableArray" _statesCurrent;
@"NSMutableArray" _statesHistory;
```

## Properties

```
@property (T@"CWFScanResult",&,V_scanResultForNetworkDenyListItem) scanResultForNetworkDenyListItem;
@property (T@"NSMutableArray",&,V_denyListTriggers) denyListTriggers;
@property (T@"NSMutableArray",&,V_statesCurrent) statesCurrent;
@property (T@"NSMutableArray",&,V_statesHistory) statesHistory;
@property (TB,V_enterprisePolicy) enterprisePolicy;
```

## Instance methods

```
-[CWFNetworkDenyListItem dealloc];
-[CWFNetworkDenyListItem containsNetwork:];
-[CWFNetworkDenyListItem enterprisePolicy];
-[CWFNetworkDenyListItem setEnterprisePolicy:];
-[CWFNetworkDenyListItem updateNetwork:];
-[CWFNetworkDenyListItem processDenyListStateMetric:denyListRemove:denyListRemoveReason:];
-[CWFNetworkDenyListItem _copyCreateDenyListState:reason:reasonData:];
-[CWFNetworkDenyListItem addDenyListState:reason:reasonData:];
-[CWFNetworkDenyListItem addDenyListStateHistory:state:reason:reasonData:];
-[CWFNetworkDenyListItem addDenyListTrigger:reasonData:BSSID:];
-[CWFNetworkDenyListItem denyListTriggers];
-[CWFNetworkDenyListItem hasDenyListState:];
-[CWFNetworkDenyListItem initWithDenyListNetwork:];
-[CWFNetworkDenyListItem isEqualToDenyListScanResult:];
-[CWFNetworkDenyListItem processDenyListedBSSForMetrics];
-[CWFNetworkDenyListItem scanResultForNetworkDenyListItem];
-[CWFNetworkDenyListItem setDenyListTriggers:];
-[CWFNetworkDenyListItem setScanResultForNetworkDenyListItem:];
-[CWFNetworkDenyListItem setStatesCurrent:];
-[CWFNetworkDenyListItem setStatesHistory:];
-[CWFNetworkDenyListItem statesCurrent];
-[CWFNetworkDenyListItem statesHistory];
```
