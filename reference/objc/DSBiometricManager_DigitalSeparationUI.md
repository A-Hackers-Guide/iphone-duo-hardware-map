# `DSBiometricManager`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 8 instance methods, 8 class methods

## Instance variables

```
@"CIDVUIBiometricBindingFlowManager" __biometricBindingFlowManager;
@"LAContext" _authContext;
```

## Properties

```
@property (T@"CIDVUIBiometricBindingFlowManager",&,N,V__biometricBindingFlowManager) _biometricBindingFlowManager;
@property (T@"LAContext",&,N,V_authContext) authContext;
```

## Class methods

```
+[DSBiometricManager deviceWithType:];
+[DSBiometricManager supportsPearl];
+[DSBiometricManager supportsMesa];
+[DSBiometricManager pearlIdentities];
+[DSBiometricManager deleteAllTouchIDs];
+[DSBiometricManager identitiesWithType:device:];
+[DSBiometricManager pearlIdentityCount];
+[DSBiometricManager touchIDCount];
```

## Instance methods

```
-[DSBiometricManager initWithContext:];
-[DSBiometricManager authContext];
-[DSBiometricManager setAuthContext:];
-[DSBiometricManager _biometricBindingFlowManager];
-[DSBiometricManager configurePeriocularEnabled:device:];
-[DSBiometricManager deleteAllPearlIdentities];
-[DSBiometricManager deleteGlobalAuthACL];
-[DSBiometricManager set_biometricBindingFlowManager:];
```
