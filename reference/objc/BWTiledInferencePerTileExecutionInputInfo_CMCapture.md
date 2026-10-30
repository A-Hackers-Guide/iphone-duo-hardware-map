# `BWTiledInferencePerTileExecutionInputInfo`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"<MTLCommandQueue>" _commandQueue;
@"<MTLCommandBuffer>" _commandBuffer;
_tilePosition;
```

## Properties

```
@property (T@"<MTLCommandQueue>",R,N,V_commandQueue) commandQueue;
@property (T@"<MTLCommandBuffer>",R,N,V_commandBuffer) commandBuffer;
@property (T,R,N,V_tilePosition) tilePosition;
```

## Class methods

```
+[BWTiledInferencePerTileExecutionInputInfo initialize];
```

## Instance methods

```
-[BWTiledInferencePerTileExecutionInputInfo dealloc];
-[BWTiledInferencePerTileExecutionInputInfo commandQueue];
-[BWTiledInferencePerTileExecutionInputInfo commandBuffer];
-[BWTiledInferencePerTileExecutionInputInfo tilePosition];
-[BWTiledInferencePerTileExecutionInputInfo initWithCommandQueue:commandBuffer:tilePosition:];
```
