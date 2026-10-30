# `TVL1_v3_SolverParameters`

- Image: [`/System/Library/VideoProcessors/FPDisparityV3.bundle/FPDisparityV3`](../userland/System__Library__VideoProcessors__FPDisparityV3.bundle__FPDisparityV3.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 16 instance methods, 0 class methods

## Instance variables

```
f _tau;
f _sigma;
f _theta;
f _huber_eps;
i _warpings;
i _iterations;
f _a_checkerboard;
f _b_checkerboard;
```

## Properties

```
@property (Tf,N,V_tau) tau;
@property (Tf,N,V_sigma) sigma;
@property (Tf,N,V_theta) theta;
@property (Tf,N,V_huber_eps) huber_eps;
@property (Ti,N,V_warpings) warpings;
@property (Ti,N,V_iterations) iterations;
@property (Tf,N,V_a_checkerboard) a_checkerboard;
@property (Tf,N,V_b_checkerboard) b_checkerboard;
```

## Instance methods

```
-[TVL1_v3_SolverParameters iterations];
-[TVL1_v3_SolverParameters setIterations:];
-[TVL1_v3_SolverParameters sigma];
-[TVL1_v3_SolverParameters setSigma:];
-[TVL1_v3_SolverParameters theta];
-[TVL1_v3_SolverParameters tau];
-[TVL1_v3_SolverParameters setTheta:];
-[TVL1_v3_SolverParameters setTau:];
-[TVL1_v3_SolverParameters a_checkerboard];
-[TVL1_v3_SolverParameters b_checkerboard];
-[TVL1_v3_SolverParameters huber_eps];
-[TVL1_v3_SolverParameters setA_checkerboard:];
-[TVL1_v3_SolverParameters setB_checkerboard:];
-[TVL1_v3_SolverParameters setHuber_eps:];
-[TVL1_v3_SolverParameters setWarpings:];
-[TVL1_v3_SolverParameters warpings];
```
