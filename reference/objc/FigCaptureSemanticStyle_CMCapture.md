# `FigCaptureSemanticStyle`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FigXPCCoding`, `NSSecureCoding`
- 5 instance variables, 9 properties, 13 instance methods, 3 class methods

## Instance variables

```
f _toneBias;
f _mappedToneBias;
f _warmthBias;
f _mappedWarmthBias;
Q _hash;
```

## Properties

```
@property (Tf,R,N,V_toneBias) toneBias;
@property (Tf,R,N,V_mappedToneBias) mappedToneBias;
@property (Tf,R,N,V_warmthBias) warmthBias;
@property (Tf,R,N,V_mappedWarmthBias) mappedWarmthBias;
@property (TB,R,N,GisIdentity) identity;
@property (TQ,R,V_hash) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FigCaptureSemanticStyle supportsSecureCoding];
+[FigCaptureSemanticStyle identityStyle];
+[FigCaptureSemanticStyle semanticStyleWithToneBias:warmthBias:];
```

## Instance methods

```
-[FigCaptureSemanticStyle debugDescription];
-[FigCaptureSemanticStyle encodeWithCoder:];
-[FigCaptureSemanticStyle hash];
-[FigCaptureSemanticStyle copyXPCEncoding];
-[FigCaptureSemanticStyle description];
-[FigCaptureSemanticStyle isIdentity];
-[FigCaptureSemanticStyle initWithXPCEncoding:];
-[FigCaptureSemanticStyle initWithCoder:];
-[FigCaptureSemanticStyle toneBias];
-[FigCaptureSemanticStyle isEqual:];
-[FigCaptureSemanticStyle warmthBias];
-[FigCaptureSemanticStyle mappedToneBias];
-[FigCaptureSemanticStyle mappedWarmthBias];
```
