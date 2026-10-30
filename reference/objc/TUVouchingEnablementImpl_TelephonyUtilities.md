# `TUVouchingEnablementImpl`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUVouchingEnablement`
- 2 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSUserDefaults" _userDefaults;
@"FTServerBag" _serverBag;
```

## Properties

```
@property (T@"NSUserDefaults",&,N,V_userDefaults) userDefaults;
@property (T@"FTServerBag",&,N,V_serverBag) serverBag;
@property (TB,R,N,GisEnabled) enabled;
@property (TB,R,N) shouldForceVerificationFailures;
```

## Instance methods

```
-[TUVouchingEnablementImpl serverBag];
-[TUVouchingEnablementImpl setServerBag:];
-[TUVouchingEnablementImpl userDefaults];
-[TUVouchingEnablementImpl init];
-[TUVouchingEnablementImpl isEnabled];
-[TUVouchingEnablementImpl setUserDefaults:];
-[TUVouchingEnablementImpl initWithUserDefaults:serverBag:];
-[TUVouchingEnablementImpl shouldForceVerificationFailures];
-[TUVouchingEnablementImpl serverBagValueForKey:withDefault:];
```
