# `NWPathFlow`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NWPrettyDescription`
- 1 instance variables, 15 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_nw_path_flow>" _internalPathFlow;
```

## Properties

```
@property (T@"NSObject<OS_nw_path_flow>",R,V_internalPathFlow) internalPathFlow;
@property (T@"NWInterface",R,N) interface;
@property (T@"NWEndpoint",R,N) localEndpoint;
@property (T@"NWEndpoint",R,N) remoteEndpoint;
@property (T@"NSUUID",R,N) flowID;
@property (T@"NSUUID",R,N) nexusAgent;
@property (T@"NSUUID",R,N) nexusInstance;
@property (TI,R,N) nexusPort;
@property (TB,R,N,GisViable) viable;
@property (TB,R,N,GisAssigned) assigned;
@property (TB,R,N,GisLocal) local;
@property (TB,R,N,GisDirect) direct;
@property (TB,R,N,GisDefunct) defunct;
@property (TB,R,N) supportsIPv4;
@property (TB,R,N) supportsIPv6;
```

## Instance methods

```
-[NWPathFlow supportsIPv4];
-[NWPathFlow supportsIPv6];
-[NWPathFlow localEndpoint];
-[NWPathFlow flowID];
-[NWPathFlow isDefunct];
-[NWPathFlow privateDescription];
-[NWPathFlow isLocal];
-[NWPathFlow remoteEndpoint];
-[NWPathFlow descriptionWithIndent:showFullContent:];
-[NWPathFlow interface];
-[NWPathFlow isViable];
-[NWPathFlow description];
-[NWPathFlow isDirect];
-[NWPathFlow initWithPathFlow:];
-[NWPathFlow internalPathFlow];
-[NWPathFlow isAssigned];
-[NWPathFlow nexusAgent];
-[NWPathFlow nexusInstance];
-[NWPathFlow nexusPort];
```
