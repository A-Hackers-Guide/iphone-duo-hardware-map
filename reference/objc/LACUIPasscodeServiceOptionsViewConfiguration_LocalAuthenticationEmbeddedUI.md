# `LACUIPasscodeServiceOptionsViewConfiguration`

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 11 properties, 22 instance methods, 0 class methods

## Instance variables

```
B _isPasscodeRecoveryOptionVisible;
B _isPasscodeRecoverySupported;
B _isPasscodeRecoveryEnabled;
B _isPasscodeRecoveryRestricted;
@"NSString" _title;
@"NSString" _passcodeRecoveryTitle;
@"NSString" _passcodeRecoveryEnabledTitle;
@"NSString" _passcodeRecoveryDisabledTitle;
@"NSString" _cancelTitle;
@"NSOrderedSet" _allowedPasscodeTypes;
@"LACPasscode" _selectedPasscodeType;
```

## Properties

```
@property (T@"NSString",&,N,V_title) title;
@property (T@"NSString",&,N,V_passcodeRecoveryTitle) passcodeRecoveryTitle;
@property (T@"NSString",&,N,V_passcodeRecoveryEnabledTitle) passcodeRecoveryEnabledTitle;
@property (T@"NSString",&,N,V_passcodeRecoveryDisabledTitle) passcodeRecoveryDisabledTitle;
@property (T@"NSString",&,N,V_cancelTitle) cancelTitle;
@property (T@"NSOrderedSet",&,N,V_allowedPasscodeTypes) allowedPasscodeTypes;
@property (T@"LACPasscode",&,N,V_selectedPasscodeType) selectedPasscodeType;
@property (TB,N,V_isPasscodeRecoveryOptionVisible) isPasscodeRecoveryOptionVisible;
@property (TB,N,V_isPasscodeRecoverySupported) isPasscodeRecoverySupported;
@property (TB,N,V_isPasscodeRecoveryEnabled) isPasscodeRecoveryEnabled;
@property (TB,N,V_isPasscodeRecoveryRestricted) isPasscodeRecoveryRestricted;
```

## Instance methods

```
-[LACUIPasscodeServiceOptionsViewConfiguration isPasscodeRecoveryRestricted];
-[LACUIPasscodeServiceOptionsViewConfiguration title];
-[LACUIPasscodeServiceOptionsViewConfiguration isPasscodeRecoverySupported];
-[LACUIPasscodeServiceOptionsViewConfiguration setTitle:];
-[LACUIPasscodeServiceOptionsViewConfiguration setCancelTitle:];
-[LACUIPasscodeServiceOptionsViewConfiguration cancelTitle];
-[LACUIPasscodeServiceOptionsViewConfiguration isPasscodeRecoveryOptionVisible];
-[LACUIPasscodeServiceOptionsViewConfiguration setIsPasscodeRecoverySupported:];
-[LACUIPasscodeServiceOptionsViewConfiguration allowedPasscodeTypes];
-[LACUIPasscodeServiceOptionsViewConfiguration isPasscodeRecoveryEnabled];
-[LACUIPasscodeServiceOptionsViewConfiguration passcodeRecoveryDisabledTitle];
-[LACUIPasscodeServiceOptionsViewConfiguration passcodeRecoveryEnabledTitle];
-[LACUIPasscodeServiceOptionsViewConfiguration passcodeRecoveryTitle];
-[LACUIPasscodeServiceOptionsViewConfiguration selectedPasscodeType];
-[LACUIPasscodeServiceOptionsViewConfiguration setAllowedPasscodeTypes:];
-[LACUIPasscodeServiceOptionsViewConfiguration setIsPasscodeRecoveryEnabled:];
-[LACUIPasscodeServiceOptionsViewConfiguration setIsPasscodeRecoveryOptionVisible:];
-[LACUIPasscodeServiceOptionsViewConfiguration setIsPasscodeRecoveryRestricted:];
-[LACUIPasscodeServiceOptionsViewConfiguration setPasscodeRecoveryDisabledTitle:];
-[LACUIPasscodeServiceOptionsViewConfiguration setPasscodeRecoveryEnabledTitle:];
-[LACUIPasscodeServiceOptionsViewConfiguration setPasscodeRecoveryTitle:];
-[LACUIPasscodeServiceOptionsViewConfiguration setSelectedPasscodeType:];
```
