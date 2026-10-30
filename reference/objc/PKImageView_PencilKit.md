# `PKImageView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 6 instance variables, 3 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"UIView" _imageView;
@"UIView" _addView;
@"UIView" _mulView;
@"UIImage" _image;
@"UIImage" _addImage;
@"UIImage" _mulImage;
```

## Properties

```
@property (T@"UIImage",&,N,V_image) image;
@property (T@"UIImage",&,N,V_addImage) addImage;
@property (T@"UIImage",&,N,V_mulImage) mulImage;
```

## Instance methods

```
-[PKImageView initWithImage:];
-[PKImageView setBounds:];
-[PKImageView setFrame:];
-[PKImageView image];
-[PKImageView initWithFrame:];
-[PKImageView setImage:];
-[PKImageView addImage];
-[PKImageView _updateAddLayer];
-[PKImageView _updateMulLayer];
-[PKImageView _createViewWithImage:compositingFiler:];
-[PKImageView _updateImageLayer];
-[PKImageView _updateLayerFrames];
-[PKImageView mulImage];
-[PKImageView setAddImage:];
-[PKImageView setMulImage:];
-[PKImageView setupWithDrawing:imageSize:scale:strokeSpaceClipRect:sixChannel:extendedDynamicRange:];
```
