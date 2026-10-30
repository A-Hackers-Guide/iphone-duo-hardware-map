# `LACDTOFeatureState` (protocol)

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 7 properties, 7 instance methods, 0 class methods

## Properties

```
@property (TB,R,N) isSupported;
@property (TB,R,N) isAvailable;
@property (TB,R,N) isEnabled;
@property (T@"<LACDTOFeatureEnablementMode>",R,N) enablementMode;
@property (TB,R,N) isStrictModeEnabled;
@property (TB,R,N) isExtendedPolicyProtectionAvailable;
@property (TB,R,N) isExtendedPolicyProtectionEnabled;
```

## Instance methods

```
-[LACDTOFeatureState isAvailable];
-[LACDTOFeatureState enablementMode];
-[LACDTOFeatureState isStrictModeEnabled];
-[LACDTOFeatureState isSupported];
-[LACDTOFeatureState isEnabled];
-[LACDTOFeatureState isExtendedPolicyProtectionEnabled];
-[LACDTOFeatureState isExtendedPolicyProtectionAvailable];
```
