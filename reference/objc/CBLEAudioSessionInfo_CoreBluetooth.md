# `CBLEAudioSessionInfo`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"CBCoordinatedSetInfo" _coordinatedSetInfo;
@"NSUUID" _audioSessionIdentifier;
q _sessionState;
@"NSMutableArray" _connectedIdentifiers;
@"NSMutableDictionary" _locations;
```

## Properties

```
@property (T@"CBCoordinatedSetInfo",R,N,V_coordinatedSetInfo) coordinatedSetInfo;
@property (T@"NSUUID",R,N,V_audioSessionIdentifier) audioSessionIdentifier;
@property (Tq,R,N,V_sessionState) sessionState;
@property (T@"NSMutableArray",R,N,V_connectedIdentifiers) connectedIdentifiers;
@property (T@"NSMutableDictionary",R,N,V_locations) locations;
```

## Instance methods

```
-[CBLEAudioSessionInfo locations];
-[CBLEAudioSessionInfo sessionState];
-[CBLEAudioSessionInfo initWithSession:];
-[CBLEAudioSessionInfo copyWithZone:];
-[CBLEAudioSessionInfo audioSessionIdentifier];
-[CBLEAudioSessionInfo connectedIdentifiers];
-[CBLEAudioSessionInfo initWithInfo:withSessionId:withState:withCoordIds:withLocation:];
-[CBLEAudioSessionInfo coordinatedSetInfo];
-[CBLEAudioSessionInfo retrieveConnectedLEAudioPeripheralIdentifiers];
```
