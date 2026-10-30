# `LAPSFetchNewPasscodeRequest`

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _isPasscodeSet;
B _isPasscodeRecoverySupported;
B _isPasscodeRecoveryEnabled;
B _isPasscodeRecoveryRestricted;
@"LACPasscode" _passcodeType;
@"NSOrderedSet" _allowedPasscodeTypes;
```

## Properties

```
@property (T@"LACPasscode",&,N,V_passcodeType) passcodeType;
@property (T@"NSOrderedSet",&,N,V_allowedPasscodeTypes) allowedPasscodeTypes;
@property (TB,N,V_isPasscodeSet) isPasscodeSet;
@property (TB,N,V_isPasscodeRecoverySupported) isPasscodeRecoverySupported;
@property (TB,N,V_isPasscodeRecoveryEnabled) isPasscodeRecoveryEnabled;
@property (TB,N,V_isPasscodeRecoveryRestricted) isPasscodeRecoveryRestricted;
```

## Instance methods

```
-[LAPSFetchNewPasscodeRequest init];
-[LAPSFetchNewPasscodeRequest isPasscodeRecoveryRestricted];
-[LAPSFetchNewPasscodeRequest isPasscodeRecoverySupported];
-[LAPSFetchNewPasscodeRequest isPasscodeSet];
-[LAPSFetchNewPasscodeRequest setPasscodeType:];
-[LAPSFetchNewPasscodeRequest passcodeType];
-[LAPSFetchNewPasscodeRequest setIsPasscodeRecoverySupported:];
-[LAPSFetchNewPasscodeRequest allowedPasscodeTypes];
-[LAPSFetchNewPasscodeRequest isPasscodeRecoveryEnabled];
-[LAPSFetchNewPasscodeRequest setAllowedPasscodeTypes:];
-[LAPSFetchNewPasscodeRequest setIsPasscodeRecoveryEnabled:];
-[LAPSFetchNewPasscodeRequest setIsPasscodeRecoveryRestricted:];
-[LAPSFetchNewPasscodeRequest setIsPasscodeSet:];
```
