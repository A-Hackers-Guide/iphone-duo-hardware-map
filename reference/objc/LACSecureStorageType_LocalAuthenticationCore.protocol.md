# `LACSecureStorageType` (protocol)

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 1 properties, 6 instance methods, 2 class methods

## Properties

```
@property (T@"<LACSecureStorageDelegate>",W,N) delegate;
```

## Class methods

```
+[LACSecureStorageType isKeyAvailable:];
+[LACSecureStorageType isKeyAvailable:operation:];
```

## Instance methods

```
-[LACSecureStorageType setDelegate:];
-[LACSecureStorageType delegate];
-[LACSecureStorageType objectForRequest:completionHandler:];
-[LACSecureStorageType processError:forRequest:completionHandler:];
-[LACSecureStorageType removeObjectForRequest:completionHandler:];
-[LACSecureStorageType setObject:forRequest:completionHandler:];
```
