# `EGInput`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `EGElement`, `EGNodeInput`, `EGInputPort`
- 4 instance variables, 8 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"NSString" _name;
@"<EGInputHandler>" _inputHandler;
@"<EGSourcePort>" _source;
@"<EGPortInterface>" _portInterface;
```

## Properties

```
@property (T@"<EGPortInterface>",R,N) portInterface;
@property (T@"<EGSourcePort>",R,N) source;
@property (T@"NSString",R,N,V_name) name;
@property (T@"<EGElement>",R,W,N) parent;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[EGInput initialize];
```

## Instance methods

```
-[EGInput dealloc];
-[EGInput parent];
-[EGInput description];
-[EGInput setInputHandler:];
-[EGInput name];
-[EGInput source];
-[EGInput initWithName:];
-[EGInput receiveData:];
-[EGInput handleData:];
-[EGInput registerSource:];
-[EGInput addDownstreamNodeInputPortsIntoArray:];
-[EGInput addInputsIntoArray:];
-[EGInput portInterface];
-[EGInput setPortInterface:];
```
