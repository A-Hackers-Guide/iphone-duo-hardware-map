# `LAPSFetchOldPasscodeCoordinatorInput`

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSString" _title;
@"NSString" _prompt;
@"NSString" _subPrompt;
@"NSString" _nextButton;
@"NSString" _errorMessage;
q _backoffTimeout;
@"LACPasscode" _passcodeType;
```

## Properties

```
@property (T@"NSString",&,N,V_title) title;
@property (T@"NSString",&,N,V_prompt) prompt;
@property (T@"NSString",&,N,V_subPrompt) subPrompt;
@property (T@"NSString",&,N,V_nextButton) nextButton;
@property (T@"NSString",&,N,V_errorMessage) errorMessage;
@property (Tq,N,V_backoffTimeout) backoffTimeout;
@property (T@"LACPasscode",&,N,V_passcodeType) passcodeType;
```

## Instance methods

```
-[LAPSFetchOldPasscodeCoordinatorInput prompt];
-[LAPSFetchOldPasscodeCoordinatorInput title];
-[LAPSFetchOldPasscodeCoordinatorInput setTitle:];
-[LAPSFetchOldPasscodeCoordinatorInput setPasscodeType:];
-[LAPSFetchOldPasscodeCoordinatorInput setPrompt:];
-[LAPSFetchOldPasscodeCoordinatorInput passcodeType];
-[LAPSFetchOldPasscodeCoordinatorInput errorMessage];
-[LAPSFetchOldPasscodeCoordinatorInput setErrorMessage:];
-[LAPSFetchOldPasscodeCoordinatorInput nextButton];
-[LAPSFetchOldPasscodeCoordinatorInput setNextButton:];
-[LAPSFetchOldPasscodeCoordinatorInput backoffTimeout];
-[LAPSFetchOldPasscodeCoordinatorInput setBackoffTimeout:];
-[LAPSFetchOldPasscodeCoordinatorInput setSubPrompt:];
-[LAPSFetchOldPasscodeCoordinatorInput subPrompt];
```
