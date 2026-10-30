# `_TtC25LocalAuthenticationCoreUI22LACUIPasscodeViewModel`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCoreUI.framework/LocalAuthenticationCoreUI`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCoreUI.framework__LocalAuthenticationCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACUIPasscodeViewModelType`
- 24 instance variables, 8 properties, 20 instance methods, 0 class methods

## Instance variables

```
(objc_protocol 0x28d599240) ? _delegate;
_$sSo6UIViewCSg _accessoryView;
_$sSS _navigationTitle;
_$sSS _title;
_$sSS _subtitle;
_$sSS _footer;
_$sSSSg _errorMessage;
Swift.Bool _showSpinner;
_$sSo44LACUIPasscodeServiceOptionsViewConfigurationCSg _optionsConfiguration;
_$sSSSg _callerBundleIdentifier;
_$sSSSg _callerIconPath;
_$sSSSg4path_AA16bundleIdentifier LocalAuthenticationCoreUI.LACUIImageConfiguration _$sSg13configurationtSg cachedCallerIconConfiguration;
LocalAuthenticationCoreUI.LACUIPasscodeSoundPlayer ? $__lazy_storage_$_soundPlayer;
__C.LACUIPasscodeViewModelState _state;
Swift.Bool _lockedOut;
_$sSS _passcode;
LocalAuthenticationCoreUI.LACUIPasscodeViewMetrics _viewMetrics;
_$sSi _failedAttempts;
LocalAuthenticationCoreUI.LACUIPasscodeViewModelEditableState _editableState;
LocalAuthenticationCoreUI.LACUILockViewModel _lockViewModel;
_$sSo11LACPasscodeC _passcodeType;
_$sShySo19UIGestureRecognizerCG _systemGestures;
Swift.Bool _shouldShowCancel;
Observation.ObservationRegistrar _$observationRegistrar;
```

## Properties

```
@property (T@"<LACUIPasscodeViewModelDelegate>",N,W) delegate;
@property (T@"NSString",N,C) title;
@property (T@"NSString",N,C) subtitle;
@property (T@"NSString",N,C) callerBundleIdentifier;
@property (T@"NSString",N,C) callerIconPath;
@property (TQ,N) state;
@property (T@"NSString",N,C) passcode;
@property (T@"LACPasscode",N,&) passcodeType;
```

## Instance methods

```
-[_TtC25LocalAuthenticationCoreUI22LACUIPasscodeViewModel clear];
-[_TtC25LocalAuthenticationCoreUI22LACUIPasscodeViewModel setState:];
-[_TtC25LocalAuthenticationCoreUI22LACUIPasscodeViewModel passcode];
-[_TtC25LocalAuthenticationCoreUI22LACUIPasscodeViewModel subtitle];
-[_TtC25LocalAuthenticationCoreUI22LACUIPasscodeViewModel init];
-[_TtC25LocalAuthenticationCoreUI22LACUIPasscodeViewModel setSubtitle:];
-[_TtC25LocalAuthenticationCoreUI22LACUIPasscodeViewModel setDelegate:];
-[_TtC25LocalAuthenticationCoreUI22LACUIPasscodeViewModel title];
-[_TtC25LocalAuthenticationCoreUI22LACUIPasscodeViewModel delegate];
-[_TtC25LocalAuthenticationCoreUI22LACUIPasscodeViewModel setTitle:];
-[_TtC25LocalAuthenticationCoreUI22LACUIPasscodeViewModel setPasscodeType:];
-[_TtC25LocalAuthenticationCoreUI22LACUIPasscodeViewModel state];
-[_TtC25LocalAuthenticationCoreUI22LACUIPasscodeViewModel passcodeType];
-[_TtC25LocalAuthenticationCoreUI22LACUIPasscodeViewModel setPasscode:];
-[_TtC25LocalAuthenticationCoreUI22LACUIPasscodeViewModel callerBundleIdentifier];
-[_TtC25LocalAuthenticationCoreUI22LACUIPasscodeViewModel callerIconPath];
-[_TtC25LocalAuthenticationCoreUI22LACUIPasscodeViewModel setCallerBundleIdentifier:];
-[_TtC25LocalAuthenticationCoreUI22LACUIPasscodeViewModel registerPasscodeVerificationFailureWithCompletion:];
-[_TtC25LocalAuthenticationCoreUI22LACUIPasscodeViewModel registerPasscodeVerificationSuccessWithCompletion:];
-[_TtC25LocalAuthenticationCoreUI22LACUIPasscodeViewModel setCallerIconPath:];
```
