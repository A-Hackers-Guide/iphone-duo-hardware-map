# `AVCaptureSmartStyle`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 5 properties, 11 instance methods, 2 class methods

## Instance variables

```
@"NSString" _cast;
f _intensity;
f _toneBias;
f _colorBias;
Q _hash;
q _version;
```

## Properties

```
@property (T@"NSString",R,N,V_cast) cast;
@property (Tf,R,N,V_intensity) intensity;
@property (Tf,R,N,V_toneBias) toneBias;
@property (Tf,R,N,V_colorBias) colorBias;
@property (Tq,R,N,V_version) version;
```

## Class methods

```
+[AVCaptureSmartStyle identityStyle];
+[AVCaptureSmartStyle styleWithCast:intensity:toneBias:colorBias:];
```

## Instance methods

```
-[AVCaptureSmartStyle intensity];
-[AVCaptureSmartStyle colorBias];
-[AVCaptureSmartStyle debugDescription];
-[AVCaptureSmartStyle dealloc];
-[AVCaptureSmartStyle version];
-[AVCaptureSmartStyle hash];
-[AVCaptureSmartStyle description];
-[AVCaptureSmartStyle toneBias];
-[AVCaptureSmartStyle isEqual:];
-[AVCaptureSmartStyle cast];
-[AVCaptureSmartStyle _initWithCast:intensity:toneBias:colorBias:];
```
