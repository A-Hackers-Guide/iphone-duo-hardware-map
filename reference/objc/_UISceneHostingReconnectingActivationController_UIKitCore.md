# `_UISceneHostingReconnectingActivationController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UISceneHostingActivationControlling`
- 6 instance variables, 7 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"<_UISceneHostingActivationHandle>" _activationHandle;
@"_UISimpleTimedInhibitor" _activationInhibitor;
@"UIScene" _parentScene;
Q _maxRetryCount;
d _retryTimeout;
@"<_UISceneHostingReconnectingActivationControllerDelegate>" _delegate;
```

## Properties

```
@property (TQ,N,V_maxRetryCount) maxRetryCount;
@property (Td,N,V_retryTimeout) retryTimeout;
@property (T@"<_UISceneHostingReconnectingActivationControllerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UISceneHostingReconnectingActivationController setMaxRetryCount:];
-[_UISceneHostingReconnectingActivationController endManagingHostedSceneActivationForHostingController:];
-[_UISceneHostingReconnectingActivationController init];
-[_UISceneHostingReconnectingActivationController setRetryTimeout:];
-[_UISceneHostingReconnectingActivationController maxRetryCount];
-[_UISceneHostingReconnectingActivationController setDelegate:];
-[_UISceneHostingReconnectingActivationController activationHandleDidUpdate:forHostingController:];
-[_UISceneHostingReconnectingActivationController _performActivationForHostingController:];
-[_UISceneHostingReconnectingActivationController delegate];
-[_UISceneHostingReconnectingActivationController _setupActivationInhibitor];
-[_UISceneHostingReconnectingActivationController beginManagingHostedSceneActivationUsingHandle:forHostingController:];
-[_UISceneHostingReconnectingActivationController retryTimeout];
-[_UISceneHostingReconnectingActivationController hostingController:isMovingToParentScene:];
```
