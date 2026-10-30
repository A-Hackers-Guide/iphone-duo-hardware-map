# `NetworkDriverSession`

- Image: [`/System/Library/Frameworks/CoreAudioKit.framework/CoreAudioKit`](../userland/System__Library__Frameworks__CoreAudioKit.framework__CoreAudioKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 11 properties, 59 instance methods, 1 class methods

## Instance variables

```
I mDevice;
I mEntity;
{RTPEndpoint="endpoint"I"uid"i"thruConnection"I"connectedUID"i} mSource;
{RTPEndpoint="endpoint"I"uid"i"thruConnection"I"connectedUID"i} mDest;
@"NSString" mLocalName;
@"NSMutableDictionary" mProperties;
@"NSMutableArray" mPeers;
i _sessionType;
```

## Properties

```
@property (TQ,N) index;
@property (TI,R,N) entityID;
@property (Ti,R,N,V_sessionType) sessionType;
@property (T@"NSMutableArray",R,N) peers;
@property (Ti,N) joinPolicy;
@property (T@"NSString",&,N) UMPEndpointName;
@property (T@"NSString",R,N) productInstanceID;
@property (Ti,N) protocolID;
@property (Ti,N) authenticationMethod;
@property (T@"NSString",C,N) sharedSecret;
@property (T@"NSDictionary",C,N) userAuthData;
```

## Class methods

```
+[NetworkDriverSession getLocalAddresses];
```

## Instance methods

```
-[NetworkDriverSession peers];
-[NetworkDriverSession active];
-[NetworkDriverSession networkName];
-[NetworkDriverSession addPeer:];
-[NetworkDriverSession localName];
-[NetworkDriverSession peerAtIndex:];
-[NetworkDriverSession setLocalPort:];
-[NetworkDriverSession setActive:];
-[NetworkDriverSession index];
-[NetworkDriverSession setIndex:];
-[NetworkDriverSession sessionType];
-[NetworkDriverSession localPort];
-[NetworkDriverSession protocolID];
-[NetworkDriverSession peerCount];
-[NetworkDriverSession description];
-[NetworkDriverSession setNetworkName:];
-[NetworkDriverSession authenticationMethod];
-[NetworkDriverSession setLocalName:];
-[NetworkDriverSession setSharedSecret:];
-[NetworkDriverSession sharedSecret];
-[NetworkDriverSession setAuthenticationMethod:];
-[NetworkDriverSession entityID];
-[NetworkDriverSession deleteSession];
-[NetworkDriverSession getPeerLatency:];
-[NetworkDriverSession UMPEndpointName];
-[NetworkDriverSession addPersistentPeer:address:];
-[NetworkDriverSession connectToEntry:withAuthorization:];
-[NetworkDriverSession connectToService:withAuthorization:];
-[NetworkDriverSession deletePeerAtIndex:];
-[NetworkDriverSession destinationEndpoint];
-[NetworkDriverSession entityInfoKey];
-[NetworkDriverSession getLocalAddressesWithInterfaceInfo];
-[NetworkDriverSession getParticipantNames];
-[NetworkDriverSession hasPersistentPeer:];
-[NetworkDriverSession indexOfPersistentPeerInArray:withAddress:];
-[NetworkDriverSession initNew:computerName:sessionType:];
-[NetworkDriverSession initWithExistingMIDIEntity:device:];
-[NetworkDriverSession joinPolicy];
-[NetworkDriverSession persistentPeers:];
-[NetworkDriverSession productInstanceID];
-[NetworkDriverSession prunePersistentPeers:];
-[NetworkDriverSession removePersistentPeer:];
-[NetworkDriverSession setJoinPolicy:];
-[NetworkDriverSession setPeerLatency:latency:];
-[NetworkDriverSession setPeerProperty:value:forKey:];
-[NetworkDriverSession setProtocolID:];
-[NetworkDriverSession setStateToEntity];
-[NetworkDriverSession setThruDest:];
-[NetworkDriverSession setThruSource:];
-[NetworkDriverSession setUMPEndpointName:];
-[NetworkDriverSession setUserAuthData:];
-[NetworkDriverSession sourceEndpoint];
-[NetworkDriverSession takeThruConnection:params:];
-[NetworkDriverSession thruDest];
-[NetworkDriverSession thruSource];
-[NetworkDriverSession updateAuthDictionaryEntry:value:];
-[NetworkDriverSession updateFromEntity];
-[NetworkDriverSession updateThru:];
-[NetworkDriverSession userAuthData];
```
