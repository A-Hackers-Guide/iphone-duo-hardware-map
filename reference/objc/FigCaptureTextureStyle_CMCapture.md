# `FigCaptureTextureStyle`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FigXPCCoding`, `NSSecureCoding`, `NSCopying`
- 4 instance variables, 9 properties, 16 instance methods, 4 class methods

## Instance variables

```
@"NSString" _preset;
f _intensity;
f _grain;
Q _hash;
```

## Properties

```
@property (T@"NSString",R,N,V_preset) preset;
@property (Tf,R,N,V_intensity) intensity;
@property (Tf,R,N,V_grain) grain;
@property (TB,R,N,GisIdentity) identity;
@property (T@"NSDictionary",R,N) dictionaryRepresentation;
@property (TQ,R,V_hash) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FigCaptureTextureStyle supportsSecureCoding];
+[FigCaptureTextureStyle createFromDictionary:];
+[FigCaptureTextureStyle identityStyle];
+[FigCaptureTextureStyle styleWithPreset:intensity:grain:];
```

## Instance methods

```
-[FigCaptureTextureStyle intensity];
-[FigCaptureTextureStyle debugDescription];
-[FigCaptureTextureStyle preset];
-[FigCaptureTextureStyle dealloc];
-[FigCaptureTextureStyle encodeWithCoder:];
-[FigCaptureTextureStyle hash];
-[FigCaptureTextureStyle copyXPCEncoding];
-[FigCaptureTextureStyle description];
-[FigCaptureTextureStyle isIdentity];
-[FigCaptureTextureStyle initWithXPCEncoding:];
-[FigCaptureTextureStyle initWithCoder:];
-[FigCaptureTextureStyle copyWithZone:];
-[FigCaptureTextureStyle isEqual:];
-[FigCaptureTextureStyle dictionaryRepresentation];
-[FigCaptureTextureStyle grain];
-[FigCaptureTextureStyle isStandardPreset];
```
