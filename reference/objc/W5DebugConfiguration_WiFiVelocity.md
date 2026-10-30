# `W5DebugConfiguration`

- Image: [`/System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity`](../userland/System__Library__PrivateFrameworks__WiFiVelocity.framework__WiFiVelocity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 7 instance variables, 7 properties, 23 instance methods, 1 class methods

## Instance variables

```
q _wifi;
q _megaWiFiProfile;
q _noLoggingWiFiProfile;
q _eapol;
q _bluetooth;
q _stbc;
@"W5DiagnosticsMode" _diagnosticsMode;
```

## Properties

```
@property (T@"W5DiagnosticsMode",&,N,V_diagnosticsMode) diagnosticsMode;
@property (Tq,N,V_wifi) wifi;
@property (Tq,N,V_megaWiFiProfile) megaWiFiProfile;
@property (Tq,N,V_noLoggingWiFiProfile) noLoggingWiFiProfile;
@property (Tq,N,V_eapol) eapol;
@property (Tq,N,V_bluetooth) bluetooth;
@property (Tq,N,V_stbc) stbc;
```

## Class methods

```
+[W5DebugConfiguration supportsSecureCoding];
```

## Instance methods

```
-[W5DebugConfiguration setWifi:];
-[W5DebugConfiguration setBluetooth:];
-[W5DebugConfiguration encodeWithCoder:];
-[W5DebugConfiguration hash];
-[W5DebugConfiguration description];
-[W5DebugConfiguration initWithCoder:];
-[W5DebugConfiguration wifi];
-[W5DebugConfiguration copyWithZone:];
-[W5DebugConfiguration isEqual:];
-[W5DebugConfiguration bluetooth];
-[W5DebugConfiguration diagnosticsMode];
-[W5DebugConfiguration megaWiFiProfile];
-[W5DebugConfiguration eapol];
-[W5DebugConfiguration initDiagnosticsMode:wifiState:megaWiFiProfileState:noLoggingWiFiProfileState:eapolState:bluetoothState:];
-[W5DebugConfiguration initDiagnosticsMode:wifiState:megaWiFiProfileState:noLoggingWiFiProfileState:eapolState:bluetoothState:stbcState:];
-[W5DebugConfiguration isEqualToDebugConfiguration:];
-[W5DebugConfiguration noLoggingWiFiProfile];
-[W5DebugConfiguration setDiagnosticsMode:];
-[W5DebugConfiguration setEapol:];
-[W5DebugConfiguration setMegaWiFiProfile:];
-[W5DebugConfiguration setNoLoggingWiFiProfile:];
-[W5DebugConfiguration setStbc:];
-[W5DebugConfiguration stbc];
```
