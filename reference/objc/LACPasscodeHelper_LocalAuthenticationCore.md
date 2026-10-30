# `LACPasscodeHelper`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACPasscodeVerifying`
- 6 instance variables, 7 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"_TtC23LocalAuthenticationCore18LACPasscodeMonitor" monitor;
@"LACPasscodeUserHelper" userHelper;
@"_TtC23LocalAuthenticationCore21LACPasscodeSuccessAge" passcodeSuccessAgeController;
@"<LACPasscodeRateLimiting>" rateLimiting;
@"LACPasscodeMKBHelper" mkbHelper;
@"_TtC23LocalAuthenticationCore19LACPasscodeVerifier" verifier;
```

## Properties

```
@property (T@"_TtC23LocalAuthenticationCore18LACPasscodeMonitor",N,R,Vmonitor) monitor;
@property (T@"LACPasscodeUserHelper",N,R,VuserHelper) userHelper;
@property (T@"_TtC23LocalAuthenticationCore21LACPasscodeSuccessAge",N,R,VpasscodeSuccessAgeController) passcodeSuccessAgeController;
@property (T@"<LACPasscodeRateLimiting>",N,R,VrateLimiting) rateLimiting;
@property (T@"LACPasscodeMKBHelper",N,R,VmkbHelper) mkbHelper;
@property (T@"_TtC23LocalAuthenticationCore19LACPasscodeVerifier",N,R,Vverifier) verifier;
@property (Td,N,R) passcodeSuccessAge;
```

## Class methods

```
+[LACPasscodeHelper sharedInstance];
```

## Instance methods

```
-[LACPasscodeHelper monitor];
-[LACPasscodeHelper verifier];
-[LACPasscodeHelper removeObserver:];
-[LACPasscodeHelper init];
-[LACPasscodeHelper addObserver:];
-[LACPasscodeHelper passcodeType];
-[LACPasscodeHelper verifyPasscode:];
-[LACPasscodeHelper initWithVerifier:passcodeSuccessAge:rateLimiting:mkbHelper:userHelper:keyBagProvider:];
-[LACPasscodeHelper isPasscodeSetForUser:error:];
-[LACPasscodeHelper mkbHelper];
-[LACPasscodeHelper passcodeScreenStyleWithPolicy:options:darkInterface:];
-[LACPasscodeHelper passcodeSuccessAge];
-[LACPasscodeHelper passcodeSuccessAgeController];
-[LACPasscodeHelper rateLimiting];
-[LACPasscodeHelper updatePasscodeSuccessAgeWithUptime:];
-[LACPasscodeHelper userHelper];
```
