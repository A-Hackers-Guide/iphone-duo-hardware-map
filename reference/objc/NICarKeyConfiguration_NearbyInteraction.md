# `NICarKeyConfiguration`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NIConfiguration`
- 4 instance variables, 4 properties, 19 instance methods, 3 class methods

## Instance variables

```
q _configurationTypeInternal;
S _protocolVersion;
@"NSString" _vehicleIdentifier;
@"NSDictionary" _debugOptions;
```

## Properties

```
@property (Tq,R) configurationType;
@property (T@"NSString",C,V_vehicleIdentifier) vehicleIdentifier;
@property (TS,V_protocolVersion) protocolVersion;
@property (T@"NSDictionary",C,V_debugOptions) debugOptions;
```

## Class methods

```
+[NICarKeyConfiguration supportsSecureCoding];
+[NICarKeyConfiguration _labTestModeConfigurationWithOptions:];
+[NICarKeyConfiguration _vehicleSimConfigurationWithOptions:];
```

## Instance methods

```
-[NICarKeyConfiguration descriptionInternal];
-[NICarKeyConfiguration debugOptions];
-[NICarKeyConfiguration protocolVersion];
-[NICarKeyConfiguration initWithConfiguration:];
-[NICarKeyConfiguration configurationType];
-[NICarKeyConfiguration canUpdateToConfiguration:];
-[NICarKeyConfiguration setDebugOptions:];
-[NICarKeyConfiguration encodeWithCoder:];
-[NICarKeyConfiguration hash];
-[NICarKeyConfiguration description];
-[NICarKeyConfiguration initWithCoder:];
-[NICarKeyConfiguration setProtocolVersion:];
-[NICarKeyConfiguration copyWithZone:];
-[NICarKeyConfiguration isEqual:];
-[NICarKeyConfiguration setVehicleIdentifier:];
-[NICarKeyConfiguration vehicleIdentifier];
-[NICarKeyConfiguration initWithVehicleIdentifier:];
-[NICarKeyConfiguration initLabTestModeConfiguration:];
-[NICarKeyConfiguration initVehicleSimConfiguration:];
```
