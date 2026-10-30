# `LACUIBiometryAlertAction`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCoreUI.framework/LocalAuthenticationCoreUI`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCoreUI.framework__LocalAuthenticationCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 5 properties, 6 instance methods, 2 class methods

## Instance variables

```
B _shouldDismissAlert;
@? _handler;
@"NSString" _title;
q _type;
```

## Properties

```
@property (T@"NSString",R,N) axIdentifier;
@property (T@?,R,N,V_handler) handler;
@property (TB,R,N,V_shouldDismissAlert) shouldDismissAlert;
@property (T@"NSString",R,N,V_title) title;
@property (Tq,R,N,V_type) type;
```

## Class methods

```
+[LACUIBiometryAlertAction actionWithType:title:handler:];
+[LACUIBiometryAlertAction actionWithType:title:shouldDismissAlert:handler:];
```

## Instance methods

```
-[LACUIBiometryAlertAction type];
-[LACUIBiometryAlertAction title];
-[LACUIBiometryAlertAction handler];
-[LACUIBiometryAlertAction axIdentifier];
-[LACUIBiometryAlertAction initWithType:title:shouldDismissAlert:handler:];
-[LACUIBiometryAlertAction shouldDismissAlert];
```
