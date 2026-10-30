# `LACDeviceLifecycleManager`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDeviceLifecycleManaging`
- 0 instance variables, 4 properties, 2 instance methods, 1 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[LACDeviceLifecycleManager sharedInstance];
```

## Instance methods

```
-[LACDeviceLifecycleManager rebootDeviceWithReason:completion:];
-[LACDeviceLifecycleManager rebootDeviceWithReason:forced:completion:];
```
