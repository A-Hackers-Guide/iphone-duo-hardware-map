# `SBStateDumpMultipeerController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MCSessionDelegate`, `MCNearbyServiceAdvertiserDelegate`
- 5 instance variables, 5 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"MCPeerID" _localPeerID;
@"MCSession" _session;
@"MCNearbyServiceAdvertiser" _advertiser;
@"NSMutableDictionary" _clientPeers;
@"<SBStateDumpMultipeerControllerDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBStateDumpMultipeerControllerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBStateDumpMultipeerController connectedClients];
-[SBStateDumpMultipeerController init];
-[SBStateDumpMultipeerController dealloc];
-[SBStateDumpMultipeerController isAdvertising];
-[SBStateDumpMultipeerController setDelegate:];
-[SBStateDumpMultipeerController stopAdvertising];
-[SBStateDumpMultipeerController delegate];
-[SBStateDumpMultipeerController advertiser:didReceiveInvitationFromPeer:withContext:invitationHandler:];
-[SBStateDumpMultipeerController session:didFinishReceivingResourceWithName:fromPeer:atURL:withError:];
-[SBStateDumpMultipeerController session:didReceiveData:fromPeer:];
-[SBStateDumpMultipeerController session:didReceiveStream:withName:fromPeer:];
-[SBStateDumpMultipeerController session:didStartReceivingResourceWithName:fromPeer:withProgress:];
-[SBStateDumpMultipeerController session:peer:didChangeState:];
-[SBStateDumpMultipeerController sendState:forDomain:toClients:];
-[SBStateDumpMultipeerController startAdvertising];
-[SBStateDumpMultipeerController transferFileAtURL:withName:toClient:completion:];
```
