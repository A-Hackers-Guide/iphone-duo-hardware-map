# `EGSubgraphInput`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EGSubgraphPort`
- Protocols: `EGInputPort`
- 1 instance variables, 9 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _downstreamNodeInputPorts;
```

## Properties

```
@property (T@"NSArray",R,N) downstreamNodeInputPorts;
@property (T@"<EGSourcePort>",R,N) source;
@property (T@"<EGPortInterface>",R,N) portInterface;
@property (T@"NSString",R,N) name;
@property (T@"<EGElement>",R,W,N) parent;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[EGSubgraphInput dealloc];
-[EGSubgraphInput registerDestination:];
-[EGSubgraphInput initWithName:];
-[EGSubgraphInput registerSource:];
-[EGSubgraphInput addDownstreamNodeInputPortsIntoArray:];
-[EGSubgraphInput downstreamNodeInputPorts];
```
