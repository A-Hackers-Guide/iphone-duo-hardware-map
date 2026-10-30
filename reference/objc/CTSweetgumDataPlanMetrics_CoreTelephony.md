# `CTSweetgumDataPlanMetrics`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 4 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"NSDate" _billingCycleEndDate;
@"CTSweetgumDataPlanMetricsItem" _domestic;
q _regStatus;
@"NSNumber" _domesticCapacity;
```

## Properties

```
@property (T@"NSDate",&,N,V_billingCycleEndDate) billingCycleEndDate;
@property (T@"CTSweetgumDataPlanMetricsItem",&,N,V_domestic) domestic;
@property (Tq,N,V_regStatus) regStatus;
@property (T@"NSNumber",&,N,V_domesticCapacity) domesticCapacity;
```

## Class methods

```
+[CTSweetgumDataPlanMetrics supportsSecureCoding];
```

## Instance methods

```
-[CTSweetgumDataPlanMetrics init];
-[CTSweetgumDataPlanMetrics encodeWithCoder:];
-[CTSweetgumDataPlanMetrics description];
-[CTSweetgumDataPlanMetrics initWithCoder:];
-[CTSweetgumDataPlanMetrics setDomestic:];
-[CTSweetgumDataPlanMetrics isEqual:];
-[CTSweetgumDataPlanMetrics billingCycleEndDate];
-[CTSweetgumDataPlanMetrics domestic];
-[CTSweetgumDataPlanMetrics domesticCapacity];
-[CTSweetgumDataPlanMetrics regStatus];
-[CTSweetgumDataPlanMetrics setBillingCycleEndDate:];
-[CTSweetgumDataPlanMetrics setDomesticCapacity:];
-[CTSweetgumDataPlanMetrics setRegStatus:];
```
