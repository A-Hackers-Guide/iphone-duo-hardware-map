# `CTSimSetupUsage`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 14 instance variables, 14 properties, 34 instance methods, 1 class methods

## Instance variables

```
B _inBuddy;
Q _transferablePlans;
Q _selectedTransferablePlans;
Q _alsPlans;
Q _selectedAlsPlans;
Q _odaPlans;
@"NSString" _transferPlanCarriers;
@"NSString" _selectedTransferPlanCarriers;
@"NSString" _alsPlanCarriers;
@"NSString" _selectedAlsPlanCarriers;
@"NSString" _odaPlanCarriers;
@"NSString" _selectedOdaPlanCarriers;
Q _sourceDevicesCount;
Q _selectedSourceDevicesCount;
```

## Properties

```
@property (TB,V_inBuddy) inBuddy;
@property (TQ,V_transferablePlans) transferablePlans;
@property (TQ,V_selectedTransferablePlans) selectedTransferablePlans;
@property (TQ,V_alsPlans) alsPlans;
@property (TQ,V_selectedAlsPlans) selectedAlsPlans;
@property (TQ,V_odaPlans) odaPlans;
@property (T@"NSString",&,V_transferPlanCarriers) transferPlanCarriers;
@property (T@"NSString",&,V_selectedTransferPlanCarriers) selectedTransferPlanCarriers;
@property (T@"NSString",&,V_alsPlanCarriers) alsPlanCarriers;
@property (T@"NSString",&,V_selectedAlsPlanCarriers) selectedAlsPlanCarriers;
@property (T@"NSString",&,V_odaPlanCarriers) odaPlanCarriers;
@property (T@"NSString",&,V_selectedOdaPlanCarriers) selectedOdaPlanCarriers;
@property (TQ,V_sourceDevicesCount) sourceDevicesCount;
@property (TQ,V_selectedSourceDevicesCount) selectedSourceDevicesCount;
```

## Class methods

```
+[CTSimSetupUsage supportsSecureCoding];
```

## Instance methods

```
-[CTSimSetupUsage encodeWithCoder:];
-[CTSimSetupUsage description];
-[CTSimSetupUsage initWithCoder:];
-[CTSimSetupUsage isEqual:];
-[CTSimSetupUsage inBuddy];
-[CTSimSetupUsage alsPlanCarriers];
-[CTSimSetupUsage odaPlanCarriers];
-[CTSimSetupUsage alsPlans];
-[CTSimSetupUsage initWithInBuddy:transferablePlans:selectedTransferablePlans:alsPlans:selectedAlsPlans:odaPlans:];
-[CTSimSetupUsage initWithInBuddy:transferablePlans:selectedTransferablePlans:alsPlans:selectedAlsPlans:odaPlans:transferPlanCarriers:selectedTransferPlanCarriers:alsPlanCarriers:selectedAlsPlanCarriers:odaPlanCarriers:selectedOdaPlanCarriers:sourceDevicesCount:selectedSourceDevicesCount:];
-[CTSimSetupUsage odaPlans];
-[CTSimSetupUsage selectedAlsPlanCarriers];
-[CTSimSetupUsage selectedAlsPlans];
-[CTSimSetupUsage selectedOdaPlanCarriers];
-[CTSimSetupUsage selectedSourceDevicesCount];
-[CTSimSetupUsage selectedTransferPlanCarriers];
-[CTSimSetupUsage selectedTransferablePlans];
-[CTSimSetupUsage setAlsPlanCarriers:];
-[CTSimSetupUsage setAlsPlans:];
-[CTSimSetupUsage setInBuddy:];
-[CTSimSetupUsage setOdaPlanCarriers:];
-[CTSimSetupUsage setOdaPlans:];
-[CTSimSetupUsage setSelectedAlsPlanCarriers:];
-[CTSimSetupUsage setSelectedAlsPlans:];
-[CTSimSetupUsage setSelectedOdaPlanCarriers:];
-[CTSimSetupUsage setSelectedSourceDevicesCount:];
-[CTSimSetupUsage setSelectedTransferPlanCarriers:];
-[CTSimSetupUsage setSelectedTransferablePlans:];
-[CTSimSetupUsage setSourceDevicesCount:];
-[CTSimSetupUsage setTransferPlanCarriers:];
-[CTSimSetupUsage setTransferablePlans:];
-[CTSimSetupUsage sourceDevicesCount];
-[CTSimSetupUsage transferPlanCarriers];
-[CTSimSetupUsage transferablePlans];
```
