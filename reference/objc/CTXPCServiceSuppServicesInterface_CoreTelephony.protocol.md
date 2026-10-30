# `CTXPCServiceSuppServicesInterface` (protocol)

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 0 properties, 12 instance methods, 0 class methods

## Instance methods

```
-[CTXPCServiceSuppServicesInterface fetchCallBarringValue:facility:callClass:password:completion:];
-[CTXPCServiceSuppServicesInterface fetchCallForwardingValue:reason:callClass:completion:];
-[CTXPCServiceSuppServicesInterface fetchCallWaitingValue:callClass:completion:];
-[CTXPCServiceSuppServicesInterface fetchCallingLineIdRestrictionValue:completion:];
-[CTXPCServiceSuppServicesInterface fetchCallingLinePresentationValue:completion:];
-[CTXPCServiceSuppServicesInterface fetchConnectedLineIdRestrictionValue:completion:];
-[CTXPCServiceSuppServicesInterface fetchConnectedLinePresentationValue:completion:];
-[CTXPCServiceSuppServicesInterface isUnconditionalCallForwardingActive:completion:];
-[CTXPCServiceSuppServicesInterface saveCallBarringValue:facility:callClass:enabled:password:completion:];
-[CTXPCServiceSuppServicesInterface saveCallForwardingValue:value:completion:];
-[CTXPCServiceSuppServicesInterface saveCallWaitingValue:callClass:enabled:completion:];
-[CTXPCServiceSuppServicesInterface saveCallingLineIdRestrictionValue:restrictionValue:completion:];
```
