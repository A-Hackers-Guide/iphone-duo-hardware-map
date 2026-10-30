# `NWNetworkDescription`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 8 properties, 22 instance methods, 1 class methods

## Instance variables

```
@"NSSet" _interfaceTypeOptions;
@"NSSet" _ssidOptions;
@"NSSet" _dnsSearchDomainOptions;
@"NSSet" _dnsServerAddressOptions;
q _roamingPreference;
@"NSURL" _probeURL;
q _state;
```

## Properties

```
@property (Tq,V_state) state;
@property (T@"NSString",R,N) privateDescription;
@property (T@"NSSet",C,V_interfaceTypeOptions) interfaceTypeOptions;
@property (T@"NSSet",C,V_ssidOptions) ssidOptions;
@property (T@"NSSet",C,V_dnsSearchDomainOptions) dnsSearchDomainOptions;
@property (T@"NSSet",C,V_dnsServerAddressOptions) dnsServerAddressOptions;
@property (Tq,V_roamingPreference) roamingPreference;
@property (T@"NSURL",C,V_probeURL) probeURL;
```

## Class methods

```
+[NWNetworkDescription getNewStateFromPathMatch:oldState:probeExists:];
```

## Instance methods

```
-[NWNetworkDescription setState:];
-[NWNetworkDescription interfaceTypeOptions];
-[NWNetworkDescription setDnsSearchDomainOptions:];
-[NWNetworkDescription matchesPath:];
-[NWNetworkDescription updateStateWithPath:];
-[NWNetworkDescription probeURL];
-[NWNetworkDescription privateDescription];
-[NWNetworkDescription dnsServerAddressOptions];
-[NWNetworkDescription setInterfaceTypeOptions:];
-[NWNetworkDescription descriptionWithIndent:showFullContent:];
-[NWNetworkDescription setSsidOptions:];
-[NWNetworkDescription setRoamingPreference:];
-[NWNetworkDescription dnsSearchDomainOptions];
-[NWNetworkDescription setProbeURL:];
-[NWNetworkDescription hash];
-[NWNetworkDescription description];
-[NWNetworkDescription setDnsServerAddressOptions:];
-[NWNetworkDescription copyWithZone:];
-[NWNetworkDescription isEqual:];
-[NWNetworkDescription roamingPreference];
-[NWNetworkDescription state];
-[NWNetworkDescription ssidOptions];
```
