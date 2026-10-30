# `ICDocCamZoomablePageContentViewController`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UIScrollViewDelegate`, `ICDocCamZoomablePageContentViewDelegate`
- 8 instance variables, 13 properties, 38 instance methods, 0 class methods

## Instance variables

```
B _shouldSetupScalesInViewDidLayoutSubviews;
@"<ICDocCamZoomablePageContentDelegate>" _pageContentDelegate;
@"UIImage" _image;
@"UIImageView" _imageView;
Q _pageIndex;
@"VKCImageAnalysisInteraction" _analysisInteraction;
@"UIScrollView" _scrollView;
{CGSize="width"d"height"d} _prevScrollViewSize;
```

## Properties

```
@property (T@"UIScrollView",&,N,V_scrollView) scrollView;
@property (T@"UIImageView",&,N,V_imageView) imageView;
@property (TB,N,V_shouldSetupScalesInViewDidLayoutSubviews) shouldSetupScalesInViewDidLayoutSubviews;
@property (T{CGSize=dd},N,V_prevScrollViewSize) prevScrollViewSize;
@property (T@"VKCImageAnalysisInteraction",&,N,V_analysisInteraction) analysisInteraction;
@property (T@"<ICDocCamZoomablePageContentDelegate>",W,N,V_pageContentDelegate) pageContentDelegate;
@property (T@"UIImage",&,N,V_image) image;
@property (TQ,N,V_pageIndex) pageIndex;
@property (Td,R,N) zoomScale;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[ICDocCamZoomablePageContentViewController zoomScale];
-[ICDocCamZoomablePageContentViewController doubleTap:];
-[ICDocCamZoomablePageContentViewController viewForZoomingInScrollView:];
-[ICDocCamZoomablePageContentViewController setPageIndex:];
-[ICDocCamZoomablePageContentViewController resetZoom];
-[ICDocCamZoomablePageContentViewController init];
-[ICDocCamZoomablePageContentViewController setImageView:];
-[ICDocCamZoomablePageContentViewController supportedInterfaceOrientations];
-[ICDocCamZoomablePageContentViewController scrollView];
-[ICDocCamZoomablePageContentViewController viewDidLoad];
-[ICDocCamZoomablePageContentViewController setScrollView:];
-[ICDocCamZoomablePageContentViewController viewDidLayoutSubviews];
-[ICDocCamZoomablePageContentViewController scrollViewDidZoom:];
-[ICDocCamZoomablePageContentViewController _canShowWhileLocked];
-[ICDocCamZoomablePageContentViewController viewDidAppear:];
-[ICDocCamZoomablePageContentViewController pageIndex];
-[ICDocCamZoomablePageContentViewController scrollViewWillBeginZooming:withView:];
-[ICDocCamZoomablePageContentViewController accessibilityPerformEscape];
-[ICDocCamZoomablePageContentViewController image];
-[ICDocCamZoomablePageContentViewController imageView];
-[ICDocCamZoomablePageContentViewController setImage:];
-[ICDocCamZoomablePageContentViewController setupAccessibility];
-[ICDocCamZoomablePageContentViewController zoomRectForScale:withCenter:];
-[ICDocCamZoomablePageContentViewController view:setCenter:];
-[ICDocCamZoomablePageContentViewController analysisInteraction];
-[ICDocCamZoomablePageContentViewController analyzeCurrentImageIfNecessary];
-[ICDocCamZoomablePageContentViewController isTouchingAnalyzableContentAtPoint:withEvent:];
-[ICDocCamZoomablePageContentViewController pageContentDelegate];
-[ICDocCamZoomablePageContentViewController pageContentViewDidPencilDown];
-[ICDocCamZoomablePageContentViewController prevScrollViewSize];
-[ICDocCamZoomablePageContentViewController resetImageCentering];
-[ICDocCamZoomablePageContentViewController setAnalysisInteraction:];
-[ICDocCamZoomablePageContentViewController setPageContentDelegate:];
-[ICDocCamZoomablePageContentViewController setPrevScrollViewSize:];
-[ICDocCamZoomablePageContentViewController setShouldSetupScalesInViewDidLayoutSubviews:];
-[ICDocCamZoomablePageContentViewController setupScales];
-[ICDocCamZoomablePageContentViewController shouldSetupScalesInViewDidLayoutSubviews];
-[ICDocCamZoomablePageContentViewController singleTap];
```
