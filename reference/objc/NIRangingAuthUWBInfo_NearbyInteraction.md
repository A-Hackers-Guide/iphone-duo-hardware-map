# `NIRangingAuthUWBInfo`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 5 instance variables, 8 properties, 25 instance methods, 0 class methods

## Instance variables

```
I _uwbMacAddress;
I _version;
Q _uwbSessionKey;
B _uwbAvailable;
{?="uwbMacAddress"b1"version"b1"uwbAvailable"b1"uwbSessionKey"b1} _has;
```

## Properties

```
@property (TB,N) hasVersion;
@property (TI,N,V_version) version;
@property (TB,N) hasUwbAvailable;
@property (TB,N,V_uwbAvailable) uwbAvailable;
@property (TB,N) hasUwbMacAddress;
@property (TI,N,V_uwbMacAddress) uwbMacAddress;
@property (TB,N) hasUwbSessionKey;
@property (TQ,N,V_uwbSessionKey) uwbSessionKey;
```

## Instance methods

```
-[NIRangingAuthUWBInfo hasVersion];
-[NIRangingAuthUWBInfo writeTo:];
-[NIRangingAuthUWBInfo mergeFrom:];
-[NIRangingAuthUWBInfo setHasVersion:];
-[NIRangingAuthUWBInfo version];
-[NIRangingAuthUWBInfo hash];
-[NIRangingAuthUWBInfo copyTo:];
-[NIRangingAuthUWBInfo description];
-[NIRangingAuthUWBInfo setVersion:];
-[NIRangingAuthUWBInfo readFrom:];
-[NIRangingAuthUWBInfo copyWithZone:];
-[NIRangingAuthUWBInfo isEqual:];
-[NIRangingAuthUWBInfo dictionaryRepresentation];
-[NIRangingAuthUWBInfo hasUwbAvailable];
-[NIRangingAuthUWBInfo hasUwbMacAddress];
-[NIRangingAuthUWBInfo hasUwbSessionKey];
-[NIRangingAuthUWBInfo setHasUwbAvailable:];
-[NIRangingAuthUWBInfo setHasUwbMacAddress:];
-[NIRangingAuthUWBInfo setHasUwbSessionKey:];
-[NIRangingAuthUWBInfo setUwbAvailable:];
-[NIRangingAuthUWBInfo setUwbMacAddress:];
-[NIRangingAuthUWBInfo setUwbSessionKey:];
-[NIRangingAuthUWBInfo uwbAvailable];
-[NIRangingAuthUWBInfo uwbMacAddress];
-[NIRangingAuthUWBInfo uwbSessionKey];
```
