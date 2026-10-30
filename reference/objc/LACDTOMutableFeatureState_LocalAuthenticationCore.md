# `LACDTOMutableFeatureState`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDTOFeatureState`
- 6 instance variables, 11 properties, 15 instance methods, 1 class methods

## Instance variables

```
B _isSupported;
B _isAvailable;
B _isStrictModeEnabled;
B _isExtendedPolicyProtectionAvailable;
B _isExtendedPolicyProtectionEnabled;
@"<LACDTOFeatureEnablementMode>" _enablementMode;
```

## Properties

```
@property (TB,N,V_isSupported) isSupported;
@property (TB,N,V_isAvailable) isAvailable;
@property (TB,R,N) isEnabled;
@property (T@"<LACDTOFeatureEnablementMode>",&,N,V_enablementMode) enablementMode;
@property (TB,N,V_isStrictModeEnabled) isStrictModeEnabled;
@property (TB,N,V_isExtendedPolicyProtectionAvailable) isExtendedPolicyProtectionAvailable;
@property (TB,N,V_isExtendedPolicyProtectionEnabled) isExtendedPolicyProtectionEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[LACDTOMutableFeatureState nullInstance];
```

## Instance methods

```
-[LACDTOMutableFeatureState isAvailable];
-[LACDTOMutableFeatureState enablementMode];
-[LACDTOMutableFeatureState isStrictModeEnabled];
-[LACDTOMutableFeatureState isSupported];
-[LACDTOMutableFeatureState setIsStrictModeEnabled:];
-[LACDTOMutableFeatureState isEnabled];
-[LACDTOMutableFeatureState setIsExtendedPolicyProtectionEnabled:];
-[LACDTOMutableFeatureState isExtendedPolicyProtectionEnabled];
-[LACDTOMutableFeatureState description];
-[LACDTOMutableFeatureState setIsSupported:];
-[LACDTOMutableFeatureState isExtendedPolicyProtectionAvailable];
-[LACDTOMutableFeatureState setEnablementMode:];
-[LACDTOMutableFeatureState setIsAvailable:];
-[LACDTOMutableFeatureState isEqual:];
-[LACDTOMutableFeatureState setIsExtendedPolicyProtectionAvailable:];
```
