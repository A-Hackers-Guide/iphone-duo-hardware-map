# `CTTetheringStatus`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 8 instance variables, 8 properties, 20 instance methods, 1 class methods

## Instance variables

```
@"NSNumber" _carrierEnabled;
@"NSNumber" _userAuthenticated;
@"NSNumber" _asserted;
@"NSNumber" _activationFailure;
@"NSNumber" _misPdpMaxHosts;
@"CTDataConnectionAvailabilityStatus" _connectionAvailabilityStatus;
@"CTDataConnectionStatus" _connectionStatus;
@"CTXPCServiceSubscriptionContext" _context;
```

## Properties

```
@property (T@"NSNumber",&,N,V_carrierEnabled) carrierEnabled;
@property (T@"NSNumber",&,N,V_userAuthenticated) userAuthenticated;
@property (T@"NSNumber",&,N,V_asserted) asserted;
@property (T@"NSNumber",&,N,V_activationFailure) activationFailure;
@property (T@"NSNumber",&,N,V_misPdpMaxHosts) misPdpMaxHosts;
@property (T@"CTDataConnectionAvailabilityStatus",&,N,V_connectionAvailabilityStatus) connectionAvailabilityStatus;
@property (T@"CTDataConnectionStatus",&,N,V_connectionStatus) connectionStatus;
@property (T@"CTXPCServiceSubscriptionContext",&,N,V_context) context;
```

## Class methods

```
+[CTTetheringStatus supportsSecureCoding];
```

## Instance methods

```
-[CTTetheringStatus asserted];
-[CTTetheringStatus misPdpMaxHosts];
-[CTTetheringStatus setConnectionStatus:];
-[CTTetheringStatus activationFailure];
-[CTTetheringStatus userAuthenticated];
-[CTTetheringStatus setCarrierEnabled:];
-[CTTetheringStatus setContext:];
-[CTTetheringStatus setConnectionAvailabilityStatus:];
-[CTTetheringStatus connectionAvailabilityStatus];
-[CTTetheringStatus encodeWithCoder:];
-[CTTetheringStatus description];
-[CTTetheringStatus initWithCoder:];
-[CTTetheringStatus setActivationFailure:];
-[CTTetheringStatus carrierEnabled];
-[CTTetheringStatus setAsserted:];
-[CTTetheringStatus setUserAuthenticated:];
-[CTTetheringStatus copyWithZone:];
-[CTTetheringStatus context];
-[CTTetheringStatus setMisPdpMaxHosts:];
-[CTTetheringStatus connectionStatus];
```
