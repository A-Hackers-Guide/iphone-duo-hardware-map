# `CAFStatusIndicators`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFAccessory`
- 0 instance variables, 18 properties, 22 instance methods, 2 class methods

## Properties

```
@property (T@"NSArray",R,N) statusItemServices;
@property (T@"NSArray",R,N) deepLinkStatusItemServices;
@property (T@"NSArray",R,N) buttonActionStatusItemServices;
@property (T@"CAFWiFiStatus",R,N) wiFiStatusService;
@property (T@"CAFBluetoothStatus",R,N) bluetoothStatusService;
@property (T@"CAFCellularStatus",R,N) cellularStatusService;
@property (T@"CAFCurrentUserStatus",R,N) currentUserStatusService;
@property (T@"CAFActivityIndicator",R,N) activityIndicatorService;
@property (T@"NSArray",R,N) wirelessChargerStatusServices;
@property (T@"NSArray",R,N) statusItems;
@property (T@"NSArray",R,N) deepLinkStatusItems;
@property (T@"NSArray",R,N) buttonActionStatusItems;
@property (T@"CAFWiFiStatus",R,N) wiFiStatus;
@property (T@"CAFBluetoothStatus",R,N) bluetoothStatus;
@property (T@"CAFCellularStatus",R,N) cellularStatus;
@property (T@"CAFCurrentUserStatus",R,N) currentUserStatus;
@property (T@"CAFActivityIndicator",R,N) activityIndicator;
@property (T@"NSArray",R,N) wirelessChargerStatuss;
```

## Class methods

```
+[CAFStatusIndicators accessoryIdentifier];
+[CAFStatusIndicators observerProtocol];
```

## Instance methods

```
-[CAFStatusIndicators removeObserver:];
-[CAFStatusIndicators activityIndicator];
-[CAFStatusIndicators addObserver:];
-[CAFStatusIndicators registerObserver:];
-[CAFStatusIndicators unregisterObserver:];
-[CAFStatusIndicators statusItems];
-[CAFStatusIndicators bluetoothStatus];
-[CAFStatusIndicators activityIndicatorService];
-[CAFStatusIndicators bluetoothStatusService];
-[CAFStatusIndicators buttonActionStatusItemServices];
-[CAFStatusIndicators buttonActionStatusItems];
-[CAFStatusIndicators cellularStatus];
-[CAFStatusIndicators cellularStatusService];
-[CAFStatusIndicators currentUserStatus];
-[CAFStatusIndicators currentUserStatusService];
-[CAFStatusIndicators deepLinkStatusItemServices];
-[CAFStatusIndicators deepLinkStatusItems];
-[CAFStatusIndicators statusItemServices];
-[CAFStatusIndicators wiFiStatus];
-[CAFStatusIndicators wiFiStatusService];
-[CAFStatusIndicators wirelessChargerStatusServices];
-[CAFStatusIndicators wirelessChargerStatuss];
```
