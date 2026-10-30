# `LACUIPasscodeViewType` (protocol)

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCoreUI.framework/LocalAuthenticationCoreUI`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCoreUI.framework__LocalAuthenticationCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 3 properties, 7 instance methods, 0 class methods

## Properties

```
@property (T@"<LACUIPasscodeViewDelegate>",W,N) delegate;
@property (T@"LACUIPasscodeViewState",&,N) state;
@property (T@"NSString",R,N) passcode;
```

## Instance methods

```
-[LACUIPasscodeViewType setState:];
-[LACUIPasscodeViewType passcode];
-[LACUIPasscodeViewType setDelegate:];
-[LACUIPasscodeViewType delegate];
-[LACUIPasscodeViewType state];
-[LACUIPasscodeViewType animateToFailureStateWithCompletion:];
-[LACUIPasscodeViewType animateToSuccessStateWithCompletion:];
```
