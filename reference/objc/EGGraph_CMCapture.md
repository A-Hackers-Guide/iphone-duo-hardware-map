# `EGGraph`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `EGElement`, `EGPortInterface`
- 9 instance variables, 18 properties, 29 instance methods, 1 class methods

## Instance variables

```
@"NSString" _name;
@"EGGraph" _parentGraph;
@"NSMutableDictionary" _nodes;
@"NSMutableDictionary" _subgraphs;
@"NSMutableDictionary" _subgraphInputs;
@"NSMutableDictionary" _subgraphOutputs;
@"EGSubgraphInput" _subgraphInput;
@"EGSubgraphOutput" _subgraphOutput;
@"NSMutableArray" _edges;
```

## Properties

```
@property (T@"NSDictionary",R,N) egNodesByName;
@property (T@"NSDictionary",R,N) egSubgraphsByName;
@property (T@"NSArray",R,N,V_edges) egEdges;
@property (T@"NSDictionary",R,N,V_subgraphInputs) egSubgraphInputsByName;
@property (T@"NSDictionary",R,N,V_subgraphOutputs) egSubgraphOutputsByName;
@property (T@"EGSubgraphInput",R,N,V_subgraphInput) egSubgraphInput;
@property (T@"EGSubgraphOutput",R,N,V_subgraphOutput) egSubgraphOutput;
@property (T@"EGGraph",R,W,N) parentGraph;
@property (T@"NSString",R,N,V_name) name;
@property (T@"<EGElement>",R,W,N) parent;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSDictionary",R,N) egInputPortsByName;
@property (T@"NSDictionary",R,N) egOutputPortsByName;
@property (T@"<EGInputPort>",R,N) egInputPort;
@property (T@"<EGOutputPort>",R,N) egOutputPort;
```

## Class methods

```
+[EGGraph initialize];
```

## Instance methods

```
-[EGGraph dealloc];
-[EGGraph parent];
-[EGGraph description];
-[EGGraph name];
-[EGGraph initWithName:];
-[EGGraph subgraphInputInstalledWithName:];
-[EGGraph egEdges];
-[EGGraph egSubgraphInput];
-[EGGraph setParentGraph:];
-[EGGraph connectExternalSubgraphInput:toInternalInput:];
-[EGGraph connectExternalSubgraphOutput:toInternalOutput:];
-[EGGraph connectOutput:toInput:];
-[EGGraph egInputPort];
-[EGGraph egInputPortsByName];
-[EGGraph egNodesByName];
-[EGGraph egOutputPort];
-[EGGraph egOutputPortsByName];
-[EGGraph egSubgraphInputsByName];
-[EGGraph egSubgraphOutput];
-[EGGraph egSubgraphOutputsByName];
-[EGGraph egSubgraphsByName];
-[EGGraph installNode:];
-[EGGraph installSubgraph:];
-[EGGraph parentGraph];
-[EGGraph subgraphInputInstalledFromInternalInput:];
-[EGGraph subgraphInputInstalledFromInternalInput:withName:];
-[EGGraph subgraphOutputInstalledFromInternalOutput:];
-[EGGraph subgraphOutputInstalledFromInternalOutput:withName:];
-[EGGraph subgraphOutputInstalledWithName:];
```
