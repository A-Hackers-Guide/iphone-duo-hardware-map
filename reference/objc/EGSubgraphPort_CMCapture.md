# `EGSubgraphPort`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `EGElement`, `EGSourcePort`, `EGDestinationPort`
- 4 instance variables, 10 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSString" _name;
@"EGGraph" _parentGraph;
@"<EGSourcePort>" _source;
@"NSMutableArray" _destinations;
```

## Properties

```
@property (T@"EGGraph",R,W,N) parentGraph;
@property (T@"<EGPortInterface>",R,N) portInterface;
@property (T@"<EGSourcePort>",R,N) source;
@property (T@"NSArray",R,N,V_destinations) destinations;
@property (T@"NSString",R,N,V_name) name;
@property (T@"<EGElement>",R,W,N) parent;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[EGSubgraphPort initialize];
```

## Instance methods

```
-[EGSubgraphPort destinations];
-[EGSubgraphPort dealloc];
-[EGSubgraphPort registerDestination:];
-[EGSubgraphPort parent];
-[EGSubgraphPort description];
-[EGSubgraphPort name];
-[EGSubgraphPort source];
-[EGSubgraphPort initWithName:];
-[EGSubgraphPort registerSource:];
-[EGSubgraphPort setParentGraph:];
-[EGSubgraphPort parentGraph];
-[EGSubgraphPort portInterface];
```
