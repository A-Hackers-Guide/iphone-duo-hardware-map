# `CAMSmartStylePreviewViewController`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `CAMSmartStylePreviewGridViewDelegate`
- 3 instance variables, 10 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"<CAMSmartStylePreviewViewControllerDelegate>" _delegate;
Q _gridLayout;
q _pageIndex;
```

## Properties

```
@property (T@"CAMSmartStylePreviewGridView",R,N) _previewView;
@property (T@"<CAMSmartStylePreviewViewControllerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R,N,V_gridLayout) gridLayout;
@property (Tq,R,N,V_pageIndex) pageIndex;
@property (TQ,N) expandedItemIndex;
@property (TB,R,N) didFinishRendering;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAMSmartStylePreviewViewController desiredCarouselRatio];
```

## Instance methods

```
-[CAMSmartStylePreviewViewController speedUpFadeInAnimations];
-[CAMSmartStylePreviewViewController gridLayout];
-[CAMSmartStylePreviewViewController updateViewsWithLoadResults];
-[CAMSmartStylePreviewViewController setExpandedItemIndex:];
-[CAMSmartStylePreviewViewController smartStylePreviewGridViewDidFinishRendering:];
-[CAMSmartStylePreviewViewController _previewView];
-[CAMSmartStylePreviewViewController smartStylePreviewGridView:didChangeAnimatingGrid:];
-[CAMSmartStylePreviewViewController _canShowWhileLocked];
-[CAMSmartStylePreviewViewController setDelegate:];
-[CAMSmartStylePreviewViewController loadView];
-[CAMSmartStylePreviewViewController initWithDelegate:gridLayout:pageIndex:];
-[CAMSmartStylePreviewViewController updateWithStyle:];
-[CAMSmartStylePreviewViewController pageIndex];
-[CAMSmartStylePreviewViewController setExpandedItemIndex:animated:];
-[CAMSmartStylePreviewViewController delegate];
-[CAMSmartStylePreviewViewController smartStylePreviewGridView:didTapItemAtIndex:];
-[CAMSmartStylePreviewViewController didFinishRendering];
-[CAMSmartStylePreviewViewController description];
-[CAMSmartStylePreviewViewController expandedItemIndex];
```
