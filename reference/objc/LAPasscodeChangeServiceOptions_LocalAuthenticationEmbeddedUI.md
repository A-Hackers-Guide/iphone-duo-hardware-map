# `LAPasscodeChangeServiceOptions`

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 12 properties, 26 instance methods, 0 class methods

## Instance variables

```
B _skipSuccessNotification;
B _hidePasscodeRecoveryMessage;
@"NSString" _title;
@"NSString" _currentPasscodePrompt;
@"NSString" _currentPasscodeSubPrompt;
@"NSString" _passcodePrompt;
@"NSString" _passcodeSubPrompt;
@"LACSExtractablePassword" _passcode;
@"NSURL" _calloutURL;
@"NSString" _calloutReason;
@"LAExtractablePassword" _currentPasscode;
@"LAExtractablePassword" _newPasscode;
```

## Properties

```
@property (T@"NSString",&,N,V_title) title;
@property (T@"NSString",&,N,V_currentPasscodePrompt) currentPasscodePrompt;
@property (T@"NSString",&,N,V_currentPasscodeSubPrompt) currentPasscodeSubPrompt;
@property (T@"NSString",&,N,V_passcodePrompt) passcodePrompt;
@property (T@"NSString",&,N,V_passcodeSubPrompt) passcodeSubPrompt;
@property (T@"LACSExtractablePassword",&,N,V_passcode) passcode;
@property (T@"NSURL",&,N,V_calloutURL) calloutURL;
@property (T@"NSString",&,N,V_calloutReason) calloutReason;
@property (TB,N,V_skipSuccessNotification) skipSuccessNotification;
@property (TB,N,V_hidePasscodeRecoveryMessage) hidePasscodeRecoveryMessage;
@property (T@"LAExtractablePassword",&,N,V_currentPasscode) currentPasscode;
@property (T@"LAExtractablePassword",&,N,V_newPasscode) newPasscode;
```

## Instance methods

```
-[LAPasscodeChangeServiceOptions passcode];
-[LAPasscodeChangeServiceOptions init];
-[LAPasscodeChangeServiceOptions title];
-[LAPasscodeChangeServiceOptions description];
-[LAPasscodeChangeServiceOptions setTitle:];
-[LAPasscodeChangeServiceOptions setPasscode:];
-[LAPasscodeChangeServiceOptions calloutReason];
-[LAPasscodeChangeServiceOptions setHidePasscodeRecoveryMessage:];
-[LAPasscodeChangeServiceOptions setCalloutReason:];
-[LAPasscodeChangeServiceOptions setCalloutURL:];
-[LAPasscodeChangeServiceOptions setPasscodePrompt:];
-[LAPasscodeChangeServiceOptions currentPasscode];
-[LAPasscodeChangeServiceOptions setNewPasscode:];
-[LAPasscodeChangeServiceOptions calloutURL];
-[LAPasscodeChangeServiceOptions currentPasscodePrompt];
-[LAPasscodeChangeServiceOptions currentPasscodeSubPrompt];
-[LAPasscodeChangeServiceOptions hidePasscodeRecoveryMessage];
-[LAPasscodeChangeServiceOptions newPasscode];
-[LAPasscodeChangeServiceOptions passcodePrompt];
-[LAPasscodeChangeServiceOptions passcodeSubPrompt];
-[LAPasscodeChangeServiceOptions setCurrentPasscode:];
-[LAPasscodeChangeServiceOptions setCurrentPasscodePrompt:];
-[LAPasscodeChangeServiceOptions setCurrentPasscodeSubPrompt:];
-[LAPasscodeChangeServiceOptions setPasscodeSubPrompt:];
-[LAPasscodeChangeServiceOptions setSkipSuccessNotification:];
-[LAPasscodeChangeServiceOptions skipSuccessNotification];
```
