# `WFDiagnosticsManager`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"W5Client" _client;
@"NSArray" _customTestRequests;
@"NSArray" _noInternetTestRequests;
```

## Properties

```
@property (T@"W5Client",&,N,V_client) client;
@property (T@"NSArray",&,N,V_customTestRequests) customTestRequests;
@property (T@"NSArray",&,N,V_noInternetTestRequests) noInternetTestRequests;
```

## Instance methods

```
-[WFDiagnosticsManager init];
-[WFDiagnosticsManager setClient:];
-[WFDiagnosticsManager client];
-[WFDiagnosticsManager _joinFailureDiagnosticsResultFromW5Results:];
-[WFDiagnosticsManager _noInternetDiagnosticsResultFromW5Results:];
-[WFDiagnosticsManager customTestRequests];
-[WFDiagnosticsManager initWithCustomTests:];
-[WFDiagnosticsManager joinFailureTestRequestsFor:];
-[WFDiagnosticsManager noInternetTestRequests];
-[WFDiagnosticsManager runCustomDiagnosticsFor:withUpdate:result:];
-[WFDiagnosticsManager runJoinFailureDiagnosticsFor:withUpdate:result:];
-[WFDiagnosticsManager runNoInternetDiagnosticsFor:withUpdate:result:];
-[WFDiagnosticsManager setCustomTestRequests:];
-[WFDiagnosticsManager setNoInternetTestRequests:];
```
