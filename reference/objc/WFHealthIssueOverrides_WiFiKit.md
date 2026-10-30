# `WFHealthIssueOverrides`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 20 instance methods, 0 class methods

## Instance variables

```
B _noInternetConnection;
B _hiddenNetwork;
B _commonSSID;
B _legacyPHY;
B _carrierNetwork;
B _dnsFiltered;
q _securityOverride;
q _privateAddressOverride;
q _cellularOutrankStateOverride;
q _poorCoverageOverride;
```

## Properties

```
@property (TB,N,V_noInternetConnection) noInternetConnection;
@property (TB,N,V_hiddenNetwork) hiddenNetwork;
@property (TB,N,V_commonSSID) commonSSID;
@property (TB,N,V_legacyPHY) legacyPHY;
@property (TB,N,V_carrierNetwork) carrierNetwork;
@property (TB,N,V_dnsFiltered) dnsFiltered;
@property (Tq,N,V_securityOverride) securityOverride;
@property (Tq,N,V_privateAddressOverride) privateAddressOverride;
@property (Tq,N,V_cellularOutrankStateOverride) cellularOutrankStateOverride;
@property (Tq,N,V_poorCoverageOverride) poorCoverageOverride;
```

## Instance methods

```
-[WFHealthIssueOverrides setDnsFiltered:];
-[WFHealthIssueOverrides setCarrierNetwork:];
-[WFHealthIssueOverrides setCommonSSID:];
-[WFHealthIssueOverrides setHiddenNetwork:];
-[WFHealthIssueOverrides setLegacyPHY:];
-[WFHealthIssueOverrides setNoInternetConnection:];
-[WFHealthIssueOverrides setPrivateAddressOverride:];
-[WFHealthIssueOverrides setSecurityOverride:];
-[WFHealthIssueOverrides carrierNetwork];
-[WFHealthIssueOverrides cellularOutrankStateOverride];
-[WFHealthIssueOverrides commonSSID];
-[WFHealthIssueOverrides dnsFiltered];
-[WFHealthIssueOverrides hiddenNetwork];
-[WFHealthIssueOverrides legacyPHY];
-[WFHealthIssueOverrides noInternetConnection];
-[WFHealthIssueOverrides poorCoverageOverride];
-[WFHealthIssueOverrides privateAddressOverride];
-[WFHealthIssueOverrides securityOverride];
-[WFHealthIssueOverrides setCellularOutrankStateOverride:];
-[WFHealthIssueOverrides setPoorCoverageOverride:];
```
