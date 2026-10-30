# `FigBWNodeRenderObserver`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWNodeRenderDelegate`
- 3 instance variables, 6 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"BWNode" _node;
@? _willRenderSampleBufferHandler;
@? _formatDidBecomeLiveHandler;
```

## Properties

```
@property (T@?,C,N,V_willRenderSampleBufferHandler) willRenderSampleBufferHandler;
@property (T@?,C,N,V_formatDidBecomeLiveHandler) formatDidBecomeLiveHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FigBWNodeRenderObserver dealloc];
-[FigBWNodeRenderObserver node:format:didBecomeLiveForOutput:];
-[FigBWNodeRenderObserver node:format:didBecomeLiveForInput:configurationID:];
-[FigBWNodeRenderObserver node:willRenderSampleBuffer:forInput:];
-[FigBWNodeRenderObserver initWithBWNode:];
-[FigBWNodeRenderObserver formatDidBecomeLiveHandler];
-[FigBWNodeRenderObserver setFormatDidBecomeLiveHandler:];
-[FigBWNodeRenderObserver setWillRenderSampleBufferHandler:];
-[FigBWNodeRenderObserver willRenderSampleBufferHandler];
```
