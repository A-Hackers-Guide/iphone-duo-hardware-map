# `_UIViewServiceHostSceneComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `_UISceneHostingActivationControlling`, `FBSceneObserver`
- 3 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"<_UISceneHostingActivationHandle>" _activationHandle;
{?="viewServiceClientIsReady"b1} _flags;
@"<_UIViewServiceHostSceneComponentDelegate>" _delegate;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIViewServiceHostSceneComponent sceneDidInvalidate:withContext:];
-[_UIViewServiceHostSceneComponent endManagingHostedSceneActivationForHostingController:];
-[_UIViewServiceHostSceneComponent evaluateClientIsReady];
-[_UIViewServiceHostSceneComponent sceneContentStateDidChange:];
-[_UIViewServiceHostSceneComponent activationHandleDidUpdate:forHostingController:];
-[_UIViewServiceHostSceneComponent beginManagingHostedSceneActivationUsingHandle:forHostingController:];
-[_UIViewServiceHostSceneComponent scene:didUpdateClientSettings:];
```
