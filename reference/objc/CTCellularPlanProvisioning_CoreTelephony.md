# `CTCellularPlanProvisioning`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 6 instance methods, 0 class methods

## Instance variables

```
B _supportsEmbeddedSIM;
@"CoreTelephonyClient" _client;
```

## Properties

```
@property (TB,R,N,V_supportsEmbeddedSIM) supportsEmbeddedSIM;
```

## Instance methods

```
-[CTCellularPlanProvisioning init];
-[CTCellularPlanProvisioning addPlanWith:completionHandler:];
-[CTCellularPlanProvisioning addPlanWithRequest:properties:completionHandler:];
-[CTCellularPlanProvisioning supportsCellularPlan];
-[CTCellularPlanProvisioning supportsEmbeddedSIM];
-[CTCellularPlanProvisioning updateCellularPlanProperties:completionHandler:];
```
