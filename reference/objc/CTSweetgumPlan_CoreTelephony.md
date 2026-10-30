# `CTSweetgumPlan`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 9 instance variables, 10 properties, 25 instance methods, 1 class methods

## Instance variables

```
B _planPurchasable;
C _planSubscriptionStatus;
@"NSString" _planId;
@"NSString" _planLabel;
@"NSString" _planValue;
@"NSString" _planDetailsURL;
@"NSString" _planTermsURL;
@"NSString" _planPurchaseURL;
q _planType;
```

## Properties

```
@property (T@"NSString",&,N,V_planId) planId;
@property (T@"NSString",&,N,V_planLabel) planLabel;
@property (T@"NSString",&,N,V_planValue) planValue;
@property (TC,N,V_planSubscriptionStatus) planSubscriptionStatus;
@property (TB,N,V_planPurchasable) planPurchasable;
@property (T@"NSString",&,N,V_planDetailsURL) planDetailsURL;
@property (T@"NSString",&,N,V_planTermsURL) planTermsURL;
@property (T@"NSString",&,N,V_planPurchaseURL) planPurchaseURL;
@property (Tq,N,V_planType) planType;
@property (Tq,R,N) planStatus;
```

## Class methods

```
+[CTSweetgumPlan supportsSecureCoding];
```

## Instance methods

```
-[CTSweetgumPlan init];
-[CTSweetgumPlan setPlanId:];
-[CTSweetgumPlan planId];
-[CTSweetgumPlan encodeWithCoder:];
-[CTSweetgumPlan description];
-[CTSweetgumPlan initWithCoder:];
-[CTSweetgumPlan copyWithZone:];
-[CTSweetgumPlan isEqual:];
-[CTSweetgumPlan planPurchaseURL];
-[CTSweetgumPlan planPurchasable];
-[CTSweetgumPlan planDetailsURL];
-[CTSweetgumPlan planLabel];
-[CTSweetgumPlan planStatus];
-[CTSweetgumPlan planSubscriptionStatus];
-[CTSweetgumPlan planTermsURL];
-[CTSweetgumPlan planType];
-[CTSweetgumPlan planValue];
-[CTSweetgumPlan setPlanDetailsURL:];
-[CTSweetgumPlan setPlanLabel:];
-[CTSweetgumPlan setPlanPurchasable:];
-[CTSweetgumPlan setPlanPurchaseURL:];
-[CTSweetgumPlan setPlanSubscriptionStatus:];
-[CTSweetgumPlan setPlanTermsURL:];
-[CTSweetgumPlan setPlanType:];
-[CTSweetgumPlan setPlanValue:];
```
