# `HBFGPUParameters`

- Image: [`/System/Library/VideoProcessors/FPDisparityV3.bundle/FPDisparityV3`](../userland/System__Library__VideoProcessors__FPDisparityV3.bundle__FPDisparityV3.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 11 properties, 22 instance methods, 0 class methods

## Instance variables

```
i _iterations;
i _scales;
i _radius;
i _padding;
f _sigma_0;
f _sigma_1;
f _sigma_2;
f _sigma_w;
f _conf_min;
f _conf_max;
f _occ_thres;
```

## Properties

```
@property (Ti,N,V_iterations) iterations;
@property (Ti,N,V_scales) scales;
@property (Ti,N,V_radius) radius;
@property (Ti,N,V_padding) padding;
@property (Tf,N,V_sigma_0) sigma_0;
@property (Tf,N,V_sigma_1) sigma_1;
@property (Tf,N,V_sigma_2) sigma_2;
@property (Tf,N,V_sigma_w) sigma_w;
@property (Tf,N,V_conf_min) conf_min;
@property (Tf,N,V_conf_max) conf_max;
@property (Tf,N,V_occ_thres) occ_thres;
```

## Instance methods

```
-[HBFGPUParameters setScales:];
-[HBFGPUParameters padding];
-[HBFGPUParameters scales];
-[HBFGPUParameters iterations];
-[HBFGPUParameters setIterations:];
-[HBFGPUParameters setPadding:];
-[HBFGPUParameters setRadius:];
-[HBFGPUParameters radius];
-[HBFGPUParameters sigma_0];
-[HBFGPUParameters sigma_2];
-[HBFGPUParameters sigma_1];
-[HBFGPUParameters sigma_w];
-[HBFGPUParameters conf_max];
-[HBFGPUParameters conf_min];
-[HBFGPUParameters occ_thres];
-[HBFGPUParameters setConf_max:];
-[HBFGPUParameters setConf_min:];
-[HBFGPUParameters setOcc_thres:];
-[HBFGPUParameters setSigma_0:];
-[HBFGPUParameters setSigma_1:];
-[HBFGPUParameters setSigma_2:];
-[HBFGPUParameters setSigma_w:];
```
