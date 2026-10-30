# `SecureIntentClientView` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 2 properties, 7 instance methods, 1 class methods

## Properties

```
@property (T@"BKMesaSecureIntentProvider",W,N) secureIntentProvider;
@property (T@"BKUIDevice",W,N) currentDevice;
```

## Class methods

```
+[SecureIntentClientView instanceForBKUIDevice:];
```

## Instance methods

```
-[SecureIntentClientView currentDevice];
-[SecureIntentClientView setCurrentDevice:];
-[SecureIntentClientView secureIntentProvider];
-[SecureIntentClientView setSecureIntentProvider:];
-[SecureIntentClientView showInitialUI];
-[SecureIntentClientView showRetryOnErrorUI];
-[SecureIntentClientView promptTitle];
```
