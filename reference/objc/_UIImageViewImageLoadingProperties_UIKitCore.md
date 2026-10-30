# `_UIImageViewImageLoadingProperties`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _startingLoad;
B _enqueueingLoad;
B _stoppingLoad;
@"_UIImageLoader" _imageLoader;
@"<_UIImageViewLoadingDelegate>" _loadingDelegate;
@"UIImage" _imageBeingSetByLoader;
@"UIView" _placeholderView;
```

## Properties

```
@property (T@"_UIImageLoader",&,N,V_imageLoader) imageLoader;
@property (T@"<_UIImageViewLoadingDelegate>",&,N,V_loadingDelegate) loadingDelegate;
@property (T@"UIImage",&,N,V_imageBeingSetByLoader) imageBeingSetByLoader;
@property (T@"UIView",&,N,V_placeholderView) placeholderView;
@property (TB,N,GisStartingLoad,V_startingLoad) startingLoad;
@property (TB,N,GisEnqueueingLoad,V_enqueueingLoad) enqueueingLoad;
@property (TB,N,GisStoppingLoad,V_stoppingLoad) stoppingLoad;
```

## Instance methods

```
-[_UIImageViewImageLoadingProperties setStartingLoad:];
-[_UIImageViewImageLoadingProperties isEnqueueingLoad];
-[_UIImageViewImageLoadingProperties loadingDelegate];
-[_UIImageViewImageLoadingProperties setEnqueueingLoad:];
-[_UIImageViewImageLoadingProperties isStoppingLoad];
-[_UIImageViewImageLoadingProperties setLoadingDelegate:];
-[_UIImageViewImageLoadingProperties setPlaceholderView:];
-[_UIImageViewImageLoadingProperties imageLoader];
-[_UIImageViewImageLoadingProperties imageBeingSetByLoader];
-[_UIImageViewImageLoadingProperties setImageLoader:];
-[_UIImageViewImageLoadingProperties setImageBeingSetByLoader:];
-[_UIImageViewImageLoadingProperties isStartingLoad];
-[_UIImageViewImageLoadingProperties setStoppingLoad:];
-[_UIImageViewImageLoadingProperties placeholderView];
```
