# `LACUIPasscodeViewModelType` (protocol)

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCoreUI.framework/LocalAuthenticationCoreUI`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCoreUI.framework__LocalAuthenticationCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 8 properties, 17 instance methods, 0 class methods

## Properties

```
@property (T@"<LACUIPasscodeViewModelDelegate>",W,N) delegate;
@property (T@"NSString",R,N) passcode;
@property (T@"LACPasscode",R,N) passcodeType;
@property (T@"NSString",&,N) callerBundleIdentifier;
@property (T@"NSString",&,N) callerIconPath;
@property (T@"NSString",&,N) title;
@property (T@"NSString",&,N) subtitle;
@property (TQ,N) state;
```

## Instance methods

```
-[LACUIPasscodeViewModelType clear];
-[LACUIPasscodeViewModelType setState:];
-[LACUIPasscodeViewModelType passcode];
-[LACUIPasscodeViewModelType subtitle];
-[LACUIPasscodeViewModelType setSubtitle:];
-[LACUIPasscodeViewModelType setDelegate:];
-[LACUIPasscodeViewModelType title];
-[LACUIPasscodeViewModelType delegate];
-[LACUIPasscodeViewModelType setTitle:];
-[LACUIPasscodeViewModelType state];
-[LACUIPasscodeViewModelType passcodeType];
-[LACUIPasscodeViewModelType callerBundleIdentifier];
-[LACUIPasscodeViewModelType callerIconPath];
-[LACUIPasscodeViewModelType setCallerBundleIdentifier:];
-[LACUIPasscodeViewModelType registerPasscodeVerificationFailureWithCompletion:];
-[LACUIPasscodeViewModelType registerPasscodeVerificationSuccessWithCompletion:];
-[LACUIPasscodeViewModelType setCallerIconPath:];
```
