# `_TtC7WiFiKit12StateMonitor`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_TtP7WiFiKit21StateMonitorInterface_`
- 7 instance variables, 2 properties, 12 instance methods, 0 class methods

## Instance variables

```
_$sSo12CWFInterfaceC interface;
WiFiKit.CellularOutrank cellularOutrank;
WiFiKit.WiFiState _state;
WiFiKit.LinkQuality ? _linkQuality;
DispatchQueue stateQueue;
_$sSo9OS_os_logC logger;
WiFiKit.WiFiState _$s_AAtcSg -> handler;
```

## Properties

```
@property (Tq,N,R) stateRawValue;
@property (T@"_TtC7WiFiKit11LinkQuality",N,R) linkQuality;
```

## Instance methods

```
-[_TtC7WiFiKit12StateMonitor isPowerModificationDisabled];
-[_TtC7WiFiKit12StateMonitor init];
-[_TtC7WiFiKit12StateMonitor dealloc];
-[_TtC7WiFiKit12StateMonitor setUserAutoJoinState:completion:];
-[_TtC7WiFiKit12StateMonitor initWithHandler:];
-[_TtC7WiFiKit12StateMonitor linkQuality];
-[_TtC7WiFiKit12StateMonitor stateDescription];
-[_TtC7WiFiKit12StateMonitor disassociate:];
-[_TtC7WiFiKit12StateMonitor disableCellularOutrank:];
-[_TtC7WiFiKit12StateMonitor disableMISStateAndDiscovery:];
-[_TtC7WiFiKit12StateMonitor setPowerToggle:completion:];
-[_TtC7WiFiKit12StateMonitor stateRawValue];
```
