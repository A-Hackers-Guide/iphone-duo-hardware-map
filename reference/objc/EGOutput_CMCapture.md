# `EGOutput`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `EGElement`, `EGOutputPort`
- 5 instance variables, 11 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"NSString" _name;
@"EGNode" _parentNode;
@"NSMutableArray" _destinations;
@"NSMutableArray" _downstreamNodeInputPorts;
i _emittedCount;
```

## Properties

```
@property (Ti,R,N,V_emittedCount) emittedCount;
@property (T@"NSArray",R,N,V_downstreamNodeInputPorts) downstreamNodeInputPorts;
@property (T@"NSArray",R,N,V_destinations) destinations;
@property (T@"<EGPortInterface>",R,N) portInterface;
@property (T@"NSString",R,N,V_name) name;
@property (T@"<EGElement>",R,W,N) parent;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"EGOutput",R,N) upstreamNodeOutput;
```

## Class methods

```
+[EGOutput initialize];
```

## Instance methods

```
-[EGOutput destinations];
-[EGOutput dealloc];
-[EGOutput registerDestination:];
-[EGOutput parent];
-[EGOutput description];
-[EGOutput name];
-[EGOutput initWithName:];
-[EGOutput setParentNode:];
-[EGOutput downstreamNodeInputPorts];
-[EGOutput emit:];
-[EGOutput emittedCount];
-[EGOutput portInterface];
-[EGOutput registerConnectedInputPort:];
-[EGOutput upstreamNodeOutput];
```
