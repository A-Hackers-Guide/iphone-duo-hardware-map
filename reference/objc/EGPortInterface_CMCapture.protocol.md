# `EGPortInterface` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `EGElement`
- 0 instance variables, 5 properties, 5 instance methods, 0 class methods

## Properties

```
@property (T@"NSDictionary",R,N) egInputPortsByName;
@property (T@"NSDictionary",R,N) egOutputPortsByName;
@property (T@"<EGInputPort>",R,N) egInputPort;
@property (T@"<EGOutputPort>",R,N) egOutputPort;
@property (T@"EGGraph",R,W,N) parentGraph;
```

## Instance methods

```
-[EGPortInterface egInputPort];
-[EGPortInterface egInputPortsByName];
-[EGPortInterface egOutputPort];
-[EGPortInterface egOutputPortsByName];
-[EGPortInterface parentGraph];
```
