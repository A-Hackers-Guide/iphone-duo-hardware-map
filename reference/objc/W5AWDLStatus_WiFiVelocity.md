# `W5AWDLStatus`

- Image: [`/System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity`](../userland/System__Library__PrivateFrameworks__WiFiVelocity.framework__WiFiVelocity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 18 instance variables, 18 properties, 44 instance methods, 1 class methods

## Instance variables

```
B _power;
B _isAWDLRealTimeMode;
@"NSString" _macAddress;
@"NSString" _hardwareMACAddress;
@"NSString" _interfaceName;
@"NSArray" _ipv6Addresses;
@"NSData" _awdlSyncEnabled;
@"NSData" _awdlSyncState;
@"NSData" _awdlSyncChannelSequence;
@"NSData" _awdlStrategy;
@"NSData" _awdlElectionParameters;
@"NSData" _awdlMasterChannel;
@"NSData" _awdlSecondaryMasterChannel;
@"NSData" _awdlOpMode;
@"NSData" _awdlSyncParameters;
@"NSData" _awdlPeerDatabase;
@"NSData" _awdlSidecarDiagnostics;
q _airDropDiscoverableMode;
```

## Properties

```
@property (T@"NSString",C,N,V_macAddress) macAddress;
@property (T@"NSString",C,N,V_hardwareMACAddress) hardwareMACAddress;
@property (T@"NSString",C,N,V_interfaceName) interfaceName;
@property (T@"NSArray",C,N,V_ipv6Addresses) ipv6Addresses;
@property (TB,N,V_power) power;
@property (T@"NSData",C,N,V_awdlSyncEnabled) awdlSyncEnabled;
@property (T@"NSData",C,N,V_awdlSyncState) awdlSyncState;
@property (T@"NSData",C,N,V_awdlSyncChannelSequence) awdlSyncChannelSequence;
@property (T@"NSData",C,N,V_awdlStrategy) awdlStrategy;
@property (T@"NSData",C,N,V_awdlElectionParameters) awdlElectionParameters;
@property (T@"NSData",C,N,V_awdlMasterChannel) awdlMasterChannel;
@property (T@"NSData",C,N,V_awdlSecondaryMasterChannel) awdlSecondaryMasterChannel;
@property (T@"NSData",C,N,V_awdlOpMode) awdlOpMode;
@property (T@"NSData",C,N,V_awdlSyncParameters) awdlSyncParameters;
@property (T@"NSData",C,N,V_awdlPeerDatabase) awdlPeerDatabase;
@property (T@"NSData",C,N,V_awdlSidecarDiagnostics) awdlSidecarDiagnostics;
@property (TB,N,V_isAWDLRealTimeMode) isAWDLRealTimeMode;
@property (Tq,N,V_airDropDiscoverableMode) airDropDiscoverableMode;
```

## Class methods

```
+[W5AWDLStatus supportsSecureCoding];
```

## Instance methods

```
-[W5AWDLStatus power];
-[W5AWDLStatus hardwareMACAddress];
-[W5AWDLStatus macAddress];
-[W5AWDLStatus setInterfaceName:];
-[W5AWDLStatus dealloc];
-[W5AWDLStatus interfaceName];
-[W5AWDLStatus setMacAddress:];
-[W5AWDLStatus ipv6Addresses];
-[W5AWDLStatus encodeWithCoder:];
-[W5AWDLStatus conformsToProtocol:];
-[W5AWDLStatus description];
-[W5AWDLStatus initWithCoder:];
-[W5AWDLStatus copyWithZone:];
-[W5AWDLStatus isEqual:];
-[W5AWDLStatus setPower:];
-[W5AWDLStatus setIpv6Addresses:];
-[W5AWDLStatus awdlElectionParameters];
-[W5AWDLStatus awdlMasterChannel];
-[W5AWDLStatus awdlOpMode];
-[W5AWDLStatus awdlSecondaryMasterChannel];
-[W5AWDLStatus awdlStrategy];
-[W5AWDLStatus awdlSyncChannelSequence];
-[W5AWDLStatus awdlSyncState];
-[W5AWDLStatus setAwdlElectionParameters:];
-[W5AWDLStatus setAwdlMasterChannel:];
-[W5AWDLStatus setAwdlOpMode:];
-[W5AWDLStatus setAwdlSecondaryMasterChannel:];
-[W5AWDLStatus setAwdlSyncChannelSequence:];
-[W5AWDLStatus setAwdlSyncState:];
-[W5AWDLStatus setHardwareMACAddress:];
-[W5AWDLStatus awdlSyncEnabled];
-[W5AWDLStatus airDropDiscoverableMode];
-[W5AWDLStatus awdlPeerDatabase];
-[W5AWDLStatus awdlSidecarDiagnostics];
-[W5AWDLStatus awdlSyncParameters];
-[W5AWDLStatus isAWDLRealTimeMode];
-[W5AWDLStatus isEqualToAWDLStatus:];
-[W5AWDLStatus setAirDropDiscoverableMode:];
-[W5AWDLStatus setAwdlPeerDatabase:];
-[W5AWDLStatus setAwdlSidecarDiagnostics:];
-[W5AWDLStatus setAwdlStrategy:];
-[W5AWDLStatus setAwdlSyncEnabled:];
-[W5AWDLStatus setAwdlSyncParameters:];
-[W5AWDLStatus setIsAWDLRealTimeMode:];
```
