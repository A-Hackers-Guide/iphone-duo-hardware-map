# `AuthRequestWrapper`

- Image: [`/System/Library/PrivateFrameworks/HIDRMUI.framework/HIDRMUI`](../userland/System__Library__PrivateFrameworks__HIDRMUI.framework__HIDRMUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 15 instance methods, 1 class methods

## Instance variables

```
@? _completionHandler;
@"IOUserNotification" _userNotification;
q _pairingStatus;
@"NSArray" _pairingCodeDigits;
@"NSMutableArray" _pairingCodeDigitsEntered;
Q _pairingFailureCount;
@"NSDate" _characterLockoutExpirationTimestamp;
```

## Properties

```
@property (T@?,C,N,V_completionHandler) completionHandler;
@property (T@"IOUserNotification",&,N,V_userNotification) userNotification;
@property (Tq,N,V_pairingStatus) pairingStatus;
@property (T@"NSArray",&,N,V_pairingCodeDigits) pairingCodeDigits;
@property (T@"NSMutableArray",&,N,V_pairingCodeDigitsEntered) pairingCodeDigitsEntered;
@property (TQ,N,V_pairingFailureCount) pairingFailureCount;
@property (T@"NSDate",&,N,V_characterLockoutExpirationTimestamp) characterLockoutExpirationTimestamp;
```

## Class methods

```
+[AuthRequestWrapper requestWrapperWithCompletion:andUserNotification:];
```

## Instance methods

```
-[AuthRequestWrapper setCompletionHandler:];
-[AuthRequestWrapper completionHandler];
-[AuthRequestWrapper init];
-[AuthRequestWrapper setUserNotification:];
-[AuthRequestWrapper userNotification];
-[AuthRequestWrapper pairingStatus];
-[AuthRequestWrapper setPairingStatus:];
-[AuthRequestWrapper characterLockoutExpirationTimestamp];
-[AuthRequestWrapper pairingCodeDigits];
-[AuthRequestWrapper pairingCodeDigitsEntered];
-[AuthRequestWrapper pairingFailureCount];
-[AuthRequestWrapper setCharacterLockoutExpirationTimestamp:];
-[AuthRequestWrapper setPairingCodeDigits:];
-[AuthRequestWrapper setPairingCodeDigitsEntered:];
-[AuthRequestWrapper setPairingFailureCount:];
```
