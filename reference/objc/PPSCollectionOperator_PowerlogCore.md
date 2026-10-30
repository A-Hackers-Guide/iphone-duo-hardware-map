# `PPSCollectionOperator`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLOperator`
- 7 instance variables, 7 properties, 18 instance methods, 0 class methods

## Instance variables

```
B _monitor;
@"PLXPCListenerOperatorComposition" _metricListener;
@"PLXPCResponderOperatorComposition" _allowlistResponder;
@"PLCFNotificationOperatorComposition" _startMonitor;
@"PLCFNotificationOperatorComposition" _stopMonitor;
@"NSString" _monitoredSubsystem;
@"NSString" _monitoredCategory;
```

## Properties

```
@property (T@"PLXPCListenerOperatorComposition",&,V_metricListener) metricListener;
@property (T@"PLXPCResponderOperatorComposition",&,V_allowlistResponder) allowlistResponder;
@property (T@"PLCFNotificationOperatorComposition",&,V_startMonitor) startMonitor;
@property (T@"PLCFNotificationOperatorComposition",&,V_stopMonitor) stopMonitor;
@property (TB,V_monitor) monitor;
@property (T@"NSString",&,V_monitoredSubsystem) monitoredSubsystem;
@property (T@"NSString",&,V_monitoredCategory) monitoredCategory;
```

## Instance methods

```
-[PPSCollectionOperator monitor];
-[PPSCollectionOperator init];
-[PPSCollectionOperator setMonitor:];
-[PPSCollectionOperator initOperatorDependancies];
-[PPSCollectionOperator startMonitor];
-[PPSCollectionOperator setStopMonitor:];
-[PPSCollectionOperator startCollection];
-[PPSCollectionOperator allowlistResponder];
-[PPSCollectionOperator metricListener];
-[PPSCollectionOperator monitorMetricsForSubsystem:category:payload:];
-[PPSCollectionOperator monitoredCategory];
-[PPSCollectionOperator monitoredSubsystem];
-[PPSCollectionOperator setAllowlistResponder:];
-[PPSCollectionOperator setMetricListener:];
-[PPSCollectionOperator setMonitoredCategory:];
-[PPSCollectionOperator setMonitoredSubsystem:];
-[PPSCollectionOperator setStartMonitor:];
-[PPSCollectionOperator stopMonitor];
```
