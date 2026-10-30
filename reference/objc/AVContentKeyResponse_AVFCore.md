# `AVContentKeyResponse`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 3 instance methods, 4 class methods

## Instance variables

```
@"AVContentKeyResponseInternal" _keyResponse;
```

## Class methods

```
+[AVContentKeyResponse contentKeyResponseWithAuthorizationTokenData:];
+[AVContentKeyResponse contentKeyResponseWithClearKeyData:initializationVector:];
+[AVContentKeyResponse contentKeyResponseWithFairPlayStreamingKeyResponseData:];
+[AVContentKeyResponse contentKeyResponseWithFairPlayStreamingKeyResponseData:renewalDate:];
```

## Instance methods

```
-[AVContentKeyResponse dealloc];
-[AVContentKeyResponse keySystem];
-[AVContentKeyResponse initWithKeySystem:];
```
