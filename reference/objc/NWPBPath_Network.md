# `NWPBPath`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 12 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _agents;
@"NSString" _clientUUID;
@"NWPBInterface" _delegateInterface;
@"NWPBInterface" _directInterface;
@"NWPBEndpoint" _endpoint;
@"NWPBParameters" _parameters;
i _status;
B _direct;
B _ipv4;
B _ipv6;
B _local;
{?="status"b1"direct"b1"ipv4"b1"ipv6"b1"local"b1} _has;
```

## Instance methods

```
-[NWPBPath writeTo:];
-[NWPBPath hash];
-[NWPBPath description];
-[NWPBPath readFrom:];
-[NWPBPath copyWithZone:];
-[NWPBPath isEqual:];
-[NWPBPath dictionaryRepresentation];
```
