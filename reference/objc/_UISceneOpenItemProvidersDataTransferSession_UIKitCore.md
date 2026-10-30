# `_UISceneOpenItemProvidersDataTransferSession`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIDataTransferMonitorDelegate`
- 4 instance variables, 8 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"<_UISceneOpenItemProvidersDataTransferSessionDelegate>" _delegate;
@"_UIDataTransferMonitor" _monitor;
@"NSArray" _itemProviders;
@"_DUIDragContinuation" _continuation;
```

## Properties

```
@property (T@"_UIDataTransferMonitor",&,N,V_monitor) monitor;
@property (T@"NSArray",&,N,V_itemProviders) itemProviders;
@property (T@"_DUIDragContinuation",&,N,V_continuation) continuation;
@property (T@"<_UISceneOpenItemProvidersDataTransferSessionDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UISceneOpenItemProvidersDataTransferSession monitor];
-[_UISceneOpenItemProvidersDataTransferSession setMonitor:];
-[_UISceneOpenItemProvidersDataTransferSession itemProviders];
-[_UISceneOpenItemProvidersDataTransferSession setDelegate:];
-[_UISceneOpenItemProvidersDataTransferSession delegate];
-[_UISceneOpenItemProvidersDataTransferSession setItemProviders:];
-[_UISceneOpenItemProvidersDataTransferSession continuation];
-[_UISceneOpenItemProvidersDataTransferSession dataTransferMonitorBeganTransfers:];
-[_UISceneOpenItemProvidersDataTransferSession dataTransferMonitorFinishedTransfers:];
-[_UISceneOpenItemProvidersDataTransferSession didFinishSendingRequests];
-[_UISceneOpenItemProvidersDataTransferSession initWithItemProviders:continuation:];
-[_UISceneOpenItemProvidersDataTransferSession setContinuation:];
```
