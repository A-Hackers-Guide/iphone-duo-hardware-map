# `_LABKDevice`

- Image: [`/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`](../userland/System__Library__Frameworks__LocalAuthentication.framework__LocalAuthentication.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKDeviceDelegate`
- 3 instance variables, 7 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"BKDevice" __BKDevice;
@"BKDeviceDescriptor" _descriptor;
@"_LAAuthenticationBiometricMethodShim" _shim;
```

## Properties

```
@property (T@"BKDevice",R,N,V__BKDevice) _BKDevice;
@property (T@"BKDeviceDescriptor",R,N,V_descriptor) descriptor;
@property (T@"_LAAuthenticationBiometricMethodShim",R,N,V_shim) shim;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_LABKDevice deviceWithDescriptor:error:];
```

## Instance methods

```
-[_LABKDevice descriptor];
-[_LABKDevice forwardingTargetForSelector:];
-[_LABKDevice createMatchOperationWithError:];
-[_LABKDevice createPresenceDetectOperationWithError:];
-[_LABKDevice bioLockoutState:forUser:error:];
-[_LABKDevice identitiesWithError:];
-[_LABKDevice _BKDevice];
-[_LABKDevice extendedBioLockoutState:forUser:error:];
-[_LABKDevice initWithDescriptor:error:];
-[_LABKDevice shim];
```
