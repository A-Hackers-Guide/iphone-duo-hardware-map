# `_SBMockSensorAttribution`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFSensorActivityAttribution`
- 10 instance variables, 14 properties, 11 instance methods, 2 class methods

## Instance variables

```
B _usedRecently;
B _isSystemService;
@"NSString" _bundleIdentifier;
q _sensor;
@"NSString" _activeEntityBundleIdentifier;
@"NSString" _executableDisplayName;
@"NSString" _website;
@"NSString" _displayName;
@"NSString" _cameraIdentifier;
@"NSString" _attributionGroup;
```

## Properties

```
@property (T@"NSString",R,C,N,V_displayName) displayName;
@property (T@"NSString",R,C,N,V_bundleIdentifier) bundleIdentifier;
@property (Tq,R,N,V_sensor) sensor;
@property (T@"NSString",R,C,N,V_cameraIdentifier) cameraIdentifier;
@property (T@"NSString",R,C,N,V_attributionGroup) attributionGroup;
@property (T@"NSString",R,C,N,V_website) website;
@property (TB,R,N,V_isSystemService) isSystemService;
@property (TB,R,N,V_usedRecently) usedRecently;
@property (T@"NSString",R,C,N,V_activeEntityBundleIdentifier) activeEntityBundleIdentifier;
@property (T@"NSString",R,C,N,V_executableDisplayName) executableDisplayName;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_SBMockSensorAttribution attributionForBundleIdentifier:sensor:];
+[_SBMockSensorAttribution cameraAttributionForBundleIdentifier:];
```

## Instance methods

```
-[_SBMockSensorAttribution website];
-[_SBMockSensorAttribution displayName];
-[_SBMockSensorAttribution usedRecently];
-[_SBMockSensorAttribution bundleIdentifier];
-[_SBMockSensorAttribution sensor];
-[_SBMockSensorAttribution cameraIdentifier];
-[_SBMockSensorAttribution isSystemService];
-[_SBMockSensorAttribution copyWithZone:];
-[_SBMockSensorAttribution activeEntityBundleIdentifier];
-[_SBMockSensorAttribution attributionGroup];
-[_SBMockSensorAttribution executableDisplayName];
```
