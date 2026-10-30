# `LAPSPasscodeChangeUI` (protocol)

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 1 properties, 6 instance methods, 0 class methods

## Properties

```
@property (T@"<LAPSPasscodeChangeUIDelegate>",W,N) delegate;
```

## Instance methods

```
-[LAPSPasscodeChangeUI setDelegate:];
-[LAPSPasscodeChangeUI delegate];
-[LAPSPasscodeChangeUI deactivateWithCompletion:];
-[LAPSPasscodeChangeUI fetchNewPasscode:completion:];
-[LAPSPasscodeChangeUI fetchOldPasscode:completion:];
-[LAPSPasscodeChangeUI presentAlertWithTitle:message:button:completion:];
```
