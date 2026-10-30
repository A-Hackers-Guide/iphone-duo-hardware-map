# `SBBiometricsService`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSystemServiceServerBiometricsDelegate`
- 2 instance variables, 4 properties, 2 instance methods, 1 class methods

## Instance variables

```
@"SBUIBiometricResource" _biometricResource;
@"FBServiceClientAuthenticator" _unlockCredentialAuthenticator;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBBiometricsService sharedInstance];
```

## Instance methods

```
-[SBBiometricsService init];
-[SBBiometricsService systemServiceServer:client:fetchUnlockCredentialSet:];
```
