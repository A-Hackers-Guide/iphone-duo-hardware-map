# `LACManagedConfiguration`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MCProfileConnectionObserver`, `LACManagedConfiguration`
- 2 instance variables, 6 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"MCProfileConnection" _connection;
@"LACThreadSafeCollection" _observers;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N) isPasscodeSet;
@property (Tq,R,N) passcodeType;
```

## Class methods

```
+[LACManagedConfiguration sharedInstance];
```

## Instance methods

```
-[LACManagedConfiguration removeObserver:];
-[LACManagedConfiguration init];
-[LACManagedConfiguration addObserver:];
-[LACManagedConfiguration isPasscodeSet];
-[LACManagedConfiguration passcodeType];
-[LACManagedConfiguration profileConnectionDidReceivePasscodeChangedNotification:userInfo:];
-[LACManagedConfiguration _startObservingConnection];
-[LACManagedConfiguration _stopObservingConnection];
```
