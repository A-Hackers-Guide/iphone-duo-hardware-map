# `DBSArrangementLayoutViewController`

- Image: [`/System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings`](../userland/System__Library__PrivateFrameworks__Settings__DisplayAndBrightnessSettings.framework__DisplayAndBrightnessSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UIGestureRecognizerDelegate`
- 10 instance variables, 15 properties, 30 instance methods, 0 class methods

## Instance variables

```
@"<DBSArrangementLayoutViewControllerDelegate>" _delegate;
Q _nativeDisplayLocation;
@"NSString" _nativeDisplayName;
@"NSString" _externalDisplayName;
@"UIPanGestureRecognizer" _dragGestureRecognizer;
@"UITapGestureRecognizer" _tapGestureRecogniser;
@"DBSNativeDisplayIconView" _dragView;
{CGSize="width"d"height"d} _nativeDisplaySize;
{CGSize="width"d"height"d} _externalDisplaySize;
{CGPoint="x"d"y"d} _unitDragPoint;
```

## Properties

```
@property (TQ,N,V_nativeDisplayLocation) nativeDisplayLocation;
@property (T{CGSize=dd},N,V_nativeDisplaySize) nativeDisplaySize;
@property (T{CGSize=dd},N,V_externalDisplaySize) externalDisplaySize;
@property (T@"NSString",&,N,V_nativeDisplayName) nativeDisplayName;
@property (T@"NSString",&,N,V_externalDisplayName) externalDisplayName;
@property (T@"DBSArrangementLayoutView",R,N) arrangementView;
@property (T@"UIPanGestureRecognizer",&,N,V_dragGestureRecognizer) dragGestureRecognizer;
@property (T@"UITapGestureRecognizer",&,N,V_tapGestureRecogniser) tapGestureRecogniser;
@property (T@"DBSNativeDisplayIconView",&,N,V_dragView) dragView;
@property (T{CGPoint=dd},N,V_unitDragPoint) unitDragPoint;
@property (T@"<DBSArrangementLayoutViewControllerDelegate>",&,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[DBSArrangementLayoutViewController setDelegate:];
-[DBSArrangementLayoutViewController gestureRecognizerShouldBegin:];
-[DBSArrangementLayoutViewController loadView];
-[DBSArrangementLayoutViewController delegate];
-[DBSArrangementLayoutViewController dragGestureRecognizer];
-[DBSArrangementLayoutViewController setDragGestureRecognizer:];
-[DBSArrangementLayoutViewController didTap:];
-[DBSArrangementLayoutViewController arrangementView];
-[DBSArrangementLayoutViewController dragView];
-[DBSArrangementLayoutViewController setDragView:];
-[DBSArrangementLayoutViewController currentDisplayIconView];
-[DBSArrangementLayoutViewController didDrag:];
-[DBSArrangementLayoutViewController externalDisplayName];
-[DBSArrangementLayoutViewController externalDisplaySize];
-[DBSArrangementLayoutViewController initWithNativeDisplaySize:nativeDisplayName:externalDisplaySize:externalDisplayName:currentNativeDisplayLocation:];
-[DBSArrangementLayoutViewController nativeDisplayImageWithWidth:];
-[DBSArrangementLayoutViewController nativeDisplayLocation];
-[DBSArrangementLayoutViewController nativeDisplayName];
-[DBSArrangementLayoutViewController nativeDisplaySize];
-[DBSArrangementLayoutViewController setExternalDisplayName:];
-[DBSArrangementLayoutViewController setExternalDisplaySize:];
-[DBSArrangementLayoutViewController setNativeDisplayLocation:];
-[DBSArrangementLayoutViewController setNativeDisplayName:];
-[DBSArrangementLayoutViewController setNativeDisplaySize:];
-[DBSArrangementLayoutViewController setTapGestureRecogniser:];
-[DBSArrangementLayoutViewController setUnitDragPoint:];
-[DBSArrangementLayoutViewController tapGestureRecogniser];
-[DBSArrangementLayoutViewController unitDragPoint];
-[DBSArrangementLayoutViewController updateCurrentDisplayLocation:];
-[DBSArrangementLayoutViewController updateOrientationTo:withNativeDisplaySize:];
```
