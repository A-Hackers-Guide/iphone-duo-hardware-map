# `CTDataConnectionAgentData`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 14 instance methods, 1 class methods

## Instance variables

```
i _registrationStatus;
i _dataPlanTier;
@"NSNumber" _inHomeCountry;
```

## Properties

```
@property (Ti,N,V_registrationStatus) registrationStatus;
@property (T@"NSNumber",&,N,V_inHomeCountry) inHomeCountry;
@property (Ti,N,V_dataPlanTier) dataPlanTier;
```

## Class methods

```
+[CTDataConnectionAgentData supportsSecureCoding];
```

## Instance methods

```
-[CTDataConnectionAgentData initAgentDataFromPath:agentType:];
-[CTDataConnectionAgentData setDataPlanTier:];
-[CTDataConnectionAgentData initAgentDataFromInternetPath:];
-[CTDataConnectionAgentData setRegistrationStatus:];
-[CTDataConnectionAgentData encodeWithCoder:];
-[CTDataConnectionAgentData setInHomeCountry:];
-[CTDataConnectionAgentData registrationStatus];
-[CTDataConnectionAgentData description];
-[CTDataConnectionAgentData initWithCoder:];
-[CTDataConnectionAgentData copyWithZone:];
-[CTDataConnectionAgentData dataPlanTier];
-[CTDataConnectionAgentData inHomeCountry];
-[CTDataConnectionAgentData initAgentDataFromPath:domain:agentType:];
-[CTDataConnectionAgentData initAgentDataFromCellularInternetPath];
```
