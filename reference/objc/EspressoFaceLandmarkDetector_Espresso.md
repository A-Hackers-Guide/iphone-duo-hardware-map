# `EspressoFaceLandmarkDetector`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 1 properties, 10 instance methods, 0 class methods

## Instance variables

```
{vImage_Buffer="data"^v"height"Q"width"Q"rowBytes"Q} crop_scaled;
{vImage_Buffer="data"^v"height"Q"width"Q"rowBytes"Q} crop_192;
{shared_ptr<Espresso::net>="__ptr_"^{net}"__cntrl_"^{__shared_weak_count}} net;
{shared_ptr<Espresso::net>="__ptr_"^{net}"__cntrl_"^{__shared_weak_count}} net_detect;
{vector<std::shared_ptr<Espresso::net>, std::allocator<std::shared_ptr<Espresso::net>>>="__begin_"^v"__end_"^v""{?="__cap_"^v}} nets_sub_landmark;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _newface;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},V_newface) newface;
```

## Instance methods

```
-[EspressoFaceLandmarkDetector init];
-[EspressoFaceLandmarkDetector dealloc];
-[EspressoFaceLandmarkDetector newface];
-[EspressoFaceLandmarkDetector commonInit:context:platform:computePath:];
-[EspressoFaceLandmarkDetector detect:face:sublandmark:doFaceRectFix:];
-[EspressoFaceLandmarkDetector detectInImageRect:face:sublandmark:];
-[EspressoFaceLandmarkDetector extractSubLandmarksFromCrop192:centers192:];
-[EspressoFaceLandmarkDetector initWithNetworkAtPath:context:platform:computePath:];
-[EspressoFaceLandmarkDetector initWithNetworkAtPath:contextObjC:platform:computePath:];
-[EspressoFaceLandmarkDetector setNewface:];
```
