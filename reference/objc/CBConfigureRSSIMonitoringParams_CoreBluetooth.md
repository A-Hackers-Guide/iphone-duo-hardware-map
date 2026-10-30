# `CBConfigureRSSIMonitoringParams`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CUXPCCodable`
- 19 instance variables, 19 properties, 41 instance methods, 0 class methods

## Instance variables

```
B _enable;
C _windowConfiguration;
c _averageThresholdFurther;
c _maximumThresholdFurther;
c _medianThresholdFurther;
c _averageThresholdCloser;
c _maximumThresholdCloser;
c _medianThresholdCloser;
C _CMCheckLogic;
C _enableDebugging;
S _varThreshold1;
S _varThreshold2;
S _maskDecisionLogic;
S _subsamplingRateForAOP;
S _subsamplingRateForRSSIBuffer;
S _pastRSSIValuesSize;
I _CM_AND_Mask;
I _CM_XOR_Mask;
I _CM_AND_Mask2;
```

## Properties

```
@property (TB,N,V_enable) enable;
@property (TC,N,V_windowConfiguration) windowConfiguration;
@property (Tc,N,V_averageThresholdFurther) averageThresholdFurther;
@property (Tc,N,V_maximumThresholdFurther) maximumThresholdFurther;
@property (Tc,N,V_medianThresholdFurther) medianThresholdFurther;
@property (Tc,N,V_averageThresholdCloser) averageThresholdCloser;
@property (Tc,N,V_maximumThresholdCloser) maximumThresholdCloser;
@property (Tc,N,V_medianThresholdCloser) medianThresholdCloser;
@property (TS,N,V_varThreshold1) varThreshold1;
@property (TS,N,V_varThreshold2) varThreshold2;
@property (TS,N,V_maskDecisionLogic) maskDecisionLogic;
@property (TC,N,V_CMCheckLogic) CMCheckLogic;
@property (TI,N,V_CM_AND_Mask) CM_AND_Mask;
@property (TI,N,V_CM_XOR_Mask) CM_XOR_Mask;
@property (TI,N,V_CM_AND_Mask2) CM_AND_Mask2;
@property (TC,N,V_enableDebugging) enableDebugging;
@property (TS,N,V_subsamplingRateForAOP) subsamplingRateForAOP;
@property (TS,N,V_subsamplingRateForRSSIBuffer) subsamplingRateForRSSIBuffer;
@property (TS,N,V_pastRSSIValuesSize) pastRSSIValuesSize;
```

## Instance methods

```
-[CBConfigureRSSIMonitoringParams enable];
-[CBConfigureRSSIMonitoringParams encodeWithXPCObject:];
-[CBConfigureRSSIMonitoringParams initWithXPCObject:error:];
-[CBConfigureRSSIMonitoringParams description];
-[CBConfigureRSSIMonitoringParams setEnable:];
-[CBConfigureRSSIMonitoringParams CM_AND_Mask];
-[CBConfigureRSSIMonitoringParams CM_XOR_Mask];
-[CBConfigureRSSIMonitoringParams setCM_AND_Mask:];
-[CBConfigureRSSIMonitoringParams CMCheckLogic];
-[CBConfigureRSSIMonitoringParams CM_AND_Mask2];
-[CBConfigureRSSIMonitoringParams enableDebugging];
-[CBConfigureRSSIMonitoringParams setCM_XOR_Mask:];
-[CBConfigureRSSIMonitoringParams averageThresholdCloser];
-[CBConfigureRSSIMonitoringParams averageThresholdFurther];
-[CBConfigureRSSIMonitoringParams maskDecisionLogic];
-[CBConfigureRSSIMonitoringParams maximumThresholdCloser];
-[CBConfigureRSSIMonitoringParams maximumThresholdFurther];
-[CBConfigureRSSIMonitoringParams medianThresholdCloser];
-[CBConfigureRSSIMonitoringParams medianThresholdFurther];
-[CBConfigureRSSIMonitoringParams pastRSSIValuesSize];
-[CBConfigureRSSIMonitoringParams setAverageThresholdCloser:];
-[CBConfigureRSSIMonitoringParams setAverageThresholdFurther:];
-[CBConfigureRSSIMonitoringParams setCMCheckLogic:];
-[CBConfigureRSSIMonitoringParams setCM_AND_Mask2:];
-[CBConfigureRSSIMonitoringParams setEnableDebugging:];
-[CBConfigureRSSIMonitoringParams setMaskDecisionLogic:];
-[CBConfigureRSSIMonitoringParams setMaximumThresholdCloser:];
-[CBConfigureRSSIMonitoringParams setMaximumThresholdFurther:];
-[CBConfigureRSSIMonitoringParams setMedianThresholdCloser:];
-[CBConfigureRSSIMonitoringParams setMedianThresholdFurther:];
-[CBConfigureRSSIMonitoringParams setPastRSSIValuesSize:];
-[CBConfigureRSSIMonitoringParams setSubsamplingRateForAOP:];
-[CBConfigureRSSIMonitoringParams setSubsamplingRateForRSSIBuffer:];
-[CBConfigureRSSIMonitoringParams setVarThreshold1:];
-[CBConfigureRSSIMonitoringParams setVarThreshold2:];
-[CBConfigureRSSIMonitoringParams setWindowConfiguration:];
-[CBConfigureRSSIMonitoringParams subsamplingRateForAOP];
-[CBConfigureRSSIMonitoringParams subsamplingRateForRSSIBuffer];
-[CBConfigureRSSIMonitoringParams varThreshold1];
-[CBConfigureRSSIMonitoringParams varThreshold2];
-[CBConfigureRSSIMonitoringParams windowConfiguration];
```
