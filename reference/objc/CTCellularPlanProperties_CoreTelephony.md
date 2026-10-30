# `CTCellularPlanProperties`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 4 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"NSString" _associatedIccid;
q _simCapability;
@"NSArray" _supportedRegionCodes;
@"CTCellularPlanLifecycleProperties" _lifecycleProperties;
```

## Properties

```
@property (T@"NSString",&,N,V_associatedIccid) associatedIccid;
@property (Tq,N,V_simCapability) simCapability;
@property (T@"NSArray",&,N,V_supportedRegionCodes) supportedRegionCodes;
@property (T@"CTCellularPlanLifecycleProperties",&,N,V_lifecycleProperties) lifecycleProperties;
```

## Class methods

```
+[CTCellularPlanProperties supportsSecureCoding];
```

## Instance methods

```
-[CTCellularPlanProperties init];
-[CTCellularPlanProperties encodeWithCoder:];
-[CTCellularPlanProperties description];
-[CTCellularPlanProperties initWithCoder:];
-[CTCellularPlanProperties copyWithZone:];
-[CTCellularPlanProperties associatedIccid];
-[CTCellularPlanProperties lifecycleProperties];
-[CTCellularPlanProperties setAssociatedIccid:];
-[CTCellularPlanProperties setLifecycleProperties:];
-[CTCellularPlanProperties setSimCapability:];
-[CTCellularPlanProperties setSupportedRegionCodes:];
-[CTCellularPlanProperties simCapability];
-[CTCellularPlanProperties supportedRegionCodes];
```
