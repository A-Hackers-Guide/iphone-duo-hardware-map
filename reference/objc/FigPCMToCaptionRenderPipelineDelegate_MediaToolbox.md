# `FigPCMToCaptionRenderPipelineDelegate`

- Image: [`/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`](../userland/System__Library__Frameworks__MediaToolbox.framework__MediaToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FigSpeechTranscriberBridgeDelegate`
- 2 instance variables, 6 properties, 8 instance methods, 0 class methods

## Instance variables

```
^{OpaqueFigCFWeakReferenceHolder=} _weakRPHolder;
@"NSObject<OS_dispatch_queue>" _callbackQueue;
```

## Properties

```
@property (T^{OpaqueFigCFWeakReferenceHolder=},N,V_weakRPHolder) weakRPHolder;
@property (T@"NSObject<OS_dispatch_queue>",N,V_callbackQueue) callbackQueue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FigPCMToCaptionRenderPipelineDelegate dealloc];
-[FigPCMToCaptionRenderPipelineDelegate setCallbackQueue:];
-[FigPCMToCaptionRenderPipelineDelegate callbackQueue];
-[FigPCMToCaptionRenderPipelineDelegate setWeakRPHolder:];
-[FigPCMToCaptionRenderPipelineDelegate speechTranscriberBridgeDidEncounterError:];
-[FigPCMToCaptionRenderPipelineDelegate speechTranscriberBridgeDidReceiveResult:range:];
-[FigPCMToCaptionRenderPipelineDelegate speechTranscriberBridgeDidUpdateVolatileRange:changedStart:changedEnd:];
-[FigPCMToCaptionRenderPipelineDelegate weakRPHolder];
```
