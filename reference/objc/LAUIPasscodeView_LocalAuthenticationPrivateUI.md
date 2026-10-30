# `LAUIPasscodeView`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationPrivateUI.framework/LocalAuthenticationPrivateUI`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationPrivateUI.framework__LocalAuthenticationPrivateUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `LAUIDelegate`
- 6 instance variables, 0 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"LAContext" _context;
@"<LAUIDelegate>" _originalDelegate;
B _shouldPresentUI;
B _shouldBecomeFirstResponder;
@"UIViewController<LACPasscodeUIService>" _remoteVC;
B _isRemoteVCPrepared;
```

## Instance methods

```
-[LAUIPasscodeView initWithContext:];
-[LAUIPasscodeView viewWillDisappear:];
-[LAUIPasscodeView dealloc];
-[LAUIPasscodeView becomeFirstResponder];
-[LAUIPasscodeView resignFirstResponder];
-[LAUIPasscodeView _appDidBecomeInactive:];
-[LAUIPasscodeView viewDidAppear:];
-[LAUIPasscodeView loadView];
-[LAUIPasscodeView _appDidBecomeActive:];
-[LAUIPasscodeView event:params:reply:];
-[LAUIPasscodeView _prepareHostedSceneWithCompletion:];
-[LAUIPasscodeView _prepareRemoteUI];
-[LAUIPasscodeView _presentRemoteView];
-[LAUIPasscodeView _startRemoteView];
-[LAUIPasscodeView _toggleEditingShouldStart:];
-[LAUIPasscodeView initWithContext:shouldPresentUI:];
```
