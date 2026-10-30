# `Filter`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 3 instance variables, 4 properties, 17 instance methods, 0 class methods

## Instance variables

```
I _port;
I _protocol;
{?="port"b1"protocol"b1} _has;
```

## Properties

```
@property (TB,N) hasProtocol;
@property (TI,N,V_protocol) protocol;
@property (TB,N) hasPort;
@property (TI,N,V_port) port;
```

## Instance methods

```
-[Filter setPort:];
-[Filter setProtocol:];
-[Filter protocol];
-[Filter writeTo:];
-[Filter mergeFrom:];
-[Filter port];
-[Filter hash];
-[Filter copyTo:];
-[Filter description];
-[Filter readFrom:];
-[Filter copyWithZone:];
-[Filter isEqual:];
-[Filter dictionaryRepresentation];
-[Filter setHasProtocol:];
-[Filter hasPort];
-[Filter hasProtocol];
-[Filter setHasPort:];
```
