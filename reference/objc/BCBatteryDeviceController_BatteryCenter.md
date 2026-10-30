# `BCBatteryDeviceController`

- Image: [`/System/Library/PrivateFrameworks/BatteryCenter.framework/BatteryCenter`](../userland/System__Library__PrivateFrameworks__BatteryCenter.framework__BatteryCenter.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BCBatteryDeviceObservable`
- 0 instance variables, 5 properties, 4 instance methods, 1 class methods

## Properties

```
@property (T@"NSArray",R,C,N) connectedDevices;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BCBatteryDeviceController _sharedPowerSourceController];
```

## Instance methods

```
-[BCBatteryDeviceController removeBatteryDeviceObserver:];
-[BCBatteryDeviceController connectedDevices];
-[BCBatteryDeviceController init];
-[BCBatteryDeviceController addBatteryDeviceObserver:queue:];
```
