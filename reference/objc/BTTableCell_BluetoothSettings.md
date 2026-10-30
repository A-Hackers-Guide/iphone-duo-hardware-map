# `BTTableCell`

- Image: [`/System/Library/PreferenceBundles/BluetoothSettings.bundle/BluetoothSettings`](../userland/System__Library__PreferenceBundles__BluetoothSettings.bundle__BluetoothSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PSTableCell`
- 3 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _hasLimitedConnectivity;
i _state;
@"UIActivityIndicatorView" _spinner;
```

## Properties

```
@property (T@"UIActivityIndicatorView",&,N,V_spinner) spinner;
@property (Ti,N,V_state) state;
@property (TB,N,V_hasLimitedConnectivity) hasLimitedConnectivity;
```

## Instance methods

```
-[BTTableCell setState:];
-[BTTableCell initWithStyle:reuseIdentifier:specifier:];
-[BTTableCell dealloc];
-[BTTableCell layoutSubviews];
-[BTTableCell setDeviceState:];
-[BTTableCell setSpinner:];
-[BTTableCell spinner];
-[BTTableCell state];
-[BTTableCell hasLimitedConnectivity];
-[BTTableCell setDeviceStatePaired:andConnected:andPendingSetup:];
-[BTTableCell setHasLimitedConnectivity:];
```
