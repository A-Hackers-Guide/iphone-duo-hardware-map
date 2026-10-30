# `AAProximityPairingPayload`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AAAdvertisementPayload`
- 2 instance variables, 2 properties, 4 instance methods, 1 class methods

## Instance variables

```
C _subType;
S _pid;
```

## Properties

```
@property (TC,R,V_subType) subType;
@property (TS,R,V_pid) pid;
```

## Class methods

```
+[AAProximityPairingPayload proximityPairingPayloadWithData:];
```

## Instance methods

```
-[AAProximityPairingPayload pid];
-[AAProximityPairingPayload subType];
-[AAProximityPairingPayload initWithData:];
-[AAProximityPairingPayload describeProperties];
```
