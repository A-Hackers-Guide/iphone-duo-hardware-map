# `ICDocCamViewControllerMeshTransform`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAAnimationDelegate`
- 7 instance variables, 11 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"UIImageView" _animationImageView;
@"UIView" _scrimView;
@"ICDocCamImageQuad" _imageQuad;
@? _imageMeshAnimationCompletionBlock;
{CGSize="width"d"height"d} _imageSize;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _imageViewFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _previewViewFrame;
```

## Properties

```
@property (T@"UIImageView",&,N,V_animationImageView) animationImageView;
@property (T@"UIView",&,N,V_scrimView) scrimView;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_imageViewFrame) imageViewFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_previewViewFrame) previewViewFrame;
@property (T{CGSize=dd},N,V_imageSize) imageSize;
@property (T@"ICDocCamImageQuad",&,N,V_imageQuad) imageQuad;
@property (T@?,C,N,V_imageMeshAnimationCompletionBlock) imageMeshAnimationCompletionBlock;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[ICDocCamViewControllerMeshTransform hide];
-[ICDocCamViewControllerMeshTransform imageSize];
-[ICDocCamViewControllerMeshTransform animationDidStop:finished:];
-[ICDocCamViewControllerMeshTransform imageViewFrame];
-[ICDocCamViewControllerMeshTransform setImageSize:];
-[ICDocCamViewControllerMeshTransform setImageViewFrame:];
-[ICDocCamViewControllerMeshTransform startWithCompletionBlock:];
-[ICDocCamViewControllerMeshTransform previewViewFrame];
-[ICDocCamViewControllerMeshTransform imageQuad];
-[ICDocCamViewControllerMeshTransform setImageQuad:];
-[ICDocCamViewControllerMeshTransform animationImageView];
-[ICDocCamViewControllerMeshTransform frameForImageInImageViewFrame:];
-[ICDocCamViewControllerMeshTransform imageMeshAnimationCompletionBlock];
-[ICDocCamViewControllerMeshTransform imageMeshTransformWithImageQuad:imageViewFrame:previewBounds:finalTransform:];
-[ICDocCamViewControllerMeshTransform initWithImage:backgroundImage:imageViewFrame:view:imageQuad:previewView:previewBounds:scrimView:];
-[ICDocCamViewControllerMeshTransform scrimView];
-[ICDocCamViewControllerMeshTransform setAnimationImageView:];
-[ICDocCamViewControllerMeshTransform setImageMeshAnimationCompletionBlock:];
-[ICDocCamViewControllerMeshTransform setPreviewViewFrame:];
-[ICDocCamViewControllerMeshTransform setScrimView:];
```
