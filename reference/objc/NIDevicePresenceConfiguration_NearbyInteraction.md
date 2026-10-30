# `NIDevicePresenceConfiguration`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NIConfiguration`
- 7 instance variables, 7 properties, 21 instance methods, 5 class methods

## Instance variables

```
B _cameraAssistanceEnabled;
Q _monitoringOption;
Q _allowedDevices;
@"NIRegionPredicate" _innerBoundary;
@"NIRegionPredicate" _outerBoundary;
@"NSArray" _monitoredRegions;
@"NIDiscoveryToken" _token;
```

## Properties

```
@property (TB,N,GisCameraAssistanceEnabled,V_cameraAssistanceEnabled) cameraAssistanceEnabled;
@property (TQ,V_monitoringOption) monitoringOption;
@property (TQ,V_allowedDevices) allowedDevices;
@property (T@"NIRegionPredicate",R,V_innerBoundary) innerBoundary;
@property (T@"NIRegionPredicate",R,V_outerBoundary) outerBoundary;
@property (T@"NSArray",R,V_monitoredRegions) monitoredRegions;
@property (T@"NIDiscoveryToken",R,V_token) token;
```

## Class methods

```
+[NIDevicePresenceConfiguration supportsSecureCoding];
+[NIDevicePresenceConfiguration _validateRegionPredicates:outer:];
+[NIDevicePresenceConfiguration _radiusFromDevicePresencePreset:];
+[NIDevicePresenceConfiguration _NIDevicePresenceMonitoringOptionToString:];
+[NIDevicePresenceConfiguration _validateRegionIsPreset:];
```

## Instance methods

```
-[NIDevicePresenceConfiguration setCameraAssistanceEnabled:];
-[NIDevicePresenceConfiguration setMonitoringOption:];
-[NIDevicePresenceConfiguration allowedDevices];
-[NIDevicePresenceConfiguration monitoredRegions];
-[NIDevicePresenceConfiguration innerBoundary];
-[NIDevicePresenceConfiguration outerBoundary];
-[NIDevicePresenceConfiguration descriptionInternal];
-[NIDevicePresenceConfiguration encodeWithCoder:];
-[NIDevicePresenceConfiguration initWithInnerBoundary:outerBoundary:monitoringOption:allowedDevices:error:];
-[NIDevicePresenceConfiguration _internalIsCameraAssistanceEnabled];
-[NIDevicePresenceConfiguration hash];
-[NIDevicePresenceConfiguration isCameraAssistanceEnabled];
-[NIDevicePresenceConfiguration description];
-[NIDevicePresenceConfiguration initWithCoder:];
-[NIDevicePresenceConfiguration initWithDiscoveryToken:regions:preferredUpdateRate:error:];
-[NIDevicePresenceConfiguration token];
-[NIDevicePresenceConfiguration monitoringOption];
-[NIDevicePresenceConfiguration copyWithZone:];
-[NIDevicePresenceConfiguration isEqual:];
-[NIDevicePresenceConfiguration initWithInnerBoundary:outerBoundary:error:];
-[NIDevicePresenceConfiguration setAllowedDevices:];
```
