# `CTQuickSwitchDeviceInfo`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 1 instance variables, 3 properties, 12 instance methods, 2 class methods

## Instance variables

```
@"CTDeviceIdentifier" _deviceID;
```

## Properties

```
@property (T@"CTDeviceIdentifier",&,V_deviceID) deviceID;
@property (T@"NSString",R) deviceName;
@property (T@"NSString",R) modelName;
```

## Class methods

```
+[CTQuickSwitchDeviceInfo supportsSecureCoding];
+[CTQuickSwitchDeviceInfo deviceInfoFromDictionary:];
```

## Instance methods

```
-[CTQuickSwitchDeviceInfo toDictionary];
-[CTQuickSwitchDeviceInfo deviceID];
-[CTQuickSwitchDeviceInfo setDeviceID:];
-[CTQuickSwitchDeviceInfo encodeWithCoder:];
-[CTQuickSwitchDeviceInfo hash];
-[CTQuickSwitchDeviceInfo description];
-[CTQuickSwitchDeviceInfo initWithCoder:];
-[CTQuickSwitchDeviceInfo copyWithZone:];
-[CTQuickSwitchDeviceInfo isEqual:];
-[CTQuickSwitchDeviceInfo deviceName];
-[CTQuickSwitchDeviceInfo modelName];
-[CTQuickSwitchDeviceInfo initWithDeviceName:modelName:bleDeviceId:eid:serialNumber:];
```
