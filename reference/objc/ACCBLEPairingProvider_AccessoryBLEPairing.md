# `ACCBLEPairingProvider`

- Image: [`/System/Library/PrivateFrameworks/AccessoryBLEPairing.framework/AccessoryBLEPairing`](../userland/System__Library__PrivateFrameworks__AccessoryBLEPairing.framework__AccessoryBLEPairing.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 3 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"<ACCBLEPairingProviderProtocol>" _delegate;
@"NSString" _delegateUUID;
```

## Properties

```
@property (T@"NSString",&,N,V_delegateUUID) delegateUUID;
@property (T@"<ACCBLEPairingProviderProtocol>",W,N,V_delegate) delegate;
@property (Ti,N) lastScorpiusDetectType;
```

## Instance methods

```
-[ACCBLEPairingProvider initWithDelegate:];
-[ACCBLEPairingProvider dealloc];
-[ACCBLEPairingProvider setDelegate:];
-[ACCBLEPairingProvider delegate];
-[ACCBLEPairingProvider delegateUUID];
-[ACCBLEPairingProvider devicePairingData:blePairingUUID:pairType:pairData:];
-[ACCBLEPairingProvider deviceStateUpdate:blePairingUUID:bRadioOn:pairState:bPairModeOn:];
-[ACCBLEPairingProvider deviceUpdatePairingInfo:blePairingUUID:pairType:pairInfo:];
-[ACCBLEPairingProvider lastScorpiusDetectType];
-[ACCBLEPairingProvider setDelegateUUID:];
-[ACCBLEPairingProvider setLastScorpiusDetectType:];
-[ACCBLEPairingProvider startBLEUpdates:blePairingUUID:pairType:bRadioUpdatesOn:bPairInfoUpdatesOn:];
-[ACCBLEPairingProvider stopBLEUpdates:blePairingUUID:];
-[ACCBLEPairingProvider updateResolvedAccessoryBTAddress:blePairingUUID:btAddress:];
```
