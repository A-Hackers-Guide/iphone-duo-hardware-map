# `NWPBAgent`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 10 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NWPBAgentClass" _agentClass;
@"NSData" _agentData;
@"NSString" _agentDescription;
@"NSString" _agentIdentifier;
B _active;
B _networkProvider;
B _nexusProvider;
B _userActivated;
B _voluntary;
{?="active"b1"networkProvider"b1"nexusProvider"b1"userActivated"b1"voluntary"b1} _has;
```

## Instance methods

```
-[NWPBAgent writeTo:];
-[NWPBAgent hash];
-[NWPBAgent description];
-[NWPBAgent readFrom:];
-[NWPBAgent copyWithZone:];
-[NWPBAgent isEqual:];
-[NWPBAgent dictionaryRepresentation];
```
