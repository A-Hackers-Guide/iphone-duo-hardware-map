# `LAPSFetchNewPasscodeCoordinatorInput`

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 21 instance variables, 21 properties, 42 instance methods, 0 class methods

## Instance variables

```
B _isPasscodeRecoveryOptionVisible;
B _isPasscodeRecoveryMessageHidden;
B _isPasscodeRecoverySupported;
B _isPasscodeRecoveryEnabled;
B _isPasscodeRecoveryRestricted;
@"NSString" _title;
@"NSString" _prompt;
@"NSString" _subPrompt;
@"NSString" _footerRecoveryEnabled;
@"NSString" _footerRecoveryDisabled;
@"NSString" _nextButton;
@"LACPasscode" _passcodeType;
@"NSString" _passcodeOptionsTitle;
@"NSString" _passcodeOptionsCancelTitle;
@"NSString" _passcodeRecoveryTitle;
@"NSString" _passcodeRecoveryEnabledTitle;
@"NSString" _passcodeRecoveryDisabledTitle;
@"NSOrderedSet" _allowedPasscodeTypes;
@"NSString" _verifyPrompt;
@"NSString" _verifySubPrompt;
@"NSString" _verifyNextButton;
```

## Properties

```
@property (T@"NSString",&,N,V_title) title;
@property (T@"NSString",&,N,V_prompt) prompt;
@property (T@"NSString",&,N,V_subPrompt) subPrompt;
@property (T@"NSString",&,N,V_footerRecoveryEnabled) footerRecoveryEnabled;
@property (T@"NSString",&,N,V_footerRecoveryDisabled) footerRecoveryDisabled;
@property (T@"NSString",&,N,V_nextButton) nextButton;
@property (T@"LACPasscode",&,N,V_passcodeType) passcodeType;
@property (T@"NSString",&,N,V_passcodeOptionsTitle) passcodeOptionsTitle;
@property (T@"NSString",&,N,V_passcodeOptionsCancelTitle) passcodeOptionsCancelTitle;
@property (T@"NSString",&,N,V_passcodeRecoveryTitle) passcodeRecoveryTitle;
@property (T@"NSString",&,N,V_passcodeRecoveryEnabledTitle) passcodeRecoveryEnabledTitle;
@property (T@"NSString",&,N,V_passcodeRecoveryDisabledTitle) passcodeRecoveryDisabledTitle;
@property (T@"NSOrderedSet",&,N,V_allowedPasscodeTypes) allowedPasscodeTypes;
@property (TB,N,V_isPasscodeRecoveryOptionVisible) isPasscodeRecoveryOptionVisible;
@property (TB,N,V_isPasscodeRecoveryMessageHidden) isPasscodeRecoveryMessageHidden;
@property (TB,N,V_isPasscodeRecoverySupported) isPasscodeRecoverySupported;
@property (TB,N,V_isPasscodeRecoveryEnabled) isPasscodeRecoveryEnabled;
@property (TB,N,V_isPasscodeRecoveryRestricted) isPasscodeRecoveryRestricted;
@property (T@"NSString",&,N,V_verifyPrompt) verifyPrompt;
@property (T@"NSString",&,N,V_verifySubPrompt) verifySubPrompt;
@property (T@"NSString",&,N,V_verifyNextButton) verifyNextButton;
```

## Instance methods

```
-[LAPSFetchNewPasscodeCoordinatorInput prompt];
-[LAPSFetchNewPasscodeCoordinatorInput isPasscodeRecoveryRestricted];
-[LAPSFetchNewPasscodeCoordinatorInput title];
-[LAPSFetchNewPasscodeCoordinatorInput isPasscodeRecoverySupported];
-[LAPSFetchNewPasscodeCoordinatorInput setTitle:];
-[LAPSFetchNewPasscodeCoordinatorInput setPasscodeType:];
-[LAPSFetchNewPasscodeCoordinatorInput setPrompt:];
-[LAPSFetchNewPasscodeCoordinatorInput passcodeType];
-[LAPSFetchNewPasscodeCoordinatorInput nextButton];
-[LAPSFetchNewPasscodeCoordinatorInput setNextButton:];
-[LAPSFetchNewPasscodeCoordinatorInput passcodeOptionsTitle];
-[LAPSFetchNewPasscodeCoordinatorInput setPasscodeOptionsTitle:];
-[LAPSFetchNewPasscodeCoordinatorInput isPasscodeRecoveryOptionVisible];
-[LAPSFetchNewPasscodeCoordinatorInput setIsPasscodeRecoverySupported:];
-[LAPSFetchNewPasscodeCoordinatorInput isPasscodeRecoveryMessageHidden];
-[LAPSFetchNewPasscodeCoordinatorInput verifySubPrompt];
-[LAPSFetchNewPasscodeCoordinatorInput allowedPasscodeTypes];
-[LAPSFetchNewPasscodeCoordinatorInput footerRecoveryDisabled];
-[LAPSFetchNewPasscodeCoordinatorInput footerRecoveryEnabled];
-[LAPSFetchNewPasscodeCoordinatorInput isPasscodeRecoveryEnabled];
-[LAPSFetchNewPasscodeCoordinatorInput passcodeOptionsCancelTitle];
-[LAPSFetchNewPasscodeCoordinatorInput passcodeRecoveryDisabledTitle];
-[LAPSFetchNewPasscodeCoordinatorInput passcodeRecoveryEnabledTitle];
-[LAPSFetchNewPasscodeCoordinatorInput passcodeRecoveryTitle];
-[LAPSFetchNewPasscodeCoordinatorInput setAllowedPasscodeTypes:];
-[LAPSFetchNewPasscodeCoordinatorInput setFooterRecoveryDisabled:];
-[LAPSFetchNewPasscodeCoordinatorInput setFooterRecoveryEnabled:];
-[LAPSFetchNewPasscodeCoordinatorInput setIsPasscodeRecoveryEnabled:];
-[LAPSFetchNewPasscodeCoordinatorInput setIsPasscodeRecoveryMessageHidden:];
-[LAPSFetchNewPasscodeCoordinatorInput setIsPasscodeRecoveryOptionVisible:];
-[LAPSFetchNewPasscodeCoordinatorInput setIsPasscodeRecoveryRestricted:];
-[LAPSFetchNewPasscodeCoordinatorInput setPasscodeOptionsCancelTitle:];
-[LAPSFetchNewPasscodeCoordinatorInput setPasscodeRecoveryDisabledTitle:];
-[LAPSFetchNewPasscodeCoordinatorInput setPasscodeRecoveryEnabledTitle:];
-[LAPSFetchNewPasscodeCoordinatorInput setPasscodeRecoveryTitle:];
-[LAPSFetchNewPasscodeCoordinatorInput setSubPrompt:];
-[LAPSFetchNewPasscodeCoordinatorInput setVerifyNextButton:];
-[LAPSFetchNewPasscodeCoordinatorInput setVerifyPrompt:];
-[LAPSFetchNewPasscodeCoordinatorInput setVerifySubPrompt:];
-[LAPSFetchNewPasscodeCoordinatorInput subPrompt];
-[LAPSFetchNewPasscodeCoordinatorInput verifyNextButton];
-[LAPSFetchNewPasscodeCoordinatorInput verifyPrompt];
```
