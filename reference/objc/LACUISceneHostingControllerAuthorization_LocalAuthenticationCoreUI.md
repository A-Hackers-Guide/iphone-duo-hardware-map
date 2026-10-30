# `LACUISceneHostingControllerAuthorization`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCoreUI.framework/LocalAuthenticationCoreUI`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCoreUI.framework__LocalAuthenticationCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `LACUISceneHostingController`
- Protocols: `LACUISceneHostingControllerDelegate`, `LACUIAuthenticatorUI`
- 1 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"<LACUIAuthenticatorUIDelegate>" _delegate;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<LACUIAuthenticatorUIDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[LACUISceneHostingControllerAuthorization init];
-[LACUISceneHostingControllerAuthorization handlesAction:];
-[LACUISceneHostingControllerAuthorization handleAction:completion:];
-[LACUISceneHostingControllerAuthorization setDelegate:];
-[LACUISceneHostingControllerAuthorization delegate];
-[LACUISceneHostingControllerAuthorization startWithConfiguration:reply:];
-[LACUISceneHostingControllerAuthorization stopWithReply:];
-[LACUISceneHostingControllerAuthorization authenticatorServiceDidFinishWithError:];
-[LACUISceneHostingControllerAuthorization authenticatorServiceDidObtainAuthenticationWithReply:];
-[LACUISceneHostingControllerAuthorization sceneHostingControllerDidReconnect:];
```
