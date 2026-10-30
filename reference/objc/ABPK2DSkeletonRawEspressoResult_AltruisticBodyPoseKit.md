# `ABPK2DSkeletonRawEspressoResult`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"ABPKMLImageData" _imageDataForNeuralNetwork;
@"ABPKImageData" _inputImageData;
^{__CVBuffer=} _heatMapBuffer;
^{__CVBuffer=} _affinityMapBuffer;
q _rotationNeeded;
_heatMapShape;
_heatMapStrides;
_affinityMapShape;
_affinityMapStrides;
```

## Properties

```
@property (T@"ABPKMLImageData",R,N,V_imageDataForNeuralNetwork) imageDataForNeuralNetwork;
@property (T@"ABPKImageData",R,N,V_inputImageData) inputImageData;
@property (T^{__CVBuffer=},R,N,V_heatMapBuffer) heatMapBuffer;
@property (T,R,N,V_heatMapShape) heatMapShape;
@property (T,R,N,V_heatMapStrides) heatMapStrides;
@property (T^{__CVBuffer=},R,N,V_affinityMapBuffer) affinityMapBuffer;
@property (T,R,N,V_affinityMapShape) affinityMapShape;
@property (T,R,N,V_affinityMapStrides) affinityMapStrides;
@property (Tq,R,N,V_rotationNeeded) rotationNeeded;
```

## Instance methods

```
-[ABPK2DSkeletonRawEspressoResult dealloc];
-[ABPK2DSkeletonRawEspressoResult affinityMapBuffer];
-[ABPK2DSkeletonRawEspressoResult affinityMapShape];
-[ABPK2DSkeletonRawEspressoResult affinityMapStrides];
-[ABPK2DSkeletonRawEspressoResult heatMapBuffer];
-[ABPK2DSkeletonRawEspressoResult heatMapShape];
-[ABPK2DSkeletonRawEspressoResult heatMapStrides];
-[ABPK2DSkeletonRawEspressoResult imageDataForNeuralNetwork];
-[ABPK2DSkeletonRawEspressoResult initWithHeatMapBuffer:heatMapShape:heatMapStrides:affinityMapBuffer:affinityMapShape:affinityMapStrides:rotationNeeded:];
-[ABPK2DSkeletonRawEspressoResult initWithHeatMapBuffer:heatMapShape:heatMapStrides:rotationNeeded:];
-[ABPK2DSkeletonRawEspressoResult initWithMLImage:originalImageData:heatMapBuffer:heatMapShape:heatMapStrides:affinityMapBuffer:affinityMapShape:affinityMapStrides:rotationNeeded:];
-[ABPK2DSkeletonRawEspressoResult initWithMLImage:originalImageData:heatMapBuffer:heatMapShape:heatMapStrides:rotationNeeded:];
-[ABPK2DSkeletonRawEspressoResult inputImageData];
-[ABPK2DSkeletonRawEspressoResult rotationNeeded];
```
