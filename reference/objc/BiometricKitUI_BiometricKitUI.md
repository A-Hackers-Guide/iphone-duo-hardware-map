# `BiometricKitUI`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 6 instance methods, 2 class methods

## Instance variables

```
B _triggeredfromApplePay;
@"NSObject<OS_os_log>" _log;
```

## Properties

```
@property (T@"NSObject<OS_os_log>",&,N,V_log) log;
```

## Class methods

```
+[BiometricKitUI sharedInstance];
+[BiometricKitUI setOfActiveRestrictionUUIDs:];
```

## Instance methods

```
-[BiometricKitUI setLog:];
-[BiometricKitUI log];
-[BiometricKitUI getEnrollUIViewController:bundleName:];
-[BiometricKitUI invalidateApplePayTrigger];
-[BiometricKitUI setTriggeredFromApplePay];
-[BiometricKitUI triggeredFromApplePay];
```
