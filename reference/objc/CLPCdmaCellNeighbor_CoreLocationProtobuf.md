# `CLPCdmaCellNeighbor`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 6 instance variables, 10 properties, 29 instance methods, 0 class methods

## Instance variables

```
i _channel;
i _ecn0;
i _pilotPhase;
i _pnoffset;
i _rscp;
{?="channel"b1"ecn0"b1"pilotPhase"b1"pnoffset"b1"rscp"b1} _has;
```

## Properties

```
@property (TB,N) hasPnoffset;
@property (Ti,N,V_pnoffset) pnoffset;
@property (TB,N) hasPilotPhase;
@property (Ti,N,V_pilotPhase) pilotPhase;
@property (TB,N) hasEcn0;
@property (Ti,N,V_ecn0) ecn0;
@property (TB,N) hasRscp;
@property (Ti,N,V_rscp) rscp;
@property (TB,N) hasChannel;
@property (Ti,N,V_channel) channel;
```

## Instance methods

```
-[CLPCdmaCellNeighbor rscp];
-[CLPCdmaCellNeighbor setChannel:];
-[CLPCdmaCellNeighbor channel];
-[CLPCdmaCellNeighbor writeTo:];
-[CLPCdmaCellNeighbor hasChannel];
-[CLPCdmaCellNeighbor hasEcn0];
-[CLPCdmaCellNeighbor mergeFrom:];
-[CLPCdmaCellNeighbor setHasChannel:];
-[CLPCdmaCellNeighbor setHasRscp:];
-[CLPCdmaCellNeighbor hasRscp];
-[CLPCdmaCellNeighbor hash];
-[CLPCdmaCellNeighbor copyTo:];
-[CLPCdmaCellNeighbor description];
-[CLPCdmaCellNeighbor setRscp:];
-[CLPCdmaCellNeighbor readFrom:];
-[CLPCdmaCellNeighbor copyWithZone:];
-[CLPCdmaCellNeighbor isEqual:];
-[CLPCdmaCellNeighbor setEcn0:];
-[CLPCdmaCellNeighbor dictionaryRepresentation];
-[CLPCdmaCellNeighbor setHasEcn0:];
-[CLPCdmaCellNeighbor ecn0];
-[CLPCdmaCellNeighbor setHasPnoffset:];
-[CLPCdmaCellNeighbor hasPilotPhase];
-[CLPCdmaCellNeighbor hasPnoffset];
-[CLPCdmaCellNeighbor pilotPhase];
-[CLPCdmaCellNeighbor pnoffset];
-[CLPCdmaCellNeighbor setHasPilotPhase:];
-[CLPCdmaCellNeighbor setPilotPhase:];
-[CLPCdmaCellNeighbor setPnoffset:];
```
