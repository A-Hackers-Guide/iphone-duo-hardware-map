# `BiometricKitUIEnrollViewController`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `BiometricKitDelegate`
- 4 instance variables, 7 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _properties;
@"BiometricKit" _biometricKit;
@"<BiometricKitUIEnrollResultDelegate>" _delegate;
@"NSObject<OS_os_log>" _log;
```

## Properties

```
@property (T@"NSObject<OS_os_log>",&,N,V_log) log;
@property (T@"BiometricKit",&,N,V_biometricKit) biometricKit;
@property (T@"<BiometricKitUIEnrollResultDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BiometricKitUIEnrollViewController setLog:];
-[BiometricKitUIEnrollViewController propertyForKey:];
-[BiometricKitUIEnrollViewController setProperty:forKey:];
-[BiometricKitUIEnrollViewController init];
-[BiometricKitUIEnrollViewController setDelegate:];
-[BiometricKitUIEnrollViewController delegate];
-[BiometricKitUIEnrollViewController log];
-[BiometricKitUIEnrollViewController biometricKit];
-[BiometricKitUIEnrollViewController cancelEnroll];
-[BiometricKitUIEnrollViewController restartEnroll];
-[BiometricKitUIEnrollViewController setBiometricKit:];
-[BiometricKitUIEnrollViewController startEnroll];
-[BiometricKitUIEnrollViewController startEnrollOperation];
```
