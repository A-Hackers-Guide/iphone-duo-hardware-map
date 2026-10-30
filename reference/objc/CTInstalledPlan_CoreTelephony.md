# `CTInstalledPlan`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 14 instance methods, 1 class methods

## Instance variables

```
B _isSelected;
@"CTPlanIdentifier" _planID;
@"CTPlanTransferAttributes" _transferAttributes;
```

## Properties

```
@property (T@"CTPlanIdentifier",&,N,V_planID) planID;
@property (TB,N,V_isSelected) isSelected;
@property (T@"CTPlanTransferAttributes",&,N,V_transferAttributes) transferAttributes;
```

## Class methods

```
+[CTInstalledPlan supportsSecureCoding];
```

## Instance methods

```
-[CTInstalledPlan phoneNumber];
-[CTInstalledPlan carrierName];
-[CTInstalledPlan init];
-[CTInstalledPlan iccid];
-[CTInstalledPlan encodeWithCoder:];
-[CTInstalledPlan isSelected];
-[CTInstalledPlan description];
-[CTInstalledPlan setIsSelected:];
-[CTInstalledPlan initWithCoder:];
-[CTInstalledPlan isEqual:];
-[CTInstalledPlan planID];
-[CTInstalledPlan setPlanID:];
-[CTInstalledPlan setTransferAttributes:];
-[CTInstalledPlan transferAttributes];
```
