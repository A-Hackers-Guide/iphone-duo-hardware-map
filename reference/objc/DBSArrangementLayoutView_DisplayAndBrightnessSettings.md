# `DBSArrangementLayoutView`

- Image: [`/System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings`](../userland/System__Library__PrivateFrameworks__Settings__DisplayAndBrightnessSettings.framework__DisplayAndBrightnessSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 11 instance variables, 11 properties, 30 instance methods, 0 class methods

## Instance variables

```
@"DBSArrangementLayoutViewController" _dataSource;
d _margin;
@"DBSExternalDisplayIconView" _externalDisplay;
@"DBSNativeDisplayIconView" _northDisplay;
@"DBSNativeDisplayIconView" _eastDisplay;
@"DBSNativeDisplayIconView" _southDisplay;
@"DBSNativeDisplayIconView" _westDisplay;
@"NSLayoutConstraint" _nativeIconAspectRatioConstraint;
@"NSLayoutConstraint" _widthRatioConstraint;
{CGSize="width"d"height"d} _externalDisplaySize;
{CGSize="width"d"height"d} _nativeDisplaySize;
```

## Properties

```
@property (T@"DBSArrangementLayoutViewController",W,N,V_dataSource) dataSource;
@property (T{CGSize=dd},N,V_externalDisplaySize) externalDisplaySize;
@property (T{CGSize=dd},N,V_nativeDisplaySize) nativeDisplaySize;
@property (Td,N,V_margin) margin;
@property (T@"DBSExternalDisplayIconView",&,N,V_externalDisplay) externalDisplay;
@property (T@"DBSNativeDisplayIconView",&,N,V_northDisplay) northDisplay;
@property (T@"DBSNativeDisplayIconView",&,N,V_eastDisplay) eastDisplay;
@property (T@"DBSNativeDisplayIconView",&,N,V_southDisplay) southDisplay;
@property (T@"DBSNativeDisplayIconView",&,N,V_westDisplay) westDisplay;
@property (T@"NSLayoutConstraint",&,N,V_nativeIconAspectRatioConstraint) nativeIconAspectRatioConstraint;
@property (T@"NSLayoutConstraint",&,N,V_widthRatioConstraint) widthRatioConstraint;
```

## Instance methods

```
-[DBSArrangementLayoutView margin];
-[DBSArrangementLayoutView initWithDataSource:];
-[DBSArrangementLayoutView setMargin:];
-[DBSArrangementLayoutView setDataSource:];
-[DBSArrangementLayoutView dataSource];
-[DBSArrangementLayoutView updateForOrientation:];
-[DBSArrangementLayoutView setExternalDisplay:];
-[DBSArrangementLayoutView placeCurrentDisplayAtLocation:];
-[DBSArrangementLayoutView externalDisplay];
-[DBSArrangementLayoutView setWestDisplay:];
-[DBSArrangementLayoutView nativeIconAspectRatioConstraint];
-[DBSArrangementLayoutView setEastDisplay:];
-[DBSArrangementLayoutView _placeHolderMainDisplayImageWithWidth:orientation:];
-[DBSArrangementLayoutView _pointDistanceFirst:second:];
-[DBSArrangementLayoutView arrangeDisplayIcons];
-[DBSArrangementLayoutView displayLocationForPointInView:];
-[DBSArrangementLayoutView eastDisplay];
-[DBSArrangementLayoutView externalDisplaySize];
-[DBSArrangementLayoutView nativeDisplaySize];
-[DBSArrangementLayoutView northDisplay];
-[DBSArrangementLayoutView setExternalDisplaySize:];
-[DBSArrangementLayoutView setNativeDisplaySize:];
-[DBSArrangementLayoutView setNativeIconAspectRatioConstraint:];
-[DBSArrangementLayoutView setNorthDisplay:];
-[DBSArrangementLayoutView setSouthDisplay:];
-[DBSArrangementLayoutView setWidthRatioConstraint:];
-[DBSArrangementLayoutView southDisplay];
-[DBSArrangementLayoutView updateNativeDisplayImagesWithOrientation:];
-[DBSArrangementLayoutView westDisplay];
-[DBSArrangementLayoutView widthRatioConstraint];
```
