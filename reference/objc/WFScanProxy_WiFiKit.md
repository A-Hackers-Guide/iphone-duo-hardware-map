# `WFScanProxy`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WFScanManagerScanProxy`
- 1 instance variables, 4 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"WFClient" _client;
```

## Properties

```
@property (T@"WFClient",&,N,V_client) client;
@property (Td,R,N) scanInterval;
@property (TB,R,N,GisScanningAllowed) scanningAllowed;
@property (T@"NSArray",R,N) scannableChannels;
```

## Class methods

```
+[WFScanProxy scanProxyWithClient:];
```

## Instance methods

```
-[WFScanProxy stopUIScan];
-[WFScanProxy startUIScanWithReply:];
-[WFScanProxy scanInterval];
-[WFScanProxy initWithClient:];
-[WFScanProxy setClient:];
-[WFScanProxy client];
-[WFScanProxy initiateNoNetworksSoftError];
-[WFScanProxy isChannel6GHzPSC:];
-[WFScanProxy isScanningAllowed];
-[WFScanProxy performScanWithRequest:reply:];
-[WFScanProxy scannableChannels];
```
