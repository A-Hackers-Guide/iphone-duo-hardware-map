# `LAPSCurrentPasscodeService`

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"LAPSCurrentPasscodeServiceOptions" _options;
@"<LAPSPasscodePersistence>" _persistence;
```

## Properties

```
@property (T@"<LAPSPasscodePersistence>",R,N,V_persistence) persistence;
```

## Instance methods

```
-[LAPSCurrentPasscodeService persistence];
-[LAPSCurrentPasscodeService hasPasscode];
-[LAPSCurrentPasscodeService passcodeCreationDate];
-[LAPSCurrentPasscodeService initWithPersistence:];
-[LAPSCurrentPasscodeService passcodeType];
-[LAPSCurrentPasscodeService _reportPasscodeChangedTo:];
-[LAPSCurrentPasscodeService backoffTimeout];
-[LAPSCurrentPasscodeService canChangePasscodeWithError:];
-[LAPSCurrentPasscodeService canRemovePasscodeWithError:];
-[LAPSCurrentPasscodeService changePasscode:to:enableRecovery:completion:];
-[LAPSCurrentPasscodeService failedPasscodeAttempts];
-[LAPSCurrentPasscodeService initWithPersistence:options:];
-[LAPSCurrentPasscodeService verifyPasscode:completion:];
-[LAPSCurrentPasscodeService verifyPasscode:contextRef:completion:];
```
