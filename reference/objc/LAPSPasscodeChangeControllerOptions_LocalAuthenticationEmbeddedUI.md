# `LAPSPasscodeChangeControllerOptions`

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 12 instance methods, 0 class methods

## Instance variables

```
B _skipOldPasscode;
B _skipNewPasscode;
B _dismissUIAfterCompletion;
@"LACSExtractablePassword" _passcode;
@"LAExtractablePassword" _oldPasscode;
@"LAExtractablePassword" _newPasscode;
```

## Properties

```
@property (TB,N,V_skipOldPasscode) skipOldPasscode;
@property (TB,N,V_skipNewPasscode) skipNewPasscode;
@property (TB,N,V_dismissUIAfterCompletion) dismissUIAfterCompletion;
@property (T@"LACSExtractablePassword",&,N,V_passcode) passcode;
@property (T@"LAExtractablePassword",&,N,V_oldPasscode) oldPasscode;
@property (T@"LAExtractablePassword",&,N,V_newPasscode) newPasscode;
```

## Instance methods

```
-[LAPSPasscodeChangeControllerOptions passcode];
-[LAPSPasscodeChangeControllerOptions setPasscode:];
-[LAPSPasscodeChangeControllerOptions setOldPasscode:];
-[LAPSPasscodeChangeControllerOptions skipNewPasscode];
-[LAPSPasscodeChangeControllerOptions setNewPasscode:];
-[LAPSPasscodeChangeControllerOptions skipOldPasscode];
-[LAPSPasscodeChangeControllerOptions dismissUIAfterCompletion];
-[LAPSPasscodeChangeControllerOptions newPasscode];
-[LAPSPasscodeChangeControllerOptions oldPasscode];
-[LAPSPasscodeChangeControllerOptions setDismissUIAfterCompletion:];
-[LAPSPasscodeChangeControllerOptions setSkipNewPasscode:];
-[LAPSPasscodeChangeControllerOptions setSkipOldPasscode:];
```
