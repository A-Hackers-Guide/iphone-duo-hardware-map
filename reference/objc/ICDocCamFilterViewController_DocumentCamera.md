# `ICDocCamFilterViewController`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UIScrollViewDelegate`, `UIGestureRecognizerDelegate`
- 15 instance variables, 20 properties, 52 instance methods, 0 class methods

## Instance variables

```
B _transitioning;
s _currentFilterType;
d _horizontalOffset;
d _bottomOffset;
d _bottomContentInset;
@"<ICDocCamFilterViewDelegate>" _filterViewDelegate;
@"UIScrollView" _scrollView;
@"NSLayoutConstraint" _scrollViewBottomConstraint;
@"NSLayoutConstraint" _scrollViewTrailingConstraint;
@"UIView" _backgroundView;
@"DCSinglePixelVerticalLineView" _verticalLineView;
@"DCSinglePixelHorizontalLineView" _horizontalLineView;
@"NSArray" _layoutConstraints;
@"NSMutableArray" _filterButtons;
@"UILongPressGestureRecognizer" _longPressGesture;
```

## Properties

```
@property (T@"UIScrollView",W,N,V_scrollView) scrollView;
@property (T@"UIView",W,N,V_backgroundView) backgroundView;
@property (T@"DCSinglePixelVerticalLineView",W,N,V_verticalLineView) verticalLineView;
@property (T@"DCSinglePixelHorizontalLineView",W,N,V_horizontalLineView) horizontalLineView;
@property (T@"NSArray",C,N,V_layoutConstraints) layoutConstraints;
@property (T@"NSLayoutConstraint",&,N,V_scrollViewBottomConstraint) scrollViewBottomConstraint;
@property (TB,N,V_transitioning) transitioning;
@property (T@"NSMutableArray",&,N,V_filterButtons) filterButtons;
@property (T@"UILongPressGestureRecognizer",&,N,V_longPressGesture) longPressGesture;
@property (Td,N,V_horizontalOffset) horizontalOffset;
@property (Td,N,V_bottomOffset) bottomOffset;
@property (Td,N,V_bottomContentInset) bottomContentInset;
@property (T@"<ICDocCamFilterViewDelegate>",W,N,V_filterViewDelegate) filterViewDelegate;
@property (Ts,N,V_currentFilterType) currentFilterType;
@property (T{CGSize=dd},R,N) contentSize;
@property (T@"NSLayoutConstraint",R,N,V_scrollViewTrailingConstraint) scrollViewTrailingConstraint;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[ICDocCamFilterViewController setBottomContentInset:];
-[ICDocCamFilterViewController init];
-[ICDocCamFilterViewController supportedInterfaceOrientations];
-[ICDocCamFilterViewController scrollView];
-[ICDocCamFilterViewController setLayoutConstraints:];
-[ICDocCamFilterViewController dealloc];
-[ICDocCamFilterViewController viewDidLoad];
-[ICDocCamFilterViewController setScrollView:];
-[ICDocCamFilterViewController viewDidLayoutSubviews];
-[ICDocCamFilterViewController contentSize];
-[ICDocCamFilterViewController setHorizontalOffset:];
-[ICDocCamFilterViewController viewWillAppear:];
-[ICDocCamFilterViewController _canShowWhileLocked];
-[ICDocCamFilterViewController gestureRecognizerShouldBegin:];
-[ICDocCamFilterViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[ICDocCamFilterViewController bottomContentInset];
-[ICDocCamFilterViewController horizontalOffset];
-[ICDocCamFilterViewController backgroundView];
-[ICDocCamFilterViewController setTransitioning:];
-[ICDocCamFilterViewController updateConstraints];
-[ICDocCamFilterViewController prefersStatusBarHidden];
-[ICDocCamFilterViewController layoutConstraints];
-[ICDocCamFilterViewController transitioning];
-[ICDocCamFilterViewController setBackgroundView:];
-[ICDocCamFilterViewController longPressGesture];
-[ICDocCamFilterViewController setLongPressGesture:];
-[ICDocCamFilterViewController bottomOffset];
-[ICDocCamFilterViewController setBottomOffset:];
-[ICDocCamFilterViewController longPressGesture:];
-[ICDocCamFilterViewController scrollViewTrailingConstraint];
-[ICDocCamFilterViewController scrollViewBottomConstraint];
-[ICDocCamFilterViewController setScrollViewBottomConstraint:];
-[ICDocCamFilterViewController horizontalLineView];
-[ICDocCamFilterViewController setHorizontalLineView:];
-[ICDocCamFilterViewController updateScrollViewContentSize];
-[ICDocCamFilterViewController filterSelected:];
-[ICDocCamFilterViewController setUpScrollView];
-[ICDocCamFilterViewController applyToAll:];
-[ICDocCamFilterViewController centerContent:isPortrait:];
-[ICDocCamFilterViewController currentFilterType];
-[ICDocCamFilterViewController filterButtonFromLocation:];
-[ICDocCamFilterViewController filterButtons];
-[ICDocCamFilterViewController filterViewDelegate];
-[ICDocCamFilterViewController initializeFilters];
-[ICDocCamFilterViewController prepareToAnimateIn:];
-[ICDocCamFilterViewController setCurrentFilterType:];
-[ICDocCamFilterViewController setFilterButtons:];
-[ICDocCamFilterViewController setFilterViewDelegate:];
-[ICDocCamFilterViewController setVerticalLineView:];
-[ICDocCamFilterViewController updateConstraintsPad];
-[ICDocCamFilterViewController updateConstraintsPhone];
-[ICDocCamFilterViewController verticalLineView];
```
