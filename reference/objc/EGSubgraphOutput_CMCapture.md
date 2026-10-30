# `EGSubgraphOutput`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EGSubgraphPort`
- Protocols: `EGOutputPort`
- 1 instance variables, 9 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"EGOutput" _upstreamNodeOutput;
```

## Properties

```
@property (T@"EGOutput",R,N) upstreamNodeOutput;
@property (T@"NSArray",R,N) destinations;
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
-[EGSubgraphOutput dealloc];
-[EGSubgraphOutput registerDestination:];
-[EGSubgraphOutput registerSource:];
-[EGSubgraphOutput upstreamNodeOutput];
```
