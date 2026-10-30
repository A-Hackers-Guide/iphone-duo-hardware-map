# `NWGenericNetworkAgent`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NWPrettyDescription`
- 1 instance variables, 13 properties, 23 instance methods, 0 class methods

## Instance variables

```
^{netagent=[16C][32c][32c][128c]II[0C]} _internalNetagent;
```

## Properties

```
@property (T^{netagent=[16C][32c][32c][128c]II[0C]},V_internalNetagent) internalNetagent;
@property (T@"NSString",R,C,N) privateDescription;
@property (T@"NSString",R,N) agentDomain;
@property (T@"NSString",R,N) agentType;
@property (T@"NSString",R,N) agentDescription;
@property (T@"NSUUID",R,N) agentUUID;
@property (TI,R,N) agentDataSize;
@property (TB,R,N,GisActive) active;
@property (TB,R,N,GisKernelActivated) kernelActivated;
@property (TB,R,N,GisUserActivated) userActivated;
@property (TB,R,N,GisVoluntary) voluntary;
@property (TB,R,N,GisSpecificUseOnly) specificUseOnly;
@property (TB,R,N,GisNetworkProvider) networkProvider;
```

## Instance methods

```
-[NWGenericNetworkAgent dealloc];
-[NWGenericNetworkAgent privateDescription];
-[NWGenericNetworkAgent descriptionWithIndent:showFullContent:];
-[NWGenericNetworkAgent description];
-[NWGenericNetworkAgent isActive];
-[NWGenericNetworkAgent isUserActivated];
-[NWGenericNetworkAgent isNexusProvider];
-[NWGenericNetworkAgent supportsResolve];
-[NWGenericNetworkAgent agentDataSize];
-[NWGenericNetworkAgent agentDescription];
-[NWGenericNetworkAgent agentDomain];
-[NWGenericNetworkAgent agentType];
-[NWGenericNetworkAgent agentUUID];
-[NWGenericNetworkAgent initWithKernelAgent:];
-[NWGenericNetworkAgent internalNetagent];
-[NWGenericNetworkAgent isKernelActivated];
-[NWGenericNetworkAgent isNetworkProvider];
-[NWGenericNetworkAgent isSpecificUseOnly];
-[NWGenericNetworkAgent isVoluntary];
-[NWGenericNetworkAgent requiresAssert];
-[NWGenericNetworkAgent setInternalNetagent:];
-[NWGenericNetworkAgent supportsBrowse];
-[NWGenericNetworkAgent supportsGroups];
```
