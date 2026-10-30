# `MVD`

- Image: [`/System/Library/PrivateFrameworks/ISPKit.framework/ISPKit`](../userland/System__Library__PrivateFrameworks__ISPKit.framework__ISPKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 12 properties, 32 instance methods, 0 class methods

## Instance variables

```
@"<MTLSharedEventSPI>" _mtlSharedEvent;
AQ _mtlSharedEventValue;
^{e5rt_async_event=} _dependencyE5RTEvent;
^{e5rt_async_event=} _completionE5RTEvent;
@"NSObject<OS_os_log>" _logger;
@"MVDANEMemoryProvider" _aneMemoryProvider;
@"NSString" _modelName;
^{e5rt_execution_stream=} _executionStream;
^{e5rt_execution_stream_operation=} _operation;
^{e5rt_io_port=} _cur_frame;
^{e5rt_io_port=} _his_frame;
^{e5rt_io_port=} _dnr_zoom_map;
^{e5rt_io_port=} _fusion_zoom_map;
^{e5rt_io_port=} _out_yuv;
^{e5rt_io_port=} _state_yuv;
^{e5rt_io_port=} _fusion_weight;
```

## Properties

```
@property (T@"MVDANEMemoryProvider",&,N,V_aneMemoryProvider) aneMemoryProvider;
@property (T@"NSString",&,N,V_modelName) modelName;
@property (T^{e5rt_execution_stream=},N,V_executionStream) executionStream;
@property (T^{e5rt_execution_stream_operation=},N,V_operation) operation;
@property (T^{e5rt_io_port=},N,V_cur_frame) cur_frame;
@property (T^{e5rt_io_port=},N,V_his_frame) his_frame;
@property (T^{e5rt_io_port=},N,V_dnr_zoom_map) dnr_zoom_map;
@property (T^{e5rt_io_port=},N,V_fusion_zoom_map) fusion_zoom_map;
@property (T^{e5rt_io_port=},N,V_out_yuv) out_yuv;
@property (T^{e5rt_io_port=},N,V_state_yuv) state_yuv;
@property (T^{e5rt_io_port=},N,V_fusion_weight) fusion_weight;
@property (TB,R,N) hasFusionWeightOutput;
```

## Instance methods

```
-[MVD setOperation:];
-[MVD operation];
-[MVD dealloc];
-[MVD setModelName:];
-[MVD cleanupResources];
-[MVD modelName];
-[MVD executionStream];
-[MVD aneMemoryProvider];
-[MVD setAneMemoryProvider:];
-[MVD setExecutionStream:];
-[MVD fusion_zoom_map];
-[MVD out_yuv];
-[MVD bindInputCurrent:historyWarped:dnrZoomMap:fusionZoomMap:denoisedYUV:stateYUV:fusionWeight:];
-[MVD bindPixelBuffer:port:name:];
-[MVD bypassWithCommandBuffer:curFrame:hisFrame:outYUV:stateYUV:completedHandler:];
-[MVD configANEToWait:];
-[MVD configWaitForANECompletion:];
-[MVD cur_frame];
-[MVD dnr_zoom_map];
-[MVD fusion_weight];
-[MVD hasFusionWeightOutput];
-[MVD his_frame];
-[MVD initWithMTLDevice:modelName:functionName:aneMemoryProvider:];
-[MVD setCur_frame:];
-[MVD setDnr_zoom_map:];
-[MVD setFusion_weight:];
-[MVD setFusion_zoom_map:];
-[MVD setHis_frame:];
-[MVD setOut_yuv:];
-[MVD setState_yuv:];
-[MVD state_yuv];
-[MVD submitWithCommandBuffer:completedHandler:];
```
