# `CTCellularQoSFlow`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 6 instance variables, 6 properties, 16 instance methods, 1 class methods

## Instance variables

```
Q _flowId;
Q _bearerId;
@"NSNumber" _queueSetId;
@"NSNumber" _is5G;
@"CTQoS" _txQos;
@"CTQoS" _rxQos;
```

## Properties

```
@property (TQ,N,V_flowId) flowId;
@property (TQ,N,V_bearerId) bearerId;
@property (T@"NSNumber",&,N,V_queueSetId) queueSetId;
@property (T@"NSNumber",&,N,V_is5G) is5G;
@property (T@"CTQoS",&,N,V_txQos) txQos;
@property (T@"CTQoS",&,N,V_rxQos) rxQos;
```

## Class methods

```
+[CTCellularQoSFlow supportsSecureCoding];
```

## Instance methods

```
-[CTCellularQoSFlow encodeWithCoder:];
-[CTCellularQoSFlow flowId];
-[CTCellularQoSFlow description];
-[CTCellularQoSFlow setFlowId:];
-[CTCellularQoSFlow initWithCoder:];
-[CTCellularQoSFlow copyWithZone:];
-[CTCellularQoSFlow bearerId];
-[CTCellularQoSFlow is5G];
-[CTCellularQoSFlow queueSetId];
-[CTCellularQoSFlow rxQos];
-[CTCellularQoSFlow setBearerId:];
-[CTCellularQoSFlow setIs5G:];
-[CTCellularQoSFlow setQueueSetId:];
-[CTCellularQoSFlow setRxQos:];
-[CTCellularQoSFlow setTxQos:];
-[CTCellularQoSFlow txQos];
```
