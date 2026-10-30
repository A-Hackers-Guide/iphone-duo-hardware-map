# `FigCaptureSmartStyle`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FigXPCCoding`, `NSSecureCoding`, `NSCopying`
- 5 instance variables, 10 properties, 16 instance methods, 4 class methods

## Instance variables

```
@"NSString" _cast;
f _intensity;
f _toneBias;
f _colorBias;
Q _hash;
```

## Properties

```
@property (T@"NSString",R,N,V_cast) cast;
@property (Tf,R,N,V_intensity) intensity;
@property (Tf,R,N,V_toneBias) toneBias;
@property (Tf,R,N,V_colorBias) colorBias;
@property (TB,R,N,GisIdentity) identity;
@property (T@"NSDictionary",R,N) dictionaryRepresentation;
@property (TQ,R,V_hash) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FigCaptureSmartStyle supportsSecureCoding];
+[FigCaptureSmartStyle createFromDictionary:];
+[FigCaptureSmartStyle identityStyle];
+[FigCaptureSmartStyle styleWithCast:intensity:toneBias:colorBias:];
```

## Instance methods

```
-[FigCaptureSmartStyle intensity];
-[FigCaptureSmartStyle colorBias];
-[FigCaptureSmartStyle debugDescription];
-[FigCaptureSmartStyle dealloc];
-[FigCaptureSmartStyle encodeWithCoder:];
-[FigCaptureSmartStyle hash];
-[FigCaptureSmartStyle copyXPCEncoding];
-[FigCaptureSmartStyle description];
-[FigCaptureSmartStyle isIdentity];
-[FigCaptureSmartStyle initWithXPCEncoding:];
-[FigCaptureSmartStyle initWithCoder:];
-[FigCaptureSmartStyle toneBias];
-[FigCaptureSmartStyle copyWithZone:];
-[FigCaptureSmartStyle isEqual:];
-[FigCaptureSmartStyle dictionaryRepresentation];
-[FigCaptureSmartStyle cast];
```
