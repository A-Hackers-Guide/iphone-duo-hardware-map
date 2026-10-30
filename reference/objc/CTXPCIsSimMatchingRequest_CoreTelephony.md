# `CTXPCIsSimMatchingRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCSubscriptionContextRequest`
- 1 instance variables, 1 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _carrierDescriptors;
```

## Properties

```
@property (T@"NSArray",&,N,V_carrierDescriptors) carrierDescriptors;
```

## Class methods

```
+[CTXPCIsSimMatchingRequest supportsSecureCoding];
```

## Instance methods

```
-[CTXPCIsSimMatchingRequest requiredEntitlement];
-[CTXPCIsSimMatchingRequest ct_shortName];
-[CTXPCIsSimMatchingRequest encodeWithCoder:];
-[CTXPCIsSimMatchingRequest initWithCoder:];
-[CTXPCIsSimMatchingRequest performRequestWithHandler:completionHandler:];
-[CTXPCIsSimMatchingRequest carrierDescriptors];
-[CTXPCIsSimMatchingRequest initWithDescriptor:carrierDescriptors:];
-[CTXPCIsSimMatchingRequest setCarrierDescriptors:];
```
