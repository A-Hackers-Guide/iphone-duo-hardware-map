# `CBPairingAgent`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 28 instance methods, 0 class methods

## Instance variables

```
B _useOOBMode;
@"<CBPairingAgentDelegate>" _delegate;
@"<CBPairingAgentParentDelegate>" _parentManager;
```

## Properties

```
@property (T@"<CBPairingAgentParentDelegate>",W,N,V_parentManager) parentManager;
@property (T@"<CBPairingAgentDelegate>",W,N,V_delegate) delegate;
@property (TB,N,V_useOOBMode) useOOBMode;
```

## Instance methods

```
-[CBPairingAgent unpairPeer:options:];
-[CBPairingAgent unpairPeer:];
-[CBPairingAgent observeValueForKeyPath:ofObject:change:context:];
-[CBPairingAgent pairPeer:useMITM:];
-[CBPairingAgent handleUnpaired:];
-[CBPairingAgent updateRegistration];
-[CBPairingAgent dealloc];
-[CBPairingAgent initWithParentManager:];
-[CBPairingAgent retrieveOOBDataForPeer:];
-[CBPairingAgent setGlobalTemporaryLTK:useCase:];
-[CBPairingAgent isPeerCloudPaired:];
-[CBPairingAgent setDelegate:];
-[CBPairingAgent isPeerMagicPaired:];
-[CBPairingAgent removeGlobalTemporaryLTK];
-[CBPairingAgent delegate];
-[CBPairingAgent handlePairingRequested:];
-[CBPairingAgent setOOBPairingEnabled:forPeer:];
-[CBPairingAgent pairPeer:options:];
-[CBPairingAgent retrievePairedPeers];
-[CBPairingAgent setUseOOBMode:];
-[CBPairingAgent handlePairingMessage:args:];
-[CBPairingAgent respondToPairingRequest:type:accept:data:];
-[CBPairingAgent handlePairingCompleted:];
-[CBPairingAgent parentManager];
-[CBPairingAgent useOOBMode];
-[CBPairingAgent pairPeer:];
-[CBPairingAgent setParentManager:];
-[CBPairingAgent isPeerPaired:];
```
