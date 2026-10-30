# `WFScanManagerScanProxy` (protocol)

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 3 properties, 7 instance methods, 0 class methods

## Properties

```
@property (Td,R,N) scanInterval;
@property (TB,R,N,GisScanningAllowed) scanningAllowed;
@property (T@"NSArray",R,N) scannableChannels;
```

## Instance methods

```
-[WFScanManagerScanProxy stopUIScan];
-[WFScanManagerScanProxy startUIScanWithReply:];
-[WFScanManagerScanProxy scanInterval];
-[WFScanManagerScanProxy initiateNoNetworksSoftError];
-[WFScanManagerScanProxy isScanningAllowed];
-[WFScanManagerScanProxy performScanWithRequest:reply:];
-[WFScanManagerScanProxy scannableChannels];
```
