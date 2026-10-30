# `NINearbyAccessoryConfiguration`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NIConfiguration`
- 8 instance variables, 9 properties, 28 instance methods, 1 class methods

## Instance variables

```
@"NSData" _rawData;
B _cameraAssistanceEnabled;
@"NIDiscoveryToken" _accessoryDiscoveryToken;
@"NSUUID" _bluetoothDeviceIdentifier;
@"NSUUID" _btcsBluetoothDeviceIdentifier;
@"NSUUID" _previousBTCSBluetoothDeviceIdentifier;
@"NSDictionary" _debugParameters;
q _backgroundMode;
```

## Properties

```
@property (T@"NSData",R,C) accessoryConfigData;
@property (T@"NSUUID",C,V_bluetoothDeviceIdentifier) bluetoothDeviceIdentifier;
@property (T@"NSUUID",C,V_btcsBluetoothDeviceIdentifier) btcsBluetoothDeviceIdentifier;
@property (T@"NSUUID",C,V_previousBTCSBluetoothDeviceIdentifier) previousBTCSBluetoothDeviceIdentifier;
@property (T@"NSDictionary",C,V_debugParameters) debugParameters;
@property (TB,R) dataExchangeDisabledAndUsingParameterOverrides;
@property (Tq,N,V_backgroundMode) backgroundMode;
@property (T@"NIDiscoveryToken",R,C,N,V_accessoryDiscoveryToken) accessoryDiscoveryToken;
@property (TB,N,GisCameraAssistanceEnabled,V_cameraAssistanceEnabled) cameraAssistanceEnabled;
```

## Class methods

```
+[NINearbyAccessoryConfiguration supportsSecureCoding];
```

## Instance methods

```
-[NINearbyAccessoryConfiguration setCameraAssistanceEnabled:];
-[NINearbyAccessoryConfiguration descriptionInternal];
-[NINearbyAccessoryConfiguration initWithData:error:];
-[NINearbyAccessoryConfiguration encodeWithCoder:];
-[NINearbyAccessoryConfiguration _internalIsCameraAssistanceEnabled];
-[NINearbyAccessoryConfiguration hash];
-[NINearbyAccessoryConfiguration isCameraAssistanceEnabled];
-[NINearbyAccessoryConfiguration description];
-[NINearbyAccessoryConfiguration initWithCoder:];
-[NINearbyAccessoryConfiguration copyWithZone:];
-[NINearbyAccessoryConfiguration isEqual:];
-[NINearbyAccessoryConfiguration backgroundMode];
-[NINearbyAccessoryConfiguration setBackgroundMode:];
-[NINearbyAccessoryConfiguration debugParameters];
-[NINearbyAccessoryConfiguration _internalIsPowerAssertionRequired];
-[NINearbyAccessoryConfiguration accessoryConfigData];
-[NINearbyAccessoryConfiguration accessoryDiscoveryToken];
-[NINearbyAccessoryConfiguration bluetoothDeviceIdentifier];
-[NINearbyAccessoryConfiguration btcsBluetoothDeviceIdentifier];
-[NINearbyAccessoryConfiguration dataExchangeDisabledAndUsingParameterOverrides];
-[NINearbyAccessoryConfiguration initWithAccessoryData:bluetoothPeerIdentifier:error:];
-[NINearbyAccessoryConfiguration initWithBluetoothChannelSoundingIdentifier:previousBluetoothIdentifier:];
-[NINearbyAccessoryConfiguration initWithDataExchangeDisabledAndUsingParameterOverrides:];
-[NINearbyAccessoryConfiguration previousBTCSBluetoothDeviceIdentifier];
-[NINearbyAccessoryConfiguration setBluetoothDeviceIdentifier:];
-[NINearbyAccessoryConfiguration setBtcsBluetoothDeviceIdentifier:];
-[NINearbyAccessoryConfiguration setDebugParameters:];
-[NINearbyAccessoryConfiguration setPreviousBTCSBluetoothDeviceIdentifier:];
```
