# `CAMArrangementView`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 7 instance variables, 5 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"UIView" previewView;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 secondaryView;
? delegate;
B bookBoundaryRegionRectEnabled;
{CGRect={CGPoint=dd}{CGSize=dd}} bookBoundaryRegionRect;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 previousBookBoundaryRegionRect;
q controlOrientation;
```

## Properties

```
@property (T@"UIView",N,&,VpreviewView) previewView;
@property (T@"<CAMArrangementViewDelegate>",N,W,Vdelegate) delegate;
@property (TB,N,VbookBoundaryRegionRectEnabled) bookBoundaryRegionRectEnabled;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,VbookBoundaryRegionRect) bookBoundaryRegionRect;
@property (Tq,N,VcontrolOrientation) controlOrientation;
```

## Class methods

```
+[CAMArrangementView layerClass];
```

## Instance methods

```
-[CAMArrangementView setBookBoundaryRegionRect:];
-[CAMArrangementView setOrientation:animated:];
-[CAMArrangementView previewView];
-[CAMArrangementView setPreviewView:];
-[CAMArrangementView layoutSubviews];
-[CAMArrangementView setControlOrientation:];
-[CAMArrangementView setDelegate:];
-[CAMArrangementView delegate];
-[CAMArrangementView bookBoundaryRegionRect];
-[CAMArrangementView initWithCoder:];
-[CAMArrangementView initWithFrame:];
-[CAMArrangementView bookBoundaryRegionRectEnabled];
-[CAMArrangementView controlOrientation];
-[CAMArrangementView invalidateBookBoundaryRegionRectAnimated:];
-[CAMArrangementView setArrangedSubviewsPreviewView:secondaryView:];
-[CAMArrangementView setBookBoundaryRegionRectEnabled:];
```
