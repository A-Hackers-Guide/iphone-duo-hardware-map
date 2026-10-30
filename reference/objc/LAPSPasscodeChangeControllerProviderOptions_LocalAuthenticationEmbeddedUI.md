# `LAPSPasscodeChangeControllerProviderOptions`

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 16 properties, 32 instance methods, 0 class methods

## Instance variables

```
B _dismissUIAfterCompletion;
B _skipSuccessNotification;
B _isPasscodeRecoveryMessageHidden;
@"NSString" _title;
@"NSString" _oldPasscodePrompt;
@"NSString" _oldPasscodeSubPrompt;
@"NSString" _passcodePrompt;
@"NSString" _passcodeSubPrompt;
@"LACSExtractablePassword" _passcode;
@"NSURL" _calloutURL;
@"NSString" _calloutReason;
@"NSNumber" _userId;
@"LACPasscode" _passcodeTypeOverride;
@"UIViewController" _parentVC;
@"LAExtractablePassword" _oldPasscode;
@"LAExtractablePassword" _newPasscode;
```

## Properties

```
@property (T@"NSString",&,N,V_title) title;
@property (T@"NSString",&,N,V_oldPasscodePrompt) oldPasscodePrompt;
@property (T@"NSString",&,N,V_oldPasscodeSubPrompt) oldPasscodeSubPrompt;
@property (T@"NSString",&,N,V_passcodePrompt) passcodePrompt;
@property (T@"NSString",&,N,V_passcodeSubPrompt) passcodeSubPrompt;
@property (T@"LACSExtractablePassword",&,N,V_passcode) passcode;
@property (T@"NSURL",&,N,V_calloutURL) calloutURL;
@property (T@"NSString",&,N,V_calloutReason) calloutReason;
@property (TB,N,V_dismissUIAfterCompletion) dismissUIAfterCompletion;
@property (TB,N,V_skipSuccessNotification) skipSuccessNotification;
@property (TB,N,V_isPasscodeRecoveryMessageHidden) isPasscodeRecoveryMessageHidden;
@property (T@"NSNumber",C,N,V_userId) userId;
@property (T@"LACPasscode",&,N,V_passcodeTypeOverride) passcodeTypeOverride;
@property (T@"UIViewController",R,N,V_parentVC) parentVC;
@property (T@"LAExtractablePassword",&,N,V_oldPasscode) oldPasscode;
@property (T@"LAExtractablePassword",&,N,V_newPasscode) newPasscode;
```

## Instance methods

```
-[LAPSPasscodeChangeControllerProviderOptions passcode];
-[LAPSPasscodeChangeControllerProviderOptions title];
-[LAPSPasscodeChangeControllerProviderOptions setTitle:];
-[LAPSPasscodeChangeControllerProviderOptions setUserId:];
-[LAPSPasscodeChangeControllerProviderOptions userId];
-[LAPSPasscodeChangeControllerProviderOptions setPasscode:];
-[LAPSPasscodeChangeControllerProviderOptions calloutReason];
-[LAPSPasscodeChangeControllerProviderOptions setCalloutReason:];
-[LAPSPasscodeChangeControllerProviderOptions setCalloutURL:];
-[LAPSPasscodeChangeControllerProviderOptions setPasscodePrompt:];
-[LAPSPasscodeChangeControllerProviderOptions setOldPasscode:];
-[LAPSPasscodeChangeControllerProviderOptions isPasscodeRecoveryMessageHidden];
-[LAPSPasscodeChangeControllerProviderOptions setNewPasscode:];
-[LAPSPasscodeChangeControllerProviderOptions calloutURL];
-[LAPSPasscodeChangeControllerProviderOptions dismissUIAfterCompletion];
-[LAPSPasscodeChangeControllerProviderOptions initWithParentVC:];
-[LAPSPasscodeChangeControllerProviderOptions newPasscode];
-[LAPSPasscodeChangeControllerProviderOptions oldPasscode];
-[LAPSPasscodeChangeControllerProviderOptions oldPasscodePrompt];
-[LAPSPasscodeChangeControllerProviderOptions oldPasscodeSubPrompt];
-[LAPSPasscodeChangeControllerProviderOptions parentVC];
-[LAPSPasscodeChangeControllerProviderOptions passcodePrompt];
-[LAPSPasscodeChangeControllerProviderOptions passcodeSubPrompt];
-[LAPSPasscodeChangeControllerProviderOptions passcodeTypeOverride];
-[LAPSPasscodeChangeControllerProviderOptions setDismissUIAfterCompletion:];
-[LAPSPasscodeChangeControllerProviderOptions setIsPasscodeRecoveryMessageHidden:];
-[LAPSPasscodeChangeControllerProviderOptions setOldPasscodePrompt:];
-[LAPSPasscodeChangeControllerProviderOptions setOldPasscodeSubPrompt:];
-[LAPSPasscodeChangeControllerProviderOptions setPasscodeSubPrompt:];
-[LAPSPasscodeChangeControllerProviderOptions setPasscodeTypeOverride:];
-[LAPSPasscodeChangeControllerProviderOptions setSkipSuccessNotification:];
-[LAPSPasscodeChangeControllerProviderOptions skipSuccessNotification];
```
