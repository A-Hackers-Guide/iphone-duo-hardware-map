# `AAAccessoryFeatureFlagConfiguration`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 11 instance methods, 3 class methods

## Instance variables

```
@"NSString" _identifier;
@"NSMutableDictionary" _featureFlags;
B _routed;
```

## Properties

```
@property (T@"NSString",R,N,V_identifier) identifier;
@property (T@"NSDictionary",C,V_featureFlags) featureFlags;
@property (TB,N,V_routed) routed;
```

## Class methods

```
+[AAAccessoryFeatureFlagConfiguration supportsSecureCoding];
+[AAAccessoryFeatureFlagConfiguration createQueryMessage];
+[AAAccessoryFeatureFlagConfiguration createSetFeatureFlagMessage:];
```

## Instance methods

```
-[AAAccessoryFeatureFlagConfiguration identifier];
-[AAAccessoryFeatureFlagConfiguration encodeWithCoder:];
-[AAAccessoryFeatureFlagConfiguration initWithCoder:];
-[AAAccessoryFeatureFlagConfiguration setFeatureFlags:];
-[AAAccessoryFeatureFlagConfiguration initWithIdentifier:];
-[AAAccessoryFeatureFlagConfiguration featureFlags];
-[AAAccessoryFeatureFlagConfiguration routed];
-[AAAccessoryFeatureFlagConfiguration setRouted:];
-[AAAccessoryFeatureFlagConfiguration _applyConfigurationUpdate:];
-[AAAccessoryFeatureFlagConfiguration _isConfigurationUpdateMessageValid:];
-[AAAccessoryFeatureFlagConfiguration handleUpdate:];
```
