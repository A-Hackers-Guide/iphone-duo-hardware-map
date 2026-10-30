# `WFANQPQueryResponse`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"CWFScanResult" _scanResult;
@"NSArray" _cellNetworkInfo;
@"NSArray" _roamingConsortium;
@"NSArray" _domains;
@"NSString" _ssid;
@"NSString" _bssid;
@"NSString" _operatorName;
q _channel;
```

## Properties

```
@property (T@"NSArray",C,N,V_cellNetworkInfo) cellNetworkInfo;
@property (T@"NSArray",&,N,V_roamingConsortium) roamingConsortium;
@property (T@"NSArray",&,N,V_domains) domains;
@property (T@"CWFScanResult",C,N,V_scanResult) scanResult;
@property (T@"NSString",C,N,V_ssid) ssid;
@property (T@"NSString",C,N,V_bssid) bssid;
@property (T@"NSString",C,N,V_operatorName) operatorName;
@property (Tq,V_channel) channel;
```

## Instance methods

```
-[WFANQPQueryResponse setChannel:];
-[WFANQPQueryResponse ssid];
-[WFANQPQueryResponse setSsid:];
-[WFANQPQueryResponse channel];
-[WFANQPQueryResponse domains];
-[WFANQPQueryResponse setOperatorName:];
-[WFANQPQueryResponse operatorName];
-[WFANQPQueryResponse setBssid:];
-[WFANQPQueryResponse hash];
-[WFANQPQueryResponse description];
-[WFANQPQueryResponse bssid];
-[WFANQPQueryResponse isEqual:];
-[WFANQPQueryResponse setDomains:];
-[WFANQPQueryResponse scanResult];
-[WFANQPQueryResponse setScanResult:];
-[WFANQPQueryResponse cellNetworkInfo];
-[WFANQPQueryResponse initWithScanResult:ANQPResponse:];
-[WFANQPQueryResponse isEqualToWFANQPResponse:];
-[WFANQPQueryResponse roamingConsortium];
-[WFANQPQueryResponse setCellNetworkInfo:];
-[WFANQPQueryResponse setRoamingConsortium:];
```
