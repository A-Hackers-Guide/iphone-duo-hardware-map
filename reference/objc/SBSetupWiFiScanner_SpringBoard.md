# `SBSetupWiFiScanner`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 3 properties, 14 instance methods, 0 class methods

## Instance variables

```
^{__WiFiManagerClient=} _wifiManager;
^{__WiFiDeviceClient=} _wifiDevice;
@"NSThread" _scanningThread;
@? _completionHandler;
q _state;
```

## Properties

```
@property (T@"NSThread",&,G_scanningThread,S_setScanningThread:,V_scanningThread) scanningThread;
@property (T@?,C,G_completionHandler,S_setCompletionHandler:,V_completionHandler) completionHandler;
@property (Tq,N,G_state,S_setState:,V_state) state;
```

## Instance methods

```
-[SBSetupWiFiScanner _state];
-[SBSetupWiFiScanner _setState:];
-[SBSetupWiFiScanner dealloc];
-[SBSetupWiFiScanner _setCompletionHandler:];
-[SBSetupWiFiScanner _completionHandler];
-[SBSetupWiFiScanner cancel];
-[SBSetupWiFiScanner _scanningThread];
-[SBSetupWiFiScanner _thread_wifiScanComplete:error:];
-[SBSetupWiFiScanner _setScanningThread:];
-[SBSetupWiFiScanner _thread_callCompletionHandlerWithGuessedCountries:];
-[SBSetupWiFiScanner _thread_cancelScanning];
-[SBSetupWiFiScanner _thread_closeWifiConnection];
-[SBSetupWiFiScanner _wifiScanningThread];
-[SBSetupWiFiScanner beginScanningWithCompletionHandler:];
```
