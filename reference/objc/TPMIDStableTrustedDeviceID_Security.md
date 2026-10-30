# `TPMIDStableTrustedDeviceID`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSString" _machineID;
@"TPStableTrustedDeviceID" _stableID;
```

## Properties

```
@property (T@"NSString",R,N,V_machineID) machineID;
@property (T@"TPStableTrustedDeviceID",R,N,V_stableID) stableID;
```

## Class methods

```
+[TPMIDStableTrustedDeviceID supportsSecureCoding];
```

## Instance methods

```
-[TPMIDStableTrustedDeviceID compare:];
-[TPMIDStableTrustedDeviceID machineID];
-[TPMIDStableTrustedDeviceID encodeWithCoder:];
-[TPMIDStableTrustedDeviceID hash];
-[TPMIDStableTrustedDeviceID description];
-[TPMIDStableTrustedDeviceID initWithCoder:];
-[TPMIDStableTrustedDeviceID isEqual:];
-[TPMIDStableTrustedDeviceID initWithMachineID:stableID:];
-[TPMIDStableTrustedDeviceID isEqualToMIDStableTrustedDeviceID:];
-[TPMIDStableTrustedDeviceID stableID];
```
