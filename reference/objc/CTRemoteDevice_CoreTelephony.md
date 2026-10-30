# `CTRemoteDevice`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 4 properties, 17 instance methods, 1 class methods

## Instance variables

```
B _isMultiESimEnabled;
@"CTDeviceIdentifier" _deviceID;
@"NSArray" _remoteDisplayPlans;
@"NSArray" _remotePlans;
```

## Properties

```
@property (T@"CTDeviceIdentifier",&,N,V_deviceID) deviceID;
@property (T@"NSArray",&,N,V_remoteDisplayPlans) remoteDisplayPlans;
@property (T@"NSArray",&,N,V_remotePlans) remotePlans;
@property (TB,N,V_isMultiESimEnabled) isMultiESimEnabled;
```

## Class methods

```
+[CTRemoteDevice supportsSecureCoding];
```

## Instance methods

```
-[CTRemoteDevice init];
-[CTRemoteDevice deviceID];
-[CTRemoteDevice deviceType];
-[CTRemoteDevice setDeviceID:];
-[CTRemoteDevice encodeWithCoder:];
-[CTRemoteDevice description];
-[CTRemoteDevice initWithCoder:];
-[CTRemoteDevice isEqual:];
-[CTRemoteDevice deviceName];
-[CTRemoteDevice modelName];
-[CTRemoteDevice EID];
-[CTRemoteDevice setRemotePlans:];
-[CTRemoteDevice isMultiESimEnabled];
-[CTRemoteDevice remoteDisplayPlans];
-[CTRemoteDevice remotePlans];
-[CTRemoteDevice setIsMultiESimEnabled:];
-[CTRemoteDevice setRemoteDisplayPlans:];
```
