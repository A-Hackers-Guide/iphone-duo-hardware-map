# `CAFCarConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAFCacheableDescription`, `NSSecureCoding`
- 13 instance variables, 17 properties, 32 instance methods, 5 class methods

## Instance variables

```
B _ultraEnabled;
B _rightHandDrive;
@"NSString" _name;
@"NSUUID" _uniqueIdentifier;
Q _vehicleType;
Q _pluginCount;
@"NSDictionary" _pluginConfigs;
@"CAFASCTree" _disabledASC;
@"NSDictionary" _pluginNameDictionary;
@"CAFCarAttributes" _attributes;
@"CAFCachedDescription" _cachedDescription;
@"CAFSessionAnalytics" _sessionAnalytics;
@"<CAFCarConfigurationDelegate>" _delegate;
```

## Properties

```
@property (T@"CAFCachedDescription",R,N,V_cachedDescription) cachedDescription;
@property (T@"CAFSessionAnalytics",R,N,V_sessionAnalytics) sessionAnalytics;
@property (T@"<CAFCarConfigurationDelegate>",W,N,V_delegate) delegate;
@property (T@"CAFASCTree",&,N,V_disabledASC) disabledASC;
@property (T@"CAFCarAttributes",&,N,V_attributes) attributes;
@property (T@"NSString",R,C,N,V_name) name;
@property (T@"NSUUID",R,C,N,V_uniqueIdentifier) uniqueIdentifier;
@property (TB,R,N,V_ultraEnabled) ultraEnabled;
@property (TB,R,N,V_rightHandDrive) rightHandDrive;
@property (TQ,R,N,V_vehicleType) vehicleType;
@property (TQ,R,N,V_pluginCount) pluginCount;
@property (T@"NSDictionary",R,C,N,V_pluginConfigs) pluginConfigs;
@property (T@"NSDictionary",R,N,V_pluginNameDictionary) pluginNameDictionary;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAFCarConfiguration supportsSecureCoding];
+[CAFCarConfiguration getBoolean:key:];
+[CAFCarConfiguration getType:];
+[CAFCarConfiguration getTypeString:];
+[CAFCarConfiguration getUUID:instanceID:];
```

## Instance methods

```
-[CAFCarConfiguration updateConfiguration:];
-[CAFCarConfiguration cachedDescription];
-[CAFCarConfiguration rightHandDrive];
-[CAFCarConfiguration vehicleType];
-[CAFCarConfiguration setAttributes:];
-[CAFCarConfiguration uniqueIdentifier];
-[CAFCarConfiguration setDelegate:];
-[CAFCarConfiguration encodeWithCoder:];
-[CAFCarConfiguration delegate];
-[CAFCarConfiguration description];
-[CAFCarConfiguration initWithCoder:];
-[CAFCarConfiguration attributes];
-[CAFCarConfiguration sessionAnalytics];
-[CAFCarConfiguration name];
-[CAFCarConfiguration isConfigured];
-[CAFCarConfiguration pluginCount];
-[CAFCarConfiguration setDisabledASC:];
-[CAFCarConfiguration _determineVehicleTypeFromSessionConfiguration:];
-[CAFCarConfiguration configureDisabledASCFromSessionConfig:featureDenyList:];
-[CAFCarConfiguration copyWithoutPlugins];
-[CAFCarConfiguration currentDescriptionForCache:];
-[CAFCarConfiguration disabledASC];
-[CAFCarConfiguration initWithIdentifier:session:];
-[CAFCarConfiguration initWithName:identifier:ultraEnabled:rightHandDrive:vehicleType:pluginCount:sessionAnalytics:pluginNameDictionary:];
-[CAFCarConfiguration pluginConfigs];
-[CAFCarConfiguration pluginNameDictionary];
-[CAFCarConfiguration pluginNameForIdentifier:];
-[CAFCarConfiguration ultraEnabled];
-[CAFCarConfiguration updateAttributes:];
-[CAFCarConfiguration updateCapabilitiesIfNeeded];
-[CAFCarConfiguration updateConfiguration:pluginConfig:];
-[CAFCarConfiguration updatePluginConfigs:];
```
