# `NIHomeDeviceConfiguration`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NIConfiguration`
- 7 instance variables, 6 properties, 24 instance methods, 2 class methods

## Instance variables

```
@"NSArray" _monitoredRegions;
@"NSString" _regionDescription;
B _anchor;
Q _allowedDevices;
@"NSData" _sessionKey;
q _minimumPreferredUpdatedRate;
q _antennaDiversityOverride;
```

## Properties

```
@property (Tq,V_antennaDiversityOverride) antennaDiversityOverride;
@property (TQ,V_allowedDevices) allowedDevices;
@property (T@"NSData",C,V_sessionKey) sessionKey;
@property (TB,GisAnchor,V_anchor) anchor;
@property (T@"NSArray",C) monitoredRegions;
@property (Tq,V_minimumPreferredUpdatedRate) minimumPreferredUpdatedRate;
```

## Class methods

```
+[NIHomeDeviceConfiguration supportsSecureCoding];
+[NIHomeDeviceConfiguration new];
```

## Instance methods

```
-[NIHomeDeviceConfiguration setAnchor:];
-[NIHomeDeviceConfiguration allowedDevices];
-[NIHomeDeviceConfiguration monitoredRegions];
-[NIHomeDeviceConfiguration initWithAllowedDevices:sessionKey:asAnchor:regions:];
-[NIHomeDeviceConfiguration init];
-[NIHomeDeviceConfiguration descriptionInternal];
-[NIHomeDeviceConfiguration canUpdateToConfiguration:];
-[NIHomeDeviceConfiguration antennaDiversityOverride];
-[NIHomeDeviceConfiguration encodeWithCoder:];
-[NIHomeDeviceConfiguration _updateRegionDescription];
-[NIHomeDeviceConfiguration setAntennaDiversityOverride:];
-[NIHomeDeviceConfiguration hash];
-[NIHomeDeviceConfiguration setMonitoredRegions:];
-[NIHomeDeviceConfiguration description];
-[NIHomeDeviceConfiguration initWithCoder:];
-[NIHomeDeviceConfiguration minimumPreferredUpdatedRate];
-[NIHomeDeviceConfiguration setSessionKey:];
-[NIHomeDeviceConfiguration copyWithZone:];
-[NIHomeDeviceConfiguration setMinimumPreferredUpdatedRate:];
-[NIHomeDeviceConfiguration isAnchor];
-[NIHomeDeviceConfiguration isEqual:];
-[NIHomeDeviceConfiguration initWithRegions:];
-[NIHomeDeviceConfiguration sessionKey];
-[NIHomeDeviceConfiguration setAllowedDevices:];
```
