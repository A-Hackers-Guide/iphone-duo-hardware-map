# `CTPlanBillingDetails`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 6 instance variables, 6 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSString" _planName;
@"NSNumber" _planCost;
@"NSString" _planCurrency;
@"NSNumber" _planDataAmount;
Q _planDataMeasureUnit;
Q _planType;
```

## Properties

```
@property (T@"NSString",R,N,V_planName) planName;
@property (T@"NSNumber",R,N,V_planCost) planCost;
@property (T@"NSString",R,N,V_planCurrency) planCurrency;
@property (T@"NSNumber",R,N,V_planDataAmount) planDataAmount;
@property (TQ,R,N,V_planDataMeasureUnit) planDataMeasureUnit;
@property (TQ,R,N,V_planType) planType;
```

## Class methods

```
+[CTPlanBillingDetails supportsSecureCoding];
```

## Instance methods

```
-[CTPlanBillingDetails encodeWithCoder:];
-[CTPlanBillingDetails description];
-[CTPlanBillingDetails initWithCoder:];
-[CTPlanBillingDetails isEqual:];
-[CTPlanBillingDetails initWithName:PlanCost:PlanCurrency:PlanDataAmount:PlanDataMeasureUnit:PlanType:];
-[CTPlanBillingDetails planCost];
-[CTPlanBillingDetails planCurrency];
-[CTPlanBillingDetails planDataAmount];
-[CTPlanBillingDetails planDataMeasureUnit];
-[CTPlanBillingDetails planName];
-[CTPlanBillingDetails planType];
```
