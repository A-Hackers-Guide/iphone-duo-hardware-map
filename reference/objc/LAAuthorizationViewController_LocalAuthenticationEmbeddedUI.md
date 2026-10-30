# `LAAuthorizationViewController`

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `LACUIAuthenticatorUIDelegate`
- 5 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"UIViewController<LACUIAuthenticatorUI>" _remoteVC;
B _isRemoteVCPrepared;
@? _completion;
@"LACUIAuthenticatorServiceConfiguration" _configuration;
@"<LAAuthorizationViewControllerDelegate>" _delegate;
```

## Properties

```
@property (TB,R,N) active;
@property (T@"<LAAuthorizationViewControllerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LAAuthorizationViewController _applicationDidEnterBackground:];
-[LAAuthorizationViewController active];
-[LAAuthorizationViewController dismiss];
-[LAAuthorizationViewController setDelegate:];
-[LAAuthorizationViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[LAAuthorizationViewController loadView];
-[LAAuthorizationViewController delegate];
-[LAAuthorizationViewController modalTransitionStyle];
-[LAAuthorizationViewController preferredStatusBarStyle];
-[LAAuthorizationViewController modalPresentationStyle];
-[LAAuthorizationViewController initWithConfiguration:completion:];
-[LAAuthorizationViewController didProvideAuthorizationRequirementWithReply:];
-[LAAuthorizationViewController presentInContainerViewController:];
-[LAAuthorizationViewController sheetDidFinishWithError:];
```
