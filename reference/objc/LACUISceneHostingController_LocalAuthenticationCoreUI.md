# `LACUISceneHostingController`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCoreUI.framework/LocalAuthenticationCoreUI`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCoreUI.framework__LocalAuthenticationCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `_UISceneHostingControllerDelegate`, `_UISceneHostingReconnectingActivationControllerDelegate`, `LACUIHostedSceneActionHandling`, `LACUIHostedSceneActionSending`
- 5 instance variables, 6 properties, 15 instance methods, 0 class methods

## Instance variables

```
B _didConnect;
@? _preparationHandler;
@"_UISceneHostingController" _sceneHostingController;
@"LACAngelHostedSceneConfiguration" _configuration;
@"<LACUISceneHostingControllerDelegate>" _sceneConnectionDelegate;
```

## Properties

```
@property (T@"LACAngelHostedSceneConfiguration",R,N,V_configuration) configuration;
@property (T@"<LACUISceneHostingControllerDelegate>",W,N,V_sceneConnectionDelegate) sceneConnectionDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACUISceneHostingController clientIsReady];
-[LACUISceneHostingController handlesAction:];
-[LACUISceneHostingController handleAction:completion:];
-[LACUISceneHostingController sendAction:completion:];
-[LACUISceneHostingController initWithConfiguration:];
-[LACUISceneHostingController _canShowWhileLocked];
-[LACUISceneHostingController configuration];
-[LACUISceneHostingController _remoteViewController];
-[LACUISceneHostingController prepareRemoteSceneWithCompletion:];
-[LACUISceneHostingController _remoteView];
-[LACUISceneHostingController _sendConnectionEndpoint];
-[LACUISceneHostingController _setDefaultContentSize];
-[LACUISceneHostingController hostingControllerDidReconnect:];
-[LACUISceneHostingController sceneConnectionDelegate];
-[LACUISceneHostingController setSceneConnectionDelegate:];
```
