# `NWPath`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NWPrettyDescription`
- 1 instance variables, 63 properties, 88 instance methods, 5 class methods

## Instance variables

```
@"NSObject<OS_nw_path>" _internalPath;
```

## Properties

```
@property (T@"NSObject<OS_nw_path>",R,V_internalPath) internalPath;
@property (TI,R,N) fallbackInterfaceIndex;
@property (TB,R,N) fallbackIsWeak;
@property (TB,R,N) fallbackEligible;
@property (TB,R,N) fallbackIsPreferred;
@property (TB,R,N) fallbackIsOpportunistic;
@property (T@"NSArray",R,N) dnsServersAsStrings;
@property (T@"NSArray",R,N) gateways;
@property (T@"NSArray",R,N) groupMembers;
@property (T@"NSArray",R,N) flows;
@property (T@"NSString",R,N) statusAsString;
@property (T@"NWInterface",R,N) connectedInterface;
@property (TB,R,N,GisListener) listener;
@property (TB,R,N,GisViable) viable;
@property (TB,R,N) hasProxySettings;
@property (T@"NSArray",R,N) overrideDNSServers;
@property (T@"NSArray",R,N) overrideDNSServersAsStrings;
@property (T@"NSArray",R,N) overrideDNSSearchDomains;
@property (T@"NSUUID",R,N) clientID;
@property (T@"NWInterface",R,N) interface;
@property (T@"NWInterface",R,N) scopedInterface;
@property (T@"NWInterface",R,N) fallbackInterface;
@property (TB,R,N,GisFlowDivert) flowDivert;
@property (TI,R,N) flowDivertControlUnit;
@property (TI,R,N) flowDivertAggregateUnit;
@property (TB,R,N,GisFiltered) filtered;
@property (TI,R,N) filterControlUnit;
@property (Ti,R,N) dnsServiceID;
@property (TB,R,N,GisLocal) local;
@property (TB,R,N,GisDirect) direct;
@property (TI,R,N) policyID;
@property (TB,R,N,GisRoaming) roaming;
@property (Tq,R,N) mtu;
@property (Tq,R,N) maximumDatagramSize;
@property (TQ,R,N) secondsSinceInterfaceChange;
@property (Tq,R,N) reason;
@property (T@"NSString",R,N) reasonDescription;
@property (T@"NSString",R,C,N) privateDescription;
@property (T@"NWParameters",R,N) derivedParameters;
@property (TB,R,N) supportsIPv4;
@property (TB,R,N) supportsIPv6;
@property (TB,R,N) supportsDNS;
@property (TB,R,N,GisEligibleForCrazyIvan46) eligibleForCrazyIvan46;
@property (T@"NWEndpoint",R,N) endpoint;
@property (T@"NWParameters",R,N) parameters;
@property (T@"NWEndpoint",R,N) effectiveLocalEndpoint;
@property (T@"NWEndpoint",R,N) effectiveRemoteEndpoint;
@property (T@"NSArray",R,N) proxySettings;
@property (T@"NSArray",R,N) dnsServers;
@property (T@"NSArray",R,N) dnsSearchDomains;
@property (TB,R,N) hasBrowseDescriptor;
@property (T@"NWBrowseDescriptor",R,N) browseDescriptor;
@property (TB,R,N) hasAdvertiseDescriptor;
@property (T@"NWAdvertiseDescriptor",R,N) advertiseDescriptor;
@property (TB,R,N,GisPerAppVPN) perAppVPN;
@property (TB,R,N) hasKernelExtensionFilter;
@property (TB,R,N) hasCustomPFRules;
@property (TB,R,N) hasApplicationLevelFirewall;
@property (TB,R,N) hasParentalControls;
@property (T@"NSObject<OS_nw_path>",R,N) cPath;
@property (Tq,R,N) status;
@property (TB,R,N,GisExpensive) expensive;
@property (TB,R,N,GisConstrained) constrained;
```

## Class methods

```
+[NWPath allClientIDs];
+[NWPath createStringFromStatus:];
+[NWPath pathForClientID:];
+[NWPath pathForClientID:parametersTLV:pathResultTLV:];
+[NWPath pathWithProtocolBufferData:];
```

## Instance methods

```
-[NWPath supportsIPv4];
-[NWPath supportsIPv6];
-[NWPath mtu];
-[NWPath isConstrained];
-[NWPath isExpensive];
-[NWPath clientID];
-[NWPath fallbackEligible];
-[NWPath parameters];
-[NWPath inactiveNetworkAgentUUIDsOnlyVoluntary:];
-[NWPath isRoaming];
-[NWPath initWithPath:];
-[NWPath createProtocolBufferObject];
-[NWPath isPerAppVPN];
-[NWPath init];
-[NWPath groupMembers];
-[NWPath secondsSinceInterfaceChange];
-[NWPath effectiveRemoteEndpoint];
-[NWPath overrideDNSServers];
-[NWPath copyDNSSearchDomains:];
-[NWPath hasAdvertiseDescriptor];
-[NWPath effectiveLocalEndpoint];
-[NWPath shouldProbeConnectivity];
-[NWPath endpoint];
-[NWPath fallbackInterface];
-[NWPath browseDescriptor];
-[NWPath status];
-[NWPath copyFlowDivertToken];
-[NWPath dnsSearchDomains];
-[NWPath gateways];
-[NWPath dnsServersAsStrings];
-[NWPath advertiseDescriptor];
-[NWPath copyDataFromNetworkAgentWithDomain:type:];
-[NWPath hasParentalControls];
-[NWPath fallbackInterfaceIndex];
-[NWPath privateDescription];
-[NWPath isLocal];
-[NWPath unsatisfiedVoluntaryAgentMatchesAddress:triggerImmediately:];
-[NWPath usesNetworkAgentType:];
-[NWPath hasKernelExtensionFilter];
-[NWPath descriptionWithIndent:showFullContent:];
-[NWPath hasProxySettings];
-[NWPath flowDivertControlUnit];
-[NWPath interface];
-[NWPath policyID];
-[NWPath flows];
-[NWPath usesNetworkAgent:];
-[NWPath filterControlUnit];
-[NWPath copyDNSServersStrings:];
-[NWPath isUltraConstrained];
-[NWPath reasonDescription];
-[NWPath isFlowDivert];
-[NWPath dnsServiceID];
-[NWPath isListener];
-[NWPath usesCompanion];
-[NWPath isViable];
-[NWPath internalPath];
-[NWPath isLinkQualityAbort];
-[NWPath isEqualToPath:];
-[NWPath derivedParameters];
-[NWPath isFiltered];
-[NWPath genericNetworkAgentsWithDomain:type:];
-[NWPath maximumDatagramSize];
-[NWPath hasApplicationLevelFirewall];
-[NWPath statusAsString];
-[NWPath hasCustomPFRules];
-[NWPath description];
-[NWPath delegateInterface];
-[NWPath proxySettings];
-[NWPath hasUnsatisfiedFallbackAgent];
-[NWPath hasBrowseDescriptor];
-[NWPath copyDNSServerEndpoints:];
-[NWPath networkAgentsOfType:];
-[NWPath dnsServers];
-[NWPath reason];
-[NWPath flowDivertAggregateUnit];
-[NWPath isDirect];
-[NWPath supportsDNS];
-[NWPath isListenerInterfaceSpecific];
-[NWPath fallbackIsWeak];
-[NWPath fallbackIsPreferred];
-[NWPath scopedInterface];
-[NWPath cPath];
-[NWPath isEligibleForCrazyIvan46];
-[NWPath usesInterfaceType:];
-[NWPath fallbackIsOpportunistic];
-[NWPath overrideDNSServersAsStrings];
-[NWPath connectedInterface];
-[NWPath overrideDNSSearchDomains];
```
