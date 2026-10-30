# `NWProtocolTransform`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NWPrettyDescription`
- 1 instance variables, 10 properties, 32 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_nw_protocol_transform>" _internalTransform;
```

## Properties

```
@property (T@"NSObject<OS_nw_protocol_transform>",&,V_internalTransform) internalTransform;
@property (TB,N) noProxy;
@property (Ti,N) multipathService;
@property (T@"NWEndpoint",C,N) replacementEndpoint;
@property (TB,N) tfo;
@property (TB,N) tfoNoCookie;
@property (Ti,N) dataMode;
@property (TQ,N) fallbackMode;
@property (TB,N) prohibitDirect;
@property (TB,N) disablePathFallback;
```

## Instance methods

```
-[NWProtocolTransform init];
-[NWProtocolTransform privateDescription];
-[NWProtocolTransform descriptionWithIndent:showFullContent:];
-[NWProtocolTransform setNoProxy:];
-[NWProtocolTransform setMultipathService:];
-[NWProtocolTransform noProxy];
-[NWProtocolTransform hash];
-[NWProtocolTransform dataMode];
-[NWProtocolTransform description];
-[NWProtocolTransform fastOpenForceEnable];
-[NWProtocolTransform setFastOpenForceEnable:];
-[NWProtocolTransform setDataMode:];
-[NWProtocolTransform multipathService];
-[NWProtocolTransform isEqual:];
-[NWProtocolTransform setTfo:];
-[NWProtocolTransform tfo];
-[NWProtocolTransform setTfoNoCookie:];
-[NWProtocolTransform appendProtocol:atLevel:];
-[NWProtocolTransform clearProtocolsAtLevel:];
-[NWProtocolTransform disablePathFallback];
-[NWProtocolTransform disableProtocol:];
-[NWProtocolTransform fallbackMode];
-[NWProtocolTransform initWithCTransform:];
-[NWProtocolTransform internalTransform];
-[NWProtocolTransform prohibitDirect];
-[NWProtocolTransform replacementEndpoint];
-[NWProtocolTransform setDisablePathFallback:];
-[NWProtocolTransform setFallbackMode:];
-[NWProtocolTransform setInternalTransform:];
-[NWProtocolTransform setProhibitDirect:];
-[NWProtocolTransform setReplacementEndpoint:];
-[NWProtocolTransform tfoNoCookie];
```
