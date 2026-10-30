# `CTDisplayPlan`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 8 instance variables, 8 properties, 14 instance methods, 1 class methods

## Instance variables

```
B _isPhysical;
B _hasProvisioningServiceImpact;
@"CTPlan" _plan;
@"NSString" _carrierName;
@"NSString" _phoneNumber;
@"NSString" _label;
q _status;
Q _attributes;
```

## Properties

```
@property (T@"CTPlan",R,N,V_plan) plan;
@property (T@"NSString",R,N,V_carrierName) carrierName;
@property (T@"NSString",R,N,V_phoneNumber) phoneNumber;
@property (T@"NSString",R,N,V_label) label;
@property (Tq,R,N,V_status) status;
@property (TQ,R,N,V_attributes) attributes;
@property (TB,R,N,V_isPhysical) isPhysical;
@property (TB,R,N,V_hasProvisioningServiceImpact) hasProvisioningServiceImpact;
```

## Class methods

```
+[CTDisplayPlan supportsSecureCoding];
```

## Instance methods

```
-[CTDisplayPlan phoneNumber];
-[CTDisplayPlan carrierName];
-[CTDisplayPlan label];
-[CTDisplayPlan status];
-[CTDisplayPlan encodeWithCoder:];
-[CTDisplayPlan description];
-[CTDisplayPlan initWithCoder:];
-[CTDisplayPlan attributes];
-[CTDisplayPlan copyWithZone:];
-[CTDisplayPlan isEqual:];
-[CTDisplayPlan plan];
-[CTDisplayPlan hasProvisioningServiceImpact];
-[CTDisplayPlan initWithPlan:status:attributes:isPhysical:carrierName:phoneNumber:label:hasProvisioningServiceImpact:];
-[CTDisplayPlan isPhysical];
```
