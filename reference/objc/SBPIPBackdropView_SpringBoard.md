# `SBPIPBackdropView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 3 instance variables, 3 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"CAFilter" _gaussianBlurFilter;
@"CAFilter" _averageColorFilter;
@"NSArray" _animatedLayerProperties;
```

## Properties

```
@property (T@"NSString",C,N) groupName;
@property (Td,N) gaussianBlurRadius;
@property (Td,N) backdropScale;
```

## Class methods

```
+[SBPIPBackdropView layerClass];
```

## Instance methods

```
-[SBPIPBackdropView dealloc];
-[SBPIPBackdropView setGroupName:];
-[SBPIPBackdropView gaussianBlurRadius];
-[SBPIPBackdropView _updateFilters];
-[SBPIPBackdropView setGaussianBlurRadius:];
-[SBPIPBackdropView groupName];
-[SBPIPBackdropView _shouldAnimatePropertyWithKey:];
-[SBPIPBackdropView initWithFrame:];
-[SBPIPBackdropView backdropScale];
-[SBPIPBackdropView setBackdropScale:];
```
