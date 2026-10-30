# `FigCaptureSemanticStyleSet`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FigXPCCoding`, `NSCopying`
- 2 instance variables, 6 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _semanticStyles;
@"NSArray" _regions;
```

## Properties

```
@property (T@"NSArray",R,N) semanticStyles;
@property (T@"NSArray",R,N) regions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FigCaptureSemanticStyleSet semanticStyleSetWithSemanticStyles:regions:];
```

## Instance methods

```
-[FigCaptureSemanticStyleSet regions];
-[FigCaptureSemanticStyleSet semanticStyles];
-[FigCaptureSemanticStyleSet dealloc];
-[FigCaptureSemanticStyleSet regionAtIndex:];
-[FigCaptureSemanticStyleSet copyXPCEncoding];
-[FigCaptureSemanticStyleSet description];
-[FigCaptureSemanticStyleSet initWithXPCEncoding:];
-[FigCaptureSemanticStyleSet copyWithZone:];
-[FigCaptureSemanticStyleSet largestEdgeOffset];
-[FigCaptureSemanticStyleSet largestRegionSemanticStyle];
-[FigCaptureSemanticStyleSet leftmostRegionStartXOffset];
```
