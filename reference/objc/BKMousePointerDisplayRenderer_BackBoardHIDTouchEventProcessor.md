# `BKMousePointerDisplayRenderer`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 8 instance variables, 8 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"CAContext" _context;
@"NSString" _displayName;
@"CALayer" _rootLayer;
@"CALayer" _transformLayer;
@"CALayer" _pointerLayer;
{CGPoint="x"d"y"d} _pointerPosition;
{BKMousePointerDisplayRendererTransformLayerProperties="affineTransform"{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d}"bounds"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}} _transformLayerProperties;
{BKMousePointerDisplayRendererRootLayerProperties="affineTransform"{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d}"bounds"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"displayScale"d} _rootLayerProperties;
```

## Properties

```
@property (T@"CALayer",&,N,V_pointerLayer) pointerLayer;
@property (T{CGPoint=dd},N,V_pointerPosition) pointerPosition;
@property (T{BKMousePointerDisplayRendererRootLayerProperties={CGAffineTransform=dddddd}{CGRect={CGPoint=dd}{CGSize=dd}}d},N,V_rootLayerProperties) rootLayerProperties;
@property (T{BKMousePointerDisplayRendererTransformLayerProperties={CGAffineTransform=dddddd}{CGRect={CGPoint=dd}{CGSize=dd}}},N,V_transformLayerProperties) transformLayerProperties;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKMousePointerDisplayRenderer rootLayerPropertiesForDisplay:displayRenderSpace:];
```

## Instance methods

```
-[BKMousePointerDisplayRenderer invalidate];
-[BKMousePointerDisplayRenderer setPointerPosition:];
-[BKMousePointerDisplayRenderer initWithDisplayName:];
-[BKMousePointerDisplayRenderer pointerPosition];
-[BKMousePointerDisplayRenderer _updateTransformLayerPosition];
-[BKMousePointerDisplayRenderer pointerLayer];
-[BKMousePointerDisplayRenderer rootLayerProperties];
-[BKMousePointerDisplayRenderer setPointerLayer:];
-[BKMousePointerDisplayRenderer setRootLayerProperties:];
-[BKMousePointerDisplayRenderer setTransformLayerProperties:];
-[BKMousePointerDisplayRenderer transformLayerProperties];
```
