# `WiFiSettlementObserver`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 23 instance methods, 0 class methods

## Instance variables

```
q _status;
Q _confidence;
@"NSDate" _settledDate;
@"<WiFiScanProvider>" _scanProvider;
@"WiFiSettlementContext" _currentContext;
Q _consecutiveScansWithoutMatch;
@"NSMutableArray" _callbacks;
@"WiFiSettlementConfiguration" _configuration;
```

## Properties

```
@property (T@"<WiFiScanProvider>",&,N,V_scanProvider) scanProvider;
@property (T@"WiFiSettlementContext",&,N,V_currentContext) currentContext;
@property (TQ,N,V_consecutiveScansWithoutMatch) consecutiveScansWithoutMatch;
@property (T@"NSMutableArray",&,N,V_callbacks) callbacks;
@property (Tq,N,V_status) status;
@property (TQ,N,V_confidence) confidence;
@property (T@"WiFiSettlementConfiguration",&,N,V_configuration) configuration;
@property (T@"NSDate",C,N,V_settledDate) settledDate;
```

## Instance methods

```
-[WiFiSettlementObserver currentContext];
-[WiFiSettlementObserver setCallbacks:];
-[WiFiSettlementObserver setCurrentContext:];
-[WiFiSettlementObserver setConfiguration:];
-[WiFiSettlementObserver status];
-[WiFiSettlementObserver setScanProvider:];
-[WiFiSettlementObserver callbacks];
-[WiFiSettlementObserver setConfidence:];
-[WiFiSettlementObserver configuration];
-[WiFiSettlementObserver scanProvider];
-[WiFiSettlementObserver setStatus:];
-[WiFiSettlementObserver confidence];
-[WiFiSettlementObserver resetSettlement];
-[WiFiSettlementObserver setSettledDate:];
-[WiFiSettlementObserver _callSettlementCallbackWithStatus:userInfo:];
-[WiFiSettlementObserver _handleScanResults:error:userInfo:];
-[WiFiSettlementObserver _updateSettlementStatus:confidence:];
-[WiFiSettlementObserver addSettlementCallback:];
-[WiFiSettlementObserver consecutiveScansWithoutMatch];
-[WiFiSettlementObserver initWithScanProvider:configuration:];
-[WiFiSettlementObserver removeSettlementCallback:];
-[WiFiSettlementObserver setConsecutiveScansWithoutMatch:];
-[WiFiSettlementObserver settledDate];
```
