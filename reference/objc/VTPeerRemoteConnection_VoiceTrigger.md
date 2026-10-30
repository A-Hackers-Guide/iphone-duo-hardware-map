# `VTPeerRemoteConnection`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `IDSServiceDelegate`
- 7 instance variables, 4 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSString" _identifier;
B _requireNearbyPeer;
@"NSObject<OS_dispatch_queue>" _queue;
@"IDSService" _idsService;
@"NSMutableDictionary" _completions;
@"NSMutableDictionary" _responseClasses;
@"<VTPeerRemoteConnectionDelegate>" _delegate;
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
-[VTPeerRemoteConnection service:account:identifier:didSendWithSuccess:error:];
-[VTPeerRemoteConnection initWithServiceIdentifier:];
-[VTPeerRemoteConnection _account];
-[VTPeerRemoteConnection setDelegate:];
-[VTPeerRemoteConnection serviceIdentifier];
-[VTPeerRemoteConnection service:account:incomingUnhandledProtobuf:fromID:context:];
-[VTPeerRemoteConnection _service];
-[VTPeerRemoteConnection hasPeer];
-[VTPeerRemoteConnection _destination];
-[VTPeerRemoteConnection _hasNearbyPeer];
-[VTPeerRemoteConnection _invokeCompletionForIdentifier:response:error:];
-[VTPeerRemoteConnection _pairedDevice];
-[VTPeerRemoteConnection _sendResponse:forRequestId:];
-[VTPeerRemoteConnection _wrappedSendFailureError:];
-[VTPeerRemoteConnection initWithServiceIdentifier:requireNearbyPeer:];
-[VTPeerRemoteConnection sendRequestType:nonWaking:];
```
