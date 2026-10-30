# `SBExternalDisplayService`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSDisplayLayoutPublisherObserving`, `_SBExternalDisplayServiceConnectionListenerDelegate`
- 8 instance variables, 4 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"<_SBExternalDisplayServiceConnectionListening>" _serviceConnectionListener;
@"SBSConnectedDisplayInfoFactory" _connectedDisplayInfoFactory;
@"SBExternalDisplayLayoutPublisherFactory" _layoutPublisherFactory;
@"NSObject<OS_dispatch_queue>" _serviceQueue;
@"SBExternalDisplayDefaults" _defaults;
@"NSMutableDictionary" _rootToConnectedParticipants;
@"NSMutableDictionary" _rootToLayoutPublisher;
@"NSHashTable" _observers;
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
-[SBExternalDisplayService removeObserver:];
-[SBExternalDisplayService init];
-[SBExternalDisplayService dealloc];
-[SBExternalDisplayService publisher:didUpdateLayout:withTransition:];
-[SBExternalDisplayService addObserver:];
-[SBExternalDisplayService activate];
-[SBExternalDisplayService _createLayoutPublisherForRootDisplayIdentityIfNeeded:displayConfiguration:];
-[SBExternalDisplayService _extendedModeDisplayConfigurationForHardwareIdentifier:error:];
-[SBExternalDisplayService _invalidateLayoutPublisherForRootDisplayIdentity:];
-[SBExternalDisplayService _notifyOfPropertyChangesForDisplayConfiguration:requestingClient:];
-[SBExternalDisplayService client:getConnectedDisplayInfoWithCompletion:];
-[SBExternalDisplayService client:setDisplayArrangement:forDisplay:];
-[SBExternalDisplayService client:setDisplayMirroringEnabled:forDisplay:];
-[SBExternalDisplayService client:setDisplayModeSettings:forDisplay:options:completionHandler:];
-[SBExternalDisplayService didConnectParticipant:];
-[SBExternalDisplayService didUpdateParticipant:];
-[SBExternalDisplayService initWithServiceListenerFactory:connectedDisplayInfoFactory:layoutPublisherFactory:defaults:];
-[SBExternalDisplayService layoutPublisherForRootDisplayIdentity:];
-[SBExternalDisplayService preferredArrangementOfDisplay:relativeTo:];
-[SBExternalDisplayService willDisconnectParticipant:];
```
