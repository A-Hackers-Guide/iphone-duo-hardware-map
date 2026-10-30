# `FigCaptureSinkConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FigXPCCoding`, `NSCopying`, `NSSecureCoding`
- 2 instance variables, 7 properties, 15 instance methods, 2 class methods

## Instance variables

```
@"NSString" _sinkID;
B _deferredStartEnabled;
```

## Properties

```
@property (T@"NSString",C,N,V_sinkID) sinkID;
@property (Ti,R,N) sinkType;
@property (TB,N,V_deferredStartEnabled) deferredStartEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FigCaptureSinkConfiguration supportsSecureCoding];
+[FigCaptureSinkConfiguration stringForSinkType:];
```

## Instance methods

```
-[FigCaptureSinkConfiguration sinkType];
-[FigCaptureSinkConfiguration reasonForNotEqualingConfiguration:];
-[FigCaptureSinkConfiguration dealloc];
-[FigCaptureSinkConfiguration encodeWithCoder:];
-[FigCaptureSinkConfiguration hash];
-[FigCaptureSinkConfiguration copyXPCEncoding];
-[FigCaptureSinkConfiguration description];
-[FigCaptureSinkConfiguration initWithXPCEncoding:];
-[FigCaptureSinkConfiguration initWithCoder:];
-[FigCaptureSinkConfiguration setSinkID:];
-[FigCaptureSinkConfiguration copyWithZone:];
-[FigCaptureSinkConfiguration setDeferredStartEnabled:];
-[FigCaptureSinkConfiguration isEqual:];
-[FigCaptureSinkConfiguration sinkID];
-[FigCaptureSinkConfiguration deferredStartEnabled];
```
