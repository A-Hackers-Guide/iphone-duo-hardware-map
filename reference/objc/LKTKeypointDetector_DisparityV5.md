# `LKTKeypointDetector`

- Image: [`/System/Library/VideoProcessors/DisparityV5.bundle/DisparityV5`](../userland/System__Library__VideoProcessors__DisparityV5.bundle__DisparityV5.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 37 instance variables, 11 properties, 30 instance methods, 1 class methods

## Instance variables

```
@"FigMetalContext" _mtlContext;
@"<MTLCommandQueue>" _commandQueue;
[9@"<MTLComputePipelineState>"] _computePipelines;
Q _maxThreadExecutionWidth;
[10{CGSize="width"d"height"d}] _ref_pyr_size;
[10{CGSize="width"d"height"d}] _aux_pyr_size;
[2[10@"<MTLTexture>"]] _I_tex;
^{__CVBuffer=} _G0_pxbuf;
^{__CVBuffer=} _G1_pxbuf;
[10@"<MTLTexture>"] _G0_tex;
[10@"<MTLTexture>"] _G1_tex;
^{__CVBuffer=} _C0_pxbuf;
^{__CVBuffer=} _C1_pxbuf;
[10@"<MTLTexture>"] _C0_tex;
[10@"<MTLTexture>"] _C1_tex;
[2@"<MTLBuffer>"] _Adiagb_buf;
[2@"<MTLBuffer>"] _Ixy_buf;
@"<MTLBuffer>" _idt_buf;
[2^{__CVBuffer}] _uv_fwd_pxbuf;
[2^{__CVBuffer}] _uv_bwd_pxbuf;
[2[10@"<MTLTexture>"]] _uv_fwd_tex;
[2[10@"<MTLTexture>"]] _uv_bwd_tex;
^{__CVBuffer=} _conf_fwd_pxbuf;
^{__CVBuffer=} _conf_bwd_pxbuf;
[10@"<MTLTexture>"] _conf_fwd_tex;
[10@"<MTLTexture>"] _conf_bwd_tex;
@"<MTLTexture>" _uv_fwd_tex_user_ref;
@"<MTLTexture>" _uv_bwd_tex_user_ref;
@"<MTLTexture>" _conf_fwd_tex_user_ref;
@"<MTLTexture>" _conf_bwd_tex_user_ref;
@"<MTLBuffer>" _kpt_buf;
@"<MTLBuffer>" _kpt_confidence;
i _nscales;
i _lastScale;
i _nwarpings;
{CGSize="width"d"height"d} _ref_size;
{CGSize="width"d"height"d} _aux_size;
```

## Properties

```
@property (T{CGSize=dd},R,N,V_ref_size) ref_size;
@property (T{CGSize=dd},R,N,V_aux_size) aux_size;
@property (Ti,R,N,V_nscales) nscales;
@property (Ti,R,N,V_lastScale) lastScale;
@property (Ti,N,V_nwarpings) nwarpings;
@property (T@"<MTLTexture>",R,N) uv_fwd;
@property (T@"<MTLTexture>",R,N) uv_bwd;
@property (T@"<MTLTexture>",R,N) conf_fwd;
@property (T@"<MTLTexture>",R,N) conf_bwd;
@property (T@"<MTLBuffer>",R,N) keypoints;
@property (T@"<MTLBuffer>",R,N) keypoints_confidence;
```

## Class methods

```
+[LKTKeypointDetector _computeScalingFactor:dst_tex:scale_xy_inv:coeff:];
```

## Instance methods

```
-[LKTKeypointDetector waitUntilCompleted];
-[LKTKeypointDetector aux_size];
-[LKTKeypointDetector lastScale];
-[LKTKeypointDetector nwarpings];
-[LKTKeypointDetector nscales];
-[LKTKeypointDetector dealloc];
-[LKTKeypointDetector _setDefaultParameters];
-[LKTKeypointDetector setNwarpings:];
-[LKTKeypointDetector ref_size];
-[LKTKeypointDetector keypoints];
-[LKTKeypointDetector _setupBuffer];
-[LKTKeypointDetector _computeFeaturesDerivativesWithCommandBuffer:in_tex:out_tex:];
-[LKTKeypointDetector _computeFeaturesWithCommandBuffer:in_tex:out_tex:];
-[LKTKeypointDetector _zeroFlowWithCommandBuffer:uv_tex:];
-[LKTKeypointDetector _setupPipelines];
-[LKTKeypointDetector computeKeypointsFromForwardFlow:backwardFlow:forwardConfidence:backwardConfidence:bidirectionalError:confidenceRadialWeight:confidenceMinimum:blockSize:outNumKeypoints:];
-[LKTKeypointDetector conf_bwd];
-[LKTKeypointDetector conf_fwd];
-[LKTKeypointDetector estimateFlowFromReference:target:];
-[LKTKeypointDetector initWithMetalContext:width:height:nscales:lastScale:];
-[LKTKeypointDetector keypoints_confidence];
-[LKTKeypointDetector uv_bwd];
-[LKTKeypointDetector uv_fwd];
-[LKTKeypointDetector _computeOpticalFlowBidirectional];
-[LKTKeypointDetector _doSolverWithCommandBuffer:scale:in_uv_tex:in_G0_tex:in_G1_tex:in_C0_tex:in_C1_tex:out_uv_tex:out_w_tex:];
-[LKTKeypointDetector _downscale2XWithCommandBuffer:in_tex:out_tex:];
-[LKTKeypointDetector _enqueueFlowConsistencyWithCommandBuffer:in_uv0_tex:in_uv1_tex:out_uv_tex:];
-[LKTKeypointDetector _createImagePyramidWithCommandBuffer:in_tex:I_idx:];
-[LKTKeypointDetector _enqueueKeypointsFromFlowWithCommandBuffer:in_uv_fwd_tex:in_uv_bwd_tex:in_conf_fwd_tex:in_conf_bwd_tex:out_kpt_buf:out_kpt_conf:block_size:bidirectional_error:confidence_radial_weight:confidence_minimum:out_num_keypoints:];
-[LKTKeypointDetector _initMemory:height:nscales:lastScale:];
```
