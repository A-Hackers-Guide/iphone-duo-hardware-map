# `WiFiP2PTrafficRegistrationReservation`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WiFiP2PXPCConnectionDelegate`
- 4 instance variables, 6 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"WiFiP2PXPCConnection" _xpcConnection;
Q _enabledCount;
B _showsUIAlertOnError;
@"NSString" _service;
```

## Properties

```
@property (T@"NSString",R,N,V_service) service;
@property (TB,N,V_showsUIAlertOnError) showsUIAlertOnError;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[WiFiP2PTrafficRegistrationReservation activateWithCompletion:];
-[WiFiP2PTrafficRegistrationReservation startConnectionUsingProxy:completionHandler:];
-[WiFiP2PTrafficRegistrationReservation remoteObjectInterface];
-[WiFiP2PTrafficRegistrationReservation invalidate];
-[WiFiP2PTrafficRegistrationReservation initForService:];
-[WiFiP2PTrafficRegistrationReservation service];
-[WiFiP2PTrafficRegistrationReservation setShowsUIAlertOnError:];
-[WiFiP2PTrafficRegistrationReservation handleConnectionEstablishedWithProxy:];
-[WiFiP2PTrafficRegistrationReservation showsUIAlertOnError];
-[WiFiP2PTrafficRegistrationReservation trafficRegistrationConfiguration];
```
