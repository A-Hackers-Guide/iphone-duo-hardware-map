# `LACSysUtility`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACSysUtilityType`
- 0 instance variables, 8 properties, 7 instance methods, 1 class methods

## Properties

```
@property (TB,R,N) hasPPL;
@property (TB,R,N) hasTXM;
@property (TB,R,N) hasCodeSigningMonitor;
@property (TQ,R,N) txmSecurityBootMode;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[LACSysUtility sharedInstance];
```

## Instance methods

```
-[LACSysUtility _getCodeSigningConfig];
-[LACSysUtility _getCodeSigningMonitorType];
-[LACSysUtility _hasCodeSigningMonitorOfType:];
-[LACSysUtility hasCodeSigningMonitor];
-[LACSysUtility hasPPL];
-[LACSysUtility hasTXM];
-[LACSysUtility txmSecurityBootMode];
```
