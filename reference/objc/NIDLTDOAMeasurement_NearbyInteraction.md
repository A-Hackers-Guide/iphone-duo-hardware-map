# `NIDLTDOAMeasurement`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 13 instance variables, 13 properties, 36 instance methods, 1 class methods

## Instance variables

```
Q _address;
Q _clusterInitiatorAddress;
q _measurementType;
q _coordinatesType;
d _transmitTime;
Q _rawTransmitTime;
d _receiveTime;
Q _rawReceiveTime;
d _signalStrength;
d _carrierFrequencyOffset;
@"NSNumber" _responderClockFrequencyOffset;
@"NIDLTDOAMeasurementFloorElevation" _floorElevation;
_coordinates;
```

## Properties

```
@property (TQ,R,N,V_address) address;
@property (TQ,R,N,V_clusterInitiatorAddress) clusterInitiatorAddress;
@property (Tq,R,N,V_measurementType) measurementType;
@property (Td,R,N,V_transmitTime) transmitTime;
@property (TQ,R,N,V_rawTransmitTime) rawTransmitTime;
@property (Td,R,N,V_receiveTime) receiveTime;
@property (TQ,R,N,V_rawReceiveTime) rawReceiveTime;
@property (Td,R,N,V_signalStrength) signalStrength;
@property (Td,R,N,V_carrierFrequencyOffset) carrierFrequencyOffset;
@property (T@"NSNumber",R,N,V_responderClockFrequencyOffset) responderClockFrequencyOffset;
@property (Tq,R,N,V_coordinatesType) coordinatesType;
@property (T,R,N,V_coordinates) coordinates;
@property (T@"NIDLTDOAMeasurementFloorElevation",R,C,N,V_floorElevation) floorElevation;
```

## Class methods

```
+[NIDLTDOAMeasurement supportsSecureCoding];
```

## Instance methods

```
-[NIDLTDOAMeasurement signalStrength];
-[NIDLTDOAMeasurement address];
-[NIDLTDOAMeasurement setAddress:];
-[NIDLTDOAMeasurement encodeWithCoder:];
-[NIDLTDOAMeasurement hash];
-[NIDLTDOAMeasurement description];
-[NIDLTDOAMeasurement initWithCoder:];
-[NIDLTDOAMeasurement copyWithZone:];
-[NIDLTDOAMeasurement isEqual:];
-[NIDLTDOAMeasurement setCoordinates:];
-[NIDLTDOAMeasurement coordinates];
-[NIDLTDOAMeasurement setSignalStrength:];
-[NIDLTDOAMeasurement coordinatesType];
-[NIDLTDOAMeasurement measurementType];
-[NIDLTDOAMeasurement receiveTime];
-[NIDLTDOAMeasurement setMeasurementType:];
-[NIDLTDOAMeasurement rawTransmitTime];
-[NIDLTDOAMeasurement setReceiveTime:];
-[NIDLTDOAMeasurement carrierFrequencyOffset];
-[NIDLTDOAMeasurement clusterInitiatorAddress];
-[NIDLTDOAMeasurement floorElevation];
-[NIDLTDOAMeasurement initWithAnchorAddress:clusterInitiatorAddress:measurementType:coordinatesType:transmitTime:rawTransmitTime:receiveTime:rawReceiveTime:signalStrength:carrierFrequencyOffset:responderClockFrequencyOffset:coordinates:floorElevation:];
-[NIDLTDOAMeasurement initWithAnchorAddress:clusterInitiatorAddress:measurementType:coordinatesType:transmitTime:receiveTime:signalStrength:carrierFrequencyOffset:coordinates:floorElevation:];
-[NIDLTDOAMeasurement initWithAnchorAddress:clusterInitiatorAddress:measurementType:coordinatesType:transmitTime:receiveTime:signalStrength:carrierFrequencyOffset:responderClockFrequencyOffset:coordinates:floorElevation:];
-[NIDLTDOAMeasurement initWithAnchorAddress:measurementType:coordinatesType:transmitTime:receiveTime:signalStrength:carrierFrequencyOffset:coordinates:];
-[NIDLTDOAMeasurement rawReceiveTime];
-[NIDLTDOAMeasurement responderClockFrequencyOffset];
-[NIDLTDOAMeasurement setCarrierFrequencyOffset:];
-[NIDLTDOAMeasurement setClusterInitiatorAddress:];
-[NIDLTDOAMeasurement setCoordinatesType:];
-[NIDLTDOAMeasurement setFloorElevation:];
-[NIDLTDOAMeasurement setRawReceiveTime:];
-[NIDLTDOAMeasurement setRawTransmitTime:];
-[NIDLTDOAMeasurement setResponderClockFrequencyOffset:];
-[NIDLTDOAMeasurement setTransmitTime:];
-[NIDLTDOAMeasurement transmitTime];
```
