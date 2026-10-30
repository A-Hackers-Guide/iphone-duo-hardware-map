# `MLFeatureFlags`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSUserDefaults" _userDefaults;
@"NSMutableDictionary" _flags;
@"NSMutableDictionary" _overrideOriginalValues;
```

## Properties

```
@property (T@"NSUserDefaults",R,N,V_userDefaults) userDefaults;
@property (T@"NSMutableDictionary",R,N,V_flags) flags;
@property (T@"NSMutableDictionary",R,N,V_overrideOriginalValues) overrideOriginalValues;
```

## Class methods

```
+[MLFeatureFlags sharedFeatureFlags];
```

## Instance methods

```
-[MLFeatureFlags userDefaults];
-[MLFeatureFlags flags];
-[MLFeatureFlags init];
-[MLFeatureFlags isFeatureEnabled:];
-[MLFeatureFlags addFeature:withControlName:defaultValue:];
-[MLFeatureFlags controlKeyForFeature:];
-[MLFeatureFlags defineFeatures];
-[MLFeatureFlags isMPSGraphEnabled];
-[MLFeatureFlags isMPSGraphFP16Enabled];
-[MLFeatureFlags overrideOriginalValues];
-[MLFeatureFlags removeOverrideForFeature:];
-[MLFeatureFlags setOverride:forFeature:];
```
