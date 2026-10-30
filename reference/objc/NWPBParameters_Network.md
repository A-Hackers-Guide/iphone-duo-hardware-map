# `NWPBParameters`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 30 instance variables, 0 properties, 8 instance methods, 0 class methods

## Instance variables

```
{?="list"^i"count"Q"size"Q} _prohibitedInterfaceSubTypes;
{?="list"^i"count"Q"size"Q} _prohibitedInterfaceTypes;
@"NSString" _account;
I _addressFamily;
i _dataMode;
@"NSString" _effectiveBundleID;
@"NSString" _effectiveProcessUUID;
I _ipProtocol;
@"NWPBEndpoint" _localEndpoint;
@"NSData" _metadata;
I _multipathService;
@"NSMutableArray" _preferredAgents;
@"NSMutableArray" _prohibitedAgents;
@"NSMutableArray" _prohibitedInterfaces;
@"NSString" _realProcessUUID;
@"NSMutableArray" _requiredAgents;
@"NWPBInterface" _requiredInterface;
i _requiredInterfaceType;
I _trafficClass;
@"NSString" _url;
B _fastOpen;
B _keepalive;
B _longOutstandingQueries;
B _noFallback;
B _prohibitExpensive;
B _reduceBuffering;
B _reuseLocalAddress;
B _useAWDL;
B _useP2P;
{?="addressFamily"b1"dataMode"b1"ipProtocol"b1"multipathService"b1"requiredInterfaceType"b1"trafficClass"b1"fastOpen"b1"keepalive"b1"longOutstandingQueries"b1"noFallback"b1"prohibitExpensive"b1"reduceBuffering"b1"reuseLocalAddress"b1"useAWDL"b1"useP2P"b1} _has;
```

## Instance methods

```
-[NWPBParameters writeTo:];
-[NWPBParameters dealloc];
-[NWPBParameters hash];
-[NWPBParameters description];
-[NWPBParameters readFrom:];
-[NWPBParameters copyWithZone:];
-[NWPBParameters isEqual:];
-[NWPBParameters dictionaryRepresentation];
```
