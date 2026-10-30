# `_UIDragMonitorSession`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 26 instance methods, 0 class methods

## Instance variables

```
B _connectedToDruid;
I _sessionIdentifier;
@"NSArray" _itemProviders;
@"NSDictionary" _previewsByItemProviderIndex;
@"<_UIDragMonitorSessionDelegate>" _delegate;
@ _userInfo;
@"<_DUIServerSessionRemoteDragManipulation>" _remoteControlProxy;
@"_UIDruidDestinationConnection" _druidDestinationConnection;
@"PBItemCollection" _itemCollection;
```

## Properties

```
@property (TI,N,V_sessionIdentifier) sessionIdentifier;
@property (T@"<_DUIServerSessionRemoteDragManipulation>",&,N,V_remoteControlProxy) remoteControlProxy;
@property (T@"_UIDruidDestinationConnection",&,N,V_druidDestinationConnection) druidDestinationConnection;
@property (TB,N,V_connectedToDruid) connectedToDruid;
@property (T@"NSArray",&,N,V_itemProviders) itemProviders;
@property (T@"PBItemCollection",&,N,V_itemCollection) itemCollection;
@property (T@"NSDictionary",&,N,V_previewsByItemProviderIndex) previewsByItemProviderIndex;
@property (T@"<_UIDragMonitorSessionDelegate>",W,N,V_delegate) delegate;
@property (T@,&,N,V_userInfo) userInfo;
```

## Instance methods

```
-[_UIDragMonitorSession connect];
-[_UIDragMonitorSession sessionIdentifier];
-[_UIDragMonitorSession userInfo];
-[_UIDragMonitorSession itemProviders];
-[_UIDragMonitorSession setUserInfo:];
-[_UIDragMonitorSession setSessionIdentifier:];
-[_UIDragMonitorSession setDelegate:];
-[_UIDragMonitorSession delegate];
-[_UIDragMonitorSession setItemProviders:];
-[_UIDragMonitorSession _updateModelWithPreviewUpdates:];
-[_UIDragMonitorSession requestPreviews];
-[_UIDragMonitorSession sawDragEndEvent];
-[_UIDragMonitorSession setPreviewsByItemProviderIndex:];
-[_UIDragMonitorSession connectedToDruid];
-[_UIDragMonitorSession druidDestinationConnection];
-[_UIDragMonitorSession initWithSessionIdentifier:remoteControlProxy:];
-[_UIDragMonitorSession itemCollection];
-[_UIDragMonitorSession performOffscreenDrop];
-[_UIDragMonitorSession previewsByItemProviderIndex];
-[_UIDragMonitorSession remoteControlProxy];
-[_UIDragMonitorSession requestDrop];
-[_UIDragMonitorSession setConnectedToDruid:];
-[_UIDragMonitorSession setDruidDestinationConnection:];
-[_UIDragMonitorSession setItemCollection:];
-[_UIDragMonitorSession setRemoteControlProxy:];
-[_UIDragMonitorSession shouldHideLocalDragDisplay];
```
