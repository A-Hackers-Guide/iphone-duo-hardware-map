# `PLInterfaceOSMetric`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_os_metric_double_gauge>" _rxPacketTotal;
@"NSObject<OS_os_metric_double_gauge>" _txPacketTotal;
@"NSObject<OS_os_metric_double_gauge>" _rxErrorsTotal;
@"NSObject<OS_os_metric_double_gauge>" _txErrorsTotal;
@"NSObject<OS_os_metric_double_gauge>" _rxBytesTotal;
@"NSObject<OS_os_metric_double_gauge>" _txBytesTotal;
@"NSObject<OS_os_metric_double_gauge>" _rxMulticastTotal;
@"NSObject<OS_os_metric_double_gauge>" _txMulticastTotal;
```

## Properties

```
@property (T@"NSObject<OS_os_metric_double_gauge>",&,V_rxPacketTotal) rxPacketTotal;
@property (T@"NSObject<OS_os_metric_double_gauge>",&,V_txPacketTotal) txPacketTotal;
@property (T@"NSObject<OS_os_metric_double_gauge>",&,V_rxErrorsTotal) rxErrorsTotal;
@property (T@"NSObject<OS_os_metric_double_gauge>",&,V_txErrorsTotal) txErrorsTotal;
@property (T@"NSObject<OS_os_metric_double_gauge>",&,V_rxBytesTotal) rxBytesTotal;
@property (T@"NSObject<OS_os_metric_double_gauge>",&,V_txBytesTotal) txBytesTotal;
@property (T@"NSObject<OS_os_metric_double_gauge>",&,V_rxMulticastTotal) rxMulticastTotal;
@property (T@"NSObject<OS_os_metric_double_gauge>",&,V_txMulticastTotal) txMulticastTotal;
```

## Class methods

```
+[PLInterfaceOSMetric load];
```

## Instance methods

```
-[PLInterfaceOSMetric logMetric:];
-[PLInterfaceOSMetric initWithName:];
-[PLInterfaceOSMetric createGauge:withGroup:];
-[PLInterfaceOSMetric rxBytesTotal];
-[PLInterfaceOSMetric rxErrorsTotal];
-[PLInterfaceOSMetric rxMulticastTotal];
-[PLInterfaceOSMetric rxPacketTotal];
-[PLInterfaceOSMetric setRxBytesTotal:];
-[PLInterfaceOSMetric setRxErrorsTotal:];
-[PLInterfaceOSMetric setRxMulticastTotal:];
-[PLInterfaceOSMetric setRxPacketTotal:];
-[PLInterfaceOSMetric setTxBytesTotal:];
-[PLInterfaceOSMetric setTxErrorsTotal:];
-[PLInterfaceOSMetric setTxMulticastTotal:];
-[PLInterfaceOSMetric setTxPacketTotal:];
-[PLInterfaceOSMetric txBytesTotal];
-[PLInterfaceOSMetric txErrorsTotal];
-[PLInterfaceOSMetric txMulticastTotal];
-[PLInterfaceOSMetric txPacketTotal];
```
