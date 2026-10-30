# `EGNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `EGElement`, `EGPortInterface`, `EGInputHandler`, `EGInputGroupHandler`
- 8 instance variables, 16 properties, 23 instance methods, 1 class methods

## Instance variables

```
@"NSString" _name;
@"EGGraph" _parentGraph;
@"NSMutableDictionary" _outputs;
@"NSMutableDictionary" _inputs;
@"NSMutableDictionary" _inputPorts;
@"<EGNodeInput>" _egNodeInput;
@"<EGInputPort>" _egInputPort;
@"EGOutput" _egOutput;
```

## Properties

```
@property (T@"NSDictionary",R,N) egInputsByName;
@property (T@"NSDictionary",R,N) egOutputsByName;
@property (T@"NSArray",R,N) egInputsFlat;
@property (T@"<EGNodeInput>",R,N) egNodeInput;
@property (T@"EGOutput",R,N) egOutput;
@property (T@"NSDictionary",R,N) egInputPortsByName;
@property (T@"<EGInputPort>",R,N) egInputPort;
@property (T@"NSString",R,N,V_name) name;
@property (T@"<EGElement>",R,W,N) parent;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSDictionary",R,N) egOutputPortsByName;
@property (T@"<EGOutputPort>",R,N) egOutputPort;
@property (T@"EGGraph",R,W,N) parentGraph;
```

## Class methods

```
+[EGNode initialize];
```

## Instance methods

```
-[EGNode dealloc];
-[EGNode parent];
-[EGNode description];
-[EGNode name];
-[EGNode initWithName:];
-[EGNode egOutputsByName];
-[EGNode setParentGraph:];
-[EGNode egInputPort];
-[EGNode egInputPortsByName];
-[EGNode egInputsByName];
-[EGNode egInputsFlat];
-[EGNode egNodeInput];
-[EGNode egOutput];
-[EGNode egOutputPort];
-[EGNode egOutputPortsByName];
-[EGNode inputInstalledWithName:];
-[EGNode installInput:];
-[EGNode installInputGroup:];
-[EGNode installOutput:];
-[EGNode outputInstalledWithName:];
-[EGNode parentGraph];
-[EGNode receiveData:fromInput:];
-[EGNode receiveData:fromInputGroup:];
```
