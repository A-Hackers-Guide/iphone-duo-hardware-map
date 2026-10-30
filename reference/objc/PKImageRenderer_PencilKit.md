# `PKImageRenderer`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 8 properties, 40 instance methods, 3 class methods

## Instance variables

```
B _extendedDynamicRange;
B _synchronous;
d _scale;
@"PKMetalRendererController" _rendererController;
q _cancelCount;
{CGSize="width"d"height"d} _size;
```

## Properties

```
@property (T@"PKMetalRendererController",&,N,V_rendererController) rendererController;
@property (Tq,N,V_cancelCount) cancelCount;
@property (TB,N,V_synchronous) synchronous;
@property (T{CGSize=dd},R,N,V_size) size;
@property (Td,R,N,V_scale) scale;
@property (TB,R,N,V_extendedDynamicRange) extendedDynamicRange;
@property (TB,N) invertColors;
@property (TB,R,N) sixChannelBlending;
```

## Class methods

```
+[PKImageRenderer _fuzzTestUnzippedData:];
+[PKImageRenderer createImageByUnpremultiplyingAlphaInImage:];
+[PKImageRenderer createJPEGCopyFrom:compressionQuality:];
```

## Instance methods

```
-[PKImageRenderer setSynchronous:];
-[PKImageRenderer dealloc];
-[PKImageRenderer size];
-[PKImageRenderer scale];
-[PKImageRenderer initWithSize:scale:];
-[PKImageRenderer cancel];
-[PKImageRenderer synchronous];
-[PKImageRenderer resume];
-[PKImageRenderer initWithSize:scale:renderQueue:];
-[PKImageRenderer setCancelCount:];
-[PKImageRenderer _renderCGStrokes:clippedToStrokeSpaceRect:scale:strokeTransform:completion:];
-[PKImageRenderer blendingModeForSixChannelBlending:withTransparentBlending:];
-[PKImageRenderer buildStrokeRenderCacheForDrawing:];
-[PKImageRenderer cancelCount];
-[PKImageRenderer extendedDynamicRange];
-[PKImageRenderer initSyncWithSize:scale:];
-[PKImageRenderer initSyncWithSize:scale:extendedDynamicRange:];
-[PKImageRenderer initWithSize:scale:renderQueue:sixChannelBlending:];
-[PKImageRenderer initWithSize:scale:renderQueue:sixChannelBlending:extendedDynamicRange:];
-[PKImageRenderer initWithSize:scale:renderQueue:sixChannelBlending:transparentBlending:];
-[PKImageRenderer initWithSize:scale:renderQueue:sixChannelBlending:transparentBlending:extendedDynamicRange:];
-[PKImageRenderer initWithSize:scale:useMetal:];
-[PKImageRenderer initWithSize:scale:useMetal:renderQueue:];
-[PKImageRenderer invertColors];
-[PKImageRenderer renderCGStrokes:clippedToStrokeSpaceRect:scale:completion:];
-[PKImageRenderer renderCGStrokes:clippedToStrokeSpaceRect:scale:strokeTransform:completion:];
-[PKImageRenderer renderDrawing:clippedToStrokeSpaceRect:scale:completion:];
-[PKImageRenderer renderDrawing:clippedToStrokeSpaceRect:scale:strokeTransform:completion:];
-[PKImageRenderer renderDrawing:completion:];
-[PKImageRenderer renderStrokes:clippedToStrokeSpaceRect:scale:completion:];
-[PKImageRenderer renderStrokes:clippedToStrokeSpaceRect:scale:strokeTransform:completion:];
-[PKImageRenderer rendererController];
-[PKImageRenderer setInvertColors:];
-[PKImageRenderer setRendererController:];
-[PKImageRenderer setupWithSize:scale:renderQueue:sixChannelBlending:synchronous:transparentBlending:extendedDynamicRange:];
-[PKImageRenderer sixChannelBlending];
-[PKImageRenderer sixChannelCGRenderDrawing:clippedToStrokeSpaceRect:scale:completion:];
-[PKImageRenderer sixChannelCGRenderDrawing:clippedToStrokeSpaceRect:scale:strokeTransform:completion:];
-[PKImageRenderer sixChannelCGRenderStrokes:clippedToStrokeSpaceRect:scale:completion:];
-[PKImageRenderer sixChannelPDFRenderDrawing:context:clippedToStrokeSpaceRect:scale:completion:];
```
