# `WFMobileWiFiStateMonitor`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 16 instance methods, 0 class methods

## Instance variables

```
q _state;
@? _handler;
^{__WiFiManagerClient=} _manager;
^{__WiFiDeviceClient=} _device;
@"WFLinkQuality" _linkQuality;
```

## Properties

```
@property (Tq,N,V_state) state;
@property (T^{__WiFiManagerClient=},N,V_manager) manager;
@property (T^{__WiFiDeviceClient=},N,V_device) device;
@property (T@"WFLinkQuality",&,N,V_linkQuality) linkQuality;
@property (T@?,C,V_handler) handler;
```

## Instance methods

```
-[WFMobileWiFiStateMonitor startMonitoring];
-[WFMobileWiFiStateMonitor _updateState];
-[WFMobileWiFiStateMonitor setState:];
-[WFMobileWiFiStateMonitor setDevice:];
-[WFMobileWiFiStateMonitor _updateWithDeviceAttachment:];
-[WFMobileWiFiStateMonitor device];
-[WFMobileWiFiStateMonitor setManager:];
-[WFMobileWiFiStateMonitor dealloc];
-[WFMobileWiFiStateMonitor setHandler:];
-[WFMobileWiFiStateMonitor setLinkQuality:];
-[WFMobileWiFiStateMonitor manager];
-[WFMobileWiFiStateMonitor stopMonitoring];
-[WFMobileWiFiStateMonitor initWithHandler:];
-[WFMobileWiFiStateMonitor linkQuality];
-[WFMobileWiFiStateMonitor handler];
-[WFMobileWiFiStateMonitor state];
```
