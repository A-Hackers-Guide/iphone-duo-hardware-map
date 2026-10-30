# `AABattery`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 8 instance variables, 20 properties, 38 instance methods, 2 class methods

## Instance variables

```
C _chargingOBCTimeUntilCharged;
C _lastOrigin;
I _productID;
I _sourceFlags;
d _level;
q _state;
q _type;
d _lastSeen;
```

## Properties

```
@property (Td,N,V_level) level;
@property (TI,N,V_productID) productID;
@property (Tq,V_state) state;
@property (Tq,V_type) type;
@property (TC,V_chargingOBCTimeUntilCharged) chargingOBCTimeUntilCharged;
@property (TB,R) inAACP;
@property (TB,R) isExpired;
@property (Td,V_lastSeen) lastSeen;
@property (TC,V_lastOrigin) lastOrigin;
@property (Td,R,N) lowLevel;
@property (TI,V_sourceFlags) sourceFlags;
@property (Tq,R,N) chargeStatus;
@property (TB,R) charging;
@property (TB,R) chargingDEOC;
@property (TB,R) chargingOBC;
@property (TB,R) fullyCharged;
@property (TB,R) isCaseBattery;
@property (TB,R,N) isChargingPaused;
@property (TB,R,N) isLow;
@property (TB,R) valid;
```

## Class methods

```
+[AABattery supportsSecureCoding];
+[AABattery invalidBattery];
```

## Instance methods

```
-[AABattery valid];
-[AABattery setProductID:];
-[AABattery productID];
-[AABattery setState:];
-[AABattery isExpired];
-[AABattery level];
-[AABattery lastSeen];
-[AABattery setLevel:];
-[AABattery setType:];
-[AABattery setLastSeen:];
-[AABattery type];
-[AABattery encodeWithCoder:];
-[AABattery hash];
-[AABattery description];
-[AABattery initWithCoder:];
-[AABattery charging];
-[AABattery copyWithZone:];
-[AABattery isEqual:];
-[AABattery state];
-[AABattery fullyCharged];
-[AABattery isLow];
-[AABattery isChargingPaused];
-[AABattery initWithLevel:productID:state:type:];
-[AABattery lowLevel];
-[AABattery setChargingOBCTimeUntilCharged:];
-[AABattery setSourceFlags:];
-[AABattery chargeStatus];
-[AABattery chargingDEOC];
-[AABattery chargingOBC];
-[AABattery chargingOBCTimeUntilCharged];
-[AABattery inAACP];
-[AABattery initWithAACPBatteryInfo:productID:];
-[AABattery isCaseBattery];
-[AABattery isEqualToBattery:];
-[AABattery lastOrigin];
-[AABattery setLastOrigin:];
-[AABattery sourceFlags];
-[AABattery updateWithAABattery:];
```
