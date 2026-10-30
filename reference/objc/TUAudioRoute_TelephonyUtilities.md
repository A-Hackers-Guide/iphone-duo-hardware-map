# `TUAudioRoute`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `TURoute`
- 4 instance variables, 6 properties, 40 instance methods, 1 class methods

## Instance variables

```
B _modelIdentifierCached;
@"NSString" _avAudioRouteName;
@"NSString" _cachedModelIdentifier;
@"NSDictionary" _route;
```

## Properties

```
@property (T@"NSString",R,C,N,V_avAudioRouteName) avAudioRouteName;
@property (T@"NSString",R,C,N) mxBluetoothProductIdentifier;
@property (TB,R,N,GisHeadphoneJackConnected) headphoneJackConnected;
@property (T@"NSString",C,N,V_cachedModelIdentifier) cachedModelIdentifier;
@property (TB,N,V_modelIdentifierCached) modelIdentifierCached;
@property (T@"NSDictionary",R,C,N,V_route) route;
```

## Class methods

```
+[TUAudioRoute supportsSecureCoding];
```

## Instance methods

```
-[TUAudioRoute customDescription];
-[TUAudioRoute route];
-[TUAudioRoute isBluetoothLE];
-[TUAudioRoute isPreferred];
-[TUAudioRoute initWithDictionary:];
-[TUAudioRoute modelIdentifier];
-[TUAudioRoute isSiblingRoutePresent];
-[TUAudioRoute deviceType];
-[TUAudioRoute isCarAudio];
-[TUAudioRoute isCurrentlyPicked];
-[TUAudioRoute isDefaultRoute];
-[TUAudioRoute setCachedModelIdentifier:];
-[TUAudioRoute supportsHighQualityVoiceWithMedia];
-[TUAudioRoute isWiredHeadphones];
-[TUAudioRoute avAudioRouteName];
-[TUAudioRoute isInEarDetectionEnabled];
-[TUAudioRoute identifiersOfOtherConnectedDevices];
-[TUAudioRoute isSpeaker];
-[TUAudioRoute _routeTypeEqualTo:];
-[TUAudioRoute modelIdentifierCached];
-[TUAudioRoute cachedModelIdentifier];
-[TUAudioRoute isPartnerRouteRoutable];
-[TUAudioRoute isBluetooth];
-[TUAudioRoute isHandset];
-[TUAudioRoute encodeWithCoder:];
-[TUAudioRoute mxBluetoothProductIdentifier];
-[TUAudioRoute isInEarDetectionSupported];
-[TUAudioRoute isHeadphoneJackConnected];
-[TUAudioRoute initWithCoder:];
-[TUAudioRoute isA2DPRoute];
-[TUAudioRoute isPreferredAndActive];
-[TUAudioRoute isReceiver];
-[TUAudioRoute setModelIdentifierCached:];
-[TUAudioRoute isBluetoothManaged];
-[TUAudioRoute isWiredHeadset];
-[TUAudioRoute isAirTunes];
-[TUAudioRoute bluetoothProductIdentifierAsUInt32];
-[TUAudioRoute supportsSharePlay];
-[TUAudioRoute bluetoothEndpointType];
-[TUAudioRoute isWirelessHeadset];
```
