# `CTLocalDevice`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"CTDeviceIdentifier" _deviceID;
@"NSArray" _installedPlans;
```

## Properties

```
@property (T@"CTDeviceIdentifier",&,N,V_deviceID) deviceID;
@property (T@"NSArray",&,N,V_installedPlans) installedPlans;
```

## Class methods

```
+[CTLocalDevice supportsSecureCoding];
```

## Instance methods

```
-[CTLocalDevice init];
-[CTLocalDevice deviceID];
-[CTLocalDevice deviceType];
-[CTLocalDevice setDeviceID:];
-[CTLocalDevice encodeWithCoder:];
-[CTLocalDevice description];
-[CTLocalDevice initWithCoder:];
-[CTLocalDevice isEqual:];
-[CTLocalDevice deviceName];
-[CTLocalDevice EID];
-[CTLocalDevice installedPlans];
-[CTLocalDevice setInstalledPlans:];
```
